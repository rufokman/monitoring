import re
from django_tables2 import SingleTableView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .tables import *
import pandas as pd
import datetime
import openpyxl as opx
from django.core.files.storage import FileSystemStorage


# Create your views here.

def choosing_form(request):
    un_ver = Card.objects.all().values_list('verificator', flat=True).distinct().exclude(verificator='-')  # Уникальные верификаторы
    un_own = Card.objects.filter(verificator='-').values_list('fio', flat=True).distinct()  # Уникальные владельцы с пустым верификатором
    no_ver = Card.objects.filter(verificator='-').values_list('verificator', flat=True).distinct()  # Дефис в верифиакторе (пустой)
    if request.method == 'POST':
        if request.POST['choose_ver'] != 'Выберите верификатора':
            data = Card.objects.filter(verificator__exact=request.POST['choose_ver'], delete=0)
            formset = CardFormSetCertain(queryset=data)
            return render(request, "choosing_form.html", {'formset': formset, 'un_ver': un_ver, 'un_own': un_own,
                                                          'no_ver': no_ver})
        if request.POST['choose_own'] != 'Выберите владельца':
            data = Card.objects.filter(fio__exact=request.POST['choose_own'], delete=0)
            formset = CardFormSetCertain(queryset=data)
            return render(request, "choosing_form.html", {'formset': formset, 'un_ver': un_ver, 'un_own': un_own,
                                                          'no_ver': no_ver})
    return render(request, "choosing_form.html", {'un_ver': un_ver, 'un_own': un_own, 'no_ver': no_ver})


def cards_user_certain(request):

    credits = request.GET['credits']
    choose_ver = request.GET['choose_ver']
    data = Card.objects.filter(verificator__exact=choose_ver, delete=0)
    config_data = Config.objects.first()
    # allow_edit = config_data.allow_edit
    if request.method == 'POST':
        formset = CardFormSetCertain(request.POST, queryset=data)
        if formset.is_valid():
            # if allow_edit == False:
            #     return redirect('user_certain')
            for form in formset:
                changed_data = form.changed_data
                changed = form.has_changed()
                qform = form.save(commit=False)
                if qform.status != 0:
                    if 'save' in request.POST and changed:
                        qform.status = 3
                    if qform.send == True and 'send_to_check' in request.POST:
                        qform.status = 1
                    qform.send = False
                    qform.name_of_user = credits
                    qform.verificator = choose_ver
                    qform.save()
                else:
                    continue

            credits_for_url = re.sub(r"\s", '+', credits)
            choose_ver_for_url = re.sub(r"\s", "+", choose_ver)
            return HttpResponseRedirect(f"?credits={credits_for_url}&choose_ver={choose_ver_for_url}")
        else:
            print(formset.errors)
    else:
        formset = CardFormSetCertain(queryset=data)

    context = {'formset': formset,
               'credits': credits,
               'choose_ver': choose_ver,
               }
    return render(request, "user_page.html", context)


def cards_owner_certain(request):

    choose_own = request.GET['choose_own']
    data = Card.objects.filter(fio__exact=choose_own, verificator__exact='-', delete=0)
    config_data = Config.objects.first()
    # allow_edit = config_data.allow_edit

    if request.method == 'POST':
        formset = CardFormSetCertain(request.POST, queryset=data)
        if formset.is_valid():
            # if allow_edit == False:
            #     return redirect('user_certain')
            for form in formset:
                changed_data = form.changed_data
                changed = form.has_changed()
                qform = form.save(commit=False)
                if qform.status != 0:
                    if 'save' in request.POST and changed:
                        qform.status = 3
                    if qform.send == True and 'send_to_check' in request.POST:
                        qform.status = 1
                    qform.send = False
                    qform.name_of_user = choose_own
                    qform.fio = choose_own
                    qform.save()
                else:
                    continue

            choose_own_for_url = re.sub(r"\s", "+", choose_own)
            return HttpResponseRedirect(f"?choose_own={choose_own_for_url}")
        else:
            print(formset.errors)
    else:
        formset = CardFormSetCertain(queryset=data)

    context = {'formset': formset,
               'choose_own': choose_own,
               }
    return render(request, "owner_page.html", context)


def import_excel(request):
    try:
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            empexceldata = pd.read_excel('.' + excel_file, engine='openpyxl') #Назвать исходный файл латиницей
            dbframe = empexceldata
            for i in range(dbframe.shape[0]):  # iterate over rows
                for j in range(dbframe.shape[1]):  # iterate over columns
                    if isinstance(dbframe.iloc[i, j], datetime.datetime):
                        dbframe.iloc[i, j] = dbframe.iloc[i, j].strftime('%d.%m.%Y')  # Задаем формат даты
            # Получим общий список записей
            dflist = []
            for i in dbframe.index:
                dflist.append(list(dbframe.iloc[i]))
            # Получим список мультиверификаторных записей
            list_value = []  # Записи с мультмиверификаторами
            names = []  # Массив разбитых имен мильтиверификаторов
            for i in dbframe.index:
                if (dbframe['Верификатор'][i] == dbframe['Верификатор'][i]) and ('/' in str(dbframe['Верификатор'][i])):
                    names.append(str(dbframe['Верификатор'][i]).replace('/ ', '/').split('/'))
                    list_value.append(list(dbframe.iloc[i]))
            # Получим список записей с разбитыми мультиверификаторными записями
            i = 0
            k = 0  # Индекс в массиве мультиверификаторных записей
            while k < len(list_value):
                if list_value[k] == dflist[i]:
                    dflist.pop(i)
                    for t in range(len(names[k])):
                        dflist.insert(i + t, list_value[k].copy())
                        dflist[i + t][-1] = names[k][t]
                    k += 1
                i += 1
            # Осуществим обратное преобразование в датафрейм
            cols = dbframe.columns
            dbframe = pd.DataFrame(dflist)
            dbframe.columns = cols
            # Уберем NaN
            for i in range(dbframe.shape[0]):  # iterate over rows
                for j in range(dbframe.shape[1]):  # iterate over columns
                    if dbframe.iloc[i, j] != dbframe.iloc[i, j]:
                        dbframe.iloc[i, j] = "-"
            for dbframe in dbframe.itertuples():
                obj = Card.objects.create(name_of_user='start_user', organization=dbframe[1], fio=dbframe[2],
                                          role=dbframe[3], type=dbframe[4],
                                          name=dbframe[5], method=dbframe[6],
                                          low_level=dbframe[7], target_level=dbframe[8],
                                          high_level=dbframe[9], weight=dbframe[10],
                                          verificator=dbframe[11])
                obj.save()

            return render(request, 'import_excel.html', {
                'uploaded_file_url': uploaded_file_url
            })
    except Exception as identifier:
        print(identifier)

    return render(request, 'import_excel.html', {})


class UserPivotView(SingleTableView):
    template_name = "user_pivot_tab.html"
    table_class = CardTable
    queryset = Card.objects.filter(status=0, delete=0)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = Card.objects.filter(status=0, delete=0)
        context['data'] = data

        return context

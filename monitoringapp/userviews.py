import re
from django_tables2 import SingleTableView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .tables import *


# Create your views here.

def choosing_form(request):
    un_ver = Card.objects.all().values_list('verificator', flat=True).distinct()
    print(un_ver)
    if request.method == 'POST':
        if request.POST['choose_ver'] != 'Выберите верификатора':
            data = Card.objects.filter(verificator__exact=request.POST['choose_ver'], delete=0)
            formset = CardFormSetCertain(queryset=data)
            return render(request, "choosing_form.html", {'formset': formset, 'un_ver': un_ver})
    return render(request, "choosing_form.html", {'un_ver': un_ver})


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
                if qform.status!=0:

                    if 'save' in request.POST and changed :
                        qform.status = 3
                    if qform.send == True and qform.status == 3 and 'send_to_check' in request.POST:
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
        formset = CardFormSetCertain(queryset=data)

    context = {'formset': formset,
               'credits': credits,
               'choose_ver': choose_ver,
               }
    return render(request, "user_page.html", context)


class UserPivotView(SingleTableView):
    template_name = "user_pivot_tab.html"
    table_class = CardTable
    queryset = Card.objects.filter(status=0, delete=0)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = Card.objects.filter(status=0, delete=0)
        context['data'] = data

        return context

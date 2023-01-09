from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .admin_forms import *
from .models import *
from django_tables2 import SingleTableView
from .tables import *

# class AdminPivotView(TemplateView):
#     template_name = "admin_pivot_tab.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         data = Card.objects.filter(status=0, delete=0)
#         formset = AdminCardFormSet(queryset=data)
#         context['formset'] = formset
#
#         return context


class AdminPivotView(SingleTableView):
    SingleTableView.table_pagination = False
    template_name = "admin_pivot_tab.html"
    table_class = AdminCardTable
    # queryset = Card.objects.filter(status=0, delete=0)
    queryset = Card.objects.filter(delete=0)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # data = Card.objects.filter(status=0, delete=0)
        data = Card.objects.filter(delete=0)
        context['data'] = data

        return context


class OnCheckingView(TemplateView):
    template_name = "admin_onchecking.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = Card.objects.filter(status=1, delete=0)
        formset = AdminCardFormSet(queryset=data)
        context['formset'] = formset

        return context

    def post(self, request):
        data = Card.objects.filter(status=1, delete=0)

        formset = AdminCardFormSet(request.POST, queryset=data)
        for form in formset:

            if form.is_valid():
                qform = form.save(commit=False)
                qform.save()

            else:
                print(form.errors.as_data())
        return redirect(reverse_lazy("onchecking"))


def accept_kpi(request, pk):
    card_data = get_object_or_404(Card, pk=pk)
    card_data.status = 0
    card_data.save(update_fields=['status'])
    return redirect('onchecking')


def reject_kpi(request, pk):

    card_data = get_object_or_404(Card, pk=pk)
    card_data.status = 2
    card_data.save(update_fields=['status'])
    return redirect('onchecking')


def reject_pivot(request, pk):

    card_data = get_object_or_404(Card, pk=pk)
    if card_data.status == 0:
        card_data.status = 2
    card_data.save(update_fields=['status'])
    return redirect('admin_pivot')




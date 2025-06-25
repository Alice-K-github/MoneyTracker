from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
import recs.forms
from datetime import datetime
import categorys.models
from django.db.models import Q

from unicodedata import category


# Домашняя страница
def home(request):
    return render(request, 'home.html')


# Страница справочника
def directory(request):
    return render(request, 'directory.html')


# Создание статуса
class StatusCreateView(CreateView):
    model = recs.models.Status # Подключение модели
    form_class = recs.forms.StatusForm # Подключение формы
    template_name = 'Status/status_form.html' # шаблон
    success_url = reverse_lazy('recs:status_list') # Перенаправление после успешного создания


# Список статусов
class StatusListView(ListView):
    model = recs.models.Status # Подключение модели
    template_name = 'Status/status_list.html' # шаблон


# Редактирование статуса
class StatusUpdateView(UpdateView):
    model = recs.models.Status # Подключение модели
    form_class = recs.forms.StatusForm # Подключение формы
    template_name = 'Status/status_form.html' # шаблон
    success_url = reverse_lazy('recs:status_list') # Перенаправление после успешного редактирования


# Удаление статуса
class StatusDeleteView(DeleteView):
    model = recs.models.Status # Подключение модели
    template_name = 'Status/status_delete.html' # шаблон
    success_url = reverse_lazy('recs:status_list') # Перенаправление после удаления


# Создание типа
class TypeCreateView(CreateView):
    model = recs.models.Type # Подключение модели
    form_class = recs.forms.TypeForm # Подключение формы
    template_name = 'Type/type_form.html' # шаблон
    success_url = reverse_lazy('recs:home') # Перенаправление после успешного создания типа


# Список типов
class TypeListView(ListView):
    model = recs.models.Type # Подключение модели
    template_name = 'Type/type_list.html' # шаблон


# Редактирование типа
class TypeUpdateView(UpdateView):
    model = recs.models.Type # Подключение модели
    form_class = recs.forms.TypeForm # Подключение формы
    template_name = 'Type/type_form.html' # шаблон
    success_url = reverse_lazy('recs:type_list') # Перенаправление после успешного редактирования типа


# Удаление типа
class TypeDeleteView(DeleteView):
    model = recs.models.Type # Подключение типа
    template_name = 'Type/type_delete.html' # шаблон
    success_url = reverse_lazy('recs:type_list') # Перенаправление после удаления типа


# Создание записи
class RecordCreateView(CreateView):
    model = recs.models.Record # Подключение модели
    form_class = recs.forms.RecordForm # Подключение формы
    template_name = 'Records/Record_form.html' # шаблон
    success_url = reverse_lazy('recs:records_list') # перенаправление после создания записи

    def form_valid(self, form):
        # Автоматическое добавление даты создания
        form.instance.created_at = datetime.now()
        return super().form_valid(form)


# Список записей
class RecordListView(ListView):
    model = recs.models.Record # Подключение модели
    template_name = 'Records/Record_list.html' # шаблон
    context_object_name = 'records'

    def get_queryset(self):
        queryset = super().get_queryset()
        record_status = self.request.GET.get('record_status')
        record_type = self.request.GET.get('record_type')
        record_category = self.request.GET.get('record_category')
        record_subcategory = self.request.GET.get('record_subcategory')

        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')

        if start_date_str and end_date_str:
            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
                queryset = queryset.filter(
                    Q(created_at__gte=start_date) & Q(created_at__lte=end_date)
                )
            except ValueError:
                pass

        if record_status:
            queryset = queryset.filter(status_id=record_status)
        if record_type:
            queryset = queryset.filter(type_id=record_type)
        if record_category:
            queryset = queryset.filter(category_id=record_category)
        if record_subcategory:
            queryset = queryset.filter(subcategory_id=record_subcategory)
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['record_statuss'] = recs.models.Status.objects.all()
        context['record_types'] = recs.models.Type.objects.all()
        context['record_categorys'] = categorys.models.Category.objects.all()
        context['record_subcategorys'] = categorys.models.Sub_Category.objects.all()
        return context


# Редактирование записи
class RecordUpdateView(UpdateView):
    model = recs.models.Record # Подключение модели
    form_class = recs.forms.RecordUpdateForm # Подключение формы
    template_name = 'Records/record_update_form.html' # шаблон
    success_url = reverse_lazy('recs:records_list') # Перенаправление после успешного редактирования записи


# Удаление записи
class RecordDeleteView(DeleteView):
    model = recs.models.Record # Подключение модели
    template_name = 'Records/record_delete.html' # шаблон
    success_url = reverse_lazy('recs:records_list') # Перенаправление после удаления записи

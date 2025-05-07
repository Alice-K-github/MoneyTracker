from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
import recs.forms
from datetime import datetime


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

    def get_queryset(self):
        return recs.models.Record.objects.all()


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

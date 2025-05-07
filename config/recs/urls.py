from django.contrib import admin
from django.urls import path
import recs.views

app_name = 'recs' # Название приложения

urlpatterns = [
    path("admin/", admin.site.urls), # Админка
    path('', recs.views.home, name='home'), # Главная домашняя страница
    path('directory/', recs.views.directory, name='directory'), # Справочник

    path('record/new/', recs.views.RecordCreateView.as_view(), name='Record_create'), # Создание записи
    path('records/list/', recs.views.RecordListView.as_view(), name='records_list'), # Список записей
    path('record/<int:pk>/update', recs.views.RecordUpdateView.as_view(), name='record_update'), # Редактирование записи
    path('record/<int:pk>/detele', recs.views.RecordDeleteView.as_view(), name='record_delete'), # Удаление записи

    path('status/new/', recs.views.StatusCreateView.as_view(), name='status_create'), # Создание статуса
    path('status/list/', recs.views.StatusListView.as_view(), name='status_list'), # Список статусов
    path('status/<int:pk>/update', recs.views.StatusUpdateView.as_view(), name='status_update'), # Редактирование статуса
    path('status/<int:pk>/detele', recs.views.StatusDeleteView.as_view(), name='status_delete'), # Удаление статуса

    path('type/new/', recs.views.TypeCreateView.as_view(), name='type_create'), # Создание типа
    path('type/list/', recs.views.TypeListView.as_view(), name='type_list'), # Список типов
    path('type/<int:pk>/update', recs.views.TypeUpdateView.as_view(), name='type_update'), # Редактирование типа
    path('type/<int:pk>/detele', recs.views.TypeDeleteView.as_view(), name='type_delete'), # Удаление типа
    ]

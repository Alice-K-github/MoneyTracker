from django.contrib import admin
from django.urls import path
import categorys.views


app_name = 'categorys' # Название приложения

urlpatterns = [
    path("admin/", admin.site.urls),
    path('category/list/', categorys.views.CategoryListView.as_view(), name='category_list'), # Список категорий
    path('category/new/', categorys.views.CategoryCreateView.as_view(), name='category_create'), # Создание категории
    path('category/<int:pk>/update', categorys.views.CategoryUpdateView.as_view(), name='category_update'), # Редактирование категории
    path('category/<int:pk>/detele', categorys.views.CategoryDeleteView.as_view(), name='category_delete'), # Удаление категории

    path('subcategory/list/', categorys.views.Sub_CategoryListView.as_view(), name='subcategory_list'), # Список подкатегорий
    path('subcategory/new/', categorys.views.Sub_CategoryCreateView.as_view(), name='subcategory_create'), # Создание подкатегории
    path('subcategory/<int:pk>/update', categorys.views.Sub_CategoryUpdateView.as_view(), name='subcategory_update'), # Редактирование подкатегории
    path('subcategory/<int:pk>/detele', categorys.views.Sub_CategoryDeleteView.as_view(), name='subcategory_delete'), # Удаление подкатегории
    ]

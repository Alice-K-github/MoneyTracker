from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
import categorys.forms


# Список категорий
class CategoryListView(ListView):
    model = categorys.models.Category # Подключение модели
    template_name = 'category_list.html' # шаблон


# Создание категории
class CategoryCreateView(CreateView):
    model = categorys.models.Category # Подключение модели
    form_class = categorys.forms.CategoryForm # Подключение формы
    template_name = 'category_form.html' # шаблон
    success_url = reverse_lazy('categorys:category_list') # Перенаправление после успешного создания


# Редактирование категории
class CategoryUpdateView(UpdateView):
    model = categorys.models.Category # Подключение модели
    form_class = categorys.forms.CategoryForm # Подключение формы
    template_name = 'category_form.html' # шаблон
    success_url = reverse_lazy('categorys:category_list') # Перенаправление после успешного редактирования категории


# Удаление категории
class CategoryDeleteView(DeleteView):
    model = categorys.models.Category # Подключение модели
    template_name = 'category_delete.html' # шаблон
    success_url = reverse_lazy('categorys:category_list') # Перенаправление после удаления категории


# Список подкатегорий
class Sub_CategoryListView(ListView):
    model = categorys.models.Sub_Category # Подключение модели
    template_name = 'subcategory_list.html' # шаблон


# Создание подкатегории
class Sub_CategoryCreateView(CreateView):
    model = categorys.models.Sub_Category # Подключение модели
    form_class = categorys.forms.Sub_CategoryForm # Подключение формы
    template_name = 'subcategory_form.html' # шаблон
    success_url = reverse_lazy('categorys:subcategory_list') # Перенаправление после успешного создания категории


# Редактирование подкатегории
class Sub_CategoryUpdateView(UpdateView):
    model = categorys.models.Sub_Category # Подключение модели
    form_class = categorys.forms.Sub_CategoryForm # Подключение формы
    template_name = 'subcategory_form.html' # шаблон
    success_url = reverse_lazy('categorys:subcategory_list') # Пренаправление после успешного редактирования подкатегории


# Удаление категории
class Sub_CategoryDeleteView(DeleteView):
    model = categorys.models.Sub_Category # Подключение модели
    template_name = 'subcategory_delete.html' # шаблон
    success_url = reverse_lazy('categorys:subcategory_list') # Перенаправление после удаления категории

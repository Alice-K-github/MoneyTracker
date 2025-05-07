from django import forms
from .models import Category, Sub_Category


# Форма для категорий
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category # Модель
        # Включённые в форму элементы модели
        fields = ['name', 'type']

    def __init__(self, *args, **kwargs):
        # Подключение стилизации полей формы
        super(CategoryForm, self).__init__(*args, **kwargs)

        # Настройка атрибутов виджета для поля 'name'
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите наименование категории'  # Текст подсказки внутри поля
        })

        self.fields['type'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
        })


# Форма для подкатегории
class Sub_CategoryForm(forms.ModelForm):
    class Meta:
        model = Sub_Category # Модель
        # Включённые в форму элементы модели
        fields = ['name', 'category']

    def __init__(self, *args, **kwargs):
        # Подключение стилизации полей формы
        super(Sub_CategoryForm, self).__init__(*args, **kwargs)

        # Настройка атрибутов виджета для поля 'name'
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите наименование категории'  # Текст подсказки внутри поля
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
        })

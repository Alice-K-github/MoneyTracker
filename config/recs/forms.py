from django import forms
from .models import Status, Type, Record


class StatusForm(forms.ModelForm):
    # Форма для создания\редактирования статуса
    class Meta:
        model = Status # Модель
        # Включённые в форму элементы модели
        fields = ['name']

    def __init__(self, *args, **kwargs):
        # Подключение стилизации полей формы
        super(StatusForm, self).__init__(*args, **kwargs)

        # Настройка атрибутов виджета для поля 'name'
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите наименование статуса'  # Текст подсказки внутри поля
        })


class TypeForm(forms.ModelForm):
    # Форма для создания\редактирования типа
    class Meta:
        model = Type # Модель
        # Включённые в форму элементы модели
        fields = ['name']

    def __init__(self, *args, **kwargs):
        # Подключение стилизации полей формы
        super(TypeForm, self).__init__(*args, **kwargs)

        # Настройка атрибутов виджета для поля 'name'
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите наименование типа операции'  # Текст подсказки внутри поля
        })


class RecordForm(forms.ModelForm):
    # Форма для создания записи
    class Meta:
        model = Record # Модель
        # Включённые в форму элементы модели
        fields = ['status', 'type', 'category', 'subcategory', 'summ', 'comment']

    def __init__(self, *args, **kwargs):
        # Подключение стилизации полей формы
        super(RecordForm, self).__init__(*args, **kwargs)

        # Настройка атрибутов виджета
        self.fields['status'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
        })

        # Настройка атрибутов виджета
        self.fields['type'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
        })

        # Настройка атрибутов виджета
        self.fields['category'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
        })

        # Настройка атрибутов виджета
        self.fields['subcategory'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
        })

        # Настройка атрибутов виджета
        self.fields['summ'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
        })

        # Настройка атрибутов виджета
        self.fields['comment'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
        })


    def clean(self):
        # Валидация соответствия полей
        cleaned_data = super().clean() # Получаем значения
        category = cleaned_data.get('category') # Значение категории
        subcategory = cleaned_data.get('subcategory') # Значение подкатегории
        type = cleaned_data.get('type') # Значения типа

        if subcategory.category != category:
            # Проверка того, что подкатегория относится к соответствующей категории
            self.add_error('subcategory', 'Подкатегория не относится к этой категории')

        if category.type != type:
            # Проверка того, что категория относится к соответствующему типу
            self.add_error('type', 'Категория не относится к выбранному типу')


class RecordUpdateForm(forms.ModelForm):
    # Форма редактирования записи
    class Meta:
        model = Record # Модель
        # Включённые в форму элементы модели
        fields = ['created_at', 'status', 'type', 'category', 'subcategory', 'summ', 'comment']

    def __init__(self, *args, **kwargs):
        # Подключение стилизации полей формы
        super(RecordUpdateForm, self).__init__(*args, **kwargs)

        # Настройка атрибутов виджета
        self.fields['created_at'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
        })

        # Настройка атрибутов виджета
        self.fields['status'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
        })

        # Настройка атрибутов виджета
        self.fields['type'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
        })

        # Настройка атрибутов виджета
        self.fields['category'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
        })

        # Настройка атрибутов виджета
        self.fields['subcategory'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
        })

        # Настройка атрибутов виджета
        self.fields['summ'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
        })

        # Настройка атрибутов виджета
        self.fields['comment'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
        })

    def clean(self):
        # Валидация соответствия полей
        cleaned_data = super().clean()  # Получаем значения
        category = cleaned_data.get('category')  # Значение категории
        subcategory = cleaned_data.get('subcategory')  # Значение подкатегории
        type = cleaned_data.get('type')  # Значения типа

        if subcategory.category != category:
            # Проверка того, что подкатегория относится к соответствующей категории
            self.add_error('subcategory', 'Подкатегория не относится к этой категории')

        if category.type != type:
            # Проверка того, что категория относится к соответствующему типу
            self.add_error('type', 'Категория не относится к выбранному типу')

from django.contrib import admin
from .models import News, Category, Appointment


def nullfy_quantity(modeladmin, request, queryset):
    queryset.update(title='', text='')


nullfy_quantity.short_description = 'Очистить список новостей'


class NewsModel(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('title', 'text')  # оставляем только имя и цену товара
    list_filter = ('title', 'pub_date')  # добавляем примитивные фильтры в нашу админку
    search_fields = ('title', 'pub_date')  # тут всё очень похоже на фильтры из запросов в базу
    actions = [nullfy_quantity]  # добавляем действия в список


admin.site.register(News, NewsModel)
admin.site.register(Category)
admin.site.register(Appointment)


# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, View

from .filters import NewsFilter
from .forms import NewsForm
from .models import News, Appointment

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import mail_managers  # импортируем класс для создание объекта письма с html
from django.template.loader import render_to_string  # импортируем функцию, которая срендерит наш html в текст
# from django.utils.decorators import method_decorator
from django.shortcuts import render, HttpResponseRedirect, redirect
from datetime import datetime
from django.core.cache import cache

from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.db.models.signals import post_save
from django.dispatch import receiver

class NewsList(LoginRequiredMixin, ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = News
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'title'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news_list.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news_list'
    paginate_by = 2  # Вот так мы можем указать(ограничить) кол-во записей на странице

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем Обычный запрос
        queryset = super().get_queryset()
        '''
            # Используем наш класс фильтрации.
       # self.request.GET содержит объект QueryDict, который мы рассматривали
       # в этом юните ранее.
       # Сохраняем нашу фильтрацию в объекте класса,
       # чтобы потом добавить в контекст и использовать в шаблоне.
        '''
        self.filterset = NewsFilter(self.request.GET, queryset)
        # Возвращаем из функций отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст обьект фильтраций
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    # Модель та же, но мы хотим получать информацию по отдельности
    model = News
    # Используем другой шаблон product.html
    template_name = 'news_detail.html'
    # Название обьекта, в которм будет выбранный пользователем продукт
    context_object_name = 'news_detail'

    # queryset = News.objects.all()
    #
    # def get_object(self, *args, **kwargs):
    #
    #     obj = cache.get(f'news_detail{self.kwargs["pk"]}', None)  # кэш очень похож на словарь, и метод get действует так же. Он забирает значение по ключу, если его нет, то забирает None.
    #
    #     # если объекта нет в кэше, то получаем его и записываем в кэш
    #
    #     if not obj:
    #         obj = super().get_object(queryset=self.queryset)
    #         cache.set(f'news_detail-{self.kwargs["pk"]}', obj)
    #
    #     return obj



# Добавляем новое представление для создания товаров
class NewsCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = NewsForm
    # Модель товаров
    model = News
    # и новый шаблон, в котором используется форма.
    template_name = 'news_edit.html'



# Добавляем представление для изменения товара
class NewsUpdate(LoginRequiredMixin, UpdateView):
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'
    success_url = reverse_lazy('mails:news_list')
    # context_object_name = 'update'

# Представление удаляющее товар.
class NewsDelete(DeleteView):
    model = News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('mails:news_list')
    # context_object_name = 'delete'


# Пример использование метод_декоратор, для предостовление сайта пользователю, при условий аунентификациий
# @method_decorator(login_required, name='dispatch')
# class ProtectedView(TemplateView):
#     template_name = 'prodected_page.html'


# Пример использований миксина LoginRequiredMixin ещё проще.
# Всего лишь необходимо добавить его в списке наследуемых классов при создании представления.
class SuccessView(TemplateView):
    template_name = 'success.html'




# Авторизация и Регистрация
# Использование декоратора login_required;
# @method_decorator(login_required, name='dispatch')
# class NewsedView(TemplateView):
#     template_name = 'newsed_page.html'

'''
    Использование миксина LoginRequiredMixin ещё проще. 
    Всего лишь необходимо добавить его в списке наследуемых 
    классов при создании представления.
'''


# class NewsedView(LoginRequiredMixin, TemplateView):
#     template_name = 'newsed_page.html'

# @login_required
# def profile_view(request):
    # return render(request, 'profile.html')


# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, View
from .models import News, Appointment
from .forms import NewsForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
# from django.utils.decorators import method_decorator
from django.shortcuts import render, HttpResponseRedirect, redirect
from datetime import datetime
from django.core.cache import cache

class NewsList(ListView):
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


class NewsDetail(DetailView):
    # Модель та же, но мы хотим получать информацию по отдельности
    # model = News
    # Используем другой шаблон product.html
    template_name = 'news_detail.html'
    # Название обьекта, в которм будет выбранный пользователем продукт
    context_object_name = 'news_detail'

    queryset = News.objects.all()

    def get_object(self, *args, **kwargs):

        obj = cache.get(f'news_detail-{self.kwargs["pk"]}', None)  # кэш очень похож на словарь, и метод get действует так же. Он забирает значение по ключу, если его нет, то забирает None.

        # если объекта нет в кэше, то получаем его и записываем в кэш

        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'news_detail-{self.kwargs["pk"]}', obj)

        return obj


# Добавляем новое представление для создания товаров
class NewsCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = NewsForm
    # Модель товаров
    model = News
    # и новый шаблон, в котором используется форма.
    template_name = 'news_edit.html'


# Добавляем представление для изменения товара
class NewsUpdate(UpdateView):
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'
    context_object_name = 'update'


# Представление удаляющее товар.
class NewsDelete(DeleteView):
    model = News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')
    context_object_name = 'delete'


# Пример использование метод_декоратор, для предостовление сайта пользователю, при условий аунентификациий
# @method_decorator(login_required, name='dispatch')
# class ProtectedView(TemplateView):
#     template_name = 'prodected_page.html'


# Пример использований миксина LoginRequiredMixin ещё проще.
# Всего лишь необходимо добавить его в списке наследуемых классов при создании представления.
class NewsView(LoginRequiredMixin, TemplateView):
    template_name = 'news_page.html'


# Отправка писем по электронной почте
class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mails.html')

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()

        send_mail(
            subject=f'{appointment.client_name}: {appointment.date.strftime("%Y-%m-%d")}',
            message=appointment.message,
            from_email='imaralievasadbek@yandex.ru',
            recipient_list=['imaraliev.kg2005@gmail.com']
        )

        return redirect('mails:mails')


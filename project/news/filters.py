from django_filters import FilterSet
from .models import News


''' 
Создаем свой набор фильтров для модели News.
FilterSet, который мы наследуем,
должен чем-то напомнить знакомые вам Django дженерики.
'''
class NewsFilter(FilterSet):
    class Meta:
        # В Meta классе мы должны указать Django модель, в которой будем фильтровать записи.
        model = News
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            # Поиск по названию
            'title': ['icontains'],
        }

    '''
    Теперь созданный нами класс нужно использовать в представлении 
    (view) для фильтрации списка товаров.
    
    Вот таким вот образом:
        class ProductsList(ListView):
   model = Product
   ordering = 'name'
   template_name = 'products.html'
   context_object_name = 'products'
   paginate_by = 2

   # Переопределяем функцию получения списка товаров
   def get_queryset(self):
       # Получаем обычный запрос
       queryset = super().get_queryset()
       # Используем наш класс фильтрации.
       # self.request.GET содержит объект QueryDict, который мы рассматривали
       # в этом юните ранее.
       # Сохраняем нашу фильтрацию в объекте класса,
       # чтобы потом добавить в контекст и использовать в шаблоне.
       self.filterset = ProductFilter(self.request.GET, queryset)
       # Возвращаем из функции отфильтрованный список товаров
       return self.filterset.qs

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       # Добавляем в контекст объект фильтрации.
       context['filterset'] = self.filterset
       return context
    '''




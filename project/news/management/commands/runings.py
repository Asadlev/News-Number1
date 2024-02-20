from django.core.management.base import BaseCommand, CommandError
from news.models import News, Category


# class Command(BaseCommand):
#     help = '''Documentation
#     Обнуляет все новости'''
#
#     def hundle(self, *args, **kwargs):
#         for new in News.objects.all():
#             new.title = ''
#             new.save()
#
#             self.stdout.write(self.style.SUCCESS('null news "%s"'% str(new)))

'''
Задание
    Доработайте свой интернет-сервис. 
    Напишите команду для manage.py, 
    которая будет удалять все 
    новости из какой-либо категории, 
    но только при 
    подтверждении действия в консоли при выполнении команды.
'''
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Подсказка вашей команды'

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        answer = input(f'Вы правда хотите удалить все статьи в категории {options["category"]}? yes/no')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))
            return
        try:
            category = Category.objects.get(name=options['category'])
            Category.objects.filter(category=category).delete()
            self.stdout.write(self.style.SUCCESS(f'Succesfully deleted all news from category {category.name}')) # в случае неправильного подтверждения говорим, что в доступе отказано
        except Category.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Could not find category {Category}'))
https://github.com/VladPath/Django_PhoneShop/assets/146530026/14a05635-d31c-42e9-88bc-850bd78c20b2

runserver
для запуска сервера ls - проверка положения  
-cd phoneShop / python3 manage.py runserver

run tailwind
для запуска tailwind ls - проверка положения 
 -cd phoneShop / npm run build


продвижение создания моего сайта 'PHONE SHOP'

                14 шаг

объединение html в файле бейз для избежания копирования кода 
создавая в базе стили и разметку мы переносим ее как шаблон в остальные файлы 
с помощью {% extends "./base.html" %} это позволяет нам избежать копирование кода 
в базовый мы загружаем тайливнд стили и прочие повторяющиеся моменты 
    {% block content %}
    {% endblock content %} - определяет индивидуальный контент для каждого файла отличающийся от базы 
создание файла navbar.html - хранение кода навбара в этом файле и связка в базу с помощью 
    {% include "./navbar.html" %}

                шаг 15 

добавление фотографий в джанго 
в файле моделс добавляем  в класс myproducts / image = models.ImageField(blank=True, upload_to='images')

в сетингс прописываем 
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

в phoneShop/urls
from django.conf.urls.static import static

from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
связываем настройки с помощью python3 manage.py makemigrations and migrate

в панеле админа появилась возможность добавлять фотографии к экземплярам телефонов 
добавляем их в файле html с помощью             
<img src="{{item.image.url}}" alt="">

                шаг 16

корректируем стили для main
сетка общая  - <div class="p-10 grid grid-cols-1 sm:grid-cols-1 md:grid-cols-3 xl:grid-cols-3 lg:grid-cols-3 gap-3">
для элементов <div class="rounded overflow-hidden shadow-lg">

                шаг 17
                

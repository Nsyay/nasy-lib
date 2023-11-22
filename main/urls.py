from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('book_entry', book_entry, name='book_entry'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
    path('book_delete/<str:pk>/', book_delete, name='book_delete'),
    path('add_amount/<str:pk>/', add_amount, name='add_amount'),
    path('sub_amount/<str:pk>/', sub_amount, name='sub_amount'),
    path('get-book/', get_book_json, name='get_book_json'),
    path('entry-book-ajax/', create_ajax, name='create_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]
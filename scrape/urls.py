from django.urls import path
from scrape.views import *

app_name = 'scrape'
urlpatterns = [
    path('', scrape, name='scrape'),
    path('change_path/<int:path_id>/', change_path, name='change_path'),
    path('add_files', add_files, name="add_files"),
    path('add_all_files', add_all_files, name="add_all_files"),
    # path('test/', test_view, name="test_view")
]

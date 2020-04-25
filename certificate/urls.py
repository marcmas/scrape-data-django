from django.urls import path
from certificate.views import *

app_name = 'certificate'
urlpatterns = [
    path('create/', create, name='create'),
    path('<int:certificate_id>/', detail, name='detail'),
    path('<int:certificate_id>/accept', accept, name='accept'),
    path('<int:certificate_id>/delete', delete, name='delete'),
    path('lists/', lists, name='lists'),
    path('confirm_lists/', confirm_lists, name='confirm_lists'),
    path('cancle_lists/', cancle_lists, name='cancle_lists'),
    path('<int:certificate_id>/pdf', print_pdf, name='print_pdf'),
    path('<int:certificate_id>/downloadpdf', download_pdf, name='download_pdf'),

]

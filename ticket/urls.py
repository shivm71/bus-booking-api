from django.urls import path

from . import views

app_name = 'ticket'

urlpatterns = [
    # path('', views.homeview.as_view(), name='index'),
    path('', views.show_dates, name='index'),
    path('<pk>/', views.show_ticket, name='datetotic'),
    path('book/<tk>/', views.book_ticket, name='booktic'),
]


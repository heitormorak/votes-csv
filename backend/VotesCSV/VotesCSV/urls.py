from django.contrib import admin
from django.urls import include, path
from appcsv import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('legislator_votes/', views.legislator_votes_view, name='legislator_votes'),
    path('bill_votes/', views.bill_votes_view, name='bill_votes'),
]
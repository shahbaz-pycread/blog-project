from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('post/<int:id>/', views.post, name='post_detail'),
	path('category/<str:foo>/', views.category, name='category'),
	path('contact/', views.contact, name='contact')
]
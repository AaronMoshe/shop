from django.urls import path
from . import views

app_name = 'contact_app'

urlpatterns = [
	path('contact_form/', views.contact_form, name='contact_form'),
	path('contact_form/sucess/', views.sucess, name='sucess')
]
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from menus import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),

    path('section/<str:section_name>/', views.section_view, name='section'),

    path('for_clients/', TemplateView.as_view(template_name='named_url/for_clients.html'), name='for_clients'),
    path('about/', TemplateView.as_view(template_name='named_url/about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='named_url/contact.html'), name='contact'),
    path('reviews/', TemplateView.as_view(template_name='named_url/reviews.html'), name='reviews'),
]

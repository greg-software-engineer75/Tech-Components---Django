from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from . import authentication, products

app_name = 'components'

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('', RedirectView.as_view(pattern_name='components:login')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', authentication.register, name='register'),

    path('products/create/', products.create_component, name='create_component'),
    path('products/list/', products.list_components, name='list_components'),
    path('products/update/<int:component_id>/', products.edit_component, name='edit_component'),
    path('products/delete/<int:component_id>/', products.delete_component, name='delete_component'),
]
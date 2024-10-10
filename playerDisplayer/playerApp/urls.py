from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Usar una cadena vacía para que sea la URL de inicio.
    path("", views.index, name="index"),
    path('add_default/', views.add_default, name='add_default'),
    path('displayer/<int:item_id>/', views.displayer, name='displayer'),
    path('ok/', views.ok, name='ok'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('protect_page/', views.protect_page, name='protect_page'),
    path('register/', views.register, name='register'),
    path('register/protect_page/', views.protect_page, name='protect_page'),
    path('stats/', views.stats, name='stats'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
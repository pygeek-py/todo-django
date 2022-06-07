from django.urls import path  
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('create/', views.create, name="create"),
    path('up/<str:pk>', views.update, name="update"),
    path('delete/<str:pk>', views.del_view, name="del_view"),
    path('dis/<str:pk>', views.disdate, name="disdate"),
    
    path('register/', views.register, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

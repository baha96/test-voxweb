from django.urls import path
# from django.conf.urls import include, url

from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='registor'),
    path('auth/', views.LoginView.as_view(), name='login'),
    path('get/user/', views.MyProfileGetView.as_view(), name='my-profile'),
    path('<int:pk>/change-data/', views.ProfileEditView.as_view(), name='change-profile-data'),
]

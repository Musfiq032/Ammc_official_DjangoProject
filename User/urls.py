from django.urls import path
from User.views import login_register_view

app_name= 'User'

urlpatterns = [

         path('register_login_user/', login_register_view, name='register-login'),
        # path('logout_user/', views.user_logout, name='logout'),
        # path('user_details/', views.dynamic_lookup_view, name='user-detail'),
        # path('user_list/', views.user_list_view, name= 'user-list')

]

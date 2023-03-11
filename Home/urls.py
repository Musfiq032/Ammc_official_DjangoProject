from Home.views import (home_view,
                        contacts_view,
                        academics_view,
                        history,
                        coming_soon,
                        news_list_view,
                        event_view,
                        notice_view,
                        dynamic_lookup_view,
                        dynamic_lookup_view_dep,
                        faculty_member_view,
                        gallery,
                        notfound,
                        job_view,
                        dynamic_lookup_view_job,
                        course_details,
                        administration,
                        eligibility,
                        fees,
                        application,
                        prospectus_view,governing_body_view)
from django.urls import path

# from django.contrib.auth import views as auth_views

app_name = 'Home'
urlpatterns = [
    path('', home_view, name='Home'),
    # path('department_view/',department_view, name='department'),
    # path('service/',service_view,name='service'),
    # path('appointment/', appointment_view, name= 'appointment'),
    path('contact/', contacts_view, name='contact-us'),
    path('academics/', academics_view, name='academics'),
    path('history/', history, name='History'),
    path('coming-soon/', coming_soon, name='coming-soon'),
    path('news/', news_list_view, name="all-news"),
    path('news-details/<int:id>/', dynamic_lookup_view, name='news-details'),
    path('events/', event_view, name='event'),
    path('notice/', notice_view, name='notice'),
    path('department/<int:id>/', dynamic_lookup_view_dep, name='department-details'),
    path('faculty-member/', faculty_member_view, name='faculty-member'),
    path('gallery/', gallery, name='gallery'),
    path('page-not-found/', notfound, name='404'),
    path('job-circular/', job_view, name='job-circular'),
    path('job-circular-details/<int:id>/', dynamic_lookup_view_job, name='job-circular-details'),
    path('course-details/', course_details, name='course-details'),
    path('administration/', administration, name='administration'),
    path('eligibility/', eligibility, name='eligibility'),
    path('fees/', fees, name='fees'),
    path('application/', application, name='application'),
    path('prospectus_view/', prospectus_view, name='prospectus_view'),
    path('governing_body/', governing_body_view, name='governing_body'),
    



    # path('blog/',blog_view, name='blog'),
    # path('about/',about_us_view,name= 'about'),
    # path('login_user/',views.user_login , name='login'),
    # path('register_user',views.register_view, name= 'register')

]


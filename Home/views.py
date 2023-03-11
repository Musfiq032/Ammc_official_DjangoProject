from django.shortcuts import render
from Home.models import Department, Gallery, News, Category, Notice, FacultyMember,Jobcircular,GoverningBody
from django.db.models import Q
from django.contrib import messages
from django.core.mail import send_mail
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.paginator import Paginator


# Create your views here.
def home_view(request):
    department1 = Department.objects.all()[:5]
    department2 = Department.objects.all()[6:]
    notice = Notice.objects.order_by('-published_date')[:3]
   
    galleries = Gallery.objects.all()
    news = News.objects.order_by('-news_publish_date')[:3]
    context = {
        'department1': department1,
        'department2': department2,
        'gallery': galleries,
        'news': news,
        'notice': notice
    }
    return render(request, 'Home/home-1.html', context)


def dynamic_lookup_view_dep(request, id):
    department1 = Department.objects.all()[:5]
    department2 = Department.objects.all()[6:]
    faculty_members = FacultyMember.objects.all()
    departments = request.GET.get('departments')
    if departments is None:
        pass
    else:
        faculty_members = FacultyMember.objects.filter(faculty_member_department__department_name=departments)

    departments = Department.objects.get(id=id)
    context = {
        'faculty_members': faculty_members,
        'departments': departments,
        'department1': department1,
        'department2': department2
    }
    return render(request, "Home/department.html", context)


def is_valid_queryparam(param):
    return param != '' and param is not None


def news_list_view(request):
    department1 = Department.objects.all()[:5]
    department2 = Department.objects.all()[6:]
    qs = Gallery.objects.all()[:6]
    categories = request.GET.get('categories')
    news = News.objects.all()
    if categories is None:
        filtered_news_list = News.objects.order_by('-news_publish_date')
    else:
        filtered_news_list = News.objects.filter(categories__name=categories)

    title_or_author_query = request.GET.get('title_or_author')

    if is_valid_queryparam(title_or_author_query):
        filtered_news_list = news.filter(Q(title__icontains=title_or_author_query)).distinct()

    elif title_or_author_query is None:
        News.objects.all()

    paginated_filtered_news_list = Paginator(filtered_news_list.all(), 5)
    page_number = request.GET.get('page')
    news_page_object = paginated_filtered_news_list.get_page(page_number)

    nums = "a" * news_page_object.paginator.num_pages

    categories = Category.objects.all()
    context = {
        'categories': categories,
        'news_page_object': news_page_object,
        'department1': department1,
        'department2': department2,
        'nums': nums,
        'qs': qs

    }
    return render(request, "Home/all_news.html", context)



def dynamic_lookup_view(request, id):
    obj = News.objects.get(id=id)
    news = News.objects.all()[:3]
    department1 = Department.objects.all()[:5]
    department2 = Department.objects.all()[6:]
    context = {
        'object': obj,
         'department1': department1,
        'department2': department2,
        'news': news
    }
    return render(request, "Home/news_details.html", context)


def notice_view(request):

    department1 = Department.objects.all()[:5]
    department2 = Department.objects.all()[6:]
    notice = Notice.objects.all()
    p = Paginator(Notice.objects.all(), 3)
    page = request.GET.get('page')
    notice_list = p.get_page(page)
    nums = "a" * notice_list.paginator.num_pages
    context = {
        'notice': notice,
        'department1': department1,
        'department2': department2,
        'notice_list': notice_list,
        'nums': nums
    }

    return render(request, 'Home/notice.html', context)

def contacts_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            email,
            ['info@ammch.edu.bd']
        )
        return render(request, 'Home/contacts.html', {'message_name': name})

    department1 = Department.objects.all()[:5]
    department2 = Department.objects.all()[6:]
    context = {
        'department1': department1,
        'department2': department2,
    }
    return render(request, 'Home/contacts.html', context)



def academics_view(request):
    department1 = Department.objects.all()[:5]
    department2 = Department.objects.all()[6:]
    context = {
        'department1': department1,
        'department2': department2,
    }
    return render(request, 'Home/academics.html', context)
    

def prospectus_view(request):
    department1 = Department.objects.all()[:5]
    department2 = Department.objects.all()[6:]
    context = {
        'department1': department1,
        'department2': department2,
    }
    return render(request, 'Home/prospectus.html', context)
    

def history(request):
    department1 = Department.objects.all()[:5]
    department2 = Department.objects.all()[6:]
    context = {
         'department1': department1,
        'department2': department2,
    }
    return render(request, 'Home/history.html', context)


def coming_soon(request):
    department1 = Department.objects.all()[:5]
    department2 = Department.objects.all()[6:]
    context = {
         'department1': department1,
         'department2': department2
    }
    return render(request, 'Home/coming-soon.html', context)


def event_view(request):
    department1 = Department.objects.all()[:5]
    department2 = Department.objects.all()[6:]
    context = {
         'department1': department1,
        'department2': department2,
    }
    return render(request, 'Home/event-page.html', context)


def faculty_member_view(request):
    department1 = Department.objects.all()[:5]
    department2 = Department.objects.all()[6:]
    faculty_member = FacultyMember.objects.all()
    context = {
        'faculty_member': faculty_member,
            'department1': department1,
        'department2': department2,
    }
    return render(request, 'people.html', context)


def gallery(request):
    qs = Gallery.objects.all()
    department1 = Department.objects.all()[:5]
    department2 = Department.objects.all()[6:]
    year_query = request.GET.get('year')

    if year_query == 'All':
        qs = Gallery.objects.all()
    elif is_valid_queryparam(year_query):
        qs = qs.filter(published_year=year_query)

    context = {
        'gallery': qs,
        'department1': department1,
        'department2': department2,
    }
    return render(request, 'Home/gallery.html', context)
    
def notfound(request):
    department1 = Department.objects.all()[:5]
    department2 = Department.objects.all()[6:]
    context = {
           'department1': department1,
        'department2': department2,
    }
    return render(request, '404.html',context)

def job_view(request):
    department1 = Department.objects.all()[:5]
    department2 = Department.objects.all()[6:]
    job = Jobcircular.objects.all()
    context ={
        'job': job,
        'department1': department1,
        'department2': department2,
    }
    return render(request, 'Home/job-list.html', context)

    
def dynamic_lookup_view_job(request, id):
    obj = Jobcircular.objects.get(id=id)
    department1 = Department.objects.all()[:5]
    department2 = Department.objects.all()[6:]
    context = {
        'object': obj,
        'department1': department1,
        'department2': department2,
    }
    return render(request, "Home/job-detail.html", context)

def course_details(request):
    department1 = Department.objects.all()[:5]
    department2 = Department.objects.all()[6:]
    context = {
        'department1': department1,
        'department2': department2,
    }
    return render(request, 'Home/course_details.html',context)
    
def administration(request):
    department1 = Department.objects.all()[:5]
    department2 = Department.objects.all()[6:]
    context = {
        'department1': department1,
        'department2': department2,
    }
    return render(request, 'Home/administration.html', context)
    
def fees(request):
    department1 = Department.objects.all()[:5]
    department2 = Department.objects.all()[6:]
    context = {
        'department1': department1,
        'department2': department2,
    }
    return render(request, 'Home/fees.html', context)


def application(request):
    department1 = Department.objects.all()[:5]
    department2 = Department.objects.all()[6:]
    context = {
        'department1': department1,
        'department2': department2,
    }
    return render(request, 'Home/application.html', context)
    
def eligibility(request):
    department1 = Department.objects.all()[:5]
    department2 = Department.objects.all()[6:]
    context = {
        'department1': department1,
        'department2': department2,
    }
    return render(request, 'Home/eligibility.html', context)
    
    
def governing_body_view(request):
    department1 = Department.objects.all()[:5]
    department2 = Department.objects.all()[6:]
    governing_body_1 = GoverningBody.objects.all()[:1]
    governing_body_2 = GoverningBody.objects.all()[1:]

    context = {
        'governing_body_2':governing_body_2,
        'governing_body_1': governing_body_1,
        'department1': department1,
        'department2': department2,
    }
    return render(request, 'Home/governing_body.html', context)

from django.db import models
from ckeditor.fields import RichTextField
from django.shortcuts import reverse
from datetime import datetime


# Create your models here.


class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_description = RichTextField(null=True, blank=False)
    department_image = models.ImageField(upload_to='department_image',blank=True,null= True, default='default_department.jpg')

    def __str__(self):
        return self.department_name

    def get_absolute_url(self):
        return reverse("Home:department-details", kwargs={"id": self.id})  # /* dynamic url */


class FacultyMember(models.Model):
    faculty_member_name = models.CharField(max_length=100)
    faculty_member_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    faculty_member_degree = models.CharField(max_length=255, blank=False)
    faculty_member_designation = models.CharField(max_length=255, blank=False)
    faculty_member_profile_image = models.ImageField(upload_to='Faculty Member',default='default.png')
    faculty_member_contact = models.EmailField(blank=True)

    def __str__(self):
        return self.faculty_member_name


class Gallery(models.Model):
    image_name = models.CharField(max_length=255)
    gallery_image = models.ImageField(upload_to='Gallery')
    published_year = models.IntegerField(default='2021')

    def __str__(self):
        return self.image_name


# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=30)
    author_details = models.CharField(max_length=500)
    author_profile_image = models.ImageField(upload_to='Author_Profile', default='default.png')

    def __str__(self):
        return self.author_name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255)
    news_thumbnail = models.ImageField(upload_to="News/Thumbnail", default="default.png")
    news_image = models.ImageField(upload_to="News", default="default.png")
    excert = models.CharField(max_length=133, default="None")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = RichTextField(default='No Information Available', blank=False, null=False)
    categories = models.ManyToManyField(Category)
    news_publish_date = models.DateTimeField(default=datetime.now, blank=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Home:news-details", kwargs={"id": self.id})  # /* dynamic url */

    def yearpublished(self):
        return self.news_publish_date.strftime('%Y')

    def monthpublished(self):
        return self.news_publish_date.strftime('%B')

    def datepublished(self):
        return self.news_publish_date.strftime('%d')


class Notice(models.Model):
    notice_title = models.CharField(max_length=255)
    notice_file = models.FileField(upload_to='Notices')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    notice_category = models.ManyToManyField(Category)
    published_date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.notice_title
        
    def yearpublished(self):
        return self.published_date.strftime('%Y')

    def monthpublished(self):
        return self.published_date.strftime('%B')

    def datepublished(self):
        return self.published_date.strftime('%d')
        
        
class Jobcircular(models.Model):
    circular_title = models.CharField(max_length=255)
    circular_publishe_date = models.DateField(default=datetime.now, blank=False)
    circular_valid_date = models.CharField(max_length=255)
    circular_details = RichTextField(default='No info', blank=False)
    circular_file = models.FileField(upload_to='Jobcircular')
    circular_vacancy= models.IntegerField(default=1)
    circular_job_nature= models.CharField(max_length=255, default='Full Time')
    location= models.CharField(max_length=255, default='Uttara-10,Dhaka-1230,Bangladesh')


    def __str__(self):
        return self.circular_title

    def yearpublished(self):
        return self.circular_publishe_date.strftime('%Y')

    def monthpublished(self):
        return self.circular_publishe_date.strftime('%B')

    def datepublished(self):
        return self.circular_publishe_date.strftime('%d')

    def get_absolute_url(self):
        return reverse("Home:job-circular-details", kwargs={"id": self.id}) 


class PositionOfGoveringBody(models.Model):
    position_name = models.CharField(max_length=255)

    def __str__(self):
        return self.position_name


class GoverningBody(models.Model):
    member_name = models.CharField(max_length=255)
    position = models.ForeignKey(PositionOfGoveringBody, on_delete=models.CASCADE)
    member_details = models.CharField(max_length=255)
    member_image = models.ImageField(upload_to='Governing_Body', default='default.png')

    def __str__(self):
        return self.member_name

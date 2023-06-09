# Generated by Django 3.2.13 on 2022-08-08 05:40

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=30)),
                ('author_details', models.CharField(max_length=500)),
                ('author_profile_image', models.ImageField(default='default.png', upload_to='Author_Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100)),
                ('department_description', ckeditor.fields.RichTextField(null=True)),
                ('department_image', models.ImageField(blank=True, default='default_department.jpg', null=True, upload_to='department_image')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=255)),
                ('gallery_image', models.ImageField(upload_to='Gallery')),
                ('published_year', models.IntegerField(default='2021')),
            ],
        ),
        migrations.CreateModel(
            name='Jobcircular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('circular_title', models.CharField(max_length=255)),
                ('circular_publishe_date', models.DateField(default=datetime.datetime.now)),
                ('circular_valid_date', models.CharField(max_length=255)),
                ('circular_details', ckeditor.fields.RichTextField(default='No info')),
                ('circular_file', models.FileField(upload_to='Jobcircular')),
                ('circular_vacancy', models.IntegerField(default=1)),
                ('circular_job_nature', models.CharField(default='Full Time', max_length=255)),
                ('location', models.CharField(default='Uttara-10,Dhaka-1230,Bangladesh', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PositionOfGoveringBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_title', models.CharField(max_length=255)),
                ('notice_file', models.FileField(upload_to='Notices')),
                ('published_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.author')),
                ('notice_category', models.ManyToManyField(to='Home.Category')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('news_thumbnail', models.ImageField(default='default.png', upload_to='News/Thumbnail')),
                ('news_image', models.ImageField(default='default.png', upload_to='News')),
                ('excert', models.CharField(default='None', max_length=133)),
                ('description', ckeditor.fields.RichTextField(default='No Information Available')),
                ('news_publish_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('views', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.author')),
                ('categories', models.ManyToManyField(to='Home.Category')),
            ],
        ),
        migrations.CreateModel(
            name='GoverningBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=255)),
                ('member_details', models.CharField(max_length=255)),
                ('member_image', models.ImageField(default='default.png', upload_to='Governing_Body')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.positionofgoveringbody')),
            ],
        ),
        migrations.CreateModel(
            name='FacultyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_member_name', models.CharField(max_length=100)),
                ('faculty_member_degree', models.CharField(max_length=255)),
                ('faculty_member_designation', models.CharField(max_length=255)),
                ('faculty_member_profile_image', models.ImageField(default='default.png', upload_to='Faculty Member')),
                ('faculty_member_contact', models.EmailField(blank=True, max_length=254)),
                ('faculty_member_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.department')),
            ],
        ),
    ]

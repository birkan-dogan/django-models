from distutils.command.upload import upload
from django.db import models

# Create your models here.

# modal = class

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField("soyadı",max_length=30)  # title will be "soyadı" not last_name if we use that parameter
    number = models.IntegerField()
    about = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to="media/",blank=True, null=True)  # to control image we should install pillow module

    # after writing new columns to class, new columns should be added to database table


    def __str__(self):  # changing appearance of the objects in admin panel by using __str__ method
        return f"{self.number} {self.first_name} {self.last_name}"

    class Meta:  # changing default values
        ordering = ["number"]  # DESC --> ["-number"]

# after creating modal, we should update database by using these codes --> python manage.py makemigrations && python manage.py migrate
# also we need to introduce this modal to admin panel

"""
# using shell environment to write sql, open shell with this command --> python manage.py shell

# firstly,  we need to introduce our modals to shell environment --> from application.models import Student

# after that, the instances will be created from Student class  --> 1 = Student(first_name= "Victor", last_name = "Hugo", number = 5)

# after creating instance, we should insert this instance to database table --> s1.save()

# we have second way to create new objects and this way does both creating new objects and saving to database in one line --> Student.objects.create(first_name="hank", last_name="schrader",number=6)

# to see all objects in database table (Student)  --> alls = Student.objects.all()  # this will return queryset

# to get one object in database table (it will just return one record) --> g1 = Student.objects.get(number=1)  # if we don't know how many records have number = 1, we should use filter() method

# f1 = Student.objects.filter(number = 1)

# f3 = Student.objects.filter(first_name__startswith="H")  # Django uses the 2 underscores between first_name and startswith to seperate field names and operations or filters

# f4 = Student.objects.filter(last_name__endswith = "c")

# to have objects that don't match with the query  --> f2 = Student.objects.exclude(number = 1)

"""
from django.db import models

# Create your models here.

# modal = class

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField("soyadı",max_length=30)  # title will be "soyadı" not last_name if we use that parameter
    number = models.IntegerField()

    def __str__(self):  # changing appearance of the objects in admin panel by using __str__ method
        return f"{self.number} {self.first_name} {self.last_name}"

    class Meta:  # changing default values
        ordering = ["number"]  # DESC --> ["-number"]

# after creating modal, we should update database by using these codes --> python manage.py makemigrations && python manage.py migrate
# also we need to introduce this modal to admin panel
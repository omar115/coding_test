from django.db import models

# Create your models here.

class ParentUser(models.Model):
    first_name = models.CharField("Parent First Name", max_length=150)
    last_name = models.CharField("Parent Last Name", max_length=150)
    street = models.CharField("Street Address", max_length=100)
    city = models.CharField("City Name", max_length=100)
    state = models.CharField("State Name", max_length=100)
    zip_code = models.IntegerField("Zip Code")

    class Meta:
        verbose_name_plural = "Parent Data"
    
    def __str__(self) -> str:
        return self.first_name
    

class ChildUser(models.Model):
    parent_user = models.OneToOneField(ParentUser, on_delete=models.CASCADE)
    child_first_name = models.CharField("Child First Name", max_length=150)
    child_last_name = models.CharField("Child Last Name", max_length=150)

    class Meta:
        verbose_name_plural = "Child Data"
    
    def __str__(self) -> str:
        return self.child_first_name

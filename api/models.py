from django.db import models

# Create your models here.

class ParentUserModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zip_code = models.IntegerField()

    class Meta:
        verbose_name_plural = "Parent Data"
    
    def __str__(self) -> str:
        return self.first_name



class ChildUserModel(models.Model):
    parent = models.ForeignKey(ParentUserModel, related_name="address", on_delete=models.CASCADE)
    child_first_name = models.CharField(max_length=100)
    child_last_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Child Data"
    
    def __str__(self) -> str:
        return self.child_first_name

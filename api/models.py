from django.db import models

# parent user model
class ParentUser(models.Model):
    first_name = models.CharField("Parent First Name", max_length=150, null=True, blank=True)
    last_name = models.CharField("Parent Last Name", max_length=150, null=True, blank=True)
    street = models.CharField("Street Address", max_length=100, null=True, blank=True)
    city = models.CharField("City Name", max_length=100, null=True, blank=True)
    state = models.CharField("State Name", max_length=100, null=True, blank=True)
    zip_code = models.IntegerField("Zip Code", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Parent Data"
    
    def __str__(self) -> str:
        return self.first_name
    

# child user model
class ChildUser(models.Model):
    parent_user = models.ForeignKey(ParentUser, on_delete=models.CASCADE, null=True, blank=True)
    child_first_name = models.CharField("Child First Name", max_length=150, null=True, blank=True)
    child_last_name = models.CharField("Child Last Name", max_length=150, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Child Data"
    
    def __str__(self) -> str:
        return self.child_first_name

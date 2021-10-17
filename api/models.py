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


# use of abstract class
# class Author(models.Model):
#     name = models.CharField(max_length=50)
#     age = models.CharField(max_length=50)

#     class Meta:
#         abstract = True
    
# class Book(Author):
#     zip = models.IntegerField()


# multi table model inheritence

class Address(models.Model):
    state = models.CharField(max_length=10)
    city = models.CharField(max_length=5)
    zip = models.IntegerField()

class Author(Address):
    address_ptr = models.OneToOneField(Address, on_delete=models.CASCADE,
    parent_link=True, primary_key=True)
    name = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.title
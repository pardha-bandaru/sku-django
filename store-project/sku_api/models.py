from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    created =  models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=256, unique=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField()
    created =  models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=256, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    description = models.TextField()
    created =  models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=256, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    created =  models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class SKUData(models.Model):
    name = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['name', 'location', 'category', 'department', 'subcategory']]

    def __str__(self) -> str:
        return self.name

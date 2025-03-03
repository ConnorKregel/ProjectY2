from django.db import models

# Create your models here.
class Stream(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=50)
    id_number = models.CharField(max_length=9)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    # cant have negative values for price,
    # change this later for the cart
    price = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
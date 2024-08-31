from django.db import models

# Create your models here.
class Person(models.Model):
    """class person
    """
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, default=35)
    email = models.EmailField(max_length=50, default='mark@essien.gmail.com')
    
    def __str__(self):
        return self.name
    
    def __str__(self):
        return self.age
    
    def __str__(self):
        return self.email
    
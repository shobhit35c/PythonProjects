from django.db import models
from django.contrib.auth.models import User # user model includes name and password

class Food(models.Model): # database table
    user = models.ForeignKey(
        User, on_delete = models.CASCADE, null= True, blank= True) # many foods to one user, all user's foods will be deleted if user is, user can be blank and is default to null
    title = models.CharField(max_length=200) # character field for simple header
    description = models.TextField(null=True, blank= True)
    eaten = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    calories = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
     ordering = ['eaten'] # query set is ordered by eaten values first


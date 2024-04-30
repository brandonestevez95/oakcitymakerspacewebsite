from django.db import models

class Category(models.Model):
    test = "placeholder"

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    #room to add more fields for posts 

    def __str__(self):
        return self.title

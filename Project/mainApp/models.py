from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()

    author = models.CharField(max_length = 30)

    pub_date = models.DateTimeField('date published')

    modified_date = models.DateTimeField('date modified')

    view_count = models.IntegerField()

    comments = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.text[:50]

class Comment(models.Model):
    text = models.TextField()
    author = models.CharField(max_length =30)
    pub_date = models.DateTimeField('date published', auto_now = True)

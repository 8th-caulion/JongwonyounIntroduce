from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()

    author = models.CharField(max_length = 30)

    pub_date = models.DateTimeField('date published')

    modified_date = models.DateTimeField('date modified')

    view_count = models.IntegerField()

    # comments = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank = True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.text[:50]

    # def getComments(self):
    #     commentsList = self.comments.objects.order_by('-pub_date')
    #     return commentsList

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    author = models.CharField(max_length =30)
    pub_date = models.DateTimeField('date published', auto_now = True)

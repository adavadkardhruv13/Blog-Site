
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='static', blank=True, null=True)
    timestamp = models.DateTimeField( null=True, blank=True)

    def __str__(self):
        return self.title + " by " + self.author

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + " by " + self.user.first_name


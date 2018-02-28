from django.db import models

# Create your models here.
class BlogsPost(models.Model):
	"""docstring for BlogPost"""
	title = models.CharField(max_length = 150)  #博客标题
	body = models.TextField() #博客正文
	timestamp = models.DateTimeField() #创建时间
	# def __init__(self, arg):
	# 	super(BlogPost, self).__init__()
	# 	self.arg = arg


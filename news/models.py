from django.db import models

# Create your models here.

class Author_db(models.Model):
    author_name = models.CharField(max_length=200)
    def __str__(self):
        return self.author_name

class News_db(models.Model):
    auth_id = models.ForeignKey(Author_db, on_delete=models.CASCADE)
    news_text = models.CharField(max_length=200)       
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.news_text 

from django.contrib import admin

# Register your models here.
from .models import Author_db, News_db

admin.site.register(Author_db)
admin.site.register(News_db)



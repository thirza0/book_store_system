from django.contrib import admin

from .models import Author, Publish, Classification, Tags, Book



admin.site.register(Author)
admin.site.register(Publish)
admin.site.register(Classification)
admin.site.register(Tags)
admin.site.register(Book)


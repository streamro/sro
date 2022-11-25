from django.contrib import admin
from . models import Movie , Show, Episode

from django.utils.html import format_html
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    def tumnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.image.url))
    tumnail.short_description = 'Photo'
    
    list_display = ('id', 'tumnail', 'title', 'category','tags', 'is_published')
    list_display_links = ('id', 'title', 'category', 'tags')
    search_fields = ('id', 'title', 'category', 'tags',)
    list_per_page = 20



class ShowAdmin(admin.ModelAdmin):
    def tumnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.image.url))
    tumnail.short_description = 'Photo'

    list_display = ('id', 'tumnail', 'title', 'category', 'is_published')
    list_display_links = ('id', 'title', 'category')
    search_fields = ('id', 'title', 'category')
    list_per_page = 20
    
    

class EpisodeAdmin(admin.ModelAdmin):
    def tumnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.thumbnail.url))
    tumnail.short_description = 'Photo'
    
    list_display = ('id', 'tumnail', 'title', 'season', 'episode_number', 'series', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'series' )
    list_per_page = 20
        
    
admin.site.register(Movie, MovieAdmin)
admin.site.register(Show, ShowAdmin)
admin.site.register(Episode,EpisodeAdmin)


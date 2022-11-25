from django.db import models
from datetime import datetime
from embed_video.fields import EmbedVideoField
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User



# Create your models here.

category_movies = (
    ('Action & Adventure' , 'Action & Adventure'),
    ('Comedies', 'Comedies'),
    ('Drama' , 'Drama'),
    ('Blockbuster Movies', 'Blockbuster Movies'),
    ('Popular Movies', 'Popular Movies'),
    ('Cartoons', 'Cartoons'),
    ('Documentaries', 'Documentaries')
)

category_show = (
    ('Documentary Films', 'Documentary Films'),
    ('Watch In One Night', 'Watch In One Night'),
    ("Popular Documentaries", "Popular Documentaries"),
    ('Best Of International Shows', 'Best Of International Shows'),
    ('Popular Shows', 'Popular Shows'),
    ('Familiar TV Favorites', 'Familiar TV Favorites')
)

aged_restriction = (
    ('6+' , '6+'),
    ('12' , '12'),
    ('16' , '16'),
    ('18', '18')
)

tags = (
    ('Exciting Movies', 'Exciting Movies'),
    ('Critically Acclaimed Films', 'Critically Acclaimed Films'),
    ('Familiar Favorites', 'Familiar Favorites'),
    ('Documentary Films', 'Documentary Films'),
    ('Popular Documentaries', 'Popular Documentaries')
)


tags_show = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    
)

class Movie(models.Model):
    title = models.CharField(max_length=50)
    imdb = models.CharField(max_length=50, blank=True)
    duration = models.CharField(max_length=50, blank=True)
    age_restriction = models.CharField(choices=aged_restriction, max_length=50, blank=True)
    category = models.CharField(choices=category_movies, max_length=100)
    tags = models.CharField(choices=tags, max_length=50)
    year_movie = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=205)
    main_image = models.ImageField(upload_to="main_photo/", blank=True)
    image = models.ImageField(upload_to="photos/")
    video = models.CharField(max_length=300, blank=True)
    is_published = models.BooleanField(default=True)
    is_slider = models.BooleanField(default=False)
    date_published = models.DateTimeField(default=datetime.now,blank=True)
    my_list = models.ManyToManyField(User, related_name="my_list", blank=True)

    def __str__ (self):
        return self.title

class Show(models.Model):
    title = models.CharField(max_length=100)
    imdb = models.CharField(max_length=50, null=True)
    category = models.CharField(choices=category_show, max_length=100)
    duration = models.CharField(max_length=50)
    year_show = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=200)
    main_image = models.ImageField(upload_to="main_photo/", blank=True)
    image = models.ImageField(upload_to="photos/")
    video_trailer = models.CharField(max_length=100)
    date_published = models.DateTimeField(default=datetime.now,blank=True)
    is_published = models.BooleanField(default=False)

    def __str__ (self):
        return self.title
    


class Episode(models.Model):
    series = models.ForeignKey(Show, on_delete=models.CASCADE, default=True)
    title = models.CharField(max_length=120)
    season = models.CharField(choices=tags_show, max_length=50, null=True)
    episode_number = models.IntegerField()
    duration = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to="photos/", default=True)
    video = models.CharField(max_length=300, default=True)
    is_published = models.BooleanField(default=False)
     
    def __str__ (self):
        return self.title

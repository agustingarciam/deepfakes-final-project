from django.db import models
from django.contrib.auth.models import User
from fake.nlp_generation import make_deep_fake, parse_input, get_people
import random

#Model for a new post
class Post(models.Model):
    #this is the input which is used to generate the deep fake
    input = models.CharField(max_length=200)

    #to initialize -> the type of df (song vs speech) and the output string
    output_df = models.TextField()

    #fields that rely on django
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    set_of_likes = models.ManyToManyField(User, related_name="users_who_liked_this")
    set_of_people = models.ManyToManyField('People', related_name="people_who_comprise_df")

    #magic methods!
    def __str__(self):
        return self.output_df
    
    def __hash__(self):
        return super().__hash__()

    #method to see if the two inputs had the same people
    def __eq__(self, other_set_of_people):
        return self.set_of_people == other_set_of_people

    # a function for returning the number of likes a deep fake post has
    def likes_count(self):
        return self.set_of_likes.count()
    
    #function for returning the users who liked this deep fake
    def get_likes(self):
        return self.set_of_likes
    
    #function for returning people in the deep faked post
    def get_people(self):
        return self.set_of_people
    

#People model
class People(models.Model):
    #actual hashtag field itself
    person = models.CharField(max_length=200)

    #also create a field to store set of posts which use source material from this person
    posts_with_person = models.ManyToManyField('Post', related_name="posts_with_person")

    #defining a method so that we retrieve the person's name
    def __str__(self):
        return self.person
    
    #method to see if the two inputs had the same people
    def __eq__(self, other_person):
        return self.person == other_person

    def __hash__(self):
        return super().__hash__()
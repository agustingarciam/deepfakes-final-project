from django.shortcuts import render, redirect
from fake.models import Post, People
from fake.nlp_generation import make_deep_fake, parse_input, get_people
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import re
import os
import markovify
import random

# Create your views here.
def splash(request):
    return render(request, 'splash.html', {})

def home(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    #if they post make new post and also parse for people
    if request.method == 'POST':
        body, created_at = request.POST['body'], request.POST.get('created_at')
        output = make_deep_fake(parse_input(str(body)), random.randint(5,10))
        post = Post.objects.create(input=body, author=request.user, output_df=output)

        #list of all people in the post
        people = get_people(str(post.input))

        #list of all people created thus far
        all_people = People.objects.all()
        people_names = []
        for person in all_people:
            people_names.append(person.person)

        #first go through the people in post in string form
        for individual in people:
            # if individual has an existing repository of deep fakes, just add the person to the post's set of people
            if individual in people_names:
                post.set_of_people.add(People.objects.get(person=individual))

                #also include this post under the persons set of posts
                People.objects.get(person=individual).posts_with_person.add(post)
            else:
                #create new "person"
                new_person = People.objects.create(person=individual)

                #also add this tothe list of people innate to the post
                post.set_of_people.add(new_person)

                #also include this post under the individual's existing deep fakes
                People.objects.get(person=individual).posts_with_person.add(post)

    
    all_posts = Post.objects.all()
    all_people = People.objects.all()
    return render(request, "home.html", {"posts": all_posts, "people": all_people})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/home')

    if request.method == "POST":
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is None:
            return redirect('/login?error=failure')
        
        login(request, user)
        return redirect('/home')

    return render(request, 'accounts.html')

def signup_view(request):
    if request.method == 'POST':
        username, password, email = request.POST['username'], request.POST['password'], request.POST['email']
        user = User.objects.create_user(username=username, password=password, email=email)
        
        ##now also log them in
        login(request, user)
        return redirect('/')

    return render(request, 'accounts.html')

def logout_view(request):
    logout(request)
    return redirect("/login")

def like_view(request, id_of_post):
    #get the post
    post = Post.objects.get(id=id_of_post)

    if request.user in post.set_of_likes.all():
        #remove user  from set of users who like post if possible
        post.set_of_likes.remove(request.user) 
    else:
        #add user to set of users who like this post
        post.set_of_likes.add(request.user) 

    return redirect('/home')

def delete(request):
    #get the post
    post = Post.objects.get(id=request.GET['id'])

    #only delete posts you wrote
    if post.author == request.user:
        post.delete()    
    return redirect('/user_profile')

def user_profile(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    #if they post make new post and also parse for people
    if request.method == 'POST':
        body, created_at = request.POST['body'], request.POST.get('created_at')
        output = make_deep_fake(parse_input(str(body)), random.randint(5,10))
        post = Post.objects.create(input=body, author=request.user, output_df=output)

        #list of all people in the post
        people = get_people(str(post.input))

        #list of all people created thus far
        all_people = People.objects.all()
        people_names = []
        for person in all_people:
            people_names.append(person.person)

        #first go through the people in post in string form
        for individual in people:
            # if individual has an existing repository of deep fakes, just add the person to the post's set of people
            if individual in people_names:
                post.set_of_people.add(People.objects.get(person=individual))

                #also include this post under the persons set of posts
                People.objects.get(person=individual).posts_with_person.add(post)
            else:
                #create new "person"
                new_person = People.objects.create(person=individual)

                #also add this tothe list of people innate to the post
                post.set_of_people.add(new_person)

                #also include this post under the individual's existing deep fakes
                People.objects.get(person=individual).posts_with_person.add(post)

    all_posts = Post.objects.all().filter(author=request.user)
    all_people = People.objects.all()
    return render(request, "user_profile.html", {"posts": all_posts, "people": all_people})

def profiles(request, author):
    if not request.user.is_authenticated:
        return redirect('/login')


    all_posts = Post.objects.all()

    posts = []
    count = 0
    for post in all_posts:
        if str(post.author) == str(author):
            posts.append(post)
            count += 1
            
    return render(request, "profiles.html", {"posts": posts, "author": author})

'''
def people(request, someone):
    if not request.user.is_authenticated:
        return redirect('/login')

    retrieved_person = People.objects.get(person=someone)
    posts_with_person = []
    regex = str(someone)


    for post in Post.objects.all():
        if len(re.findall(regex, post.input)) != 0:
            posts_with_person.append(post)

    return render(request, "people.html", {"person": someone, "posts": posts_with_person})
'''
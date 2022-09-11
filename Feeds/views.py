from django.urls import reverse
from re import template
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from Feeds.models import Posts,Stream,Likes
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from .form import newPost
from django.contrib import messages
from django.template.loader import render_to_string


@login_required
def feed(request):
    user = request.user
    posts = Stream.objects.filter(user=user)

    group_ids = []

    for post in posts:
        group_ids.append(post.post_id)
    
    post_items = Posts.objects.filter(id__in=group_ids).all().order_by('-posted')



    template = loader.get_template('Feeds/feed.html')

    context = {
        'post_items': post_items,
    }

    return HttpResponse(template.render(context, request))

@login_required
def addPost(request):
    user = request.user.id

    if request.method == "POST":
        form = newPost(request.POST, request.FILES)
        if form.is_valid():
            caption = form.cleaned_data.get('caption')
            pictures = form.cleaned_data.get('pictures')

            p, created = Posts.objects.get_or_create(caption=caption,pictures=pictures,user_id=user)
            p.save()

            return redirect('feeds')
    else:
        form = newPost()
    
    context = {
        "form": form
    }

    template = loader.get_template('Feeds/addPost.html')

    
    return JsonResponse(template.render(context, request))

    

    





    # if method == "POST":






    #     if request.method == "POST":
    #     form = newPost(request.POST, request.FILES)
    #     if form.is_valid():
    #         picture = form.cleaned_data.get('picture')
    #         caption = form.cleaned_data.get('caption')
    #         tags_form = form.cleaned_data.get('tags')

    #         tags_list = list(tags_form.split(','))

    #         for tag in tags_list:
    #             t, created = Tag.objects.get_or_create(title=tag)
    #             tags_obj.append(t)
    #         p ,created = Posts.objects.get_or_create(pictures=picture, caption=caption, user_id = user)
    #         p.tags.set(tags_obj)
    #         p.save()

    #         return redirect('feeds')
    # else:
    #     form = newPost()

    # context = {
    #     "form": form
    #     }
    # return render(request,'Feed/newpost.html', context)

  
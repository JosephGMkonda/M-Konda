from django.urls import reverse
from re import template
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from Feeds.models import Posts,Stream,Likes
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .form import newPost
from django.contrib import messages

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
    post = Posts.objects.all()
    if request.method == "POST":
        caption = request.POST.get('caption',False)
        pictures = request.POST.get('pictures',False)

        if not caption:
            messages.error(request,"caption needed")
        p, created = Posts.objects.get_or_create(pictures=pictures,caption=caption,user_id=user)
        p.save()
        messages.success(request,"The product added successfully")
        return redirect('feeds')

    context = {
        post:"post",
        "values":request.POST
    }
    return render(request,'Feeds/feed.html', context)


        
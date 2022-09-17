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
from comment.form import CommentForms
from comment.models import comments


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
def postDetails(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    user = request.user
    comment = comments.objects.filter(post=post).order_by('date')

    if request.method == "POST":
        form = CommentForms(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = user
            comment.save()

            return HttpResponseRedirect(reverse('postdetail',args=[post_id]))

        else: 
            form = CommentForms()

    
    
    
    template = loader.get_template('Feeds/postDetails.html')

    context = {
        'post':post
    }

    return HttpResponse(template.render(context, request))
    




@login_required
def addPost(request):
    user = request.user.id
    data = dict()
    if request.method == "POST":
        form = newPost(request.POST, request.FILES)
        if form.is_valid():
            caption = form.cleaned_data.get('caption')
            pictures = form.cleaned_data.get('pictures')

            p, created = Posts.objects.get_or_create(caption=caption,pictures=pictures,user_id=user)
            print(p)
            p.save()
            return redirect('feeds')
    

    else:
        form = newPost()

    context = {
        'form':form
    }
    data['html_form'] = render_to_string('Feeds/addPost.html',context, request=request)
    return JsonResponse(data)
    
    

    




  
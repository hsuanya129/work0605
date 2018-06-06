from __future__ import unicode_literals
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post,Category,Comment
from . import models
import datetime


# Create your views here.
def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories})

def post_list(request):
    posts =  Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories})

def category(request):
    pid=request.GET["id"]
    posts = Post.objects.filter(category=pid)
    categories = Category.objects.all()
    return render(request, 'blog/post_category.html', {'posts': posts,'categories':categories})

def view(request):
    # try:
    pid=request.GET["id"]
    posts = Post.objects.filter(p_id = pid)
    latest_cards_list = Comment.objects.filter(post = pid)

    return render(request, 'blog/post_view.html', {'posts': posts,'latest_cards_list':latest_cards_list,'pid':pid})

def post_comment(request,p_id):
    pid=p_id
    c_title =request.POST['c_title']
    c_user_name = request.POST['c_user_name']
    c_content = request.POST['c_content']
    c_pub_date = datetime.datetime.now()
    cards = models.Comment(title=c_title,user_name=c_user_name,content=c_content,pub_date=c_pub_date,post=pid)
    cards.save()
    return HttpResponseRedirect('/blog/view/?id=%s'%pid)

    # except:
    #     return HttpResponseRedirect('/blog/')


def post_page(request):
	return render_to_response('blog/post_new.html')

def edit_page(request):
	try:
		pid=request.GET["id"]
		posts = Post.objects.filter(p_id = pid)
		return render(request, 'blog/post_edit.html', {'posts': posts})
	except:
		return HttpResponseRedirect('/blog/')
		

def save(request):
    user = request.POST.get("tb_user")
    ti = request.POST.get("tb_title")
    tx = request.POST.get("tb_text")
    created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    publish = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    n_post = models.Post(author = user, title = ti, text = tx, created_date = created, published_date = publish)
    n_post.save()

    return HttpResponseRedirect('/blog/')

def update(request):
    try:
        pi = request.POST.get("tb_pid")
        thePost = Post.objects.get(p_id=pi)
        thePost.author = request.POST.get("tb_user")
        thePost.title = request.POST.get("tb_title")
        thePost.text = request.POST.get("tb_text")
        thePost.published_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        thePost.save()
        return HttpResponseRedirect('/blog/')
    except Exception as e:
         return HttpResponseRedirect('/blog/')


def delete(request):
    un = request.GET["id"]
    
    try:
        post = Post.objects.get(p_id=un)
        post.delete()
        return HttpResponseRedirect('/blog/')
    except:
         return HttpResponseRedirect('/blog/')





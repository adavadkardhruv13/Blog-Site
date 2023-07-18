from django.shortcuts import render, redirect
from .models import Post, BlogComment
from django.contrib import messages


# Create your views here.

def bloghome(request):
    allPost = Post.objects.all()
    context = {"allPost": allPost}
    return render(request, 'myapp/bloghome.html', context)

def blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post,parent=None )
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    context = {"post": post, "comments": comments}
    return render(request,'myapp/blogpost.html', context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=BlogComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment= comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")


    return redirect(f"/blog/{post.slug}")






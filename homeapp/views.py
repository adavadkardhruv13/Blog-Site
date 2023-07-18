from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from django.contrib import messages
from myapp.models import Post
from itertools import chain
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
# Create your views here.

def home(request):
    return render(request,'homeapp/home.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please fill the form correctly")

            send_mail(
                name,
                content,
                email,
                ['advvadkardhruv@gmail.com']
            )
            return render(request, 'contact.html', {'message_name' : name})
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your mail has been successfully sent")


    return render(request,'homeapp/contact.html')

def about(request):
    return render(request,'homeapp/about.html' )

def search(request):
    search = request.GET['search']
    if len(search) > 70:
        allPost = []
    else:
        allPostTitle = Post.objects.filter(title__icontains=search)
        allPostcontent = Post.objects.filter(content__icontains=search)
        allPostauthor = Post.objects.filter(author__icontains=search)
        allPost = list(chain(allPostauthor, allPostcontent, allPostTitle))

    params={'allPost': allPost, 'search':search}
    return render(request,'homeapp/search.html', params)

def handelsignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username) > 15:
            messages.error(request, "Username must be under 15 character")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Password do not match")
            return redirect('home')


        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request, "Your account is been successfully created")
        return redirect('home')
    else :
        return HttpResponse("404 - Not Found ")

def handellogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username = loginusername, password = loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged In Successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials, Please Try Again')
            return redirect('home')

    return HttpResponse('404 - Not Found')


def handellogout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('home')

class AddBlog(CreateView):
        allow_multiple_selected = True
        model = Post
        template_name = 'myapp/addblog.html'
        fields = ["title", "content", "author", "slug",
                  "thumbnail"]
        success_url = reverse_lazy('home')

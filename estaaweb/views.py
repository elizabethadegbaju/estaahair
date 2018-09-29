
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm, LoginForm
from oscar.apps.catalogue.reviews.models import *

# Create your views here.
def blog(request):
    return render(request, 'naturalhair.html', {})

def home(request):
    return render(request,"index.html", {})

def contact(request):
    return render(request, "contact.html", {})

def reviews(request):
    reviews = ProductReview.objects.all().order_by('-date_created')
    return render(request, "reviews.html", {'reviews':reviews},)

def services(request):
    hairs = Hair.objects.all().order_by('-id')
    wigessentials = WigEssential.objects.all().order_by('-id')
    hairaccessories = HairAccessory.objects.all().order_by('-id')
    appliances = Appliance.objects.all().order_by('-id')
    return render(request, "services.html", {'hairs' : hairs, 'wigessentials':wigessentials, 'hairaccessories':hairaccessories,  'appliances':appliances})

def shop(request):
    return render(request, "promotions/home.html")

def post(request):
    return render(request, "post.html", {})

def registration(request):
    return render(request, 'registration.html', {})

def userpage(request):
    return render(request, 'userpage.html', {})

#lists all posts or create a new one
#posts/
class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all().order_by('-id')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class UserFormView(View):
    form_class = UserForm
    template_name = 'registration.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User object if credentials are  correct
            user = authenticate(username = username, password = password)
            if user is not None:
                if user.is_active:
                    login(request,user )
                    return redirect('userpage')

        return render(request, self.template_name, {'form': form})


class LoginFormView(View):
    form_class = LoginForm
    template_name = 'login.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        # cleaned (normalized) data
        username = form.data['username']
        password = form.data['password']

        #returns User object if credentials are  correct
        user = authenticate(username = username, password = password)
        if user is not None:
            if user.is_active:
                login(request,user )
                return redirect('userpage')

        return render(request, self.template_name, {'form': form})

































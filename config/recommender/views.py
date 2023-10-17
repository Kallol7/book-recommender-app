from django.shortcuts import render

from .scripts import recommend
from .scripts.create_one_json import create_one_json
from .scripts.clean_one import clean_one
from django.contrib.auth import authenticate, login
from .models import User
from django.db import IntegrityError

# Create your views here.
def home(request):
    book_name = "নক্ষত্রের রাত"
    closests = recommend.recommend_from_csv(book_name)
    return render(request, "recommender/home.html", {"closests": closests})

def clean(request):
    create_one_json()
    clean_one()
    return render(request, "recommender/clean.html", {})

def update(request):
    updates = recommend.update()
    return render(request, "recommender/update.html", {"updates": updates})

def recommend_view(request):
    # recommendations = recommend.recommendations()
    # return render(request, "recommender/recommend.html", {"all_recommendations": recommendations})

    csv_html = recommend.get_csv_as_html()
    return render(request, "recommender/recommend.html", {'csv_html': csv_html})

def signup_page(request):
    if request.method=="POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        if pass1 != pass2:
            return render(request, "recommender/signup.html", {"passdidnotmatch": True})
        if fullname and email and pass1:
            try:
                user = User.objects.create(username=email,email=email,password=pass1, fullname=fullname)
            except IntegrityError:
                return render(request, "recommender/signup.html", {"useralredyexists": True})
            else:
                user.save()
                return render(request, "recommender/login.html", {"usercreated": True})
    return render(request, "recommender/signup.html", {})

def login_page(request):
    if request.method=="POST":
        email = request.POST.get("email")
        password = request.POST.get("passwd")

        user = authenticate(request, username=email, email=email, password=password)
        if user is not None:
            # login(request, user)
            print("Authentication OK")
        else:
            return render(request, "recommender/login.html", {"userorpasserror": True})
        
    return render(request, "recommender/login.html", {})

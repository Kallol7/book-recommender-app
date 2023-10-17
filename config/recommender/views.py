from django.shortcuts import render

from .scripts import recommend
from .scripts.create_one_json import create_one_json
from .scripts.clean_one import clean_one
from django.contrib.auth.models import User

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
        username = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        if pass1 != pass2:
            return render(request, "recommender/signup.html", {"passdidnotmatch": True})
        if username and email and pass1:
            user = User.objects.create_user(username, email, pass1)
            user.save()
            return render(request, "recommender/login.html", {"usercreated": True, "user_full_name": username})
    return render(request, "recommender/signup.html", {})

def login_page(request):
    return render(request, "recommender/login.html", {})

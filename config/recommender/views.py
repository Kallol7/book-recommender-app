from django.shortcuts import render, redirect

from .scripts import recommend
from .scripts.create_one_json import create_one_json

# usign dummy, not the real one
from .scripts.clean_one_dummy import clean_one

from django.contrib.auth import authenticate, login, logout
from .models import User, Book
from django.db import IntegrityError
from django.contrib.auth.decorators import user_passes_test, login_required
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def home(request):
    book_name = "নক্ষত্রের রাত"
    closests = recommend.recommend_from_csv(book_name)
    closests = [i.split(",") for i in closests]
    # closests = [(a[2:-1],b[2:-1]) for (a,b) in closests]
    return render(request, "recommender/home.html", {"closests": closests, "book_name": book_name})

def is_staff(user):
    # 'groups', 'has_module_perms', 'has_perm', 'has_perms', 'id', 
    # 'is_active', 'is_anonymous', 'is_authenticated', 'is_staff', 'is_superuser', 
    # 'pk', 'save', 'set_password', 'user_permissions', 'username'
    return user.is_active and user.is_staff

@user_passes_test(is_staff, login_url="admin:login")
def clean(request):
    create_one_json()
    clean_one()
    recommend.run_lda_view()
    return render(request, "recommender/clean.html", {})

@user_passes_test(is_staff, login_url="admin:login")
def update(request):
    updates = recommend.update()
    return render(request, "recommender/update.html", {"updates": updates})

@login_required(login_url="login")
def recommend_view(request):
    # recommendations = recommend.recommendations()
    # return render(request, "recommender/recommend.html", {"all_recommendations": recommendations})

    csv_html = recommend.get_csv_as_html()
    return render(request, "recommender/recommend.html", {'csv_html': csv_html})

@login_required(login_url="login")
def single_item_view(request,pk):
    book_name,closests = recommend.sigle_item_from_csv(pk)
    closests = [i.split(",") for i in closests]
    # closests = [(a[2:-1],b[2:-1]) for (a,b) in closests]
    return render(request, "recommender/home.html", {"closests": closests, "book_name": book_name})

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
                user = User.objects.create(username=email,email=email,fullname=fullname)
                user.set_password(pass1)
            except IntegrityError:
                return render(request, "recommender/signup.html", {"useralredyexists": True})
            except Exception:
                return render(request, "recommender/signup.html", {"somethingwentwrong": True})
            else:
                user.save()
                return render(request, "recommender/login.html", {"usercreated": True})

    return render(request, "recommender/signup.html", {})

def login_page(request):
    if request.method=="POST":
        email = request.POST.get("email")
        password = request.POST.get("passwd")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "recommender/login.html", {"userorpasserror": True})

    return render(request, "recommender/login.html", {})

def logout_view(request):
    logout(request)
    return render(request, "recommender/login.html", { "logoutsuccess": True })

def search_books(request):
    query = request.POST.get("searchbook", "")
    books = Book.objects.all()
    if query:
        books = Book.objects.filter(Q(name__icontains=query) | Q(writer__name__icontains=query))

    paginator = Paginator(books, 5)

    # Get the current page number from the request's GET parameters.
    page = request.GET.get('page')

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an integer, deliver the first page.
        books = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, deliver the last page of results.
        books = paginator.page(paginator.num_pages)
    
    return render(request, 'recommender/searchresults.html', {'books': books})

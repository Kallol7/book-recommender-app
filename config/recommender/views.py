from django.shortcuts import render

from .scripts import recommend

# Create your views here.
def home(request):
    book_name = "নক্ষত্রের রাত"
    closests = recommend.recommend(book_name)
    return render(request, "recommender/home.html", {"closests": closests})

def update(request):
    updates = recommend.update()
    return render(request, "recommender/update.html", {"updates": updates})

def recommend_view(request):
    recommendations = recommend.recommendations()
    return render(request, "recommender/recommend.html", {"all_recommendations": recommendations})

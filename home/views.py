from django.shortcuts import render, HttpResponse, redirect
from .models import News, Publication, Events, Education, Research, Job, GalleryImage, Images
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from .forms import NewsForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.paginator import Paginator


# Create your views here.
bg_image = Images.objects.get(title='hd bg')   
logo = Images.objects.get(title='iete logo')

def home(request):
    news = News.objects.get(id=3)  
    publication = Publication.objects.all()
    context = {'news':news,
               'images':bg_image,
               'logo':logo,
               'publication':publication
               }
    return render(request, 'home.html', context)

def news(request):
    articles = News.objects.all()
    paginator = Paginator(articles, per_page=5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'articles':articles,
               'images':bg_image,
               'logo':logo,
               'page_obj':page_obj
               }
    return render(request, 'news.html', context)

@login_required
def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to create a new News object
            news = form.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsForm()

    return render(request, 'create_news.html', {'form': form})

def news_land(request, pk):
    news = News.objects.get(id=pk)
    next_news = News.objects.filter(pk__gt=pk).order_by('pk').first()
    context = {'news':news,
               'next_news':next_news,
               'images':bg_image,
               'logo':logo
               }
    return render(request, 'news_land.html', context)

def event(request):
    event = Events.objects.all()
    paginator = Paginator(event, per_page=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'events':event,
               'images':bg_image,
               'logo':logo,
               'page_obj':page_obj
               }
    return render(request, 'event.html', context)

def education(request):
    edu = Education.objects.all()
    context = {'education':edu,
               'images':bg_image,
               'logo':logo
               }
    return render(request, 'education.html', context)

def publications(request):
    publication = Publication.objects.all()
    context = {'publication':publication,
               'images':bg_image,
               'logo':logo
               }
    return render(request, 'publications.html', context)

def galleries(request):
    gallery = GalleryImage.objects.all()
    context = {'gallery':gallery,
               'images':bg_image,
               'logo':logo
               }
    return render(request, 'galleries.html', context)

def about(request):
    context = {
               'images':bg_image,
               'logo':logo
               }
    return render(request, 'about1.html', context)

def membership(request):
    context = {
               'images':bg_image,
               'logo':logo
               }
    return render(request, 'membership.html', context)

def jobs(request):
    jobs = Job.objects.all()
    context = {
        'jobs':jobs,
        'images':bg_image,
        'logo':logo
    }
    return render(request, 'jobs1.html', context)

def research(request):
    research = Research.objects.all()
    context = {
        'research':research,
        'images':bg_image,
        'logo':logo
    }
    return render(request, 'research.html', context)

def modeltest(request):
    article = News.objects.all()
    context = {'article': article,
               'images':bg_image,
               'logo':logo}
    return render(request, 'about.html', context)

def admin_login(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user is not None and user.is_staff:
            auth_login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'Credentials values are Inavlid')
            return redirect('login')

    else:
        return render(request, 'login.html')

@login_required()
def admin_logout(request):
    logout(request)
    return redirect('login')
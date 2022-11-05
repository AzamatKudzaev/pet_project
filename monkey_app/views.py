
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from monkey_app.models import Article, Profile
from django.db.models import Sum, Max, Min, Count, Avg, Value
from .forms import ArticleForm
from django.urls import reverse
# Create your views here.f

def main(request):
    articles = Article.objects.filter(publication=True)
    if len(articles) <= 11:
        sorted_articles = articles.order_by(
            '-article_views').exclude(article_views=0)
    else:
        sorted_articles = articles.order_by(
            '-article_views').exclude(article_views=0)[:11]

    context = {
        'sorted_articles': sorted_articles,
    }

    return render(request, 'monkey_app/main.html', context=context)


def about_us(request):
    return render(request, 'monkey_app/about-us.html')


def articles_view(request):
    articles = Article.objects.filter(publication=True)
    agg = articles.aggregate(Count('pk'))
    context = {
        'articles': articles,
        'agg': agg
    }
    return render(request, 'monkey_app/articles.html', context=context)


def show_article(request, id_article, article_kind):
    article = get_object_or_404(
        Article, id=id_article, article_kind=article_kind)
    article.article_views += 1
    article.save()

    context = {
        'article': article
    }
    return render(request, 'monkey_app/show_article.html', context=context)


def create_article(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('articles'))
        else:
            print(form.errors)

    return render(request, 'monkey_app/create_article.html', {'form': form})


def show_profile(request, profile_name):
    return HttpResponse('profile -', profile_name)

from django.shortcuts import render
from articles.models import Article

def article(request):
    article_data_model = Article.objects.get(id=5)
    context = {'article': article_data_model}
    return render(request, 'templates/run.html', context)

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Author_db, News_db
from django.utils import timezone
from django.template import loader
# Create your views here.

temp_var=0
def index(request):
    latest_news = News_db.objects.order_by('-pub_date')[:]
    
    context = {
        'latest_news' : latest_news,
    }
    return render(request, 'news/index.html', context)
    


def detail (request, url_id):
    #print(request.get(text))
    try:
        author = Author_db.objects.get(pk=url_id)
    except Author_db.DoesNotExist:
        raise Http404("Author does not exist")
    temp_var = url_id
    return render(request, 'news/detail.html', {'author':author})
    

def results(request, url_id):
    a = get_object_or_404(Author_db, pk=url_id)
    n = News_db(auth_id = a, news_text = request.POST['author_news'], pub_date = timezone.now() )
    n.save()
    latest_news = News_db.objects.order_by('-pub_date')[:]
    
    context = {
        'latest_news' : latest_news,
    }
    return render(request, 'news/index.html', context)
'''
def results(request, )
    n = News_db(auth_id = Author_db.objects.get(pk=id), news_text = url_text, pub_date = timezone.now() )
    n.save()

    output = '\n'.join([q.news_text for q in latest_news])
    return HttpResponse(output)



    template = loader.get_template('news/index.html')
    from django.http import HttpResponse
    from django.template import loader

    response = "Please add news here Mr.%s."
    return HttpResponse(response % a)
'''    
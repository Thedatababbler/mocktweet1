from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.utils.http import is_safe_url 
from .forms import TweetForm
from .models import Tweet #.model for module in the same folder
# Create your views here.
ALLOWED_HOSTS = settings.ALLOWED_HOSTS
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>good boi</h1>")
    return render(request, 'pages/home.html', context={}, status=200)

def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get('next') or None
    if form.is_valid():
        obj = form.save(commit=False)
        # do other form related processing
        obj.save()
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
    return render(request, 'components/form.html', context={"form": form})

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    Rest Api View
    consume by JavaScript or Swift or Java/Ios/Android
    return json data
    """
    print(args, kwargs)
    data = {
        'id':tweet_id,
        #'content': obj.content
        #ToDo: imageurl
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = 'Not Found'
        status = 404
    return JsonResponse(data, status=status)#HttpResponse(f"<h1>good boi {tweet_id} - {obj.content}</h1>")

def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{'id': x.id, 'content': x.content, 'likes':10} for x in qs]
    data = {
        'isUser': False,
        'response':tweets_list
    }
    return JsonResponse(data)
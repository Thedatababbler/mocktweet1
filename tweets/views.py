from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Tweet #.model for module in the same folder
# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>good boi</h1>")
    return render(request, 'pages/home.html', context={}, status=200)

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
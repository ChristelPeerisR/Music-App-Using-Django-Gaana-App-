from django.shortcuts import render
from.models import *

# Create your views here.

def index(request):
    
    thumb_frs = Thumb_fr.objects.all()
    thumb_sns = Thumb_sn.objects.all()
    thumb_trs = Thumb_tr.objects.all()
    recents = Recent.objects.all()
    tops = Top.objects.all()
    trends = Trend.objects.all()
    artists = Artist.objects.all()

    return render(request, "index.html",{'thumb_frs':thumb_frs, 'thumb_sns':thumb_sns, 
                                         'thumb_trs':thumb_trs,'recents':recents, 
                                         'tops':tops, 'trends':trends, 
                                         'artists':artists, 'navbar':'index'})

def search(request):

    query = request.GET.get("query")
    recents = Recent.objects.all()
    trends = Trend.objects.all()
    tops = Top.objects.all()
    artists = Artist.objects.all()
    rq = recents.filter(recent_name__icontains=query)
    tcq = tops.filter(top_name__icontains=query)
    tq = trends.filter(trend_name__icontains=query)
    aq = artists.filter(artists_name__icontains=query)
    return render(request, "search.html",{'recents':rq, 'tops':tcq, 
                                          'trends':tq, 'artists':aq, 
                                          'query':query, 'navbar':'#search'})

def recent(request):

    recents = Recent.objects.all()
    return render(request, "recent.html",{'recents':recents, 'navbar':'recent'})

def recentpost(request, id):

    recents = Recent.objects.all()
    recents = Recent.objects.filter(id=id)
    return render(request, "recentpost.html",{'recents':recents})

def topcharts(request):

    tops = Top.objects.all()
    return render(request, "topcharts.html",{'tops':tops, 'navbar':'topcharts'})

def topchartspost(request, id):

    tops = Top.objects.all()
    tops = Top.objects.filter(id=id)
    recents = Recent.objects.all()
    return render(request, "topchartspost.html",{'recents':recents, 'tops':tops})

def trend(request):

    trends = Trend.objects.all()
    return render(request, "trend.html",{'trends':trends, 'navbar':'trend'})

def trendpost(request, id):

    trends = Trend.objects.all()
    trends = Trend.objects.filter(id=id)
    return render(request, "trendpost.html",{'trends':trends})

def artists(request):

    artists = Artist.objects.all()
    return render(request, "artists.html",{'artists':artists, 'navbar':'artists'})

def artistspost(request, id):
    
    artists = Artist.objects.all()
    artists = Artist.objects.filter(id=id)
    trends = Trend.objects.all()
    return render(request, "artistspost.html",{'trends':trends, 'artists':artists})





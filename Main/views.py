from django.shortcuts import render
from Main import models


#from django.contrib.auth.models import User
#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.hashers import check_password,make_password
# from json import json_util
#from django.core.mail import send_mail

def Main(request):
    events1=models.Events.objects.all()
   # print(events1)
    events = []
    for i in events1:
        #print(i.name)
        #print(i.text)
        ev = []
        ev.append(i.text)
        ev.append(i.place_city+','+i.place_country)
        ev.append(i.date_end.strftime("%#d %b %y"))
        ev.append(i.date_start.strftime("%#d %b %y"))
        #ev.append(i.date_end.month)
        #ev.append(i.date_end.day)
        #ev.append(i.date_start.month)
        #ev.append(i.date_start.day)
        ev.append(i.name)
        #print(ev)
        events.append(ev)
    #print(events[0])

    news1=models.News.objects.all()
    news=[]
    ch=False;
    for i in news1:
        new=[]
        new.append(i.text)
        new.append(i.name)
        new.append(i.img_path)
        if (ch==False):
            new.append('active')
            ch=True
        else:
            new.append('')

        news.append(new)

    news_slide=[]
    cnt=len(news1)
    ch1=False
    print(cnt)
    i=0
    while i < cnt:
        news_slide1=[]
        news_slide1.append(i)
        if ch1==False:
            news_slide1.append('active')
        else:
            news_slide1.append('')
        news_slide.append(news_slide1)
        i=i+1
    articles1=models.Articles.objects.all()
    articles=[]
    for i in articles1:
        #print(i.name)
        #print(i.text)
        art=[]
        art.append(i.name)
        art.append(i.text)
        art.reverse()
        articles.append(art)
    #kk = 185
    #print(kk)
    #print(events1)
    #print(ev)
    return render(request, 'Main.html', locals())
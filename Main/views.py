from django.shortcuts import render
from Main import models
from datetime import date, datetime, time
from babel.dates import format_date, format_datetime, format_time


#from django.contrib.auth.models import User
#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.hashers import check_password,make_password
# from json import json_util
#from django.core.mail import send_mail

def Main(request):
    events1=models.Events.objects.all()
    events = []
    for i in events1:
        ev = []
        ev.append(i.text)
        ev.append(i.place_city+','+i.place_country)
        ev.append(format_date(i.date_end, locale='ru'))
        ev.append(format_date(i.date_start, locale='ru'))
        # ev.append(i.date_end.strftime("%#d %b %y"))
        # ev.append(i.date_start.strftime("%#d %b %y"))
        ev.append(i.name)
        events.append(ev)

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
    # print(news)
    news_slide=[]
    cnt=len(news1)
    ch1=False
    # print(cnt)
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
        art=[]
        art.append(i.name)
        art.append(i.text)
        art.reverse()
        articles.append(art)

    reviews1= models.Reviews.objects.all()
    rews = []
    ch = False;
    for i in reviews1:
        rew = []
        rew.append(i.text)
        rew.append(i.city+', '+i.country)
        rew.append(i.position)
        rew.append(i.name)
        if (ch == False):
            rew.append('active')
            ch = True
        else:
            rew.append('')

        rews.append(rew)
    # print(news)
    rews_slide = []
    cnt = len(reviews1)
    ch1 = False
    i = 0
    while i < cnt:
        rews_slide1 = []
        rews_slide1.append(i)
        if ch1 == False:
            rews_slide1.append('active')
        else:
            rews_slide1.append('')
        rews_slide.append(rews_slide1)
        i = i + 1

    return render(request, 'Main.html', locals())
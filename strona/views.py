# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django_project.models import Post, Klub
from django.utils import timezone

from datetime import datetime

from django.contrib.staticfiles.templatetags.staticfiles import static

#import page_config

def js_source():
	return '<script src="../tools/js/jquery-1.11.3.min.js"></script><script src="../tools/js/bootstrap.min.js"></script>'
		
def css_source():
	return '<link rel="stylesheet" type="text/css" href="{% static /assets/css/bootstrap.css %}"><link rel="stylesheet" type="text/css" href="{% static /assets/css/bootstrap-theme.css %}">'
	
def index(request):
	dt = datetime.now()
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	kluby = Klub.objects.order_by('nazwa_klubu')
	context = {
        'czas': dt,
        'posts': posts,
		'kluby': kluby
    }
	return render_to_response('index.html', context)

def club_detail(request, ik):
	klub = Klub.objects.get(id_klubu=ik)
	context = {
		'klub': klub
    }
	return render_to_response('club_detail.html', context)

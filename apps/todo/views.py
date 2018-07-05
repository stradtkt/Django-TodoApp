# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        "todos": todos
    }
    return render(request, 'todo/index.html', context)

def add_todo(request):
    title = request.POST['title']
    author = request.POST['author']
    content = request.POST['content']
    Todo.objects.create(title=title, author=author, content=content)
    return redirect('/')
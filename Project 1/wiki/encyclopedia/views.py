from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from markdown2 import Markdown
from django.shortcuts import render
from django.urls import reverse
from . import util


class SearchEntryForm(forms.Form):
    entry = forms.CharField(label = "Search Entry")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entries(request, title):
    if util.get_entry(title) is None: 
        return render(request, "encyclopedia/error.html")
    else:
        markdowner = Markdown()
        parsed_content = markdowner.convert(util.get_entry(title))
        return render(request, "encyclopedia/entries.html", {
            "entry": title,
            "content": parsed_content
        })

def search(request):
    suggestions = []
    for title in util.list_entries():
        if request.POST.get('q') == title: 
            return entries(request, title)
        else:
            if request.POST.get('q') in title:
                for item in util.list_entries():
                    if request.POST.get('q') in item:
                        suggestions.append(item)
                return render(request, "encyclopedia/suggestions.html", {
                            "suggestions": suggestions
                        })    
    
    return render(request, "encyclopedia/error.html")

def create(request):
    return render(request, "encyclopedia/create.html")

def process_create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    if util.get_entry(title) is None:
        util.save_entry(title, content)
        return index(request)
    else:
        return render(request, "encyclopedia/error_create.html")

def edit(request, content):
    return render(request, "encyclopedia/edit_page.html", {
        'content': util.get_entry(content)
    })

def process_edit(request):
    return

##para generar azar ranint(a, b) ==> a <= N <= b



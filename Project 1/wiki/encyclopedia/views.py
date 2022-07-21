from markdown2 import Markdown
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entries(request, title):

    markdowner = Markdown()
    parsed_content = markdowner.convert(util.get_entry(title))

    if util.get_entry(title) is None: 
        return render(request, "encyclopedia/error.html")
    else:
        return render(request, "encyclopedia/entries.html", {
            "entry": title,
            "content": parsed_content
        })

def search(request):
    print("Im in search function")
    print(util.get_entry(request.GET.get('q')))
    if util.get_entry(request.GET.get('q')) is None:
        entries(request, util.get_entry(request.POST.get('q')))
    else: 
        return render(request, "encyclopedia/error.html")




from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Snippet


def snippet_list(request):
    snippet_list = Snippet.objects.all()
    return render(request,"snippets/snippets_list.html",{'snippet_list':snippet_list})

class SnippetListView(ListView):
    model = Snippet
    template_name = 'snippets/snippets_list.html'

class SnippetDetailView(DetailView):
    model = Snippet
    template_name = 'snippets/snippet_detail.html'

def snippet_detail(request, id):
    snippet = get_object_or_404(Snippet, id=id)
    return render(request,"snippets/snippet_detail.html",{'snippet':snippet})

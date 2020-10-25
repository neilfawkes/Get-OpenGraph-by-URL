from django.shortcuts import render
from opengraph import opengraph
from django.http import HttpResponse
from django import forms
from .forms import URLForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def opengraph_parse(request):
    template = "home_og.html"
    if request.method == "POST":
        try:
            result = opengraph.OpenGraph(URLForm(request.POST)['url_field'].data).to_json()
            return HttpResponse(result)
        except ValueError:
            return HttpResponse("Invalid URL! Please make sure that URL is correct and use 'http', 'https', 'ftp' or 'ftps' prefixes.")
    else:
        form = URLForm()

    context = {"form": form}
    return render(request, template, context)
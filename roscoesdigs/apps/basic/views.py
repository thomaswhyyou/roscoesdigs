from django.shortcuts import render

# Create your views here.

def render_template(request, template=None):
    return render(request, template)
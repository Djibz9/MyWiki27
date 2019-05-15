from django.views import generic
from .models import Page
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


class IndexView(generic.ListView):
    template_name='wiki/index.html'
    context_object_name = 'pages'

    def get_queryset(self):
        return Page.objects.all()

class DetailView(generic.DetailView):
    model = Page
    template_name = 'wiki/detail.html'
#from https://repl.it/@ashleyo/WorseDisfiguredAdaware

def view_page(request, pk):
    try:
        page = Page.objects.get(pk=pk)
        return render(request,'wiki/detail.html', { 'page':page })
    except Page.DoesNotExist:
        return render(request,'wiki/create_page.html', { 'page_name':pk })

@login_required
def edit_page(request, pk):
    try:
        page = Page.objects.get(pk=pk)
        content = page.content
    except Page.DoesNotExist:
        content = ""
    return render(request,'wiki/edit_page.html', { 'page_name':pk, 'content': content})

@login_required
def save_page(request, pk):
    content = request.POST["content"]    
    try:
        page = Page.objects.get(pk=pk)
        page.content = content
    except Page.DoesNotExist:
        page = Page(title=pk, content=content)
    if 'Delete' in request.POST:
        page.delete()
        return redirect('wiki:index')
    if 'Save' in request.POST:
        page.save()
    return redirect(page) 
    

@login_required
def delete_page(request, pk):
    page = Page.objects.get(pk=pk)
    return render(request, "wiki/delete.html",
    {
        'page_name': pk
    })

@login_required
def delete_confirm(request, pk):
    page = Page.objects.get(pk=pk)
    if 'Delete' in request.POST:
        page.delete()
        return redirect ('../../')


    

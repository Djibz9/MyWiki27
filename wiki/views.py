from django.views import generic
from .models import Page, UserFileUpload
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from django.http import HttpResponse
from django.db.models import F

#This is the class that enables the viewing of the homepage named as Index here
class IndexView(generic.ListView):
    template_name='wiki/index.html'
    context_object_name = 'pages'

    def get_queryset(self):
        return Page.objects.all()

#This is the class that enables the viewing of the pages created
class DetailView(generic.DetailView):
    model = Page
    template_name = 'wiki/detail.html'
#from https://repl.it/@ashleyo/WorseDisfiguredAdaware

#This is the class that enables the viewing of the pages created
def view_page(request, pk):
    try:
        page = Page.objects.get(pk=pk)
        {#This is where the page counter is defined #}
        page.counter = F('counter') + 1
        #console.log ('page counter now{}'.format(page.counter))
        page.save(update_fields=['counter'])
        page.refresh_from_db()
        return render(request,'wiki/detail.html', { 'page':page })
    except Page.DoesNotExist:
        return render(request,'wiki/create_page.html', { 'page_name':pk })

#This is the class that enables the editing of pages
# this requires the user to be logged in if he wants to modify the content
@login_required
def edit_page(request, pk):
    try:
        page = Page.objects.get(pk=pk)
        content = page.content
    except Page.DoesNotExist:
        content = ""
    return render(request,'wiki/edit_page.html', { 'page_name':pk, 'content': content})

#This is the class that enables pages to be saved
# this requires the user to be logged in if he wants to save the content he modified or created
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

#This is the class that enables the deletion of pages
# this requires the user to be logged in if he wants to delete the content
@login_required
def delete_page(request, pk):
    try:
        Page.objects.get(pk=pk)
        return render(request, "wiki/delete.html",
        {
            'page_name': pk
        })
    except Page.DoesNotExist:
        return redirect('wiki:index')

@login_required
def delete_confirmation(request, pk):
    page = Page.objects.get(pk=pk)
    if 'Delete' in request.POST:
        page.delete()
        return redirect ('/../../')

#This is the class that enables the uploading of files in the web app 
# this requires the user to be logged in if he wants to upload files
@login_required
def upload_file(request):
    context = {}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadFileForm()
    context['form'] = form
    context['files'] = UserFileUpload.objects.all().order_by('upload')
    return render(request, 'wiki/upload.html', context)

#These are classes of error tests that I wanted to perform
def test_error_500(request):
    raise HttpResponse(status=500)

def test_error_404(request):
    raise HttpResponse(status=404)

from django.views import generic
from .models import Page


class IndexView(generic.ListView):
    template_name='wiki/index.html'
    context_object_name = 'pages'

    def get_queryset(self):
        return Page.objects.filter()

class DetailView(generic.DetailView):
    model = Page
    template_name = 'wiki/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Page.objects.filter()
#from https://repl.it/@ashleyo/WorseDisfiguredAdaware
# def edit_page(request, page_name):
#     try:
#         page = Page.objects.get(pk=page_name)
#     except Page.DoesNotExist:
#         page = Page(title=page_name, content='')
# return render(request,'wiki/edit_page.html', { 'page':page })

# def save_page(request, page_name):
#     content = request.POST["content"]    
#     try:
#         page = Page.objects.get(pk=page_name)
#         page.content = content
#     except Page.DoesNotExist:
#         page = Page(name=page_name, content=content)
#     page.save()
# return redirect('wiki:detail', pk=page_name)
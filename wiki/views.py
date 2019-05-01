from django.views import generic

from .models import Page


class IndexView(generic.ListView):
    template_name='wiki/index.html'
    context_object_name = 'pages'

    def get_queryset(self):
        return Page.objects.filter()

class DetailView(generic.DetailView):
    model = Page
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Page.objects.filter(pub_date__lte=timezone.now())

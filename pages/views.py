from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Page
from registration.models import Profile
from .forms import PageForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, render


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(login_required, self).dispatch(request, *args, **kwargs)

# Create your views here.
class PageListView(ListView):
    model = Page

    def get_queryset(self):
        queryset = super(PageListView, self).get_queryset()
        queryset = queryset.filter(is_approved=True)
        return queryset

class PageListCreatedView(ListView):
    model = Page

    def get_queryset(self):
        queryset = super(PageListCreatedView, self).get_queryset()
        queryset = queryset.filter(created_by=self.request.user)
        return queryset

class PageDetailView(DetailView):
    model = Page

@method_decorator(login_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')

@method_decorator(login_required, name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'

@method_decorator(login_required, name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')


class SearchResultsView(ListView):
    model = Page

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Page.objects.filter(
            Q(title__icontains=query) | Q(address__icontains=query)
        )
        return object_list



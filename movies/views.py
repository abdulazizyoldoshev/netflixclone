from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView
from .models import *
from django.db.models import Q


class HomeView(ListView):
    model = MoviesModel
    template_name = 'main/browse.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(HomeView, self, *args, **kwargs).get_context_data()
        context["categories"] = CategoryModel.objects.all()
        return context

    def get_queryset(self):
        qs = MoviesModel.objects.all().order_by('-pk')[:1]
        return qs


class TvShowView(ListView):
    model = MoviesModel
    template_name = 'main/tv-shows.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(TvShowView, self, *args, **kwargs).get_context_data()
        context['tv'] = CategoryModel.objects.all().exclude(movies__tv_show=False)
        return context

    def get_queryset(self):
        qs = MoviesModel.objects.filter(tv_show=True).order_by('-pk')[:1]
        return qs


class MoviesView(ListView):
    model = MoviesModel
    template_name = 'main/movies.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(MoviesView, self, *args, **kwargs).get_context_data()
        context['movies'] = CategoryModel.objects.all().exclude(movies__tv_show=True)
        return context

    def get_queryset(self):
        qs = MoviesModel.objects.filter(tv_show=False).order_by('-pk')[:1]
        return qs


class LatestView(ListView):
    model = MoviesModel
    template_name = 'main/latest.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(LatestView, self, *args, **kwargs).get_context_data()
        context['latest'] = MoviesModel.objects.all().order_by('-pk')[:10]
        return context

    def get_queryset(self):
        qs = MoviesModel.objects.all().order_by('-pk')[:1]
        return qs


class DetailedView(DetailView):
    model = MoviesModel
    template_name = "main/single.html"

    def get_context_data(self, **kwargs):
        context = super(DetailedView, self).get_context_data()
        context['related'] = MoviesModel.objects.filter(category=MoviesModel.objects.get(id=self.kwargs['pk'])
                                                        .category).exclude(id=self.kwargs['pk'])
        return context


class MyView(ListView):
    model = MoviesModel
    template_name = 'main/mylist.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(MyView, self, *args, **kwargs).get_context_data()
        context["mov"] = MoviesModel.objects.all().filter(mylist__user_id=self.request.user.id)
        return context


def update_mylist(request, pk):
    movie = get_object_or_404(MoviesModel.objects.all().filter(id=pk))
    mylist = MyList.add_and_delete(request.user, movie)

    return redirect(request.GET.get('next', '/'))


class SearchView(ListView):
    model = MoviesModel
    template_name = 'main/search.html'

    def get_queryset(self, *args, **kwargs):
        search = self.request.GET.get("q")
        if search:
            object_list = MoviesModel.objects.filter(
                Q(name__icontains=search) | Q(category__category_name__icontains=search)
                | Q(presented_description__icontains=search) | Q(detailed_description__icontains=search)
            )
            return object_list


class AccountView(TemplateView):
    template_name = 'layouts/account.html'

from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required

app_name = 'movies'

urlpatterns = [
    path('', login_required(HomeView.as_view()), name='browse'),
    path('<int:pk>/addmylist/', update_mylist, name='add_mylist'),
    path('mylist/', login_required(MyView.as_view()), name='mylist'),
    path('account', login_required(AccountView.as_view()), name='account'),
    path('tvshows/', login_required(TvShowView.as_view()), name='tv-shows'),
    path('movies/', login_required(MoviesView.as_view()), name='movies'),
    path('latest/', login_required(LatestView.as_view()), name='latest'),
    path('search/', login_required(SearchView.as_view()), name='search'),
    path('<int:pk>/detail', login_required(DetailedView.as_view()), name='detail')
]

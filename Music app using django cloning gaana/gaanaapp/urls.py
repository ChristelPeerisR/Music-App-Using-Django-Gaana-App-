from django.urls import path
from .import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('recent', views.recent, name='recent'),
    path('recent/<int:id>', views.recentpost, name='recentpost'),
    path('trend', views.trend, name='trend'),
    path('trend/<int:id>', views.trendpost, name='trendpost'),
    path('search',views.search,name='search'),
    path('artists', views.artists, name='artists'),
    path('topcharts', views.topcharts, name='topcharts'),
    path('artistspost/<int:id>', views.artistspost, name='artistspost'),
    path('topchartspost/<int:id>', views.topchartspost, name='topchartspost'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('competiotion/<league_id>/', views.LeagueView.as_view(), name='league'),
    path('team/<team_id>/', views.TeamView.as_view(), name='team'),
]

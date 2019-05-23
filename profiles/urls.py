from django.urls import path
from profiles.views import ProfileListView, ProfileDetailView

profile_patterns = ([
    path('', ProfileListView.as_view(), name='list'),
    path('<username>/', ProfileDetailView.as_view(), name='detail'),
], "profiles")
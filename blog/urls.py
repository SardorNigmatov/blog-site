from django.urls import path
from .views import PostView, post_detail

app_name = 'blog'

urlpatterns = [
    path('',PostView.as_view(),name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',post_detail,name='post_detail')
]
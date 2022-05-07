from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
       # post views
       path('', views.feed_list, name='feed_list'),
       path('<int:year>/<int:month>/<int:day>/<slug:post>/',
            views.post_detail,
            name='post_detail'),
]

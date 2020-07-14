from django.conf.urls import url
from snippets import views
from snippets.views import SnippetDetail

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^snippets/(?P<pk>[0-9]+)/$', SnippetDetail.as_view()),
]
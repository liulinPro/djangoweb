from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views
from snippets.views import SnippetDetail, SnippetsList, SnippetsList5, SnippetsDetail5

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^snippets3/$', views.snippet_list3),
    url(r'^snippets3/(?P<pk>[0-9]+)/$', views.snippet_detail3),
    url(r'^snippets3/(?P<pk>[0-9]+)/$', SnippetDetail.as_view()),
    url(r'^snippets4/$', SnippetsList.as_view()),
    url(r'^snippets4/(?P<pk>[0-9]+)/$', SnippetDetail.as_view()),
    url(r'^snippets5/$', SnippetsList5.as_view()),
    url(r'^snippets5/(?P<pk>[0-9]+)/$', SnippetsDetail5.as_view()),

    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

    url(r'^$', views.api_root),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view()),
]

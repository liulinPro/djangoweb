from django.conf.urls import url, include
from rest_framework import routers

from quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'group', views.GroupViewSet)

# 使用自动 URL 路由连接 API。
# 另外，我们还包括可浏览 API 的登录 URL。
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('snippets.urls')),
]
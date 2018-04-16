from django.conf.urls import url

from board.views import *

urlpatterns = [
    # Example: /
    url(r'^$', PostList.as_view(), name='index'),

    # Example: /board/?page=3
    # 참고 https://goo.gl/BRFiJV
    # view에 paginate_by가 지정되어 있는 경우 페이지 객체수를 전달한다.
    url(r'^postlist/page(?P<page>[0-9]+)/$', PostList.as_view(), name='post_list'),

    # # Example: /post/add/
    url(r'^post/add/$', PostCreate.as_view(), name="post_add",),

    # Example: /post/99/
    url(r'^post/(?P<pk>\d+)/$', PostDetail.as_view(), name='post_detail'),

    # # Example: /post/99/update/
    # url(r'^post/(?P<pk>[0-9]+)/update/$', PostUpdate.as_view(), name="post_update",),

    # # Example: /post/99/delete/
    # url(r'^post/(?P<pk>[0-9]+)/delete/$', PostDelete.as_view(), name="post_delete",),
]
from __future__ import unicode_literals

from django.conf.urls import url

#from .api_views import (
#    APIDocumentTagView, APIDocumentTagListView, APITagDocumentListView,
#    APITagListView, APITagView
#)
from .api_views import DocumentTagViewSet, TagViewSet

from .views import (
    DocumentTagListView, TagAttachActionView, TagCreateView,
    TagDeleteActionView, TagDocumentListView, TagEditView, TagListView,
    TagRemoveActionView
)

urlpatterns = [
    url(
        regex=r'^documents/(?P<document_id>\d+)/tags/$',
        name='document_tag_list', view=DocumentTagListView.as_view()
    ),
    url(
        regex=r'^documents/(?P<document_id>\d+)/tags/multiple/attach/$',
        name='document_tag_multiple_attach', view=TagAttachActionView.as_view()
    ),
    url(
        regex=r'^documents/(?P<document_id>\d+)/tags/multiple/remove/$',
        name='document_tag_multiple_remove',
        view=TagRemoveActionView.as_view()
    ),
    url(
        regex=r'^documents/multiple/attach/$',
        name='document_multiple_tag_multiple_attach',
        view=TagAttachActionView.as_view()
    ),
    url(
        regex=r'^documents/multiple/tags/remove/$',
        name='document_multiple_tag_multiple_remove',
        view=TagRemoveActionView.as_view()
    ),
    url(regex=r'^tags/$', name='tag_list', view=TagListView.as_view()),
    url(
        regex=r'^tags/create/$', name='tag_create',
        view=TagCreateView.as_view()
    ),
    url(
        regex=r'^tags/(?P<tag_id>\d+)/delete/$', name='tag_delete',
        view=TagDeleteActionView.as_view()
    ),
    url(
        regex=r'^tags/(?P<tag_id>\d+)/edit/$', name='tag_edit',
        view=TagEditView.as_view()
    ),
    url(
        regex=r'^tags/(?P<tag_id>\d+)/documents/$',
        name='tag_document_list', view=TagDocumentListView.as_view()
    ),
    url(
        regex=r'^tags/multiple/delete/$', name='tag_multiple_delete',
        view=TagDeleteActionView.as_view()
    )
]


api_router_entries = (
    {'prefix': r'tags', 'viewset': TagViewSet, 'basename': 'tag'},
    {
        'prefix': r'documents/(?P<document_id>\d+)/tags',
        'viewset': DocumentTagViewSet, 'basename': 'document_tag'
    },
)

"""
    url(
        regex=r'^tags/(?P<tag_pk>\d+)/documents/$',
        name='tag-document-list', view=APITagDocumentListView.as_view(),
    ),
    url(
        regex=r'^tags/(?P<tag_pk>\d+)/$', name='tag-detail',
        view=APITagView.as_view()
    ),
    url(regex=r'^tags/$', name='tag-list', view=APITagListView.as_view()),
    url(
        regex=r'^documents/(?P<document_pk>\d+)/tags/$',
        name='document-tag-list', view=APIDocumentTagListView.as_view()
    ),
    url(
        regex=r'^documents/(?P<document_pk>\d+)/tags/(?P<tag_pk>[0-9]+)/$',
        name='document-tag-detail', view=APIDocumentTagView.as_view()
    ),
"""

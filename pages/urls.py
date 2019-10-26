from django.urls import path
from .views import PageListView, PageDetailView, PageCreate, PageUpdate, PageDelete,PageListCreatedView, SearchResultsView

pages_patterns = ([
    path('', PageListView.as_view(), name='pages'),
    path('created', PageListCreatedView.as_view(), name='pages_crated_by'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('create/', PageCreate.as_view(), name='create'),
    path('update/<int:pk>/', PageUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PageDelete.as_view(), name='delete'),
    path('search/', SearchResultsView.as_view(), name='search'),

], 'pages')
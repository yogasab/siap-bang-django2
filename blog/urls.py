from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlgoDeleteView

urlpatterns = [
    # Blog Delete View
    path('post/<int:pk>/delete/', BlgoDeleteView.as_view(), name='post_delete'),
    # Blog Update View
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    # Blog Create View
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    # DetailView post 
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    # ListView homepage
    path('', BlogListView.as_view(), name='home'),
]
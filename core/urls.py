from django.urls import path
from .views import LivroListCreate, LivroDetail

urlpatterns = [
    path('', LivroListCreate.as_view(), name='livros-list-create'),
    path('<int:pk>/', LivroDetail.as_view(), name='livro-detail'),
]

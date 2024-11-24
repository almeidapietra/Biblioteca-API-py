from django.urls import path
from .views import LivroListCreate, LivroDetail, ColecaoListCreate, ColecaoDetail
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('', LivroListCreate.as_view(), name='livros-list-create'),
    path('<int:pk>/', LivroDetail.as_view(), name='livro-detail'),
    path('colecoes/', ColecaoListCreate.as_view(), name='colecoes-list-create'),
    path('colecoes/<int:pk>/', ColecaoDetail.as_view(), name='colecao-detail'),
    
    # URLs para documentação da API
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
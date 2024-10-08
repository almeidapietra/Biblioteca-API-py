from rest_framework import serializers
from .models import Categoria, Autor, Livro

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome']

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nome']

class LivroSerializer(serializers.ModelSerializer):
    autor = serializers.PrimaryKeyRelatedField(queryset=Autor.objects.all())
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())

    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autor', 'categoria', 'publicado_em']

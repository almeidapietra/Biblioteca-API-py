from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Livro, Autor, Categoria, Colecao
from rest_framework.authtoken.models import Token
from django.urls import reverse

class ColecaoTests(TestCase):
    def setUp(self):
        # Criar usuários para teste
        self.user1 = User.objects.create_user(username='user1', password='pass123')
        self.user2 = User.objects.create_user(username='user2', password='pass123')
        
        # Criar tokens para os usuários
        self.token1 = Token.objects.create(user=self.user1)
        self.token2 = Token.objects.create(user=self.user2)
        
        # Configurar client
        self.client = APIClient()
        
        # Criar autor e categoria para os livros
        self.autor = Autor.objects.create(nome='Autor Teste')
        self.categoria = Categoria.objects.create(nome='Categoria Teste')
        
        # Criar um livro para teste
        self.livro = Livro.objects.create(
            titulo='Livro Teste',
            autor=self.autor,
            categoria=self.categoria,
            publicado_em='2024-01-01'
        )
        
        # Criar uma coleção para teste
        self.colecao = Colecao.objects.create(
            nome='Coleção Teste',
            descricao='Descrição teste',
            colecionador=self.user1
        )
        self.colecao.livros.add(self.livro)

    def test_criar_colecao(self):
        """Teste de criação de coleção por usuário autenticado"""
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token1.key}')
        data = {
            'nome': 'Nova Coleção',
            'descricao': 'Nova descrição',
            'livros': [self.livro.id]
        }
        response = self.client.post(reverse('colecoes-list-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Colecao.objects.count(), 2)

    def test_usuario_nao_autenticado(self):
        """Teste de acesso não autorizado"""
        data = {
            'nome': 'Coleção Não Autorizada',
            'descricao': 'Teste',
            'livros': [self.livro.id]
        }
        response = self.client.post(reverse('colecoes-list-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_editar_colecao_proprietario(self):
        """Teste de edição de coleção pelo proprietário"""
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token1.key}')
        data = {
            'nome': 'Coleção Atualizada',
            'descricao': 'Descrição atualizada',
            'livros': [self.livro.id]
        }
        response = self.client.put(
            reverse('colecao-detail', kwargs={'pk': self.colecao.id}),
            data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Colecao.objects.get(id=self.colecao.id).nome, 'Coleção Atualizada')

    def test_editar_colecao_nao_proprietario(self):
        """Teste de tentativa de edição por usuário não proprietário"""
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token2.key}')
        data = {
            'nome': 'Tentativa de Alteração',
            'descricao': 'Tentativa de alteração',
            'livros': [self.livro.id]
        }
        response = self.client.put(
            reverse('colecao-detail', kwargs={'pk': self.colecao.id}),
            data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_listar_colecoes(self):
        """Teste de listagem de coleções para usuário autenticado"""
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token1.key}')
        response = self.client.get(reverse('colecoes-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
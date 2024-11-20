import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from empresas.models import Empresa
from departamentos.models import Departamento
from funcionarios.models import Funcionario


@pytest.fixture(autouse=True, scope= 'function')
def enable_db_access(db):
    pass


@pytest.fixture()
def admin_user(db):
    return User.objects.create_superuser(username='admin', password='admin1234', email='admin@email.com')


@pytest.fixture
def common_user(db):
    return User.objects.create_user(username='testuser', password='test1234', email='test.user@email.com')


@pytest.fixture
def api_client_admin(admin_user):
    client = APIClient()
    response = client.post('/api/token/', {'username': admin_user.username, 'password': 'admin1234'})
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data['access'])
    return client


@pytest.fixture
def api_common_user(common_user):
    client = APIClient()
    response = client.post('/api/token/', {'username': common_user.username, 'password': 'test1234'})
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data['access'])
    return client


@pytest.fixture
def empresa(db):
    return Empresa.objects.create(
        nome="FSP Desenvolvimento de Software Ltda",
        cnpj="12.345.678/0001-99",
        logradouro="Rua Alan Turing, 1912",
        cidade="Rio de Janeiro",
        estado="RJ",
        pais="Brasil",
        ativo=True
    )


@pytest.fixture
def departamento(empresa):
    return Departamento.objects.create(
        nome="Desenvolvimento Backend",
        centro_custo="DEV-BKND-001",
        codigo_integracao="DEV-BKND-INT01",
        ativo=True,
        empresa=empresa
    )

@pytest.fixture
def funcionario(departamento):
    return Funcionario.objects.create(
        nome_completo= "Amanda Cardoso",
        email= "amanda.cardoso@email.com",
        telefone= "021912345678",
        data_nascimento= "1990-01-01",
        data_contratacao= "2023-01-01",
        endereco= "Rua Domingos Azevedo, 123",
        cidade= "Rio de Janeiro",
        estado= "RJ",
        pais= "Brasil",
        cep= "01000-000",
        ativo= True,
        departamento= departamento
    )


@pytest.fixture
def funcionario_pagination(db, departamento):
    # Criar 15 funcionários para teste de paginação
    for i in range(15):
        Funcionario.objects.create(
        nome_completo= f"Funcionário {i+1}",
        email= f"funcionario{i+1}@email.com",
        telefone= f"{i+1}0000000",
        data_nascimento= "2000-01-01",
        data_contratacao= "2023-01-01",
        endereco= f"Rua numerad_{i+1}, 123{i+1}",
        cidade= "Rio de Janeiro",
        estado= "RJ",
        pais= "Brasil",
        cep= "01000-000",
        ativo= True,
        departamento= departamento
    )

@pytest.fixture
def departamento_pagination(db, empresa):
    # Criar 15 departamentos para teste de paginação
    for i in range(15):
        Departamento.objects.create(
            nome=f"Desenvolvimento {i+1}",
            centro_custo=f"CC-{i+1}",
            codigo_integracao=f"CI-{i+1}",
            ativo=True,
            empresa=empresa
        )


@pytest.fixture
def empresa_pagination(db):
    # Criar 15 departamentos para teste de paginação
    for i in range(15):
        Empresa.objects.create(
        nome=f"Empresa {i+1}",
        cnpj=f"{i+1}.000.000/0000-00",
        logradouro=f"Rua empresa{i+1}",
        cidade="Rio de Janeiro",
        estado="RJ",
        pais="Brasil",
        ativo=True
    )
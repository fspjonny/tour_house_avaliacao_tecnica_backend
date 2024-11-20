from rest_framework import status

def test_usuario_não_pode_criar_empresa(api_common_user):
    
    data = {
        "nome": "Delta Desenvolvimento",
        "cnpj": "02.345.678/0001-99",
        "logradouro": "Rua Vale do Silício, 123",
        "cidade": "São Paulo",
        "estado": "SP",
        "pais": "Brasil",
        "ativo": True
    }
    response = api_common_user.post('/api/empresas/', data)

    assert response.data['detail'] == "Você não tem permissão para executar essa ação."
    assert response.status_code == status.HTTP_403_FORBIDDEN




def test_usuario_pode_listar_empresas(api_common_user, empresa):
    response = api_common_user.get('/api/empresas/')
    assert response.data['results'][0]['nome'] == "FSP Desenvolvimento de Software Ltda"
    assert response.status_code == status.HTTP_200_OK



def test_usuario_não_atualiza_empresa(api_common_user, empresa):

    data = {
        "nome":"FSP - Desenvolvimento de Software S.A.",
        "cnpj":"22.345.678/0001-99",
        "logradouro":"Rua PlanaltoExemplo, 123",
        "cidade":"São Paulo",
        "estado":"SP",
        "pais":"Brasil",
        "ativo":True
    }   

    response = api_common_user.put(f'/api/empresas/{empresa.id}/', data)

    assert response.data['detail'] == "Você não tem permissão para executar essa ação."
    assert response.status_code == status.HTTP_403_FORBIDDEN



def test_usuario_não_deleta_empresa(api_common_user, empresa):

    response = api_common_user.delete(f'/api/empresas/{empresa.id}/')

    assert response.data['detail'] == "Você não tem permissão para executar essa ação."
    assert response.status_code == status.HTTP_403_FORBIDDEN



def test_usuario_paginas_empresas(api_common_user, empresa_pagination):
    #Total de empresas criadas são 15
    #Paginação padrão é de 10 itens por página
    
    # Testando a primeira página
    response = api_common_user.get('/api/empresas/?page=1')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['count'] == 15
    assert response.data['next'] is not None  # Deve ter próxima página
    assert response.data['previous'] is None  # Não tem página anterior
    assert len(response.data['results']) == 10

    
    # Testando a segunda página
    response = api_common_user.get('/api/empresas/?page=2')

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 5  # Restante dos itens
    assert response.data['next'] is None  # Não deve ter próxima página
    assert response.data['previous'] is not None  # Deve ter página anterior
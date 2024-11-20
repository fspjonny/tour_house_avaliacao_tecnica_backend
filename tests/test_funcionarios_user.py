from rest_framework import status


def test_usuario_não_cria_funcionario(api_common_user, departamento):
    data = {
        "nome_completo":"Ana Cardoso",
        "email": "ana.cardoso@email.com",
        "telefone": "021932345678",
        "data_nascimento": "1990-01-01",
        "data_contratacao": "2023-01-01",
        "endereco": "Rua Domingos Azevedo, 123",
        "cidade": "Rio de Janeiro",
        "estado": "RJ",
        "pais": "Brasil",
        "cep": "01000-000",
        "ativo": True,
        "departamento": departamento.id
    }
    
    response = api_common_user.post('/api/funcionarios/', data)

    assert response.data['detail'] == "Você não tem permissão para executar essa ação."
    assert response.status_code == status.HTTP_403_FORBIDDEN



def test_usuario_pode_listar_funcionarios(api_common_user, funcionario):

    response = api_common_user.get('/api/funcionarios/')

    assert response.data['results'][0]['nome_completo'] == "Amanda Cardoso"
    assert response.status_code == status.HTTP_200_OK



def test_usuario_não_atualiza_funcionario(api_common_user, departamento, funcionario):

    data = {
        "nome_completo":"Ana Cardoso",
        "email": "ana.cardoso@email.com",
        "telefone": "021932345678",
        "data_nascimento": "1990-01-01",
        "data_contratacao": "2023-01-01",
        "endereco": "Rua Domingos Azevedo, 123",
        "cidade": "Rio de Janeiro",
        "estado": "RJ",
        "pais": "Brasil",
        "cep": "01000-000",
        "ativo": True,
        "departamento": departamento.id
    }

    response = api_common_user.put(f'/api/funcionarios/{funcionario.id}/', data)

    assert response.data['detail'] == "Você não tem permissão para executar essa ação."
    assert response.status_code == status.HTTP_403_FORBIDDEN



def test_usuario_não_deleta_funcionario(api_common_user, funcionario):

    response = api_common_user.delete(f'/api/funcionarios/{funcionario.id}/')
    
    assert response.data['detail'] == "Você não tem permissão para executar essa ação."
    assert response.status_code == status.HTTP_403_FORBIDDEN



def test_usuario_paginas_funcionarios(api_common_user, funcionario_pagination):
    #Total de funcionários criados são 15
    #Paginação padrão é de 10 itens por página
    
    # Testando a primeira página
    response = api_common_user.get('/api/funcionarios/?page=1')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['count'] == 15
    assert response.data['next'] is not None  # Deve ter próxima página
    assert response.data['previous'] is None  # Não tem página anterior
    assert len(response.data['results']) == 10

    
    # Testando a segunda página
    response = api_common_user.get('/api/funcionarios/?page=2')

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 5  # Restante dos itens
    assert response.data['next'] is None  # Não deve ter próxima página
    assert response.data['previous'] is not None  # Deve ter página anterior
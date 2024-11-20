from rest_framework import status

def test_admin_cria_funcionario(api_client_admin, departamento):
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
    
    response = api_client_admin.post('/api/funcionarios/', data)

    assert response.data['nome_completo'] == "Ana Cardoso"    
    assert response.status_code == status.HTTP_201_CREATED



def test_admin_lista_funcionarios(api_client_admin, funcionario):

    response = api_client_admin.get('/api/funcionarios/')

    assert response.data['results'][0]['nome_completo'] == "Amanda Cardoso"
    assert response.status_code == status.HTTP_200_OK


def test_admin_atualiza_funcionario(api_client_admin, departamento, funcionario):

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

    response = api_client_admin.put(f'/api/funcionarios/{funcionario.id}/', data)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['nome_completo'] == "Ana Cardoso"



def test_admin_deleta_funcionario(api_client_admin, funcionario):

    response = api_client_admin.delete(f'/api/funcionarios/{funcionario.id}/')
    
    assert response.data == {"detail":"Registro foi inativado com sucesso."}
    assert response.status_code == status.HTTP_202_ACCEPTED


def test_admin_paginas_funcionarios(api_client_admin, funcionario_pagination):
    #Total de funcionários criados são 15
    #Paginação padrão é de 10 itens por página
    
    # Testando a primeira página
    response = api_client_admin.get('/api/funcionarios/?page=1')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['count'] == 15
    assert response.data['next'] is not None  # Deve ter próxima página
    assert response.data['previous'] is None  # Não tem página anterior
    assert len(response.data['results']) == 10

    
    # Testando a segunda página
    response = api_client_admin.get('/api/funcionarios/?page=2')

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 5  # Restante dos itens
    assert response.data['next'] is None  # Não deve ter próxima página
    assert response.data['previous'] is not None  # Deve ter página anterior
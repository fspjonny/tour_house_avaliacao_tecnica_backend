from rest_framework import status

def test_admin_cria_empresa(api_client_admin):
    
    data = {
        "nome": "Delta Desenvolvimento",
        "cnpj": "02.345.678/0001-99",
        "logradouro": "Rua Vale do Silício, 123",
        "cidade": "São Paulo",
        "estado": "SP",
        "pais": "Brasil",
        "ativo": True
    }
    response = api_client_admin.post('/api/empresas/', data)
    assert response.status_code == status.HTTP_201_CREATED



def test_admin_lista_empresas(api_client_admin, empresa):
    response = api_client_admin.get('/api/empresas/')
    assert response.data['results'][0]['nome'] == "FSP Desenvolvimento de Software Ltda"
    assert response.status_code == status.HTTP_200_OK



def test_admin_atualiza_empresa(api_client_admin, empresa):

    data = {
        "nome":"FSP - Desenvolvimento de Software S.A.",
        "cnpj":"22.345.678/0001-99",
        "logradouro":"Rua PlanaltoExemplo, 123",
        "cidade":"São Paulo",
        "estado":"SP",
        "pais":"Brasil",
        "ativo":True
    }   

    response = api_client_admin.put(f'/api/empresas/{empresa.id}/', data)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['nome'] == "FSP - Desenvolvimento de Software S.A."



def test_admin_deleta_empresa(api_client_admin, empresa):
    response = api_client_admin.delete(f'/api/empresas/{empresa.id}/')
    assert response.data == {"detail":"Registro foi inativado com sucesso."}
    assert response.status_code == status.HTTP_202_ACCEPTED



def test_admin_paginas_empresas(api_client_admin, empresa_pagination):
    #Total de empresas criadas são 15
    #Paginação padrão é de 10 itens por página
    
    # Testando a primeira página
    response = api_client_admin.get('/api/empresas/?page=1')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['count'] == 15
    assert response.data['next'] is not None  # Deve ter próxima página
    assert response.data['previous'] is None  # Não tem página anterior
    assert len(response.data['results']) == 10

    
    # Testando a segunda página
    response = api_client_admin.get('/api/empresas/?page=2')

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 5  # Restante dos itens
    assert response.data['next'] is None  # Não deve ter próxima página
    assert response.data['previous'] is not None  # Deve ter página anterior
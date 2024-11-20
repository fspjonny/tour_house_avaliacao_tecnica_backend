from rest_framework import status

def test_admin_criar_departamento(api_client_admin, empresa):

    data = {
        "nome": "Desenvolvimento Backend",
        "centro_custo": "DEV-BKND-001",
        "codigo_integracao": "DEV-BKND-INT01",
        "ativo": True,
        "empresa": empresa.id
    }

    response = api_client_admin.post('/api/departamentos/', data)
    
    assert response.status_code == status.HTTP_201_CREATED



def test_admin_lista_departamentos(api_client_admin, departamento):

    response = api_client_admin.get('/api/departamentos/')
    
    assert response.data['results'][0]['nome'] == "Desenvolvimento Backend"
    assert response.status_code == status.HTTP_200_OK




def test_admin_atualiza_departamento(api_client_admin, departamento, empresa):

    data = {
        "nome": "Desenvolvimento de Testes",
        "centro_custo": "QA-001",
        "codigo_integracao": "QA-INT01",
        "ativo": True,
        "empresa": empresa.id
    }

    response = api_client_admin.put(f'/api/departamentos/{departamento.id}/', data)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['nome'] == "Desenvolvimento de Testes"



def test_admin_deleta_departamento(api_client_admin, departamento):

    response = api_client_admin.delete(f'/api/departamentos/{departamento.id}/')
    
    assert response.data == {"detail":"Registro foi inativado com sucesso."}
    assert response.status_code == status.HTTP_202_ACCEPTED


def test_admin_paginas_departamentos(api_client_admin, departamento_pagination):
    #Total de departamentos criados são 15
    #Paginação padrão é de 10 itens por página
    
    # Testando a primeira página
    response = api_client_admin.get('/api/departamentos/?page=1')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['count'] == 15
    assert response.data['next'] is not None  # Deve ter próxima página
    assert response.data['previous'] is None  # Não tem página anterior
    assert len(response.data['results']) == 10

    
    # Testando a segunda página
    response = api_client_admin.get('/api/departamentos/?page=2')

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 5  # Restante dos itens
    assert response.data['next'] is None  # Não deve ter próxima página
    assert response.data['previous'] is not None  # Deve ter página anterior
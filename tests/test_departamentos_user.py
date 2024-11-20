from rest_framework import status

def test_usuario_não_pode_criar_departamento(api_common_user, empresa):

    data = {
        "nome": "Desenvolvimento Backend",
        "centro_custo": "DEV-BKND-001",
        "codigo_integracao": "DEV-BKND-INT01",
        "ativo": True,
        "empresa": empresa.id
    }

    response = api_common_user.post('/api/departamentos/', data)

    assert response.data['detail'] == "Você não tem permissão para executar essa ação."
    assert response.status_code == status.HTTP_403_FORBIDDEN
    



def test_usuario_pode_listar_departamentos(api_common_user, departamento):
    
    response = api_common_user.get('/api/departamentos/')
    
    assert response.data['results'][0]['nome'] == "Desenvolvimento Backend"
    assert response.status_code == status.HTTP_200_OK



def test_usuario_não_atualiza_departamento(api_common_user, departamento, empresa):

    data = {
        "nome": "Desenvolvimento de Testes",
        "centro_custo": "QA-001",
        "codigo_integracao": "QA-INT01",
        "ativo": True,
        "empresa": empresa.id
    }

    response = api_common_user.put(f'/api/departamentos/{departamento.id}/', data)

    assert response.data['detail'] == "Você não tem permissão para executar essa ação."
    assert response.status_code == status.HTTP_403_FORBIDDEN



def test_usuario_não_deleta_departamento(api_common_user, departamento):

    response = api_common_user.delete(f'/api/departamentos/{departamento.id}/')
    
    assert response.data['detail'] == "Você não tem permissão para executar essa ação."
    assert response.status_code == status.HTTP_403_FORBIDDEN



def test_usuario_paginas_departamentos(api_common_user, departamento_pagination):
    #Total de departamentos criados são 15
    #Paginação padrão é de 10 itens por página
    
    # Testando a primeira página
    response = api_common_user.get('/api/departamentos/?page=1')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['count'] == 15
    assert response.data['next'] is not None  # Deve ter próxima página
    assert response.data['previous'] is None  # Não tem página anterior
    assert len(response.data['results']) == 10

    
    # Testando a segunda página
    response = api_common_user.get('/api/departamentos/?page=2')

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 5  # Restante dos itens
    assert response.data['next'] is None  # Não deve ter próxima página
    assert response.data['previous'] is not None  # Deve ter página anterior
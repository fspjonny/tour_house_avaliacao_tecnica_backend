
# **Documentação dos Testes Automatizados**

## **Sumário**
1. [Introdução](#introdução)  
2. [Estrutura do Projeto](#estrutura-do-projeto)  
3. [Testes por Funcionalidade](#testes-por-funcionalidade)  
   - Empresas
   - Departamentos
   - Funcionários
   - Auth e Users
4. [Detalhes de Implementação](#detalhes-de-implementação)

---

## **Introdução**

Esta documentação descreve os testes automatizados implementados para o projeto de gerenciamento de empresas, departamentos e funcionários.  
Os testes garantem que as permissões e funcionalidades da API estejam funcionando conforme esperado para diferentes tipos de usuários (administradores e usuários comuns).

---

## **Configuração dos testes**
Defini a troca do banco de dados de testes diretamente no arquivo 
settings.py utilizando SQLite em memória.  
É uma prática válida, ainda mais em container Docker, pois simplifica e centraliza o ambiente de testes e evita configurações adicionais.

```
if 'pytest' in sys.modules:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }

```
## O Raciocínio dos testes
O código detecta automaticamente se o módulo pytest está em uso, indicando que o ambiente de execução atual é para testes.  
Quando identificado, ele substitui as configurações padrão do banco de dados para utilizar um SQLite em memória.  
Isso permite que os testes sejam executados em um ambiente isolado e independente do banco de dados principal (PostgreSQL no caso da aplicação em produção).  

Todas as definições de ambiente ficam em um único arquivo (settings.py), simplificando a gestão do ambiente de execução e reduzindo a necessidade de arquivos adicionais.

## Automação:

Não é necessário passar parâmetros adicionais ou carregar configurações específicas para testes, pois o sistema detecta automaticamente o ambiente pelo módulo pytest.

## Velocidade:

O SQLite em memória é extremamente rápido para operações de leitura/escrita, melhorando o tempo de execução dos testes.

## Isolamento seguro:

Evita riscos de interferência com dados reais em outros bancos de dados, protegendo as informações sensíveis.

## Comparação com o uso do arquivo conftest.py  

O arquivo conftest.py geralmente é utilizado no contexto do Pytest para configurar fixtures ou manipular comportamentos globais para testes.  
Configurar o banco de dados no conftest.py seria uma abordagem alternativa, mas apresenta algumas diferenças:

### - Flexibilidade:

O conftest.py permite configurar várias fixtures e tornar o ambiente de testes mais modular.  
No entanto, as configurações no settings.py afetam diretamente o comportamento do Django, garantindo que o banco seja ajustado antes mesmo de qualquer código de teste ser executado.

### - Complexidade:

Configurações no conftest.py exigiriam uso de pacotes como django.conf.settings.configure ou pytest-django para ajustar dinamicamente as configurações do banco.  
Isso adiciona uma camada de complexidade que pode ser evitada com a abordagem no settings.py.

### - Padronização:

Configurar diretamente no settings.py segue a lógica padrão de Django e facilita o entendimento para quem já está habituado ao framework.  

## Por que escolher configurar no settings.py ?
Ao optar por definir as configurações de teste no settings.py, você mantém a simplicidade e a integração direta com o Django, além de evitar a necessidade de arquivos adicionais ou configurações externas.  
Isso é especialmente vantajoso em projetos menores ou quando a configuração do banco de dados para testes é a única variação necessária no ambiente.

Essa abordagem alinha-se com os princípios de KISS (Keep It Simple, Stupid), priorizando simplicidade e eficiência.

## **Estrutura do Projeto**

Os testes são organizados em arquivos modulares, cada um dedicado a uma entidade específica e separado por perfil de usuário:

```
tests/
├── users.py               # Testes para garantir nível dos usuários
├── auth.py                # Testes para obtenção e negação de token
├── empresas_admin.py      # Testes para admins manipulando empresas
├── empresas_user.py       # Testes para usuários comuns em empresas
├── departamentos_admin.py # Testes para admins manipulando departamentos
├── departamentos_user.py  # Testes para usuários comuns em departamentos
├── funcionarios_admin.py  # Testes para admins manipulando funcionários
├── funcionarios_user.py   # Testes para usuários comuns em funcionários
```

---

## **Testes por Funcionalidade**

### **1. Empresas**

#### **Admin**
**Arquivo:** `empresas_admin.py`  
- **Criar Empresa**: Verifica se um administrador pode criar uma nova empresa.  
- **Listar Empresas**: Valida se as empresas cadastradas são listadas corretamente.  
- **Atualizar Empresa**: Testa se um admin consegue editar os dados de uma empresa existente.  
- **Inativar Empresa**: Verifica se ao tentar deletar uma empresa, ela é marcada como inativa ao invés de ser excluída.  
- **Paginação**: Confirma o funcionamento da paginação ao listar empresas (10 itens por página).

#### **Usuário Comum**
**Arquivo:** `empresas_user.py`  
- **Criar Empresa**: Garante que usuários comuns não podem criar empresas.  
- **Listar Empresas**: Testa se os usuários podem visualizar as empresas cadastradas.  
- **Atualizar Empresa**: Verifica que os usuários comuns não têm permissão para editar empresas.  
- **Inativar Empresa**: Confirma que usuários comuns não podem excluir ou inativar empresas.  
- **Paginação**: Testa a paginação na listagem de empresas.

---

### **2. Departamentos**

#### **Usuário Comum**
**Arquivo:** `departamentos_user.py`  
- **Criar Departamento**: Garante que um usuário comum não pode criar novos departamentos.  
- **Listar Departamentos**: Verifica se usuários conseguem visualizar departamentos cadastrados.  
- **Atualizar Departamento**: Garante que usuários não podem editar departamentos existentes.  
- **Excluir Departamento**: Testa se usuários comuns são impedidos de excluir departamentos.  
- **Paginação**: Testa o comportamento da paginação na listagem de departamentos.

---

### **3. Funcionários**

#### **Admin**
**Arquivo:** `funcionarios_admin.py`  
- **Criar Funcionário**: Testa a criação de funcionários vinculados a um departamento específico.  
- **Listar Funcionários**: Verifica se a listagem de funcionários está funcionando corretamente.  
- **Atualizar Funcionário**: Valida que um administrador pode editar os dados de um funcionário.  
- **Inativar Funcionário**: Testa a inativação de registros ao invés de exclusão física.  
- **Paginação**: Confirma a funcionalidade de paginação ao listar funcionários.

#### **Usuário Comum**
**Arquivo:** `funcionarios_user.py`  
- **Criar Funcionário**: Garante que usuários comuns não podem adicionar funcionários.  
- **Listar Funcionários**: Testa se usuários conseguem visualizar os dados de funcionários.  
- **Atualizar Funcionário**: Garante que usuários comuns não têm permissão para editar funcionários.  
- **Excluir Funcionário**: Valida que usuários comuns não podem excluir funcionários.  
- **Paginação**: Testa o comportamento da paginação na listagem de funcionários.

---

### **4. Auth e Users**

#### **Admin e Usuários comuns**
**Arquivo:** `auth.py`  
- **Obter token de acesso**: Testa a obtenção de token de acesso informando o usuário e senha cadastrado.
- **Renovar token de acesso**: Testa a renovação de token expirado, informando o token vencido para ser renovado.

**Arquivo:** `users.py`  
- **Verificar se o usuário é Administrador**: Testa se um usuário é administrador ou não.
- **Verificar se usuário é de restrito**: Testa se um usuário é de restrição ou não.
- **Verificar se usuário pode fazer login**: Testa se os dados de acesso do usuário podem acessar a API.

---

## **Detalhes de Implementação**

### **Permissões**
- Usuários comuns recebem respostas com status `403 FORBIDDEN` e mensagem:  
  `"Você não tem permissão para executar essa ação."` ao tentar realizar ações proibidas.

### **Paginação**
- A configuração padrão exibe **10 itens por página**:
  - Endpoint: `/api/<entidade>/?page=<número_da_página>`.
  - Testado para comportar 15 registros (2 páginas, sendo a segunda com 5 itens).

### **Inativação**
- Entidades não são excluídas fisicamente, mas marcadas como inativas.  
  - Exemplo de resposta ao inativar:  
    ```json
    {
        "detail": "Registro foi inativado com sucesso."
    }
    ```

### **Status HTTP**
| Ação                              | Usuário Comum     | Administrador     |
|-----------------------------------|-------------------|-------------------|
| Criar Entidade                    | 403 FORBIDDEN     | 201 CREATED       |
| Listar Entidades                  | 200 OK            | 200 OK            |
| Atualizar Entidade                | 403 FORBIDDEN     | 200 OK            |
| Inativar/Deletar Entidade         | 403 FORBIDDEN     | 202 ACCEPTED      |

---

### **Exemplo de Teste**
#### Teste: `test_usuario_não_cria_funcionario`
**Descrição**: Garante que um usuário comum não pode criar registros de funcionários.

```python
def test_usuario_não_cria_funcionario(api_common_user, departamento):
    data = {
        "nome_completo": "Ana Cardoso",
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
```


# **ITMSS Recursos Humanos**

API desenvolvida para gerenciar o cadastro de funcionários da empresa **ITMSS Recursos Humanos**, permitindo um controle eficiente de funcionários, departamentos e empresas.  

## **📚Descrição do Projeto**  

A API resolve dificuldades enfrentadas pela empresa no gerenciamento de funcionários e suas relações com departamentos e empresas.  

**Funcionalidades principais**:
- Cadastro, listagem, filtro e inativação de registros (funcionários, departamentos e empresas).
- Vinculação de funcionários a departamentos e empresas.
- Controle de acesso baseado em usuários (administradores têm permissão total, usuários comuns têm apenas leitura).
- Nenhum registro pode ser deletado; em vez disso, são marcados como inativos.  

---

## **🛠️Pré-requisitos**  

- **Python** 3.12 ou superior  
- **Docker** e **Docker Compose**  
- **Poetry** (para gerenciamento de dependências e tarefas)  

---

## **🖥️Instalação**  

1. Clone este repositório:  
   ```bash
   git clone https://github.com/fspjonny/tour_house_avaliacao_tecnica_backend.git
   cd tour_house_avaliacao_tecnica_backend
   ```  

2. Crie um arquivo `.env` na raiz do projeto com base no `.env.example` e configure as variáveis de ambiente.  

**Exemplo**:
```env
# Django
SECRET_KEY='sua-chave-secreta'
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,[::1],web

# Postgres
POSTGRES_USER=seu-usuario
POSTGRES_PASSWORD=sua-senha
POSTGRES_DB=seu-banco
DATABASE_HOST=db
DATABASE_PORT=5432

# Django Superuser
DJANGO_SUPERUSER_USERNAME=seu-admin-username
DJANGO_SUPERUSER_PASSWORD=seu-admin-password
DJANGO_SUPERUSER_EMAIL=seu-admin-email
```

3. Instale as dependências com **Poetry**,  
recomendo usar com a flag para melhor experiência na demonstração:
   ```bash
   poetry install --with dev
   ```

---

## **🚀 Execução com Docker**  

### **Subindo os contêineres**
Certifique-se de que o Docker Desktop está ativo e execute:  
```bash
task up
```  

Os serviços serão executados em:  
- **API**: [http://localhost:8000](http://localhost:8000)  
- **Swagger (documentação)**: [http://localhost:8000/api/doc/](http://localhost:8000/api/docs/)  

### **Parando os contêineres**  
Para encerrar e remover os contêineres, use:  
```bash
task down
```

---

## **Testes Automatizados**  

### **Executar testes localmente**
Execute os testes com o seguinte comando:
```bash
task test
```

### **Relatório de cobertura**
Após os testes, você pode gerar um relatório de cobertura do coverage:
```bash
task post-test
```

### **Dentro do contêiner**
Se estiver no ambiente Docker, rode os testes com:
```bash
poetry run task test
```

---

## **Estrutura do Projeto**

```plaintext
tour_house_avaliacao_tecnica_backend
 ┣ core/
 ┣ departamentos/
 ┣ empresas/
 ┣ funcionarios/
 ┣ tests/
 ┣ utils/
 ┣ .env
 ┣ ITMSS Recursos Humanos - Cadastro API.postman_collection.json
 ┣ ITMSS Recursos Humanos - Cadastro API.yaml
 ┣ pyproject.toml
 ┗ README.md
```

### **Script Customizado**
em:
- **`funcionarios/management/commands/popular_tabelas.py`**: Popula tabelas com dados iniciais (somente para demonstração).

---

## **📍Endpoints Principais**

A documentação completa está disponível em:
- **Swagger**: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)  

Além disso, tem os arquivos de collectiosn que podem ser usados para testes:
- `ITMSS Recursos Humanos - Cadastro API.yaml`  
- `ITMSS Recursos Humanos - Cadastro API.postman_collection.json`  

---

## **✉️Contato**

Em caso de dúvidas ou problemas, entre em contato:  
- **E-mail**: [seuemail@email.com](mailto:fabio.silvapedro@gmail.com)

---

## **👋😃 Obrigado por visitar**
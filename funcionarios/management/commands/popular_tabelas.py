import factory
from empresas.models import Empresa
from departamentos.models import Departamento
from funcionarios.models import Funcionario
from django.core.management.base import BaseCommand
from faker import Faker
from utils.progressbar import progressbar
import random
import unicodedata
import re

fake = Faker('pt-BR')

"""
    Remover caracteres problemáticos para normalizar o texto para UTF-8.
    O Faker causa muitos desses problemas.
"""
def normalize_text(text):
    if not isinstance(text, str):
        return text
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
    text = re.sub(r'[^\w\s.,-]', '', text)
    return text.strip()


class EmpresaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Empresa

    nome = factory.LazyFunction(lambda: normalize_text(fake.company()))
    cnpj = factory.Faker('cnpj', locale='pt_BR')
    logradouro = factory.LazyFunction(lambda: normalize_text(fake.address()))
    cidade = factory.LazyFunction(lambda: normalize_text(fake.city()))
    estado = factory.Faker('state_abbr', locale='pt_BR')
    pais = 'Brasil'
    ativo = True


class DepartamentoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Departamento

    nome = factory.LazyFunction(lambda: normalize_text(fake.word()))
    centro_custo = factory.Faker('bothify', text='CC-???-####', locale='pt_BR')
    codigo_integracao = factory.Faker('bothify', text='INT-???-###', locale='pt_BR')
    ativo = True
    empresa = factory.SubFactory(EmpresaFactory)


class FuncionarioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Funcionario

    nome_completo = factory.LazyFunction(lambda: normalize_text(fake.name()))
    email = factory.LazyFunction(lambda: fake.email())
    telefone = factory.LazyFunction(lambda: fake.phone_number())
    data_nascimento = factory.Faker('date_of_birth', locale='pt_BR', minimum_age=18, maximum_age=60)
    data_contratacao = factory.Faker('date_this_year', locale='pt_BR')
    endereco = factory.LazyFunction(lambda: normalize_text(fake.address()))
    cidade = factory.LazyFunction(lambda: normalize_text(fake.city()))
    estado = factory.Faker('state_abbr', locale='pt_BR')
    pais = 'Brasil'
    cep = factory.Faker('postcode', locale='pt_BR')
    ativo = True
    departamento = factory.SubFactory(DepartamentoFactory)


def create_empresas(qtd=25):
    empresas = []
    for _ in progressbar(range(qtd), "Criando empresas"):
        empresas.append(EmpresaFactory.build())
    Empresa.objects.bulk_create(empresas)


def create_departamentos(qtd=20):
    empresas = list(Empresa.objects.all())
    departamentos = []

    for _ in progressbar(range(qtd), "Criando departamentos"):
        empresa = random.choice(empresas)
        departamento = DepartamentoFactory.build(empresa=empresa)
        departamentos.append(departamento)

    Departamento.objects.bulk_create(departamentos)


def create_funcionarios(qtd=150):
    departamentos = list(Departamento.objects.all())
    funcionarios = []

    for _ in progressbar(range(qtd), "Criando funcionários"):
        departamento = random.choice(departamentos)
        funcionario = FuncionarioFactory.build(departamento=departamento)
        funcionarios.append(funcionario)

    Funcionario.objects.bulk_create(funcionarios)




class Command(BaseCommand):
    help = "Popular tabelas: Empresa, Departamento e Funcionario"

    def handle(self, *args, **options):
        try:
            print("Iniciando processo de criação...")
            create_empresas()
            create_departamentos()
            create_funcionarios()
            self.stdout.write(self.style.SUCCESS("Tabelas populadas com sucesso!"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Erro ao popular tabelas: {e}"))    
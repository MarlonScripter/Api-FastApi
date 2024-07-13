from typing import Annotated, Optional
from pydantic import Field, PositiveFloat

from workout_api.categorias.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta
from workout_api.contrib.schemas import BaseShama, OutMixin

class Atleta(BaseShama):
    nome: Annotated[str, Field(description= 'Nome do Atleta', example='João', max_length=50)] # type: ignore
    cpf: Annotated[str, Field(description= 'CPF do Atleta', example='12345678900', max_length=11)] # type: ignore
    idade: Annotated[int, Field(description= 'Idade do Atleta', example='32')] # type: ignore
    peso: Annotated[PositiveFloat, Field(description= 'Peso do Atleta', example='85.6')] # type: ignore
    altura: Annotated[PositiveFloat, Field(description= 'Altura do Atleta', example='1.75')] # type: ignore
    sexo: Annotated[str, Field(description= 'Sexo do Atleta', example='M', max_length=1)] # type: ignore
    categoria: Annotated[CategoriaIn, Field(description= 'Categoria do Atleta')]
    centro_treinamneto: Annotated[CentroTreinamentoAtleta, Field(description= 'Centro de treinamento do Atleta')]

class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMixin):
    pass

class AtletaUpdate(BaseShama):
    nome: Annotated[Optional[str], Field(None, description= 'Nome do Atleta', example='João', max_length=50)] # type: ignore
     idade: Annotated[Optional[int], Field(None, description= 'Idade do Atleta', example='32')] # type: ignore
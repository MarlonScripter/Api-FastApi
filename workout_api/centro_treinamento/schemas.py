from typing import Annotated

from pydantic import UUID4, Field
from workout_api.contrib.schemas import BaseShama


class CentroTreinamentoIn(BaseShama):
    nome: Annotated[str, Field(description= 'Nome do centro de treinamento', example='Area 51', max_length=20)] # type: ignore
    endereco: Annotated[str, Field(description= 'Endereço do centro de treinamento', example='Rua X, Q02', max_length=60)] # type: ignore
    proprietario: Annotated[str, Field(description= 'Proprietario do centro de treinamento', example='Joaquim', max_length=30)] # type: ignore


class CentroTreinamentoAtleta(BaseShama):
    nome: Annotated[str, Field(description= 'Nome do centro de treinamento', example='Area 51', max_length=20)] # type: ignore


class CentroTreinamentoOut(CentroTreinamentoIn):
    id = Annotated[UUID4, Field(description='Identificador do centro de treinamento')]
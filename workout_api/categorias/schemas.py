from typing import Annotated

from pydantic import UUID4, Field
from workout_api.contrib.schemas import BaseShama


class CategoriaIn (BaseShama):
    nome: Annotated[str, Field(description= 'Nome da categoria', example='Scale', max_length=10) # type: ignore
 ]
    
class CategoriaOut(CategoriaIn):
    id = Annotated[UUID4, Field(description='Identificador da categoria')]
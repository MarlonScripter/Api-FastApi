from typing import Annotated
from pydantic import UUID4, BaseModel, Field
from datetime import datetime

class BaseShama(BaseModel):
    class config:
        extra = 'forbid'
        from_attributes = True

class OutMixin(BaseShama):
    id = Annotated[UUID4, Field(description='Identificador')]
    create_at = Annotated[datetime, Field(description='Data de criação')]
# generated by datamodel-codegen:
#   filename:  person.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, List, Optional

from pydantic import BaseModel, Field, conint


class Fur(Enum):
    Short_hair = 'Short hair'
    Long_hair = 'Long hair'


class Pet(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    fur: Optional[Fur] = None


class Person(BaseModel):
    first_name: str = Field(..., description="The person's first name.")
    last_name: str = Field(..., description="The person's last name.")
    age: Optional[conint(ge=0)] = Field(None, description='Age in years.')
    pets: Optional[List[Pet]] = None
    comment: Optional[Any] = None

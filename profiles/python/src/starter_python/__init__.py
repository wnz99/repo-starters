from pydantic import BaseModel, ConfigDict, Field


class Name(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    value: str = Field(min_length=1)

from pydantic import BaseModel
from pydantic import ConfigDict


class CountryBase(BaseModel):
    country_name: str
    region: str


class CountryCreate(CountryBase):
    pass


class CountryRead(CountryBase):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int

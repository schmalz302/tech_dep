from pydantic import BaseModel, Field


class Get_user_info_form(BaseModel):
    name: str = Field(default="Undefined", min_length=3, max_length=20)
    telegram: str = Field(pattern=r"^@[A-Za-z\d_]{5,32}$")
    direction: str
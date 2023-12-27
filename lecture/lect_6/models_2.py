from pydantic import BaseModel, Field


# #Field - Используется для предоставления дополнительной информации о поле либо
# для модели, либо для комплексной проверки. Некоторые аргументы
# применяются только к числовым полям (int, float, Decimal), а некоторые
# применяются только к str.
class Item(BaseModel):
    name: str = Field(max_length=10)


class User(BaseModel):
    age: int = Field(default=0)

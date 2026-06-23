from pydantic import BaseModel

#crear la clase cliente
class ClienteBase(BaseModel):
    id: int
    nombre: str
    email: str
    descripcion: str

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int | None = None

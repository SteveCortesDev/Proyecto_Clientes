from pydantic import BaseModel

#crear la clase cliente

class ClienteBase(BaseModel):
    nombre: str
    email: str
    descripcion: str

class ClienteCreate(ClienteBase):
    pass

class ClienteEditar(BaseModel):
    pass

class Cliente(ClienteBase):
    id: int | None = None

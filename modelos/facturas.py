from pydantic import BaseModel


class FacturaBase(BaseModel):
    fecha: str
    vr_total: float
    cliente_id: int

class FacturaCrear(FacturaBase):
    pass

class Factura(FacturaBase):
    id: int | None = None
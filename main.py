from fastapi import FastAPI, HTTPException
from modelos.clientes import Cliente, ClienteCrear ,ClienteEditar
from modelos.facturas import Factura, FacturaCrear, FacturaEditar
from modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar

app = FastAPI()



lista_clientes: list[Cliente] = []
lista_facturas: list[Factura] = []
lista_transacciones: list[Transaccion] = []

#endpoint,para listar todos los clientes
@app.get("/clientes", response_model=list[Cliente])
async def listar_clientes():
    return lista_clientes        

#endpoint,para un solo cliente
@app.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(cliente_id: int):
    #recorrer la lista de clientes y buscar el cliente con el id proporcionado
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            return obj_cliente
        
#endpint,para crear un cliente
@app.post("/clientes", response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear):
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    #generar id
    id_cliente = len(lista_clientes)+1
    cliente_val.id = id_cliente
    lista_clientes.append(cliente_val)
    return cliente_val

@app.patch("/clientes/{cliente_id}", response_model=Cliente)
async def editar_cliente(cliente_id: int, datos_cliente: ClienteEditar):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            #validar cliente
            cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            cliente_val.id = cliente_id
            listar_clientes[i] = cliente_val
            return cliente_val
        raise HTTPException(
        status_code=404, detail=f"El cliente con id {cliente_id} no existe"
    )

    #endpoint, para eliminar un cliente
@app.delete("/clientes/{cliente_id}", response_model=Cliente)
async def eliminar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            cliente_eliminado = lista_clientes.pop(i)
            return cliente_eliminado
    raise HTTPException(
        status_code=404, detail=f"El cliente con id {cliente_id} no existe"
    )







#crear los endpoints para facturas

@app.get("/facturas", response_model=list[Factura])
async def listar_facturas(): 
    return lista_facturas

@app.get("/facturas/{id_factura}", response_model=Factura)
async def listar_factura(id_factura: int):
    pass

@app.post("/facturas", response_model=Factura)
async def crear_factura(id_cliente: int, datos_factura: Factura):
    pass

@app.patch("/facturas/{id_factura}", response_model=Factura)
async def editar_factura(id_factura: int, datos_factura: Factura):
    pass

@app.delete("/facturas/{id_factura}", response_model=Factura)
async def eliminar_factura(id_factura: int):
    pass


# crear los endpoints para transacciones

@app.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones():
    pass

@app.get("/transacciones/{id_transaccion}", response_model=Transaccion)
async def listar_transaccion(id_transaccion: int):
    pass

@app.post("/transacciones", response_model=Transaccion)
async def crear_transaccion(datos_transaccion: Transaccion):
    pass

@app.patch("/transacciones/{id_transaccion}", response_model=Transaccion)
async def editar_transaccion(id_transaccion: int, datos_transaccion: Transaccion):
    pass

@app.delete("/transacciones/{id_transaccion}", response_model=Transaccion)
async def eliminar_transaccion(id_transaccion: int):
    pass

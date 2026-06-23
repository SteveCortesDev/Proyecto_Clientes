from fastapi import FastAPI
from modelos.clientes import Cliente, ClienteCrear

app = FastAPI()



lista_cliente: list[Cliente] = []

#endpoint,para listar todos los clientes
@app.get("/clientes", response_model=list[Cliente])
def listar_clientes():
    return lista_cliente        

#endpoint,para un solo cliente
@app.get("/clientes/{cliente_id}", response_model=Cliente)
def listar_cliente(cliente_id: int):
    #recorrer la lista de clientes y buscar el cliente con el id proporcionado
    for i, obj_cliente in enumerate(lista_cliente):
        if obj_cliente.get("id") == cliente_id:
            return obj_cliente
        
#endpint,para crear un cliente
@app.post("/clientes")
def crear_cliente(datos_cliente: ClienteCrear):
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    lista_cliente.append(cliente_val)
    return cliente_val

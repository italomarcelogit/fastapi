from random import randint
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.get('/api/pedidos/')
def geraPedidos(): 
    '''
    Gera lista de pedidos com dados aleatórios
    '''
    lista = [
        [
         x+randint(100, 10000),          # pedido
         f"Cliente {randint(40, 250)}",  # cliente
         f"Filial ({randint(1,10)})",    # loja
         f"Executivo {randint(15, 55)}", # Executivo
         randint(400, 8000)              # valor
        ]
        for x in range(0, randint(5,15))]
    return JSONResponse(content=jsonable_encoder(lista))

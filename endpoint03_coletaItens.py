from random import randint
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.get('/pedido/items/{id_pedido}')
async def geraItems(id_pedido: int):  
    '''
    Gera lista de itens referente a um pedido,
    de forma aleatória, com os atributos:
    - item (numero sequencial)
    - descrição do item
    '''
    items = []
    try:
        if id_pedido:
            for x in range(0, randint(6, 15)):
                items.append(
                    [f"Item {x + 1}", float(randint(100, 400))]
                )
        return JSONResponse(content=jsonable_encoder(items))
    except:
        pass

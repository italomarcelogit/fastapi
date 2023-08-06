from fastapi import FastAPI, Request
import requests
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    '''
    Constrói lista aleatória de pedidos
    '''
    uri = f"http://localhost:82/api/pedidos/"
    
    try:
        dados = requests.get(uri)  
        if dados.status_code == 200:
            dados = dados.json()
    except requests.ConnectionError:
       dados = []
       pass
    
    model = {
                "titulo": "vAp Insights",
                "h1": "Painel de Insights",
                "h4": "Vendas nos últimos 15min."
            }
    resources = {"request": request, "model": model, "dados": dados}
    return templates.TemplateResponse("index.html", resources)

@app.get("/pedido/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    '''
    Lista itens do pedido.
    '''
    model = {
                "titulo": "vAp Insights - Pedidos de Vendas",
                "h1": "Detalhes do Pedido"
            }
    uri = f"http://localhost:83/pedido/items/{id}"

    try:
        items = requests.get(uri)  
        if items.status_code == 200:
            items = items.json()
    except requests.ConnectionError:
       items = []
       pass

    resources = {"request": request, "id": id, "model": model, "dados": items}
    return templates.TemplateResponse("pedidos.html", resources)
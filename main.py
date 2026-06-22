from fastapi import FastAPI, HTTPException
from typing import List
from models import ProductCreate, ProductUpdate, ProductResponse

app = FastAPI(
    title="Products API",
    description="API REST para cadastro e gerenciamento de produtos.",
    version="1.0.0"
)

# Banco de dados em memória (simples para demonstração)
products_db: dict = {}
next_id: int = 1


@app.get("/", tags=["Root"])
def root():
    return {"message": "Products API está rodando! Acesse /docs para ver a documentação."}


@app.post("/products", response_model=ProductResponse, status_code=201, tags=["Produtos"])
def create_product(product: ProductCreate):
    """Cria um novo produto."""
    global next_id
    new_product = {"id": next_id, **product.model_dump()}
    products_db[next_id] = new_product
    next_id += 1
    return new_product


@app.get("/products", response_model=List[ProductResponse], tags=["Produtos"])
def list_products():
    """Lista todos os produtos cadastrados."""
    return list(products_db.values())


@app.get("/products/{product_id}", response_model=ProductResponse, tags=["Produtos"])
def get_product(product_id: int):
    """Busca um produto pelo ID."""
    product = products_db.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")
    return product


@app.patch("/products/{product_id}", response_model=ProductResponse, tags=["Produtos"])
def update_product(product_id: int, data: ProductUpdate):
    """Atualiza parcialmente um produto."""
    product = products_db.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")
    updates = data.model_dump(exclude_unset=True)
    product.update(updates)
    products_db[product_id] = product
    return product


@app.delete("/products/{product_id}", status_code=204, tags=["Produtos"])
def delete_product(product_id: int):
    """Remove um produto pelo ID."""
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")
    del products_db[product_id]

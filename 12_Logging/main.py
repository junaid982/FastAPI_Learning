

from fastapi import FastAPI

from helpers.logging_config import logger


app = FastAPI(name = "Loggin in FastAPI")

PRODUCTS = []


@app.post("/add/product/")
async def add_product(product : dict):
    
    logger.info("Recieve The Query Data.")
    # PRODUCTS.append(product)
    logger.info("Prodct data stores into the PRODUCT List.")
    
    return {
        "message" : "product addedd successfully"
    }
    
    

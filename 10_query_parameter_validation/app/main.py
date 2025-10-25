



from fastapi import FastAPI
from typing import Annotated

app = FastAPI( name = "Query Parameter Validation")
PRODUCTS = [
    {
        "id": 1,
        "title": "Wireless Bluetooth Headphones",
        "description": "Over-ear headphones with noise cancellation and 20-hour battery life.",
        "quantity": 25,
        "price": 3499.00
    },
    {
        "id": 2,
        "title": "Smartwatch Pro X2",
        "description": "Fitness and health tracking smartwatch with AMOLED display.",
        "quantity": 15,
        "price": 6999.00
    },
    {
        "id": 3,
        "title": "Mechanical Keyboard MK-200",
        "description": "RGB backlit mechanical keyboard with blue switches.",
        "quantity": 30,
        "price": 2899.00
    },
    {
        "id": 4,
        "title": "4K Ultra HD Monitor 27-inch",
        "description": "High-resolution display with 144Hz refresh rate and HDR support.",
        "quantity": 10,
        "price": 19999.00
    },
    {
        "id": 5,
        "title": "USB-C Fast Charger 65W",
        "description": "Compact charger compatible with laptops and smartphones.",
        "quantity": 50,
        "price": 1599.00
    }
]



# Old Method for Query Parameter Validation 

# cURL
'''

http://127.0.0.1:8000/product/?search=usb

http://127.0.0.1:8000/product/
'''

from fastapi import Query

@app.get("/product/")
async def get_product_search(search : str | None = Query(None , Default=None , max_length=5 , min_length=2 )):
    
    """
    This API is used to seach ,
    In This API we are going to show how we can use validation on Query Parameters 
    ( This is a old method we do not currently using in Fast API  Not Recommended by the Fast APi Team)
    """
    if search:
        for product in PRODUCTS:
            if search.lower() in str(product.get("title")).lower() or search.lower() in str(product.get("description")).lower():
                return product
            
    return PRODUCTS





# New Way for validation in query parameter 

# cURL
'''

http://127.0.0.1:8000/product/?search=usb

http://127.0.0.1:8000/product/

'''


from typing import Annotated


@app.get("/search/product/")
async def search_product(search : Annotated[str | None ,Query(max_length=5)] = None):

    """
    This API is used to seach ,
    In This API we are going to show how we can use validation on Query Parameters with Annotated 
    ( This is a new method we do  currently using in Fast API  Recommended by the Fast APi Team)
    """
    if search:
        for product in PRODUCTS:
            if search.lower() in str(product.get("title")).lower() or search.lower() in str(product.get("description")).lower():
                return product
            
    return PRODUCTS
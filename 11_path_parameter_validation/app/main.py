


from fastapi import FastAPI



app = FastAPI(name = "Path parameter Validation")



# API Without any validation
'''
curl -X 'GET' \
'http://127.0.0.1:8000/product/1' \
  -H 'accept: application/json'
'''

'''
# also accepts the -11 value  ( which is does not able to accept  )

curl -X 'GET' \
  'http://127.0.0.1:8000/product/-11' \
  -H 'accept: application/json'

'''

@app.get("/product/{product_id}")
async def product(product_id : int):
    """
    In this API we are going to learn how to add validation on path parameter 
    """
    
    return product_id




# APi with Validation 
# This api with Path aparameter with validation 

# Now user can pass the id between 1 to 10 only its not able to accept the negative values 

# ge "stands for Greater Then "  
# le "stands for Less Then "   

'''
Curl

curl -X 'GET' \
  'http://127.0.0.1:8000/get/product/1' \
  -H 'accept: application/json'
'''


from fastapi import Path
from typing import Annotated


@app.get("/get/product/{product_id}")
async def getproduct(product_id : Annotated[int , Path(ge=1 , le = 10)]):
    """
    In this API we are going to learn how to add validation on path parameter 
    """
    
    return product_id
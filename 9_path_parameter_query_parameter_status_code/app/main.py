




from fastapi import FastAPI
from fastapi import status
from fastapi.responses import Response 

app = FastAPI(name = "Query_Parameter Path Parameter and status code")



# 1 - Example for Path parameter and Status code 

# Example cURL 
'''
curl --location 'http://127.0.0.1:8000/product/shoes/'
'''


@app.get("/product/{product_name}/" , status_code = status.HTTP_200_OK)
async def get_product(product_name : str) :
    """
    In this Example we can learn how we can pass path parameter with statuc code 
    
    # What is Path Parameter:
    
    Path pameter which is we can pass the value throud the url which is compulsory if we define .
    
    # In this Example "product_name" is path parameter , which we allready define in the path its compulsory to use 
 
    """
    
    return {
        "message" : f"This is our product : {product_name}"
    }
    
 
 
 
 
 
   
# 2 - Example for Query Parameter and Status code 

# Example cURL

'''
curl --location 'http://127.0.0.1:8000/get/product/?product=shoes'
'''
@app.get("/get/product/")
async def get_products(product : str):
    """
    In this Example we are going to see how we can use query parameter ,
    
    # When we are not define any parameter into the path but define inside a method 
    # Example "product" is not define inside a path but define inside a function parameter its a query parametr
    
    """

    return {
        "message" : f"The Product name is : {product}",
    }
    


# 3 - Example for multiple Query Parameter and Status code 

# Example cURL

'''
curl --location 'http://127.0.0.1:8000/get/multiple/product/?product=shoes&quantity=100'
'''
@app.get("/get/multiple/product/")
async def get_products(product : str , quantity : int):
    """
    In this Example we are going to see how we can use query parameter ,
    
    # When we are not define any parameter into the path but define inside a method 
    # Example "product" and "quantity" is not define inside a path but define inside a function parameter its a query parametr
    
    """

    return {
        "message" : f"The Product name is : {product} ,and quantity is {quantity}"
    }
    
    
    
    
    
    

# 4 - Example for optional Query Parameter 

# Example cURL

'''
curl --location 'http://127.0.0.1:8000/get/optional/multiple/product/?product=shoes&quantity=100'

curl --location 'http://127.0.0.1:8000/get/optional/multiple/product/?product=shoes'

curl --location 'http://127.0.0.1:8000/get/optional/multiple/product/'

'''
@app.get("/get/optional/multiple/product/")
async def get_products(product : str | None = None , quantity : int | None = None  ):
    """
    In this Example we are going to see how we can use optional query parameter ,
    
    # Optional means this is not compulsory to use 
    # Example 
    
    product : str | None = None  
    
    this query parameter is optional to use 
     
    """

    return {
        "message" : f"The Product name is : {product} ,and quantity is {quantity}"
    }
    
    
    
    
    
    
    


# 5 - Example to use path parameter and query parameter in a same example 


'''
curl --location 'http://127.0.0.1:8000/get/product/with/path/query/shoes/?product_id=121&quantity=100'
''' 

@app.get("/get/product/with/path/query/{product_name}")
async def get_product_details(product_name : str , product_id : int , quantity : int | None = None ):
    """
    In this Example we are going to check how we can use query parameters and path paramter at a same time  
    """
    
    return {
        "message" : f"Product Name is : {product_name} , product_id : {product_id} and  quantity of the prduct : {quantity}"
    }
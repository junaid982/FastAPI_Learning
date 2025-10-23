
# command to run 
# >>> fastapi dev main.py 


from fastapi import FastAPI

app = FastAPI(name = "Path Parameter with Type")


@app.get("/")
async def index():
    
    return {
        "message" : "Check why url path order matters in fastapi"
    }  
    
# Suppose you have same two url path  as below URLS 

# /get/products/{product_name}   # Dynamic path Url 
# /get/products/shoes            # Static URL 


# if user passes "shoes" in dynamic url but you are assuming it will call dynamic its wrong 

# always called first API 

# Thats why "Order" matters in fastapi 

# always add static url first 


@app.get("/get/product/shoes")
async def get_static_product():
    return {
        "message" : f"Static Api call success "
    }
    
@app.get("/get/product/{product_name}")
async def get_dynamic_product(product_name : str):
    
    return {
        "message" : f"Dynamic API call success with product name :{product_name}"
    }
 
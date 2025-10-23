
# command to run 
# >>> fastapi dev main.py 


from fastapi import FastAPI
from enum import Enum


app = FastAPI(name = "Predefine values")



# api without predefine categories 

@app.get("/product/category/{product_category}")
async def product_category(product_category : str):
    
    if product_category in ["electronics" , "clothing" , "books" ]:
        if product_category == "electronics":
            return {
                "message" : "we have large varity of electronics gadets."
            }
            
        elif product_category == "clothing" : 
            return {
                "message" : "we have tending cloths."
            }
            
        elif product_category == "books":
            return {
                "message" : f"we have larg library of books."
            }
    
    else:
        return {
            "error" : f"the given category does not match with defined categories : {product_category}"
        }






# How we can predefine the Values in Fast API 

class ProductCategory(str , Enum):
    electronics = "electronics"
    clothing = "clothing"
    books = "books"
    
    
@app.get("/get/product/category/{category_name}")
async def get_product_category(category_name : ProductCategory):
    
    if category_name == ProductCategory.electronics:
        return {
            "message" : "We have a larg varity of electronic gadets."
        }
        
        
    elif category_name.value == "clothing":
        return {
            "messgae" : "we have tending cloths"
        }
        
    elif category_name == ProductCategory.books.value:
        return {
            "messgae" : "we have large library of books"
        }
        
    
    
    return {
        "message" : f"hello api"
    }
    
    

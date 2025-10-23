
# command to run 
# >>> fastapi dev main.py 


from fastapi import FastAPI , Request
import json

app = FastAPI(name = "Path Parameter with Type")



# Assume This is our table in a database and inside this is our data inside data 
products_table = [
    {
        "id": 1,
        "product_name": "Lenovo ThinkPad X1 Carbon",
        "specification": "Intel i7, 16GB RAM, 512GB SSD, 14-inch FHD",
        "stock_count": 12,
    },
    {
        "id": 2,
        "product_name": "Apple MacBook Pro M3",
        "specification": "Apple M3 chip, 16GB RAM, 1TB SSD, 14-inch Retina",
        "stock_count": 8,
    },
    {
        "id": 3,
        "product_name": "Dell XPS 13",
        "specification": "Intel i5, 8GB RAM, 512GB SSD, 13.4-inch FHD+",
        "stock_count": 20,
    },
    {
        "id": 4,
        "product_name": "HP Envy x360",
        "specification": "Ryzen 7, 16GB RAM, 1TB SSD, Touchscreen 15.6-inch",
        "stock_count": 15,
    },
    {
        "id": 5,
        "product_name": "Asus ROG Strix G15",
        "specification": "Ryzen 9, RTX 4070, 32GB RAM, 1TB SSD, 15.6-inch QHD",
        "stock_count": 5,
    },
    {
        "id": 6,
        "product_name": "Acer Aspire 7",
        "specification": "Intel i5, GTX 1650, 8GB RAM, 512GB SSD, 15.6-inch FHD",
        "stock_count": 18,
    },
    {
        "id": 7,
        "product_name": "Samsung Galaxy Tab S9",
        "specification": "Snapdragon 8 Gen 2, 12GB RAM, 256GB Storage, 11-inch AMOLED",
        "stock_count": 10,
    },
    {
        "id": 8,
        "product_name": "Apple iPad Pro 12.9",
        "specification": "M2 Chip, 16GB RAM, 512GB Storage, Liquid Retina XDR",
        "stock_count": 6,
    },
    {
        "id": 9,
        "product_name": "Logitech MX Master 3S",
        "specification": "Wireless Bluetooth Mouse, 8000 DPI, USB-C Rechargeable",
        "stock_count": 25,
    },
    {
        "id": 10,
        "product_name": "LG UltraFine 4K Monitor",
        "specification": "27-inch 4K IPS Display, USB-C, 60Hz Refresh Rate",
        "stock_count": 9,
    },
]
 


@app.get("/")
async def index():
    
    explain = """
    * Path Parameter and Http Methods 
    - path parameter is similer as django dynamic URL.
    - http methods are simple 
        GET
        POST
        PUT
        PATCH
        DELETE
    """
    
    return {
        "explain" : explain
    }  
    



# CRUD Operation Example 



# POST Method Example 
@app.post("/add_product")
async def add_product(request : Request):
    """
    This API is used to add the product 
    """
    
    data = await request.json()  # Read the Json Data 
    
    product_name = data.get("product_name")
    specification = data.get("specification")
    stock_count = data.get("stock_count")
    
    if not product_name or not specification or not stock_count:
        return {
            "error" : "product_name , specification and stock_count fields are required."
        }
    
    
    # Generate the Last Id 
    
    last_id = int(products_table[-1].get("id"))

    id = last_id +1
    
    new_product = {
        "id" : id,
        "product_name" : product_name,
        "specification" : specification,
        "stock_count" : stock_count,
    }
    
    products_table.append(new_product)
    
    return {
        "message" : "product added successfully"
    }
    
    


# GET Method Example 
@app.get("/products")
async def get_all_products():
    """
    This API will return all the available products .
    """
    
    all_products = products_table.copy()
    
    return {
        "producs" : all_products
    }
    
    



# GET Method Example 
@app.get("/products/{product_id}")
async def get_product_by_id(product_id):
    
    """
    This is used to get the single prodcut by its id 
    """
    product_id = int(product_id)
    
    all_products = products_table.copy()
    
    
    for product in all_products:
        
        if product_id == product.get("id"):
            
            product_index_position = all_products.index(product)
            
            prod =  all_products[product_index_position]
            return {
                "product" : prod
            }
    



# ( PUT Method Example) Complete Update or Replace  

@app.put("/update_product/{product_id}")
async def update_product(product_id , request : Request):
    """
    This API Is used to Update or replace entire product details 
    """
    
    product_id = int(product_id)
    
    data = await request.json()  # Fetch the data from request body 
    
    product_name = data.get("product_name")
    specification = data.get("specification")
    stock_count = data.get("stock_count")
    
    if not product_id or not product_name or not specification or not stock_count:
        return {
            "error" : "product_name , specification and stock_count fields are required ."
        }
    
    
    new_data = {
        "id" : product_id,
        "product_name" : product_name,
        "specification" : specification,
        "stock_count" : stock_count
    }
    
    for product in products_table:
        if product_id == product.get("id"):
            
            product_index = products_table.index(product)
            
            products_table[product_index] = new_data

            return {
                "message" : "Product updated successfully"
            }
            
    

# ( Patch method Example ) Partial Update 

@app.patch("/edit_product/{product_id}")
async def edit_product(product_id , request : Request):
    """
    This API is used to partial update or edit the products 
    """
    
    # "product_name" : product_name,
    #     "specification" : specification,
    #     "stock_count" : stock_count
    
    data = await request.json()
    product_name = data.get("product_name" , None)
    specification = data.get("specification" , None)
    stock_count = data.get("stock_count" , None)
    
    
    
    
    product_id = int(product_id)
    
    # Get the Product from the database 
    
    for product in products_table:
        if product_id == product.get("id"):
            
            product_index = products_table.index(product)
            
            if product_name :
                product["product_name"] = product_name
                
            if specification:
                product["specification"] = specification
            
            if stock_count :
                product["stock_count"] = stock_count
                
            products_table[product_index] = product
            
            
            return {
                "message" : "Product successfully edited"
            }
            
            



# ( Delete method Example ) Delete the product 

@app.delete("/delete_product/{product_id}") 
async def delete_product(product_id):
    
    """
    This API is used to delete the specif product by id 
    """
    
    product_id = int(product_id)
    
    for product in products_table:
        
        product_index = products_table.index(product)
        
        if product_id == product.get("id"):
            del products_table[product_index]
            
            return {
                "message" : "product Deleted successfully"
            }
            

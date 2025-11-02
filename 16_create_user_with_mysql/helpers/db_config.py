import aiomysql


# DB_CONFIG = {
#     "host" : "localhost",
#     "user" : "root",
#     "password" : "Opo@1234",
#     "db" : "Authentication_project"
# }



async def connection():
    conn = await aiomysql.connect(
        host="localhost",
        user="root",
        password="Opo@1234",
        db="Authentication_project"
    )
    return conn 


# async def connection():
#     conn = await aiomysql.create_pool(
#         host="localhost",
#         user="root",
#         password="Opo@1234",
#         db="Authentication_project"
#     )
#     return conn 
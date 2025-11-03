
import aiomysql


async def connection():
    
    conn = await aiomysql.connect(
        host="localhost",
        user="root",
        password="Opo@1234",
        db="Authentication_project"
    )
    return conn


from fastapi import FastAPI

app = FastAPI()



@app.get("/")
async def read_main():
    return {"msg": "DEPLOIMENT SUR LE NAMESPACE TUTU"}



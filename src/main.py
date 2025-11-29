from fastapi import FastAPI
import uvicorn


app = FastAPI()

tshirts = {
    1:{
        "id":"0001",
        "age":2,
        "gender":"male"
    },
    2:{
        "id":"0002",
        "age":1,
        "gender":"female"
    }
}

@app.get("/tshirts")
async def get_tshirst():
    return tshirts

@app.get("/tshirts/{tshirt_id}")
async def get_tshirt(tshirt_id: int):
    tshirt = tshirts[tshirt_id]
    return tshirt


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
from fastapi import FastAPI
from routes import router
# from fastapi

app = FastAPI(title="Portfolio 3D API", version="1.0.0")
app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Welcome to the Portfolio 3D API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

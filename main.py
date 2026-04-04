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
    import os
    from dotenv import load_dotenv  # pyright: ignore[reportMissingImports]
    load_dotenv()

    host = os.getenv("HOST", "localhost")
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host=host, port=port)

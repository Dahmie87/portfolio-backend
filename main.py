from fastapi import FastAPI
from routes import router
from database import engine, Base
import models

# from fastapi

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Portfolio 3D API", version="1.0.0")

app.include_router(router, prefix="/api/v1")


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

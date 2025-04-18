import uvicorn
 
from app.db.database import get_db_session
from sqlalchemy.ext.asyncio import AsyncSession
from .core.config import settings
from fastapi.middleware.cors import CORSMiddleware
 
 
from fastapi import Depends, FastAPI
 
 
app = FastAPI(
    title=settings.project_name,
    docs_url="/api/docs",
    version=settings.version,
)
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)
 
@app.on_event("startup")
def on_startup():
    print("Server is starting...")


@app.get("/", tags=["root"])
async def read_root(db: AsyncSession = Depends(get_db_session)):
    return f"{settings.environment} Server is Up"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)
from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends
from app.schemas import PostCreate
from app.db import Post, create_db_and_tables, get_async_session, User
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy import select


@asynccontextmanager
async def lifespan(app: FastAPI):
    
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    caption: str = Form(...),
    sssion: AsyncSession = Depends(get_async_session),
):
    post = Post(
        caption=caption,
        url=file.filename,
        file_type=file.content_type,
        file_name=file.filename,
    )
    sssion.add(post)
    await sssion.commit()
    await sssion.refresh(post)
    return post

@app.get("/feed")
async def get_feed(
    session: AsyncSession = Depends(get_async_session),
):
    result = await session.execute(
        "SELECT * FROM posts ORDER BY created_at DESC"
    )
    posts = result.fetchall()
    return posts
 
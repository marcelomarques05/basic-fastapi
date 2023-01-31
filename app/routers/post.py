from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from .. import models, oauth2
from ..database import get_db
from ..schemas import PostCreate, Post, PostOut

router = APIRouter(prefix="/posts", tags=["Posts"])

# @router.get("/", response_model=List[Post])
@router.get("/", response_model=List[PostOut])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
  posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
    models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(
    models.Post.owner_id == current_user.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
  
  return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Post)
def create_posts(post: PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
  new_post = models.Post(owner_id=current_user.id, **post.dict())
  db.add(new_post)
  db.commit()
  db.refresh(new_post)
  return new_post 

@router.get("/{post_id}", response_model=PostOut)
def get_post(post_id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
  post_query = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
    models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == post_id).filter(models.Post.owner_id == current_user.id)
  post = post_query.first()

  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post id {post_id} was not found or you don't have access.")

  return post

@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
  post_query = db.query(models.Post).filter(models.Post.id == post_id)
  post = post_query.first()

  if post == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"ID {post_id} does not exist.")

  if post.owner_id != current_user.id:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")

  post_query.delete(synchronize_session=False)
  db.commit()

  return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{post_id}", response_model=Post)
def update_post(post_id: int, updated_post: PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
  post_query = db.query(models.Post).filter(models.Post.id == post_id)
  post = post_query.first()

  if post == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"ID {post_id} does not exist.")

  if post.owner_id != current_user.id:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")

  post_query.update(updated_post.dict(), synchronize_session=False)
  db.commit()

  return post_query.first()
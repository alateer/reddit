from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.db.session import SessionLocal

router = APIRouter()

@router.get("gen_id", response_model=)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from .models import Item
from .schemas import ItemSchema

router = APIRouter(prefix="/example", tags=["Example"])


@router.get('/')
def test():
    return 'This is an example module'

@router.get('/item/{id}')
def get_item(id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter_by(id=id).first()

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return ItemSchema(id=item.id, name=item.name, description=item.description)
from sqlalchemy.orm import Session
from . import models, schemas

def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_clients(db: Session):
    return db.query(models.Client).all()

def get_client_by_id(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.id == client_id).first()

def delete_client(db: Session, client_id: int):
    client = get_client_by_id(db, client_id)
    if client:
        db.delete(client)
        db.commit()
        return True
    return False

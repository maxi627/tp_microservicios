from app.models import Stock
from app import db
from app.repositories import Repository_get, Repository_create, Repository_update, Repository_delete,Repository_save


class StockRepository(Repository_create,Repository_delete,Repository_update,Repository_get,Repository_save):
    def __init__(self):
        self.__model = Stock

    def get_all(self) -> list[Stock]:
        return db.session.query(self.__model).all()

    def get_by_id(self, id) -> Stock:
        return db.session.query(self.__model).get(id)

    def create(self, entity: Stock) -> Stock:
        db.session.add(entity)
        db.session.commit()
        return entity

    def update(self, id, t: Stock) -> Stock:
        entity = self.get_by_id(id)
        if entity:
            entity.id_Stock= t.id_Stock
            entity.nombre= t.nombre
            db.session.add(entity)
            db.session.commit()
            return entity
        return None

    def delete(self, id)-> bool:
        Stock = self.get_by_id(id)
        if Stock:
            db.session.delete(Stock)
            db.session.commit()
            return Stock
        return None
    
    def save(self, entity: Stock) -> Stock:
        db.session.add(entity) 
        db.session.commit()
        return entity
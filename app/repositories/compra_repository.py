from app.models import Compra
from app import db
from app.repositories import Repository_get, Repository_create, Repository_update, Repository_delete,Repository_save


class CompraRepository(Repository_create,Repository_delete,Repository_update,Repository_get,Repository_save):
    def __init__(self):
        self.__model = Compra

    def get_all(self) -> list[Compra]:
        return db.session.query(self.__model).all()

    def get_by_id(self, id) -> Compra:
        return db.session.query(self.__model).get(id)

    def create(self, entity: Compra) -> Compra:
        db.session.add(entity)
        db.session.commit()
        return entity

    def update(self, id, t: Compra) -> Compra:
        entity = self.get_by_id(id)
        if entity:
            entity.id_Compra= t.id_Compra
            entity.nombre= t.nombre
            db.session.add(entity)
            db.session.commit()
            return entity
        return None

    def delete(self, id)-> bool:
        Compra = self.get_by_id(id)
        if Compra:
            db.session.delete(Compra)
            db.session.commit()
            return Compra
        return None
    
    def save(self, entity: Compra) -> Compra:
        db.session.add(entity) 
        db.session.commit()
        return entity
     
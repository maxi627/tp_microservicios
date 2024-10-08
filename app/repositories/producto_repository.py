from app.models import Producto
from app import db
from app.repositories import Repository_get, Repository_create, Repository_update, Repository_delete,Repository_save


class ProductoRepository(Repository_create,Repository_delete,Repository_update,Repository_get,Repository_save):
    def __init__(self):
        self.__model = Producto

    def get_all(self) -> list[Producto]:
        return db.session.query(self.__model).all()

    def get_by_id(self, id) -> Producto:
        return db.session.query(self.__model).get(id)

    def create(self, entity: Producto) -> Producto:
        db.session.add(entity)
        db.session.commit()
        return entity

    def update(self, id, t: Producto) -> Producto:
        entity = self.get_by_id(id)
        if entity:
            entity.id_Producto= t.id_Producto
            entity.nombre= t.nombre
            db.session.add(entity)
            db.session.commit()
            return entity
        return None

    def delete(self, id)-> bool:
        Producto = self.get_by_id(id)
        if Producto:
            db.session.delete(Producto)
            db.session.commit()
            return Producto
        return None
    
    def save(self, entity: Producto) -> Producto:
        db.session.add(entity) 
        db.session.commit()
        return entity
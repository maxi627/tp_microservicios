from app.models import Pagos
from app import db
from app.repositories import Repository_get, Repository_create, Repository_update, Repository_delete,Repository_save


class PagosRepository(Repository_create,Repository_delete,Repository_update,Repository_get,Repository_save):
    def __init__(self):
        self.__model = Pagos

    def get_all(self) -> list[Pagos]:
        return db.session.query(self.__model).all()

    def get_by_id(self, id) -> Pagos:
        return db.session.query(self.__model).get(id)

    def create(self, entity: Pagos) -> Pagos:
        db.session.add(entity)
        db.session.commit()
        return entity

    def update(self, id, t: Pagos) -> Pagos:
        entity = self.get_by_id(id)
        if entity:
            entity.id_Pagos= t.id_Pagos
            entity.nombre= t.nombre
            db.session.add(entity)
            db.session.commit()
            return entity
        return None

    def delete(self, id)-> bool:
        Pagos = self.get_by_id(id)
        if Pagos:
            db.session.delete(Pagos)
            db.session.commit()
            return Pagos
        return None
    
    def save(self, entity: Pagos) -> Pagos:
        db.session.add(entity) 
        db.session.commit()
        return entity
     
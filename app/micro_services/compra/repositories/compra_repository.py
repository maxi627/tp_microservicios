from typing import List

from app import db
from app.micro_services.compra.models import Compra

from .repository import Repository_delete, Repository_get, Repository_save


class CompraRepository(Repository_save, Repository_get, Repository_delete):
    def save(self, entity: Compra) -> Compra:
        db.session.add(entity)
        db.session.commit()
        return entity

    def get_all(self) -> List[Compra]:
        return Compra.query.all()

    def get_by_id(self, id: int) -> Compra:
        return Compra.query.get(id)

    def delete(self, id: int) -> bool:
        compra = self.get_by_id(id)
        if compra:
            db.session.delete(compra)
            db.session.commit()
            return True
        return False

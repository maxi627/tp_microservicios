
from app.models import Compra
from app.repositories import CompraRepository


class CompraService:
    def __init__(self):
        self.repository = CompraRepository()

    def get_all(self) -> list[Compra]:
        return self.repository.get_all()

    def get_by_id(self, id)-> Compra:
        return self.repository.get_by_id(id)

    def create(self, entity: Compra)-> Compra:
        return self.repository.create(entity)

    def update(self, id, Compra) -> Compra:
        return self.repository.update(id, Compra)

    def delete(self, id)->bool:
        return self.repository.delete(id)
    
    def save(self, entity: Compra) -> Compra:
        return self.repository.save(entity)
     
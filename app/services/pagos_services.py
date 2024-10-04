
from app.models import Pagos
from app.repositories import PagosRepository


class PagosService:
    def __init__(self):
        self.repository = PagosRepository()

    def get_all(self) -> list[Pagos]:
        return self.repository.get_all()

    def get_by_id(self, id)-> Pagos:
        return self.repository.get_by_id(id)

    def create(self, entity: Pagos)-> Pagos:
        return self.repository.create(entity)

    def update(self, id, Pagos) -> Pagos:
        return self.repository.update(id, Pagos)

    def delete(self, id)->bool:
        return self.repository.delete(id)
    
    def save(self, entity: Pagos) -> Pagos:
        return self.repository.save(entity)
     
from app.models import Producto
from app.repositories import ProductoRepository


class ProductoService:
    def __init__(self):
        self.repository = ProductoRepository()

    def get_all(self) -> list[Producto]:
        return self.repository.get_all()

    def get_by_id(self, id)-> Producto:
        return self.repository.get_by_id(id)

    def create(self, entity: Producto)-> Producto:
        return self.repository.create(entity)

    def update(self, id, Producto) -> Producto:
        return self.repository.update(id, Producto)

    def delete(self, id)->bool:
        return self.repository.delete(id)
    
    def save(self, entity: Producto) -> Producto:
        return self.repository.save(entity)
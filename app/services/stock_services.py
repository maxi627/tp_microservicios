from app.models import Stock
from app.repositories import StockRepository


class StockService:
    def __init__(self):
        self.repository = StockRepository()

    def get_all(self) -> list[Stock]:
        return self.repository.get_all()

    def get_by_id(self, id)-> Stock:
        return self.repository.get_by_id(id)

    def create(self, entity: Stock)-> Stock:
        return self.repository.create(entity)

    def update(self, id, Stock) -> Stock:
        return self.repository.update(id, Stock)

    def delete(self, id)->bool:
        return self.repository.delete(id)
    
    def save(self, entity: Stock) -> Stock:
        return self.repository.save(entity)
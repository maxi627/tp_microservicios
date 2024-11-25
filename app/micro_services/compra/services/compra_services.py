from app import cache
from app.micro_services.compra.models import Compra
from app.micro_services.compra.repositories import CompraRepository

repository = CompraRepository()

class CompraService:
    def all(self) -> list[Compra]:
        result = cache.get('compras')
        if result is None:
            result = repository.get_all()
            cache.set('compras', result, timeout=15)
        return result

    def add(self, compra: Compra) -> Compra:
        compra = repository.save(compra)
        cache.set(f'compra_{compra.id}', compra, timeout=15)
        return compra

    def delete(self, id: int) -> bool:
        result = repository.delete(id)
        if result:
            cache.delete(f'compra_{id}')
        return result

    def find(self, id: int) -> Compra:
        result = cache.get(f'compra_{id}')
        if result is None:
            result = repository.get_by_id(id)
            if result:
                cache.set(f'compra_{id}', result, timeout=15)
        return result

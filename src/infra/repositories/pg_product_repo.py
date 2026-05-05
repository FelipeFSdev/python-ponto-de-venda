from uuid import UUID

from sqlmodel import Session

from src.adapters.product_db_gateway import IProductGateway
from src.domain.entities.product_model import Products

class PgProductRepository(IProductGateway):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_product(self, create_data: dict):
        new_product = Products(
            description = create_data["description"],
            stock_level = create_data["stock_level"],
            value = create_data["value"],
            category_id = create_data["category_id"]
        )

        self.db_session.add(new_product)
        self.db_session.commit()
        self.db_session.refresh(new_product)
    
    def get_product(self):
        pass
    
    def detail_product(self):
        pass
    
    def update_product(self):
        pass

    def delete_product(self):
        pass

    

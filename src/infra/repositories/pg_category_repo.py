from sqlmodel import select, Session

from src.domain.entities.category_model import Categories
from src.adapters.category_db_gateway import ICategoryGateway
from src.dto.category_dto import ICategoryUpdateDTO, ICategoryCreateDTO



class PgCategoryRepository(ICategoryGateway):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_category(self):
        category_list = self.db_session.exec(select(Categories)).all()
        return category_list
    
    def get_by_id(self, id: str):
        category = self.db_session.get(Categories, id)
        return category
    
    def create_category(self, request: ICategoryCreateDTO):
        new_category = Categories(
            description=request.description
        )

        self.db_session.add(new_category)
        self.db_session.commit()
        self.db_session.refresh(new_category)
    
    def update_category(self, id: str, request: ICategoryUpdateDTO):
        category_to_update = self.get_by_id(id)
        if category_to_update is None:
            raise 
        
        data_update = request.model_dump()
        category_to_update.sqlmodel_update(data_update)

        self.db_session.add(category_to_update)
        self.db_session.commit()
        self.db_session.refresh(category_to_update)

    def delete_category(self, id: str):
        category = self.get_by_id(id)

        self.db_session.delete(category)
        self.db_session.commit()

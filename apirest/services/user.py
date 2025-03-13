from schema.users_sch import users_schema
from sqlmodel import Session, select
from models.User import User

def get_all_users(database: Session):
    sql_read = select(User)
    users = database.exec(sql_read).all()
    return users_schema(users)
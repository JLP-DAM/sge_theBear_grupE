from schema.users_sch import users_schema
from sqlmodel import Session, select
from models.User import User

def get_all_users(database: Session):
    sql_read = select(User)
    users = database.exec(sql_read).all()
    return users_schema(users)

def create_user(name: str, email: str, database: Session):
    database_user = User(name=name, email=email)
    database.add(database_user)
    database.commit()
    database.refresh(database_user)

def update_user(id: int, name: str, email: str, database: Session):
    statement = select(User).where(User.id == id)
    results = database.exec(statement)

    found_user = results.one()

    if not found_user:
        return {"message": "No user with that Id found!"}

    found_user.name = name if name is not None else found_user.name
    found_user.email = email if email is not None else found_user.email

    database.add(found_user)
    database.commit()

    return {"message": "Updated user successfully"}

def delete_user(id: int, database: Session):
    statement = select(User).where(User.id == id)
    results = database.exec(statement)

    found_user = results.one()

    if not found_user:
        return {"message": "No user with that Id found!"}

    database.delete(found_user)
    database.commit()

    return {"message": "Deleted user successfully"}
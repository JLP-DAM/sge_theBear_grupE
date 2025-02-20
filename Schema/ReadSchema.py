def Schema(User) -> dict:
    UserSent = {
        "Id": User["Id"],
        "Name": User["Name"],
        "Surname": User["Surname"],
        "Age": User["Age"],
    }

    return UserSent

def Schemas(Users) -> list[dict]:
    return [Schema(User) for _, User in Users.items()]
from Schema import ReadSchema

def Register():
    Users = {
        "User1": {
            "Id": 1,
            "Name": "Roger",
            "Surname": "Sobrino",
            "Age": 49
        },

        "User2": {
            "Id": 2,
            "Name": "Josep Oriol",
            "Surname": "Roca",
            "Age": 23
        },

        "User3": {
            "Id": 3,
            "Name": "Juan Manuel",
            "Surname": "Sanchez",
            "Age": 40
        },
    }

    return ReadSchema.Schemas(Users)
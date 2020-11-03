class Config:
    #FORMAT: "postgres://username:password@server_address:server_port/database"
    SQLALCHEMY_DATABASE_URI = "postgres://postgres:postgres@localhost:5432/users"
    # It has to be called SQLALCHEMY_DATABASE_URI
    SECRET_KEY = "chocolate"

class Config_users:
    #FORMAT: "postgres://username:password@server_address:server_port/database"
    SQLALCHEMY_DATABASE_URI = "postgres://postgres:postgres@localhost:5432/album"
    # It has to be called SQLALCHEMY_DATABASE_URI
    SECRET_KEY = "chocolate"


class Config_album:
    #FORMAT: "postgres://username:password@server_address:server_port/database"
    SQLALCHEMY_DATABASE_URI = "postgres://postgres:postgres@localhost:5432/album"
    # It has to be called SQLALCHEMY_DATABASE_URI
    SECRET_KEY = "chocolate"

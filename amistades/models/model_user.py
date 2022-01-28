
from amistades.config.mysqlconnection import connectToMySQL

class Usuario:
    name_db = "esquema_amistades"

    def __init__(self,id,first_name,last_name,created_at):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = created_at
        self.amistades = []

    @classmethod
    def addUsuario(cls,data):
        query = "INSERT INTO usuarios(first_name,last_name,created_at) VALUES(%(first_name)s,%(last_name)s,now());"
        resultado = connectToMySQL(cls.name_db).query_db(query,data)
        return resultado

    @classmethod
    def getUsuarios(cls):
        query = "SELECT  * FROM usuarios;"
        resultado = connectToMySQL(cls.name_db).query_db(query)
        return resultado
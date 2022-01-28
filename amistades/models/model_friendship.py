from amistades.config.mysqlconnection import connectToMySQL

class Amistad:
    nombre_db = "esquema_amistades"

    def __init__(self,id_usuario,nombre_usuario,id_amistad,nombre_amistad,created_at):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.id_amistad = id_amistad
        self.nombre_amistad= nombre_amistad
        self.created_at = created_at

    @classmethod
    def listFriendships(cls):
        query = '''
                SELECT CONCAT(u.first_name,' ',u.last_name) AS usuario, CONCAT(u2.first_name,' ',u2.last_name) AS amigo, u.id AS id_usuario, u2.id AS id_amistad, a.created_at
                FROM amistades a
                INNER JOIN usuarios u ON a.usuario_id = u.id
                INNER JOIN usuarios u2 ON a.amigo_id = u2.id
                ORDER BY u.first_name,u.last_name
                '''
        resultado = connectToMySQL(cls.nombre_db).query_db(query)
        amistades = []
        for amistad in resultado:
            amistades.append(Amistad(amistad["id_usuario"],amistad["usuario"],amistad["id_amistad"],amistad["amigo"],amistad["created_at"]))

        return amistades

    @classmethod
    def addFriendships(cls,data):
        query = "INSERT INTO amistades (usuario_id,amigo_id,created_at) VALUES (%(usuario_id)s,%(amigo_id)s,now());"
        resultado = connectToMySQL(cls.nombre_db).query_db(query,data)
        return resultado

    @classmethod
    def validateFriendships(cls,data):
        query = "SELECT * FROM amistades WHERE usuario_id = %(usuario_id)s AND amigo_id = %(amigo_id)s;"
        resultado = connectToMySQL(cls.nombre_db).query_db(query,data)
        return resultado
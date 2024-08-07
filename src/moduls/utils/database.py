from pymongo import MongoClient
from urllib.parse import quote_plus
import uuid

class UserOperations:
    class types:
        user = {
            'id': str,
            'username': str,
            'tokens_user': int
        }

    def __init__(self):
        # Configurar la conexión a MongoDB
        password = "M0n0p3ru@@"
        database_name = "PRL412"
        encoded_password = quote_plus(password)
        uri = f"mongodb+srv://gjimenezdeza:{encoded_password}@prl412.s0r1rvk.mongodb.net/?retryWrites=true&w=majority&appName=PRL412"

        client = MongoClient(uri)
        self.db = client[database_name]
        self.collection = self.db['users']  # Nombre de la colección

    def create_user(self, id_user, username, tokens_user):
        """Crea un nuevo usuario en MongoDB"""
        new_user = {
            "id": str(id_user),  # Convertir a string si no lo es
            "username": username,
            "tokens_user": tokens_user
        }
        result = self.collection.insert_one(new_user)
        return result.inserted_id

    def is_registered(self, id_user):
        """Verifica si un usuario está registrado en MongoDB"""
        user = self.collection.find_one({"id": str(id_user)})
        return True if user else False
    
    def get_user_data(self, id_user):
        """Obtiene los datos de un usuario desde MongoDB"""
        user = self.collection.find_one({"id": str(id_user)})
        return user if user else None


class MethodOperations:
    def __init__(self):
        # Configurar la conexión a MongoDB
        password = "M0n0p3ru@@"
        database_name = "PRL412"
        encoded_password = quote_plus(password)
        uri = f"mongodb+srv://gjimenezdeza:{encoded_password}@prl412.s0r1rvk.mongodb.net/?retryWrites=true&w=majority&appName=PRL412"

        client = MongoClient(uri)
        self.db = client[database_name]
        self.collection = self.db['metodos']  # Nombre de la colección
    
    def obtener_metodos(self, start=0, end=5) -> list:
        """Carga un rango de métodos desde MongoDB"""
        # Obtener los documentos, saltando `start` y limitando a `end - start`
        documentos = self.collection.find().skip(start).limit(end - start)
        metodos = []
        for doc in documentos:
            metodo = {
                "id": doc.get("id"),
                "titulo": doc.get("titulo"),
                "descripcion": doc.get("descripcion"),
                "costo": doc.get("costo"),
                "contenido": doc.get("contenido"),
                "urlIMG": doc.get("urlIMG"),
                "users": doc.get("users"),
                "publicado": doc.get("publicado")
            }
            metodos.append(metodo)
        return metodos
    
    def get_metodo(self, id_metodo) -> dict:
        """Obtiene un método específico por su ID desde MongoDB"""
        document = self.collection.find_one({"id": id_metodo})
        return document if document else None

    def savemethod(self, titulo, descripcion, costo, imagen, contenido):
        """Guarda un nuevo método en MongoDB"""
        new_method = {
            "id": str(uuid.uuid4()),  # Generar un ID único
            "titulo": titulo,
            "descripcion": descripcion,
            "costo": costo,
            "urlIMG": imagen,
            "contenido": contenido,
            "users": 0,  # Valor por defecto
            "publicado": True  # Valor por defecto
        }
        result = self.collection.insert_one(new_method)
        return new_method["id"]

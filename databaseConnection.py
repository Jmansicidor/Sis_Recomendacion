import firebase_admin
from firebase_admin import credentials, firestore, storage
import uuid
import mimetypes

def init_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate("prueba-1879b-firebase-adminsdk-xalgp-e0a3a361dd.json")
        firebase_admin.initialize_app(cred, {
            'storageBucket': 'prueba-1879b.appspot.com'
        })

    db = firestore.client()    
    bucket = storage.bucket()
    return db, bucket


# Función para guardar los datos del formulario
def save_form_data(firstname, lastname, address, mail, cv):
    db, bucket = init_firebase()

    file_extension = mimetypes.guess_extension(cv.type)
    if file_extension is None: file_extension = ".unknown"
    

      # Crear un nombre único para el archivo PDF en Storage
    file_id = str(uuid.uuid4()) + file_extension
    blob = bucket.blob(f'cvs/{file_id}')

    # Subir el archivo PDF al bucket de Firebase Storage
    blob.upload_from_file(cv)

    # Hacer que el archivo sea accesible públicamente (opcional)
    blob.make_public()

    # Estructurar los datos a guardar
    data = {     
        'firstname': firstname,
        'lastname': lastname,
        'address': address,
        'mail': mail,
        'cv_filename': blob.public_url  # Guardamos solo el nombre del archivo
    }

    # Guardar los datos en la colección "cvs"
    doc_ref = db.collection('cvs').add(data)
    return doc_ref[1].id, blob.public_url


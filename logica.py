import firebase_admin
from firebase_admin import credentials, firestore, storage
import io
from PIL import Image
import pytesseract
import fitz
from torchvision import transforms
import matplotlib.pyplot as plt
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



def get_data_and_analyze():
    db, bucket = init_firebase()

    # Obtener todos los documentos de la colección 'cvs'
    docs = db.collection('cvs').stream()
    for doc in docs:
        data = doc.to_dict()
        print(data)

        # Descargar el archivo desde Firebase Storage
        blob_name = data['cv_filename'].split('/')[-1]
        blob = bucket.blob(f'cvs/{blob_name}')
        image_data = blob.download_as_bytes()        

      # Abrir la imagen en memoria usando PIL
        image = Image.open(io.BytesIO(image_data))

      # Usar Tesseract para extraer el texto de la imagen
        text = pytesseract.image_to_string(image, lang='spa')

        # Mostrar el texto extraído
        print(text)





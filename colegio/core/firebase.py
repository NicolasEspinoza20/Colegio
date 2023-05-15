
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("core/monitoreo-escolar-386701-4e76ee29c18c.json")
firebase_admin.initialize_app(cred)

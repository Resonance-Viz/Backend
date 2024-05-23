import firebase_admin
from firebase_admin import credentials, firestore
from firebasecred import credential

cred = credentials.Certificate(credential)
firebase_admin.initialize_app(cred)

db = firestore.client()

docs = db.collection("users").stream()

for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")
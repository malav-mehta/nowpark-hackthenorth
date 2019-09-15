#This file sets up the firebase. 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
import props

cred = credentials.Certificate("ServiceAccountKey.json")
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

def syncToDatabase(): 
    parkingSpaces = [props.parkingSpace1_Data, props.parkingSpace2_Data]
    for i in parkingSpaces:
        db_ref = db.collection(props.parkingLot_Data).document(i["id"])

        db_ref.set({
            u'last-update': time.time(),
            u'location': i["location"],
            u'occupied': i["occupied"],
            u'start-time': i["start-time"],
            u'user-parked-for': i["user-parked-for"]
        })
        
syncToDatabase()

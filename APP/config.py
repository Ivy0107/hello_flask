from flask import Flask
import requests


app = Flask(__name__)

FHIR_URL = "http://hapi.fhir.org/baseR4" # https://hapi.fhir.tw/fhir  http://hapi.fhir.org/baseR4  http://152.38.3.196:10021/fhir

headers = {
    "Content-Type": "application/fhir+json",
    "Accept": "application/json"
    #"Authorization":"Bearer "
  }

# token(這裡只能手動取，如果要自動取就改程式碼)

#url = "http://152.38.3.103:8081/realms/medical-server/protocol/openid-connect/token"
#data = {
#    'grant_type': 'client_credentials',  
#    'client_id': 'fhir',       
#    'client_secret': 'F1lJHPZASnXn0eg7ePJy1vSC4kaKiXkM' }
#response = requests.post(url, data=data)
#token = response.json()
#print(token)

# post
def create_fhir_resource(resource_type, data):
   response=requests.post(FHIR_URL + f"/{resource_type}", headers=headers, json=data)
   return response

# put
def update_fhir_resource(resource_type, resource_id, data):
    response = requests.put(FHIR_URL + f"/{resource_type}/{resource_id}", headers=headers, json=data)
    return response

# observation search
def search_fhir_data2(resource_type, search_param1,search_param2,search_param3,search_param4, search_text1,search_text2,search_text3,search_text4):
    response = requests.get(f"{FHIR_URL}/{resource_type}?{search_param1}={search_text1}&{search_param2}={search_text2}&{search_param3}={search_text3}&{search_param4}={search_text4}&_id=1b55df5e-a824-42e4-a59a-908d493c1778", headers=headers)
    return response








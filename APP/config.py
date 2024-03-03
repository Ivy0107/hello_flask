from flask import Flask
import requests


app = Flask(__name__)

FHIR_URL = "https://hapi.fhir.tw/fhir" # https://hapi.fhir.tw/fhir  http://hapi.fhir.org/baseR4  http://152.38.3.196:10021/fhir

headers = {
    "Content-Type": "application/fhir+json",
    "Accept": "application/json"
    #"Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJBbVUwNEtnWHNTTllKYU1oUjNkYUxXSTYwLUhvRW5vUG5oeWxzdEpWRm1ZIn0.eyJleHAiOjE2OTY1ODAyMTAsImlhdCI6MTY5NjU3NjYxMCwianRpIjoiYjcxOWE1ODAtYTFhNS00NDZkLTk0NjYtZDMwYWNkYjQyNzJhIiwiaXNzIjoiaHR0cDovLzE1Mi4zOC4zLjEwMzo4MDgxL3JlYWxtcy9tZWRpY2FsLXNlcnZlciIsImF1ZCI6WyJmaGlyIiwiYWNjb3VudCJdLCJzdWIiOiI1ODQ3M2FhMC00ZDg4LTRlM2EtYTc5Mi05Y2QyZjQwMzNkN2IiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJmaGlyIiwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyIqIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsImRlZmF1bHQtcm9sZXMtbWVkaWNhbC1zZXJ2ZXIiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImZoaXIiOnsicm9sZXMiOlsidW1hX3Byb3RlY3Rpb24iXX0sImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoiZW1haWwgcHJvZmlsZSIsImNsaWVudEhvc3QiOiIxNTIuMzguMC4xMyIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwicHJlZmVycmVkX3VzZXJuYW1lIjoic2VydmljZS1hY2NvdW50LWZoaXIiLCJjbGllbnRBZGRyZXNzIjoiMTUyLjM4LjAuMTMiLCJjbGllbnRfaWQiOiJmaGlyIn0.GiBLWdedW0SA0oCLEVFQ87fkFo2YPyD6eQu0CiQrJ3IdyiBa-SHRxqH3lvks7gl9GxiHDcDvJUcV2YDv27JyJ8GDWSj2vdv0jacJqcVOntXj1OH4NqlYUrpdRBzDUib_wjkDKF-aq4SFlARzgjKdk3yYJZSSYOlldD0ClJ9AWesE0pFLNhxozlKqBLhxb_x8UW3AWa1PQdt62XYa9vJN9dlYhvtHmjXA8v0iIGP1Q8-fZaLQCErjksdoNAkkmGgagvcqn35OVlJlxN0b0uiHzKG-2IELUgZqzimHcxk_LsToJFevclB2KNRwL3GLOW_iDJwjBjmX3LHxjhVFQzZxeQ"
  }



#create
def create_fhir_resource(resource_type, data):
   response=requests.post(FHIR_URL + f"/{resource_type}", headers=headers, json=data)
   return response

def create_fhir_resource2(resource_type,generated_id ,data):
   response=requests.put(FHIR_URL + f"/{resource_type}/{generated_id}", headers=headers, json=data)
   return response

#search2
def search_fhir_resource2():
   response=requests.get(FHIR_URL + f"/Patient/22", headers=headers)
   return response


#search
def search_fhir_data(resource_type, search_param, search_text):
    response = requests.get(f"{FHIR_URL}/{resource_type}/1d2ddfea-a1b1-4a83-b6c1-7266ef7e87bd/_history", headers=headers)
    return response


#observation search
def search_fhir_data2(resource_type, search_param1,search_param2,search_param3,search_param4, search_text1,search_text2,search_text3,search_text4):
    response = requests.get(f"{FHIR_URL}/{resource_type}?{search_param1}={search_text1}&{search_param2}={search_text2}&{search_param3}={search_text3}&{search_param4}={search_text4}&_id=1b55df5e-a824-42e4-a59a-908d493c1778", headers=headers)
    return response



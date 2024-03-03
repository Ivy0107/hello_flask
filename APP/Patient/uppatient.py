from flask import Flask, request, render_template, Blueprint
from APP.config import create_fhir_resource
import requests

app = Flask(__name__)

bp = Blueprint('pat_sc1', __name__)

@bp.route('/patient', methods=['GET', 'POST'])
def patient_page():
    return render_template('Patient/patient.html')

@bp.route('/sequel', methods=['POST'])
def sequel_page():
    try:
        identifier2 = request.form.get('identifier2')
        identifier =  request.form.get('identifier')
        contact=  request.form.get('contact')
        postalCode=  request.form.get('postalCode')
        country=  request.form.get('country')
        city=  request.form.get('city')
        District=  request.form.get('District')
        line=  request.form.get('line')
        contactname=  request.form.get('contactname')
        contacttelecom=  request.form.get('contacttelecom')
        gender = request.form.get('gender')
        name = request.form.get('name')
        birthdate = request.form.get('birthdate')
        managingOrganization = request.form.get('managingOrganization')


        # 上傳 FHIR 伺服器
        data = {
            "resourceType": "Patient",
            "identifier": [
                {
                    "use": "official",
                    "type": {
                        "coding": [
                            {
                                "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                "code": "MR"
                            }
                        ]
                    },
                    "system": "http://www.tph.mohw.gov.tw/",
                    "value": identifier2
                },
                {
                    "system": "http://www.tph.mohw.gov.tw/",
                    "value": identifier
                }
            ],
            "name": [
                {
                    "use": "official",
                    "text": name
                }
            ],
            "gender": gender,
            "birthDate": birthdate,
            "telecom": [
                {
                    "system": "phone",
                    "value": contact
                }
            ],
            "address": [
                {
                    "city": city,
                    "district": District,
                    "line": [line],
                    "postalCode": postalCode,
                    "country": country
                }
            ],
            "contact": [
                {
                    "name": {
                        "text": contactname,
                        "use": "official"
                    }
                },
                {
                    "telecom": [
                        {
                            "system": "phone",
                            "value": contacttelecom
                        }
                    ]
                }
            ]
        }

        response = create_fhir_resource("Patient", data)
        server_response_text = response.text

        return render_template('Results/sequel.html',  server_response_text=server_response_text)

    except Exception as e:
     return {"error": str(e)}    

if __name__ == '__main__':
    app.run(debug=True, threaded=True)


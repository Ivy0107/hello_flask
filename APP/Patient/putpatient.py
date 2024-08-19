from flask import Flask, request, Blueprint
from APP.config import update_fhir_resource


app = Flask(__name__)

# 定義Blueprint
bp = Blueprint('pat_put', __name__)

# 定義route
@bp.route('/putsequel', methods=['PUT'])
def sequelput_page():
    try:
        #抓表單輸入的資料
        resource_id = request.form.get('resource_id')
        name = request.form.get('name')
        gender = request.form.get('gender')
        identifier2 = request.form.get('identifier2')
        birthDate = request.form.get('birthDate')
        telecom = request.form.get('telecom')
        postalCode = request.form.get('postalCode')
        country = request.form.get('country')
        city = request.form.get('city')
        district = request.form.get('district')
        line = request.form.get('line')
        
        # 轉換格式
        data = {
            "resourceType": "Patient",
            "id": resource_id,
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
                }
            ],
            "name": [
                {
                    "use": "official",
                    "text": name
                }
            ],
            "gender": gender,
            "birthDate": birthDate,
            "telecom": [
                {
                    "system": "phone",
                    "value": telecom
                }
            ],
            "address": [
                {
                    "city": city,
                    "district": district,
                    "line": [line],
                    "postalCode": postalCode,
                    "country": country
                }
            ],
        }
        
        
        # 發送請求到 FHIR server
        response = update_fhir_resource("Patient", data)
        server_response_text = response.text
        print(server_response_text)

        
    except Exception as e:
     return {"error": str(e)}    

if __name__ == '__main__':
    app.run(debug=True, threaded=True)


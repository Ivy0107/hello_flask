from flask import Flask, request,Blueprint,jsonify
import json
import requests
 

app = Flask(__name__)

fhir_server = "http://hapi.fhir.org/BaseR4/Patient/"

bp = Blueprint('pat_put', __name__)

@bp.route('/putsequel', methods=['PUT'])
def sequelput_page():
    try:
       
        resource_id = request.form.get('resource_id')
        name = request.form.get('name')
        gender = request.form.get('gender')
        identifier2 =  request.form.get('identifier2')
        birthDate = request.form.get('birthDate')
        telecom=  request.form.get('telecom')
        postalCode=  request.form.get('postalCode')
        country=  request.form.get('country')
        city=  request.form.get('city')
        district= request.form.get('district')
        line=  request.form.get('line')  
        
        data = {
            "resourceType": "Patient",
            "id": resource_id,
            "identifier": [
                {
                        "use" : "official", 
                         "type" : { "coding" :
                                    [ 
                                        { 
                             "system" : "http://terminology.hl7.org/CodeSystem/v2-0203", 
                             "code" : "MR" 
                             } 
                        ] 
                    }, 
                        "system" : "http://www.tph.mohw.gov.tw/", 
                        "value" :identifier2 }] ,
            
            "name":[
                {
                        "use":"official",
                        "text":name
                }
                    ],
            "gender":gender,
            "birthDate":birthDate,
            "telecom":[
                {
                    "system":"phone",
                    "value":telecom
                }
            ],
            "address":[
                {
                    "city":city,
                    "district":district,
                    "line":[line],
                    "postalCode":postalCode,
                    "country":country
                }
            ],
           
        }
        print(data)

        headers = {'Content-Type': 'application/fhir+json',
                   "Accept": "application/json"}
        response = requests.put(fhir_server+resource_id , headers=headers, data=json.dumps(data))
        print(fhir_server+resource_id)

        if response.status_code == 200:
            return jsonify({"success": True, "message": "更新成功", "data": response.json()})
        elif response.status_code == 404:
            return jsonify({"success": False, "message": "資源未找到"})
        else:
            return jsonify({"success": False, "message": f"請求失敗，狀態碼: {response.status_code}"})
    except requests.exceptions.RequestException as fhir_error:
        # 返回錯誤訊息
        return jsonify({"success": False, "message": str(fhir_error)})


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
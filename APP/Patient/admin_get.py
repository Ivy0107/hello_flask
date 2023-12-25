from flask import Flask, render_template, request, Blueprint,jsonify
import requests

app = Flask(__name__)
bp = Blueprint('admin_get', __name__)

# 修改 fhir_server_api，使其包含 "/Patient/{id}"
fhir_server_api = "http://hapi.fhir.tw/fhir/Patient/{}"

@bp.route('/patients', methods=['GET'])
def patient_list():
    try:
        search_id = request.args.get('search_id', '')
        if search_id:
            # 向 HAPI FHIR 伺服器發送 GET 請求，獲取指定病患資料
            response = requests.get(fhir_server_api.format(search_id))
            response.raise_for_status()  # 檢查是否有錯誤發生
            patient_data = response.json()

            # 提取有用的病患資訊，例如 resource_id、name 和 gender
            patients = [{
                "resource_id": patient_data.get('id', ''),
                "name": patient_data.get('name', [{}])[0].get('text', ''),
                "gender": patient_data.get('gender', '')
            }]
        else:
            # 向 HAPI FHIR 伺服器發送 GET 請求，獲取所有病患資料
            response = requests.get("http://hapi.fhir.tw/fhir/Patient")
            response.raise_for_status()  # 檢查是否有錯誤發生
            data = response.json()

            # 提取有用的病患資訊，例如 resource_id、name 和 gender
            patients = []
            for entry in data.get('entry', []):
                resource = entry.get('resource', {})
                patient_id = resource.get('id', '')
                name = resource.get('name', [{}])[0].get('text', '')
                gender = resource.get('gender', '')
                patients.append({"resource_id": patient_id, "name": name, "gender": gender})

        return render_template('Patient/admin_get.html', patients=patients, search_id=search_id)

    except requests.exceptions.RequestException as e:
        return str(e)
    
@bp.route('/patients/delete/<string:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    try:
        delete_url = fhir_server_api.format(patient_id)
        response = requests.delete(delete_url)
        response.raise_for_status()

        return jsonify({"success": True, "message": f"Patient {patient_id} deleted successfully."})

    except requests.exceptions.RequestException as e:
        return jsonify({"success": False, "message": str(e)})    
    
@bp.route('/patients/view/<string:resource_id>', methods=['GET'])
def detail2(resource_id):
    try:
        response = requests.get(fhir_server_api.format(resource_id))
        response.raise_for_status()
        patient_data = response.json()

        # 提取有用的患者資訊，例如姓名、性別等
        patient_detail = {
            "resource_id": patient_data.get('id', ''),
            "name": patient_data.get('name', [{}])[0].get('text', ''),
            "gender": patient_data.get('gender', ''),
            "birthDate": patient_data.get('birthDate', ''),
            "identifier2": patient_data.get('identifier', [{}])[0].get('value', ''),
            "address": {
                "postalCode": patient_data.get('address', [{}])[0].get('postalCode', ''),
                "country": patient_data.get('address', [{}])[0].get('country', ''),
                "city": patient_data.get('address', [{}])[0].get('city', ''),
                "district": patient_data.get('address', [{}])[0].get('district', ''),
                "line": patient_data.get('address', [{}])[0].get('line', '')
            },
            "telecom": patient_data.get('telecom', [{}])[0].get('value', '') # 這裡的索引修正為[0]
           
        }

        return render_template('Patient/detail2.html', patient_detail=patient_detail, edit_mode=False)

    except requests.exceptions.RequestException as e:
        return str(e)
    
   


if __name__ == '__main__':
    app.run(debug=True)
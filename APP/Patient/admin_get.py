from flask import Flask, render_template, request, Blueprint,jsonify
import requests

app = Flask(__name__)
bp = Blueprint('admin_get', __name__)

fhir_server_api = "http://hapi.fhir.org/baseR4/Patient/{}"

#list
@bp.route('/patients', methods=['GET'])
def patient_list():
    try:
        search_id = request.args.get('search_id', '')
        if search_id:
            # 向 HAPI FHIR 伺服器發送 GET 請求，獲取指定病患資料的歷史紀錄
            response = requests.get(fhir_server_api.format(search_id) + "/_history")
            response.raise_for_status()  # 檢查是否有錯誤發生
            history_data = response.json()
            
            # 提取歷史紀錄中的所有版本資訊
            patients = []
            for entry in history_data.get('entry', []):
                resource = entry.get('resource', {})
                patient_id = resource.get('id', '')
                version_id = entry.get('versionId', '')
                name = resource.get('name', [{}])[0].get('text', '')
                gender = resource.get('gender', '')
                patients.append({"resource_id": patient_id, "version_id": version_id, "name": name, "gender": gender})
        else:
            # 如果沒有指定搜索 ID，則返回空列表
            patients = []

        return render_template('Patient/admin_get.html', patients=patients, search_id=search_id)

    except requests.exceptions.RequestException as e:
        return str(e)
#delete    
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

        # 提取資訊
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
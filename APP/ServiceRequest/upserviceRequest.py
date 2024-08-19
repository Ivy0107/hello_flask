from flask import Flask, request, render_template, Blueprint
from .. import config

app = Flask(__name__)

# 定義Blueprint
bp = Blueprint('ser', __name__)

# 定義route
@bp.route('/service', methods=['GET', 'POST'])
def service_page():
    
    return render_template('serviceRequest/upserviceRequest.html')

# 定義route
@bp.route('/sequelser', methods=['POST'])

def sequelser_page():
    try:
        #抓表單輸入的資料
        authoredon = request.form.get('authoredon')
        patientid = request.form.get('patientid')
        requester = request.form.get('requester')
        
        # 轉換格式
        servicerequest_data = {
            "resourceType": "ServiceRequest",
            "identifier": [
            {
               "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
               "value": "1234567"
             }
            ],
             "status": "completed",
             "intent": "order",
             "code": {
                 "coding": [
                     {
                       "system": "http://snomed.info/sct",
                       
                       "display": "Monitoring of cardiac output by electrocardiogram"
                     }
                   ]
               },
	         "quantityQuantity": {
		          "value": 1
	          },
           "subject": {
                 "reference": "Patient/"+patientid
            },
            "authoredOn": authoredon,
             "requester": {
                  "reference": "Practitioner/"+requester
           }
      
}
        # 發送請求到 FHIR server
        response = config.create_fhir_resource("ServiceRequest", servicerequest_data)
        server_response_text = response.text
        return render_template('Results/sequel.html',  server_response_text=server_response_text)

    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
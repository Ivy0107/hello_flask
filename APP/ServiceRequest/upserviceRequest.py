from flask import Flask, request, render_template, Blueprint
from .. import config

app = Flask(__name__)

bp = Blueprint('ser', __name__)

@bp.route('/service', methods=['GET', 'POST'])
def service_page():
    
    return render_template('serviceRequest/upserviceRequest.html')

@bp.route('/sequelser', methods=['POST'])
def sequelser_page():
    try:
        authoredon = request.form.get('authoredon')
        patientid = request.form.get('patientid')
        requester = request.form.get('requester')

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

        response = config.create_fhir_resource("ServiceRequest", servicerequest_data)

        server_response_text = response.text

        return render_template('Results/sequel.html',  server_response_text=server_response_text)

    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
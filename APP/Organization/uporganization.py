from flask import Flask, request, render_template, Blueprint
from APP import config

app = Flask(__name__)

bp = Blueprint('org', __name__)

@bp.route('/organization', methods=['GET', 'POST'])
def organization_page():
    
    return render_template('Organization/uporganization.html')

@bp.route('/sequelorg', methods=['POST'])
def sequelorg_page():
    try:
        name = request.form.get('name')
        identifier = request.form.get('identifier')

        organization_data = {
            "resourceType": "Organization",
             # "meta":{
      #     "profile":["https://hapi.fhir.tw/fhir/StructureDefinition/Patient-MITW2022-T1SC1"
      #         ]},
      
            "identifier": [{
            "type": {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                        "code": 'PRN'
                    }
                ],
                "text":"機構代碼"
            },
            "system":"http://ns.electronichealth.net.au/id/hi/hpio/1.0",
            "value":  identifier
        }],
        "name":name 
    }

        response = config.create_fhir_resource("Organization", organization_data)

        server_response_text = response.text

        return render_template('Results/sequel.html',  server_response_text=server_response_text)

    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
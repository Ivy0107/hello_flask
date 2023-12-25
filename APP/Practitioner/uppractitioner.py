from flask import Flask, request, render_template, Blueprint
from .. import config

app = Flask(__name__)

bp = Blueprint('pra', __name__)

@bp.route('/practitioner', methods=['GET', 'POST'])
def practitioner_page():
    
    return render_template('Practitioner/uppractitioner.html')

@bp.route('/sequelpra', methods=['POST'])
def sequelpra_page():
    try:
        name1 = request.form.get('name1')
        identifier3 = request.form.get('identifier3')

        practitioner_data = {
           "resourceType": "Practitioner",
            "identifier" : [
                   {
                   "use" : "official",
                   "type" : {
                    "coding" : [
                        {
                        "system" : "http://terminology.hl7.org/CodeSystem/v2-0203",
                          "code" : "MD"
                         }
                         ]
                         },
                      "system" : "https://www.tph.mohw.gov.tw",
                         "value" : identifier3
                      }
                     ],
                       "name" : [
                           {
                         "use" : "official",
                         "text" : name1
                        
                         }]
   
                             }

        response = config.create_fhir_resource("Practitioner", practitioner_data)

        server_response_text = response.text

        return render_template('Results/sequel.html',  server_response_text=server_response_text)

    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
from flask import Flask, request, render_template, Blueprint
from APP import config

app = Flask(__name__)

# 定義Blueprint
bp = Blueprint('org', __name__)

# 定義route
@bp.route('/organization', methods=['GET', 'POST'])
def organization_page():
    
    return render_template('Organization/uporganization.html')


# 定義route
@bp.route('/sequelorg', methods=['POST'])
def sequelorg_page():
    try:
        #抓表單輸入的資料
        name = request.form.get('name')
        identifier = request.form.get('identifier')
        
        # 轉換格式
        organization_data = {
            "resourceType": "Organization",
                  # "meta":{
              #  "profile":["https://hapi.fhir.tw/fhir/StructureDefinition/Patient-MITW2022-T1SC1"
              #   ]},
      
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


        # 發送請求到 FHIR server
        response = config.create_fhir_resource("Organization", organization_data)
        server_response_text = response.text
        return render_template('Results/sequel.html',  server_response_text=server_response_text)

    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
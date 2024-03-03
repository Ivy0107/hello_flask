from flask import Flask, request, render_template, Blueprint
from APP import config


app = Flask(__name__)

bp = Blueprint('obs', __name__)

@bp.route('/observation', methods=['GET', 'POST'])
def obs_page():
    
    return render_template('Observation/Observation.html')

@bp.route('/sequelobs', methods=['POST'])
def sequelobs_page():
    try:
        id1 = request.form.get('id1')
        id2 = request.form.get('id2')
        time = request.form.get('time')
        data1 = request.form.get('data1')
        data2 = request.form.get('data2')
        data3 = request.form.get('data3')
        data4 = request.form.get('data4')
        data5 = request.form.get('data5')
        data6 = request.form.get('data6')
        data7 = request.form.get('data7')
        data8 = request.form.get('data8')
        data9 = request.form.get('data9')
        data10 = request.form.get('data10')
        data11 = request.form.get('data11')
        data12 = request.form.get('data12')

        observation_data ={
            
    "resourceType": "Observation",
    
#    "meta": {

#       "profile": [
#            "https://hapi.fhir.tw/fhir/StructureDefinition/Observation.SC4.12LeadsECG"
#        ]
#    },
    "basedOn": [
        {
            "reference": "ServiceRequest/"+id2
        }
    ],
    "status": "final",
    "category": [
        {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                    "code": "procedure",
                    "display": "Procedure"
                }
            ]
        }
    ],
    "code": {
        "coding": [
            {
                "system": "urn:oid:2.16.840.1.113883.6.24",
                "code": "131329",
                "display": "MDC_ECG_ELEC_POTL"
            },
        
          
            {
                "system": "http://unitsofmeasure.org",
                "display": "mV"
            }
        ]
                
    },
    "subject": {
        "reference": "Patient/"+id1
    },
    "effectiveDateTime": time,
    "performer": [
        {
            "reference": "Practitioner/187",
            
        }
    ],
    "component": [
        {
            "code": {
                "coding": [
                    {
                        "system": "urn:oid:2.16.840.1.113883.6.24",
                        "code": "131329",
                        "display": "MDC_ECG_ELEC_POTL_I"
                    }
                ]
            },
            "valueSampledData": {
                "origin": {
                    "value": 0
                },
                "period": 2,
                "factor": 0.001,
                "lowerLimit": -2,
                "upperLimit": 2,
                "dimensions": 1,
                "data": data1
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "urn:oid:2.16.840.1.113883.6.24",
                        "code": "131330",
                        "display": "MDC_ECG_ELEC_POTL_II"
                    }
                ]
            },
            "valueSampledData": {
                "origin": {
                    "value": 0
                },
                "period": 2,
                "factor": 0.001,
                "lowerLimit": -2,
                "upperLimit": 2,
                "dimensions": 1,
                "data": data2
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "urn:oid:2.16.840.1.113883.6.24",
                        "code": "131389",
                        "display": "MDC_ECG_ELEC_POTL_III"
                    }
                ]
            },
            "valueSampledData": {
                "origin": {
                    "value": 0
                },
                "period": 2,
                "factor": 0.001,
                "lowerLimit": -2,
                "upperLimit": 2,
                "dimensions": 1,
                "data":data3
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "urn:oid:2.16.840.1.113883.6.24",
                        "code": "131390",
                        "display": "MDC_ECG_ELEC_POTL_AVR"
                    }
                ]
            },
            "valueSampledData": {
                "origin": {
                    "value": 0
                },
                "period": 2,
                "factor": 0.001,
                "lowerLimit": -2,
                "upperLimit": 2,
                "dimensions": 1,
                "data":data4
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "urn:oid:2.16.840.1.113883.6.24",
                        "code": "131391",
                        "display": "MDC_ECG_ELEC_POTL_AVL"
                    }
                ]
            },
            "valueSampledData": {
                "origin": {
                    "value": 0
                },
                "period": 2,
                "factor": 0.001,
                "lowerLimit": -2,
                "upperLimit": 2,
                "dimensions": 1,
                "data": data5
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "urn:oid:2.16.840.1.113883.6.24",
                        "code": "131392",
                        "display": "MDC_ECG_ELEC_POTL_AVF"
                    }
                ]
            },
            "valueSampledData": {
                "origin": {
                    "value": 0
                },
                "period": 2,
                "factor": 0.001,
                "lowerLimit": -2,
                "upperLimit": 2,
                "dimensions": 1,
                "data":data6
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "urn:oid:2.16.840.1.113883.6.24",
                        "code": "131331",
                        "display": "MDC_ECG_ELEC_POTL_V1"
                    }
                ]
            },
            "valueSampledData": {
                "origin": {
                    "value": 0
                },
                "period": 2,
                "factor": 0.001,
                "lowerLimit": -2,
                "upperLimit": 2,
                "dimensions": 1,
                "data":data7
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "urn:oid:2.16.840.1.113883.6.24",
                        "code": "131332",
                        "display": "MDC_ECG_ELEC_POTL_V2"
                    }
                ]
            },
            "valueSampledData": {
                "origin": {
                    "value": 0
                },
                "period": 2,
                "factor": 0.001,
                "lowerLimit": -2,
                "upperLimit": 2,
                "dimensions": 1,
                "data":data8
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "urn:oid:2.16.840.1.113883.6.24",
                        "code": "131333",
                        "display": "MDC_ECG_ELEC_POTL_V3"
                    }
                ]
            },
            "valueSampledData": {
                "origin": {
                    "value": 0
                },
                "period": 2,
                "factor": 0.001,
                "lowerLimit": -2,
                "upperLimit": 2,
                "dimensions": 1,
                "data": data9
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "urn:oid:2.16.840.1.113883.6.24",
                        "code": "131334",
                        "display": "MDC_ECG_ELEC_POTL_V4"
                    }
                ]
            },
            "valueSampledData": {
                "origin": {
                    "value": 0
                },
                "period": 2,
                "factor": 0.001,
                "lowerLimit": -2,
                "upperLimit": 2,
                "dimensions": 1,
                "data": data10
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "urn:oid:2.16.840.1.113883.6.24",
                        "code": "131335",
                        "display": "MDC_ECG_ELEC_POTL_V5"
                    }
                ]
            },
            "valueSampledData": {
                "origin": {
                    "value": 0
                },
                "period": 2,
                "factor": 0.001,
                "lowerLimit": -2,
                "upperLimit": 2,
                "dimensions": 1,
                "data":data11
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "urn:oid:2.16.840.1.113883.6.24",
                        "code": "131336",
                        "display": "MDC_ECG_ELEC_POTL_V6"
                    }
                ]
            },
            "valueSampledData": {
                "origin": {
                    "value": 0
                },
                "period": 2,
                "factor": 0.001,
                "lowerLimit": -2,
                "upperLimit": 2,
                "dimensions": 1,
                "data":data12
            }
        }
    ]
}   

        

        response1 = config.create_fhir_resource("Observation", observation_data)

        server_response_text1 = response1.text

        return render_template('Results/sequel.html',  server_response_text=server_response_text1)

    except Exception as e:
     return {"error": str(e)}        
   


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
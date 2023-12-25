from flask import Flask, request, render_template, Blueprint
from .. import config
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__,static_url_path='/static')

bp = Blueprint('obs_get', __name__)

@bp.route('/get1', methods=['GET', 'POST'])
def search_page2():
    result = None
    lead_data = {} 
    if request.method == 'POST':

        search_param1 = 'based-on'
        search_text1 = request.form.get('search_text')
        search_param2 = 'subject'
        search_text2 = request.form.get('search_text1')
        search_param3 = 'code'
        search_text3 = request.form.get('search_text2')
        search_param4 = 'date'
        search_text4 = request.form.get('search_text3')
    
        response = config.search_fhir_data2("Observation", search_param1, search_param2, search_param3, search_param4, search_text1, search_text2, search_text3, search_text4)
    
        data = response.json()
        result=data.get('entry', [])
        
    
   
    if result:
        for entry in result:
            if 'resource' in entry:
                resource = entry['resource']
                if 'component' in resource:
                    for component in resource['component']:
                        if isinstance(component, dict): 
                            display_name = component.get('code', {}).get('coding', [{}])[0].get('display', '')
                            ecg_data_str = component.get('valueSampledData', {}).get('data', '')
                            ecg_data_values = []
                            for value_str in ecg_data_str.split():
                             if value_str == '-':
        
                              ecg_data_values.append(-2.0)
                             else:
                                   try:
                                    value = float(value_str)
                                    ecg_data_values.append(value)
                                   except ValueError:
           
                                    pass

                            scaled_ecg_data = np.array(ecg_data_values) * (3.0 / max(ecg_data_values))
                            lead_data[display_name] = scaled_ecg_data
   
    
    
    #建立圖像  
    fig = plt.figure(figsize=(12, 8))

    for i, (lead_name, ecg_data) in enumerate(lead_data.items()):
        ax = fig.add_subplot(6, 2, i + 1)  
        num_samples = len(ecg_data)
        plt.grid(True)
        time_points = np.arange(0, num_samples) * 0.002  # 取樣頻率:500 Hz，間隔0.002sec
        ax.plot(time_points, ecg_data)
 
        ax.set_title(lead_name)
        ax.set_xlim(0, 10)  

    fig.tight_layout()  
    fig.savefig('static/ecg_pot.png')
    
    return render_template('Observation/getObservation.html', image_file='ecg_pot.png')

if __name__ == '__main__':
    app.run(debug=True,threaded=True)


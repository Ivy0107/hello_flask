from flask import Flask, request, render_template, Blueprint
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__, static_url_path='/static')

bp = Blueprint('obs_get', __name__)

# 指定心電圖資料檔案路徑
ecg_data_paths = ['D:\\leadI.txt']

@bp.route('/get1', methods=['GET', 'POST'])
def search_page2():
    lead_data = {}

    # 讀取心電圖資料
    for i, ecg_data_path in enumerate(ecg_data_paths):
        with open(ecg_data_path, 'r') as file:
            ecg_data_str = file.read()
        
        ecg_data_values = [float(value_str) for value_str in ecg_data_str.split()]
        ecg_data_values_mV = np.array(ecg_data_values) / 1000
        lead_data[f'ECG'] = ecg_data_values_mV

    # 建立圖像
    fig = plt.figure(figsize=(12, 6))

    for i, (lead_name, ecg_data) in enumerate(lead_data.items()):
        ax = fig.add_subplot(3, 1, i + 1)  
        num_samples = len(ecg_data)
        plt.grid(True)
        time_points = np.arange(0, num_samples) * 0.002  # 取樣頻率:500 Hz，間隔0.002sec
        ax.plot(time_points, ecg_data)
 
        ax.set_title(lead_name)
        ax.set_xlim(0, 10)  
    
    plt.ylabel('Voltage (mV)')
    plt.xlabel('Time (sec)')
    fig.tight_layout()  
    fig.savefig('static/ecg_plots.png')
    
    return render_template('Observation/getObservation.html', image_file='ecg_pot.png')
if __name__ == '__main__':
    app.run(debug=True, threaded=True)
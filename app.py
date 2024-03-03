from flask import Flask, render_template, request
import logging
from APP.Patient import uppatient,admin_get
from APP.Observation import upObservation, getObservation
from APP.Organization import uporganization
from APP.ServiceRequest import upserviceRequest
from APP.Practitioner import uppractitioner
from APP.Patient import putpatient



app = Flask(__name__)

app.register_blueprint(uppatient.bp)
app.register_blueprint(admin_get.bp)
app.register_blueprint(upObservation.bp)
app.register_blueprint(getObservation.bp)
app.register_blueprint(uporganization.bp)
app.register_blueprint(upserviceRequest.bp)
app.register_blueprint(uppractitioner.bp)
app.register_blueprint(putpatient.bp)


@app.route("/")
def home_page():

    return render_template('index.html')

@app.route("/cover", methods=["GET", "POST"])
def cover_page():
    if request.method == "POST":
      return render_template('cover.html')
    elif request.method == "GET":
      return render_template('cover.html')


#debug    
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
app.logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000, threaded=True)


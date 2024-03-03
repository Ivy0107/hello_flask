from flask import Flask, render_template, request, jsonify
import logging, pymysql
from APP.Patient import uppatient,admin_get
from APP.Observation import upObservation, getObservation
from APP.Organization import uporganization
from APP.ServiceRequest import upserviceRequest
from APP.Practitioner import uppractitioner
from APP.Patient import putpatient
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_mysqldb import MySQL



app = Flask(__name__)





#login


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

# 配置 Flask App、JWT 和 MySQL
app.config['JWT_SECRET_KEY'] = 'super-secret'
db_settings = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'test',
    'cursorclass': pymysql.cursors.DictCursor
} # 返回字典格式的結果
jwt = JWTManager(app)
mysql = MySQL(app)

# 註冊 API
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
            confirm_password = data.get('confirm_password')
            role = data.get('role')

            # 簡單的驗證，你可能需要更複雜的驗證機制
            if not username or not password or not confirm_password or not role:
                return jsonify({'message': 'Missing required fields'}), 400

            if password != confirm_password:
                return jsonify({'message': 'Passwords do not match'}), 400

            # 在資料庫中新增使用者
            conn = pymysql.connect(**db_settings)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", (username, password, role))
            conn.commit()
            cursor.close()
            return render_template('Login/register.html')
        
        elif request.form:
            # 如果不是 JSON，處理表單數據
            username = request.form.get('username')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm_password')
            role = request.form.get('role')
            
            conn = pymysql.connect(**db_settings)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", (username, password, role))
            conn.commit()
            cursor.close()
            return render_template('Login/register.html')
        else:
            return jsonify({'message': 'Unsupported Media Type'}), 415

    return render_template('Login/register.html')

# 登入 API
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')

            conn = pymysql.connect(**db_settings)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()
            cursor.close()

            if not user:
                return jsonify({'message': 'Invalid credentials'}), 401

            # 產生 JWT Token
            access_token = create_access_token(identity={'username': username, 'role': user['role']})
            print(access_token)
            return render_template('Login/login.html')
        
        elif request.form:
            # 處理表單數據
            username = request.form.get('username')
            password = request.form.get('password')

            conn = pymysql.connect(**db_settings)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()
            cursor.close()
            
            if not user:
                return jsonify({'message': 'Invalid credentials'}), 401

            # 產生 JWT Token
            access_token = create_access_token(identity={'username': username, 'role': user['role']})
            print(access_token)
            return render_template('Login/login.html')

        else:
            return jsonify({'message': 'Unsupported Media Type'}), 415

    return render_template('Login/login.html')


# 保護的資源，需要驗證身份
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200





#debug    
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
app.logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000, threaded=True)


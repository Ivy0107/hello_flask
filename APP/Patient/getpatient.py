from flask import Flask, request, render_template, Blueprint, jsonify, send_file, redirect, url_for
from .. import config
import json, requests
import pymysql

app = Flask(__name__)

bp = Blueprint('pat_get', __name__)

# search
@bp.route('/get', methods=['GET', 'POST'])
def search_page():
    search_text = request.form.get('search_text')

    # 資料庫參數設定
    db_settings = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "123456",
        "db": "test",
        "charset": "utf8"
    }

    # 連接到資料庫
    conn = pymysql.connect(**db_settings)
    cursor = conn.cursor()

    # 選擇所有資料
    command = "SELECT 姓名, 性別, 身分證字號 FROM patient"

    if search_text:
        # 有輸入搜尋條件，執行查詢
        command += " WHERE 身分證字號 = %s"
        cursor.execute(command, (search_text,))
    else:
        # 沒有搜尋條件，顯示所有資料
        cursor.execute(command)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('Patient/getpatient.html', data=data)


@bp.route('/detail/<patient_id>', methods=['GET'])
def detail(patient_id):
    # 資料庫參數設定
    db_settings = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "123456",
        "db": "test",
        "charset": "utf8"
    }

    # 連接到資料庫
    conn = pymysql.connect(**db_settings)
    cursor = conn.cursor()

    # 根據患者 ID 查詢詳細資訊
    command = "SELECT * FROM patient WHERE 身分證字號 = %s"
    cursor.execute(command, (patient_id,))
    patient_detail = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template('Patient/detail.html', patient_detail=patient_detail)

    
if __name__ == '__main__':
    app.run(debug=True)


 
    













from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os

app = Flask('testapp', template_folder='./src/templates', static_folder='C:/Users/suman/OneDrive/Documents/collegeProject/EventManagement/EventManagement/src/static')

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'event',
}

db_conn = mysql.connector.connect(**db_config)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    gender = request.form['gender']
    field = request.form['perform']
    comments = request.form['comments']

    cursor = db_conn.cursor()
    insert_query = "INSERT INTO eventdata (name, email, phone, gender, field, comments) VALUES (%s, %s, %s, %s, %s, %s)"
    data = (name, email, phone, gender, field, comments)
    cursor.execute(insert_query, data)
    db_conn.commit()
    cursor.close()

    return redirect(url_for('interstitial'))

@app.route('/interstitial')
def interstitial():
    return render_template('interstitial.html')

@app.route('/details')
def details():
    cursor = db_conn.cursor()
    select_query = "SELECT name, email, field, comments FROM eventdata"
    cursor.execute(select_query)
    data = cursor.fetchall()
    cursor.close()
    return render_template('details.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)


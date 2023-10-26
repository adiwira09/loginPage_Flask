from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'secret_key' # Ganti dengan kunci rahasia yang lebih kuat

# Konfigurasi database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'login'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/proses_login', methods=['POST'])
def proses_login():
    username = request.form['username']
    password = request.form['password']

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user WHERE username=%s AND password=%s", (username, password))
    user = cur.fetchone()
    cur.close()

    if user:
        session['username'] = username
        return redirect(url_for('welcome'))
    else:
        session['login_fail'] = True
        return redirect(url_for('index', error=1))

@app.route('/welcome')
def welcome():
    if 'username' in session:
        return render_template('/website/index.html')  # Mengarahkan ke halaman lokal
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

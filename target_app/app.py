from flask import Flask, request, render_template, g
import sqlite3, os

app = Flask(__name__)
DB = os.path.join(os.path.dirname(__file__), 'data.db')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return render_template('index.html')

# Simple XSS demo: reflects 'name' param
@app.route('/greet')
def greet():
    name = request.args.get('name','Guest')
    # intentionally not escaping to demo XSS
    return f"<h3>Hello {name}</h3>"

# Simple SQLi demo: vulnerable query
@app.route('/search', methods=['GET','POST'])
def search():
    q = request.values.get('q','')
    cur = get_db().cursor()
    # intentionally vulnerable string interpolation
    sql = "SELECT id, username FROM users WHERE username LIKE '%{}%'".format(q)
    cur.execute(sql)
    rows = cur.fetchall()
    result = "<br>".join([f"{r[0]} - {r[1]}" for r in rows]) or "No results"
    return f"<h3>Query: {sql}</h3><div>{result}</div>"

# Command injection demo (for controlled lab demos only)
@app.route('/ping', methods=['GET','POST'])
def ping():
    host = request.values.get('host','127.0.0.1')
    # intentionally naive use of shell - DO NOT use in production
    import subprocess, shlex
    cmd = f"ping -c 1 {host}"
    try:
        out = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT, timeout=5)
        return f"<pre>{out.decode()}</pre>"
    except Exception as e:
        return f"<pre>Error: {e}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

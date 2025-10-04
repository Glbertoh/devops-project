from flask import Flask, request, jsonify
import psycopg2
import os
import time

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST","db")
DB_NAME = os.getenv("DB_NAME","namesdb")
DB_USER = os.getenv("DB_USER","postgres")
DB_PASS = os.getenv("DB_PASS","postgres")

def get_connection():
    retries = 10
    while retries > 0:
        try:
            return psycopg2.connect(
                   host=DB_HOST, database=DB_NAME,
                   user=DB_USER, password=DB_PASS
            )
        except psycopg2.OperationalError as e:
            print("DB not ready, retrying in 3s...")
            time.sleep(3)
            retries =- 1
    raise Exception("Connection to DB failed after 10 tries...")


@app.route("/add", methods=["POST"])
def add_name():
    data = request.json
    name = data.get("name")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO names (name) VALUES (%s)", (name,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": f"Nombre {name} guardado"})

@app.route("/list", methods=["GET"])
def list_names():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT name FROM names;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify([r[0] for r in rows])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


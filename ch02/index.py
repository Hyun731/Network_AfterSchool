from flask import Flask, render_template
import pymysql

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/save/<num>")
def save(num):
    conn = pymysql.connect(host='localhost', user='root', password='q1w2e3', charset='utf8', database="numcount")
    cursor = conn.cursor() 
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS numcount (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    num INT NOT NULL
                )
            """)
    conn.commit()

    cursor.execute("INSERT INTO numcount (num) VALUES (%s)", (num,))
    conn.commit()

    cursor.execute("SELECT * FROM numcount")
    results = cursor.fetchall()
    print("현재 numcount 테이블:")
    for row in results:
        print(row)

    return {"status": "ok", "data": results}

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

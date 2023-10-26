from flask import Flask, request, send_file

app = Flask(__name__)
port = 3000

@app.route("/")
def root():
    return send_file("public/index.html")

@app.route("/about")
def about():
    return '이것은 "About" 페이지입니다.'

@app.route("/contact")
def contact():
    return '이것은 "Contact" 페이지입니다.'

@app.route("/submit", methods=["POST"])
def submit():
    data = request.form  # request.data를 사용할 수도 있음
    print("POST 요청을 받았습니다. 데이터:", data)
    return "POST 요청을 받았습니다."

if __name__ == "__main__":
    app.run(port=port)
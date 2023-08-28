from flask import Flask

##Create a Simple Flask Application
app = Flask(__name__)
@app.route("/",methods=['GET'])
def welcom():
    return "Hello Flask"

@app.route("/index",methods=['GET'])
def index():
    return "Welcome To index page"

@app.route("/succes/<score>",methods=['GET'])
def success(score):
    return "<h1>This person passed with this score:</h1>" + score



if __name__=="__main__":
    app.run(debug=True)


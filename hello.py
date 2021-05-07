from flask import Flask, render_template
app = Flask(__name__)                         
@app.route('/')
def index():
    return render_template("index.html",col = 4, rows = 4)
@app.route("/<rows>")
def display_four(rows):
    return render_template("index.html",col = 4, rows= int(rows))
@app.route("/<rows>/<col>")
def display_xandy(rows,col):
    return render_template("index.html",col = int(col), rows = int(rows))
@app.route("/<rows>/<col>/<color1>/<color2>")
def display_color(rows,col,color1,color2):
    return render_template("index.html",col = int(col), rows = int(rows), color1 = color1,color2 = color2)


if __name__=="__main__":
    app.run(debug=True)
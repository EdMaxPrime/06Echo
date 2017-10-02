from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def root():
    return render_template("form.html")

@app.route('/welcome', methods=['GET', 'POST'])
def tracker():
    print request.method
    print request.args
    return render_template("welcome.html", name = request.args['motto'], query = request.args, method = request.method)

if __name__ == "__main__":
    app.debug = True
    app.run()

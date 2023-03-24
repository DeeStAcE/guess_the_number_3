from flask import Flask, request, render_template

app = Flask(__name__, template_folder="./templates")


@app.route("/", methods=["POST", 'GET'])
def data_submitted():
    if request.method == "POST":
        if request.form.get('too_small'):
            return render_template("guess_the_number.html")
        if request.form.get('too_big'):
            return render_template("guess_the_number.html")
        if request.form.get('you_win'):
            return render_template("guess_the_number.html")
    if request.method == "GET":
        return render_template("guess_the_number.html")


if __name__ == "__main__":
    app.run(debug=True)

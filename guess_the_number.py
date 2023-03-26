from flask import Flask, request, render_template

app = Flask(__name__, template_folder="./templates")


@app.route("/", methods=["POST", 'GET'])
def guess_the_number():
    if request.method == "POST":
        min_ = request.form.get('min')
        max_ = request.form.get('max')
        min_ = int(min_)
        max_ = int(max_)
        guess = int((max_ - min_) / 2 + min_)
        if request.form.get('too_small'):
            return render_template("html_guess.html", min_=guess, max_=max_)
        if request.form.get('too_big'):
            return render_template("html_guess.html", min_=min_, max_=guess)
        if request.form.get('you_win'):
            return 'You win!'
    if request.method == "GET":
        # min_ = 0
        # max_ = 1000
        # guess = int((max_ - min_)) / 2 + min_
        return render_template("html_guess.html", min_=0, max_=1000)


if __name__ == "__main__":
    app.run(debug=True)

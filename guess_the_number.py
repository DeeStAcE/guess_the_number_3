from flask import Flask, request, render_template

app = Flask(__name__, template_folder="./templates")


@app.route("/", methods=["POST", 'GET'])
def guess():
    if request.method == "GET":
        return render_template("html_start.html", min_=0, max_=1000)


@app.route("/guess", methods=["POST", 'GET'])
def guess_the_number():
    if request.method == "POST":
        min_ = request.form.get('min')
        max_ = request.form.get('max')
        min_ = int(min_)
        max_ = int(max_)
        guess = int((max_ - min_) / 2 + min_)
        if request.form.get('too_small'):
            return render_template("html_guess.html", min_=guess, max_=max_, guess_=int((max_ - guess) / 2 + guess))
        if request.form.get('too_big'):
            return render_template("html_guess.html", min_=min_, max_=guess, guess_=int((guess - min_) / 2 + min_))
        if request.form.get('you_win'):
            return 'You win!'
        else:
            return render_template("html_guess.html", min_=min_, max_=max_, guess_=guess)


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, render_template

app = Flask(__name__, template_folder="./templates")


@app.route("/", methods=["POST", 'GET'])
def guess_the_number():

    # print(guess)
    if request.method == "POST":
        min_ = request.form.get('min')
        max_ = request.form.get('max')
        print(min_, max_)
        min_ = float(min_)
        max_ = float(max_)
        print(min_, max_)
        guess = int((max_ - min_)) / 2 + min_
        if request.form.get('too_small'):
            return render_template("html_guess.html", min_=guess, max_=max_)
        if request.form.get('too_big'):
            return render_template("html_guess.html", min_=min_, max_=guess)
        if request.form.get('you_win'):
            return 'You win!'
    if request.method == "GET":
        return render_template("html_guess.html", min_=0, max_=1000)


if __name__ == "__main__":
    app.run(debug=True)

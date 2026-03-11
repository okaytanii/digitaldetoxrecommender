from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    result = ""

    if request.method == "POST":

        screen = int(request.form["screen"])
        social = int(request.form["social"])
        unlocks = int(request.form["unlocks"])

        if screen > 7 or social > 4 or unlocks > 100:
            result = "High Usage ⚠️ - Try a 24 hour digital detox"

        elif screen > 4 or social > 2:
            result = "Moderate Usage 📱 - Set daily screen limits"

        else:
            result = "Healthy Usage ✅ - Maintain balanced habits"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, url_for, request 
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/length", methods=["POST","GET"])
def length():
    if request.method == "POST":
        num = float(request.form["nu"])
        value=float(request.form["from_unit"])*num/float(request.form["to_unit"])
        return render_template("length.html", value=value)
    else:
         return render_template("length.html")

@app.route("/weight",  methods=["POST","GET"])
def weight():
    if request.method == "POST":
        num = float(request.form["nu"])
        value=float(request.form["from_unit"])*num/float(request.form["to_unit"])
        return render_template("weight.html", value=value)
    else:
        return render_template("weight.html")

@app.route("/temperature", methods=["POST","GET"])
def temperature():
    if request.method == "POST":
        num = float(request.form["nu"])
        from_temp=request.form["from_unit"]
        to_temp=request.form["to_unit"]

        if from_temp == "celsius":
            celsius = num

        elif from_temp == "fahrenheit":
            celsius = (num - 32) * 5 / 9

        elif from_temp == "kelvin":
            celsius = num - 273.15


# Then convert Celsius to the selected output
        if to_temp == "celsius":
            value = celsius

        elif to_temp == "fahrenheit":
            value = (celsius * 9 / 5) + 32

        elif to_temp == "kelvin":
            value = celsius + 273.15
        return render_template("temperature.html", value=value)
    else:
        return render_template("temperature.html")

if __name__ == "__main__":
    app.run()
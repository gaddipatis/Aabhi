"""Web app to sum two integers."""

from flask import Flask, render_template, request

app = Flask(__name__)


def sum_integers(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    num1 = ""
    num2 = ""

    if request.method == "POST":
        num1 = request.form.get("num1", "").strip()
        num2 = request.form.get("num2", "").strip()

        try:
            a = int(num1)
            b = int(num2)
            result = sum_integers(a, b)
        except ValueError:
            error = "Please enter valid integers in both fields."

    return render_template(
        "index.html",
        result=result,
        error=error,
        num1=num1,
        num2=num2,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)

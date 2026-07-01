"""Web app to sum and multiply two integers."""

from flask import Flask, render_template, request

app = Flask(__name__)


def sum_integers(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def multiply_integers(a: int, b: int) -> int:
    """Return the product of two integers."""
    return a * b


@app.route("/", methods=["GET", "POST"])
def index():
    active_tab = "sum"
    result = None
    error = None
    operator = "+"
    num1 = ""
    num2 = ""

    if request.method == "POST":
        active_tab = request.form.get("operation", "sum")
        num1 = request.form.get("num1", "").strip()
        num2 = request.form.get("num2", "").strip()

        try:
            a = int(num1)
            b = int(num2)
            if active_tab == "multiply":
                result = multiply_integers(a, b)
                operator = "×"
            else:
                result = sum_integers(a, b)
                operator = "+"
        except ValueError:
            error = "Please enter valid integers in both fields."

    return render_template(
        "index.html",
        active_tab=active_tab,
        result=result,
        error=error,
        operator=operator,
        num1=num1,
        num2=num2,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)

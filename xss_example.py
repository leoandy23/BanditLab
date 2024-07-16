from flask import Flask, request, render_template_string

app = Flask(__name__)


# Página de inicio con un formulario de entrada
@app.route("/")
def index():
    return """
        <form action="/greet" method="post">
            <label for="name">Enter your name:</label>
            <input type="text" id="name" name="name">
            <input type="submit" value="Submit">
        </form>
    """


# Ruta que recibe el nombre del usuario y lo muestra
@app.route("/greet", methods=["POST"])
def greet():
    name = request.form["name"]
    return render_template_string(f"Hello, {name}!")


if __name__ == "__main__":
    app.run(debug=True)

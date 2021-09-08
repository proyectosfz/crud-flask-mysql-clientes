
from flask import Flask, render_template, request, redirect, flash
import controlador_clientes

app = Flask(__name__)

"""
Definición de rutas
"""


@app.route("/agregar_cliente")
def formulario_agregar_cliente():
    return render_template("agregar_cliente.html")


@app.route("/guardar_cliente", methods=["POST"])
def guardar_cliente():
    nombre = request.form["nombre"]
    telefono = request.form["telefono"]
    controlador_clientes.insertar_cliente(nombre, telefono)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/clientes")


@app.route("/")
@app.route("/clientes")
def clientes():
    clientes = controlador_clientes.obtener_clientes()
    return render_template("clientes.html", clientes=clientes)


@app.route("/eliminar_cliente", methods=["POST"])
def eliminar_cliente():
    controlador_clientes.eliminar_cliente(request.form["id"])
    return redirect("/clientes")


@app.route("/formulario_editar_cliente/<int:id>")
def editar_cliente(id):
    # Obtener el juego por ID
    cliente = controlador_clientes.obtener_cliente_por_id(id)
    return render_template("editar_cliente.html", cliente=cliente)


@app.route("/actualizar_cliente", methods=["POST"])
def actualizar_cliente():
    id = request.form["id"]
    nombre = request.form["nombre"]
    telefono = request.form["telefono"]
    controlador_clientes.actualizar_cliente(nombre, telefono, id)
    return redirect("/clientes")


# Iniciar el servidor
if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8000, debug=True)
    app.run(port=5300, debug=True)

"""https://github.com/parzibyte/crud-flask-mysql"""
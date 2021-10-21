import os
from re import escape
from flask import Flask, render_template, redirect, session, flash, request
from werkzeug.security import check_password_hash, generate_password_hash
from database import accion, seleccion

from forms import Login, Registro 


app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/", methods= ["GET"])
def inicio():
  return render_template('index.html')

@app.route("/productos", methods= ["GET"])
def productos():
    return render_template("product-list.html")

@app.route("/listadeseos", methods= ["GET", "POST"])
def lista_deseos():
    return render_template("listadeseos.html")

@app.route("/carcompras", methods= ["GET","POST"])
def car_compras():
    return render_template("cart.html")

@app.route("/registro", methods=["GET", "POST"] )
def registro():
    form = Registro()
    if  request.method == "GET": #Si la ruta es accedida a través del método GET entonces
	    return render_template('register.html', form=form,titulo=' ')
    else:
        # Recuperar los datos del formulario
        nom = escape(request.form['nombre'])
        ape = escape(request.form['apellido'])
        ema = escape(request.form['email'])
        tel = escape(request.form['telefono'])
        tipo_id = escape(request.form['tipo_ide'])
        num_ide = escape(request.form['num_ide'])
        pa = escape(request.form['pais'])
        dep = escape(request.form['departamento'])
        ciu = escape(request.form['ciudad'])
        dir = escape(request.form['direccion'])
        fec_naci = escape(request.form['fecha_naci'])
        con = escape(request.form['contrasena'])
        ver = escape(request.form['val_cont'])
        ter = escape(request.form['Condition'])
        prom = escape(request.form['promocional'])
        tip_user= 'user_final'

        sql = "INSERT INTO PERSONAS(nombre, apellido, email, telefono, tipo_id, num_id, pais, departamento, ciudad, direccion, fecha_naci, condition, promocional) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

        res = accion(sql,(nom, ape, ema, tel, tipo_id, num_ide, pa, dep, ciu, dir, fec_naci, ter, prom))
        if res!=0:
                flash('INFO: Datos almacenados con exito en PERSONA')
        else:
                flash('ERROR EN PERSONA: Por favor reintente')
              
        sql = "INSERT INTO USUARIOS(email, contrasena, tipo_user) VALUES (?, ?,?)"
        pwd = generate_password_hash(con)
        res= accion(sql,(ema, pwd, tip_user))
        if res!=0:
                flash('INFO: Datos almacenados con exito EN USUARIO')
        else:
                flash('ERROR USUARIO: Por favor reintente')

        return render_template('register.html', form=form, titulo=' ')



@app.route("/login", methods=["GET","POST"])
def login():
    form = Login()
    if  request.method == "GET": #Si la ruta es accedida a través del método GET entonces
	    return render_template('login.html', form=form,titulo=' ')
    else:
     ema = escape(request.form['email'])
     con = escape(request.form['contrasena'])

    sql = f'SELECT u.id_usuario, u.email, u.contrasena, u.tipo_user, p.nombre FROM usuarios as u inner join personas as p on u.email=p.email  WHERE u.email= "{ema}"'
    res = seleccion(sql)
    if len(res)==0:
        flash('ERROR: Usuario o clave invalidas')
        return render_template("login.html", form=form, titulo= " ")
    else:
        cbd = res[0][2]
        if check_password_hash(cbd, con):
            session.clear()
            session['id_usuario'] = res[0][0]
            session['email'] = ema
            session['contrasena'] = con
            session['tipo_user'] = res[0][3]
            session['nombre'] = res[0][4]
            return render_template('indexuser.html',form=form, titulo= f"Bienvenido {session['nombre']}", messages =res)
        else:
            flash('ERROR: Usuario o clave invalidas')
        return render_template('login.html', form=form, titulo=' ')





@app.route("/soporte", methods= ["GET", "POST"])
def soporte():
    return render_template("soporte.html")

@app.route("/contacto", methods=[ "GET","POST"])
def contacto():
    return render_template("contact.html")

@app.route("/administrador", methods=[ "GET","POST"])
def administrador():
    return render_template("dashboardn.html")

@app.route("/editarP", methods=[ "GET","POST"])
def editarP():
    return render_template("editP.html")

@app.route("/calproducto", methods=[ "GET","POST"])
def calproducto():
    return render_template("calproducto.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')








    

from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, PasswordField
from wtforms.fields.core import SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import EqualTo, InputRequired

class Registro(FlaskForm):
    nom = TextField('nombre *', validators = [InputRequired(message='Indique el nombre')])
    ape = TextField('apellido *', validators = [InputRequired(message='Indique el apellido')])
    ema = EmailField('email *', validators = [InputRequired(message='Indique el email')])
    tel = TextField('telefono *', validators = [InputRequired(message='Indique el telefono')])
    tipo_id = TextField('tipo_ide *', validators = [InputRequired(message='Indique el tipo de documento')])
    num_id = TextField('num_ide*', validators = [InputRequired(message='Indique el numero de documento')])
    pa = TextField('pais *', validators = [InputRequired(message='Indique el nombre')])
    dep = TextField('departamento *', validators = [InputRequired(message='Indique el nombre')])
    ciu = TextField('ciudad *', validators = [InputRequired(message='Indique el nombre')])
    dir = TextField('direccion*', validators = [InputRequired(message='Indique el nombre')])
    fec_naci = TextField('fecha_naci *', validators = [InputRequired(message='Indique el nombre')])
    con = PasswordField('Clave *', validators = [InputRequired(message='Indique la clave')])
    ver = PasswordField('val_cont *', validators = [InputRequired(message='Indique la verificación'), EqualTo(con,message='Clave y la verificación no coinciden')])
    ter = TextField('terminos *', validators = [InputRequired(message='Indique el nombre')])
    prom = TextField('promocion *', validators = [InputRequired(message='Indique el nombre')])
    btn = SubmitField('Registrar')

class Login(FlaskForm):
    ema = EmailField('email *', validators = [InputRequired(message='Indique su Email')])
    con = PasswordField('Contrasena *', validators = [InputRequired(message='Indique la Contraseña')])
    btn = SubmitField('Login')

class Producto(FlaskForm):
    nomp = TextField('nombre *', validators = [InputRequired(message='Indique el nombre')])
    tipop = TextField('tipo *', validators = [InputRequired(message='Indique el tipo')])
    can = TextField('cantidad *', validators = [InputRequired(message='Indique la cantidad')])
    canmin = TextField('can_minima *', validators = [InputRequired(message='Indique la cantidad minima')])
    canmax = TextField('can_max *', validators = [InputRequired(message='Indique la cantidad maxima')])
    pre = TextField('precio*', validators = [InputRequired(message='Indique el precio')])
    cali = TextField('calificacion *', validators = [InputRequired(message='Indique la calificacion')])
    des = TextField('descripcion *', validators = [InputRequired(message='Indique la descripcion')])
    btn = SubmitField('Enviar')

class EditarP(FlaskForm):
    id_pro = TextField('Codigo *', validators = [InputRequired(message='Indique el Codigo')])
    btn = SubmitField('Buscar')
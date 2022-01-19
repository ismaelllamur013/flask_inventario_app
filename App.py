from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='flaskinventario'
mysql =MySQL(app)

app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    return render_template('index.html', contacts = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        id_num=request.form['id_num']
        type=request.form['type']
        descr=request.form['descr']
        fabric=request.form['fabric']
        model=request.form['model']
        n_serie=request.form['n_serie']
        ubic=request.form['ubic']
        estado=request.form['estado']
        alimen=request.form['alimen']
        requis=request.form['requis']
        fecha=request.form['fecha']
        prov_mant=request.form['prov_mant']
        prov_com=request.form['prov_com']
        cur=mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (id_num, type, descr, fabric, model, n_serie, ubic, estado, alimen, requis, fecha, prov_mant, prov_com) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (id_num, type, descr, fabric, model, n_serie, ubic, estado, alimen, requis, fecha, prov_mant, prov_com))
        mysql.connection.commit()
        flash('Contact Added Successfully')
        return (redirect(url_for('Index')))


@app.route('/edit/<id>')
def get_contact(id):
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s', (id))
    data = cur.fetchall()
    return (render_template('edit-contact.html', contact = data[0]))

@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        id_num=request.form['id_num']
        type=request.form['type']
        descr=request.form['descr']
        fabric=request.form['fabric']
        model=request.form['model']
        n_serie=request.form['n_serie']
        ubic=request.form['ubic']
        estado=request.form['estado']
        alimen=request.form['alimen']
        requis=request.form['requis']
        fecha=request.form['fecha']
        prov_mant=request.form['prov_mant']
        prov_com=request.form['prov_com']
        cur=mysql.connection.cursor()
        cur.execute("""
            UPDATE contacts
            SET id_num = %s, 
                type = %s,
                descr = %s,
                fabric = %s,
                model = %s,
                n_serie = %s,
                ubic = %s,
                estado = %s,
                alimen = %s,
                requis = %s,
                fecha = %s,
                prov_mant = %s,
                prov_com = %s
            WHERE id = %s
        """,(id_num, type, descr, fabric, model, n_serie, ubic, estado, alimen, requis, fecha, prov_mant, prov_com, id))
        mysql.connection.commit()
        flash('Contact Updated Successfully')
        return (redirect(url_for('Index')))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur=mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact Removed Successfully')
    return (redirect(url_for('Index')))

if __name__ == '__main__':
    app.run(port = 3010, debug = True)
from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
import operator
import json

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        return jsonify(dict((key, request.form.getlist(key) if len(request.form.getlist(key)) > 1 else request.form.getlist(key)[0]) for key in request.form.keys()))
    else:
        #print request.args.get('roles')
        hostname = request.args.get('hostname', '')
        roles    = request.args.get('roles', '')
        recipes  = request.args.get('recipes', '')
        n_srv    = request.args.get('n_srv', '')
        vlan     = request.args.get('vlan', '')
        tipo  = request.args.get('tipo', '')
    return render_template('form.html', hostname=hostname, roles=roles, recipes=recipes, n_srv=n_srv, vlan=vlan, tipo=tipo)


if __name__ == "__main__":
    app.debug = True
    app.run()

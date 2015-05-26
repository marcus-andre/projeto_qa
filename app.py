from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def form():
    values = {}
    print request.form
    if request.method == 'POST':
        for a, i in request.form.iteritems():
            values.update({a: i})
        return jsonify(values.sort())

    else:
        json_render = {
            'hostname': request.args.get('hostname', None),
            'roles': request.args.get('roles', None),
            'recipes': request.args.get('recipes', None),
            'n_srv': request.args.get('n_srv', None),
            'vlan': request.args.get('vlan', None),
            'tipo': request.args.get('tipo', None)
        }
    return render_template('form.html', args=json_render)


if __name__ == "__main__":
    app.debug = True
    app.run()

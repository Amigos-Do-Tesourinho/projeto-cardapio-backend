from flask import Flask
from Routes import routes_blueprint

app = Flask(__name__)
app.register_blueprint(routes_blueprint)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)
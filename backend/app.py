from flask import Flask
from flask import Flask, request, jsonify
from routes import routes 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from routes.routes import create_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:%password%@localhost/Akiwacu'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(routes.bp)


if __name__ == '__main__':
    app.run(debug=True)
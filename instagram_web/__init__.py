from app import app
from flask import render_template
from instagram_web.blueprints.users.views import users_blueprint
from flask_assets import Environment, Bundle
from .util.assets import bundles

assets = Environment(app)
assets.register(bundles)

app.register_blueprint(users_blueprint, url_prefix="/users")

@app.errorhandler(500)
def error_500(e):
    return render_template('500.html'), 500

@app.errorhandler(404)
def error_404(e):
    return render_template('404.html'), 404


@app.route("/")
def home():
    return render_template('home.html')

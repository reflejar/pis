############################
### Configuraciones iniciales
############################
import os

############################
### Se inicia Flask
############################
from flask import Flask, render_template
web = Flask(__name__)

# Se agregan variables de entorno
@web.context_processor
def inject_env():
    return dict(
          GOOGLE_ANALYTICS_TRACKING_ID=os.getenv('GOOGLE_ANALYTICS_TRACKING_ID'),
	)

# Se incorporan endpoints necesarios
@web.route("/")
def index(): return render_template("index.html")

@web.route("/mapa-normativo")
def normativo(): return render_template("app.html", source=os.getenv('URI_MAPA_NORMATIVO'))


# Se corre la aplicación
if __name__ == "__main__":
	web.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)
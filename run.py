import os

from flask import Flask
from flask import request

app = Flask(__name__)

from gomashio.views import gomashio
app.register_blueprint(gomashio, url_prefix='/gomashio')

from mediciner.views import mediciner
app.register_blueprint(mediciner, url_prefix='/mediciner')


if __name__ == "__main__":
    LISTEN_PORT = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=LISTEN_PORT)

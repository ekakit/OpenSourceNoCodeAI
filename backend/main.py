from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from ml_features.tabular_data.predict import tabular_predictions
import sys

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSON_AS_ASCII'] = False

@app.route("/generate_tabular_predictions", methods = ['GET'])
@cross_origin()
def generate_tabular_predictions():
    with app.app_context():
        return tabular_predictions(request)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    if(len(sys.argv) > 1 and sys.argv[1] == 'dev_mode'):
        local_database = 'localhost'
    app.run(host='127.0.0.1', port=8080, debug=True)

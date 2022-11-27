from ml_features.tabular_data.timeseries.predict import generate_timeseries_predictions


def tabular_predictions(request):
    prediction_type = ""
    file_url = ""
    if request.args:
        if 'prediction_type' in request.args:
            prediction_type = request.args.get('prediction_type')
        if 'file_url' in request.args:
            file_url = request.args.get('file_url')
    response = {}
    if prediction_type == "timeseries":
        if file_url:
                generate_timeseries_predictions(file_url)
        else:
            raise Exception("XA002: No File Specified")
    if not response:
        raise Exception('XA001: Error when using the model')
    return response


import os
from waitress import serve
import webbrowser
import house_price_predictor_app as app # Import your app

# Run from the same directory as this script
this_files_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(this_files_dir)

# `url_prefix` is optional, but useful if you are serving app on a sub-dir
# behind a reverse-proxy.
webbrowser.open("127.0.0.1:8050")
serve(app.flask_app, host='127.0.0.1', port=8050)

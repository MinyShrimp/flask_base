from flask import Flask, request, jsonify, render_template, make_response, send_from_directory, redirect

app = Flask(__name__)

#@app.route('/favicon.ico')
#def favicon():
#    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

#@app.errorhandler(404)
#def page_not_found(error):
#    return render_template('404.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True)
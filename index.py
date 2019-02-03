from flask import Flask, render_template, request, jsonify
from musilette import get_ranges
# Initialize the Flask application
app = Flask(__name__)
 
# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/')
def index():
    return render_template('musilette.html')
 
# Route that will process the AJAX request, sum up two
# integer numbers (defaulted to zero) and return the
# result as a proper JSON response (Content-Type, etc.)
@app.route('/compute_ranges', methods=['POST'])
def compute_ranges():

    notes = request.form.getlist('notes[]')
    result = get_ranges(notes)
    return jsonify(result)
 
# sur requete AJAX _get_message on renvoie le texte   
# je suis la reponse ajax du serveur a + le parametre transmis  
@app.route('/_get_message')
def get_message():
    param = request.args['notes']
    return jsonify(result='je suis la reponse ajax du serveur a ' + param)
 
if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("8090"),
        debug=True
    )
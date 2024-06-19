from flask import Flask, jsonify, request
import data_handling as dt

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'

@app.route('/input')
def theform():
    return '''<form method="POST" action="/process">
                  <h5>Barcode</h5>
                  <input type="text" name="barcode">
                  <br>
                  <input type="submit" value="Submit">
              </form>'''

@app.route('/process', methods=['POST'])
def process():

    barcode = request.form['barcode']
    data_dict = dt.seperate_input(barcode)

    return '''
            <h5>Barcode: {}</h5>
            <br>
            <h5>Seriennummer: {}</h5>
            <br>
            <h5>Artikelnummer: {}</h5>
            <br>
            <h5>Bestellnummer: {}</h5>
            <br>
            <h5>Eichschein: {}</h5>
            <br>
            '''.format(barcode, data_dict['serialnumber'], data_dict['articlenumber'], data_dict['ordernumber'], data_dict['certificat'])

    # return '<h1>Hello {}. You are from {}. You have submitted the form successfully!<h1>'.format(barcode, serialnumber)

if __name__ == '__main__':
    app.run()
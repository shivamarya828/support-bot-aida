from email.policy import default
from flask import Flask, redirect, render_template, request, url_for, redirect
from datetime import datetime

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/MLS/')
def MLS():
    return render_template('MLS.html')

@app.route('/EI/')
def EI():
    return render_template('EI.html')

@app.route('/MLS/Pyspark/')
def Pyspark():
    return render_template('Pyspark.html')

@app.route('/MLS/Hive/')
def Hive():
    return render_template('Hive.html')

@app.route('/MLS/MLSLogin/')
def MLSLogin():
    return render_template('MLSLogin.html')

@app.route('/MLS/Pyspark/GeneralUsage/')
def GeneralUsage():
    return render_template('GeneralUsage.html')

@app.route('/MLS/Pyspark/CommonErrors/')
def CommonErrors():
    return render_template('CommonErrors.html')

@app.route('/MLS/Hive/HiveMagics/')
def Magics():
    return render_template('HiveMagics.html')

@app.route('/MLS/Hive/HiveWorkbench/')
def Workbench():
    return render_template('HiveWorkbench.html')

if __name__ == "__main__":
    app.run(debug = True)
from tkinter import font
import tensorflow as tf
import numpy as np
from tkinter.filedialog import askopenfilename
import PySimpleGUI as sg
from flask import Flask, render_template, url_for, redirect, session, request
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "super secret key"

CORS(app, resources={r'/*': {'origins': '*'}})

def prediction_status(prediction):
    match prediction:
        case 0:
            return " 20km/h"
        case 1:
            return " 30km/h"
        case 2:
            return " 50km/h"
        case 23:
            return " 60km/h"
        case 34:
            return " 70km/h"
        case 38:
            return " 80km/h"
        case 6:
            return " prestanak ogranicenja 80km/h"
        case 40:
            return " 100km/h"
        case 8:
            return " 120km/h"
        case 9:
            return " zabrana pretjecanja svih motornih vozila, osim mopeda"
        case 10:
            return ""
        case 11:
            return ""
        case 12:
            return " 50km/h"
        case 13:
            return ""
        case 14:
            return ""
        case 15:
            return ""
        case _:
            return "Something's went wrong with predicting "

def predict_with_model(model, imgpath):

    image = tf.io.read_file(imgpath)
    image = tf.image.decode_png(image, channels=3)
    image = tf.image.convert_image_dtype(image, dtype=tf.float32)
    image = tf.image.resize(image, [60,60]) # (60,60,3)
    image = tf.expand_dims(image, axis=0) # (1,60,60,3)

    predictions = model.predict(image) #return exact class 
    predictions = np.argmax(predictions) 

    return predictions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=["POST", "GET"])

def predict():

    imgpath = "C:\\Users\\niniy\\Downloads\\TrafficSigns\\Images\\" + request.form.get("imagePath")
    model = tf.keras.models.load_model('./Models')
    prediction = predict_with_model(model, imgpath)

    print('prediction', prediction)

    predictedSign = prediction_status(prediction)
    
    return predictedSign

@app.route('/background_process_test', methods=["POST", "GET"])

def background_process_test():
    img_path = askopenfilename()


    model = tf.keras.models.load_model('./Models')
    prediction = predict_with_model(model, img_path)

    predictedSign = prediction_status(prediction)

    session['my_var'] = predictedSign

    
    print(f"prediction is = {prediction}")
    return redirect(url_for('prediction'))


@app.route('/prediction', methods=["GET"])
def prediction():
    my_var = session.get('my_var', prediction)
    return render_template('prediction.html', var=my_var)
    

if __name__=="__main__":

    app.run(debug = True)
from tkinter import font
import tensorflow as tf
import numpy as np
from tkinter.filedialog import askopenfilename
import PySimpleGUI as sg



def predict_with_model(model, imgpath):

    image = tf.io.read_file(imgpath)
    image = tf.image.decode_png(image, channels=3)
    image = tf.image.convert_image_dtype(image, dtype=tf.float32)
    image = tf.image.resize(image, [60,60]) # (60,60,3)
    image = tf.expand_dims(image, axis=0) # (1,60,60,3)

    predictions = model.predict(image) #return exact class 
    predictions = np.argmax(predictions) 

    return predictions



if __name__=="__main__":

    img_path = askopenfilename()

    model = tf.keras.models.load_model('./Models')
    prediction = predict_with_model(model, img_path)

    print(f"prediction is = {prediction}")

    def prediction_status(prediction):
        match prediction:
            case 0:
                return "sign type : 20km/h"
            case 1:
                return "sign type : 30km/h"
            case 2:
                return "sign type : 50km/h"
            case 3:
                return "sign type : 60km/h"
            case 4:
                return "sign type : 70km/h"
            case 5:
                return "sign type: 80km/h"
            case 6:
                return "sign type: prestanak ogranicenja 80km/h"
            case 7:
                return "sign type: 100km/h"
            case 8:
                return "sign type : 120km/h"
            case 9:
                return "sign type : zabrana pretjecanja svih motornih vozila, osim mopeda"
            case 10:
                return "sign type :"
            case 11:
                return "sign type :"
            case 12:
                return "sign type : 50km/h"
            case 13:
                return "sign type :"
            case 14:
                return "sign type :"
            case 15:
                return "sign type :"
            case _:
                return "Something's went wrong with predicting "

    font = ("Arial", 12)
    sg.popup_no_buttons(f"--- Prediction is {prediction_status(prediction)} ---", title='Prediction', text_color=('#F7F6F2'), keep_on_top=True, image=img_path, font=font)
    print(f"prediction_status is = {prediction_status(prediction)}")
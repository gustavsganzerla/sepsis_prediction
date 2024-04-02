from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from . import models
from . forms import Model1Form, Model2Form, Model3Form
import os
from django.conf import settings
import joblib
from django.conf import settings
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import pickle
import xgboost as xgb
import numpy as np

#loading models
def load_model1():
    model_path = os.path.join(settings.BASE_DIR, 'predictor/models/', 'model1.model')
    model1 = xgb.Booster(model_file=model_path)
    return model1

def load_model2():
    model_path = os.path.join(settings.BASE_DIR, 'predictor/models/', 'model2.model')
    model2 = xgb.Booster(model_file=model_path)
    return model2

def load_model3():
    model_path = os.path.join(settings.BASE_DIR, 'predictor/models/', 'model3.model')
    model3 = xgb.Booster(model_file=model_path)
    return model3


# Create your views here.

def home(request):
    return render(request, 'predictor/home.html')

def models(request):
    return render(request, 'predictor/models.html')

def model1(request):
    predictor_model1 = load_model1()

    if request.method == 'POST':
        form = Model1Form(request.POST)
        if form.is_valid():
            collected_data = form.cleaned_data

            inputs = [collected_data[field] for field in collected_data]
            inputs = np.array(inputs)
            inputs = inputs.reshape(1, -1)
            scaler = StandardScaler()
            inputs = scaler.fit_transform(inputs)
            inputs = xgb.DMatrix(inputs)

            output = ""

            prediction = predictor_model1.predict(inputs)

            if prediction > 0.5:
                output = "Severe"
            else:
                output = "Non-severe"
            
            return render(request, "predictor/results.html", {'output':output})
    else:
        form = Model1Form()
    
    return render(request, "predictor/model1.html", {'form': form})

def model2(request):
    predictor_model1 = load_model2()

    if request.method == 'POST':
        form = Model2Form(request.POST)
        if form.is_valid():
            collected_data = form.cleaned_data

            inputs = [collected_data[field] for field in collected_data]
            inputs = np.array(inputs)
            inputs = inputs.reshape(1, -1)
            scaler = StandardScaler()
            inputs = scaler.fit_transform(inputs)
            inputs = xgb.DMatrix(inputs)

            output = ""

            prediction = predictor_model1.predict(inputs)

            if prediction > 0.5:
                output = "Severe"
            else:
                output = "Non-severe"
            
            return render(request, "predictor/results.html", {'output':output})
    else:
        form = Model2Form()
    
    return render(request, "predictor/model2.html", {'form': form})

def model3(request):
    predictor_model1 = load_model3()

    if request.method == 'POST':
        form = Model3Form(request.POST)
        if form.is_valid():
            collected_data = form.cleaned_data

            inputs = [collected_data[field] for field in collected_data]
            inputs = np.array(inputs)
            inputs = inputs.reshape(1, -1)
            scaler = StandardScaler()
            inputs = scaler.fit_transform(inputs)
            inputs = xgb.DMatrix(inputs)

            output = ""

            prediction = predictor_model1.predict(inputs)

            if prediction > 0.5:
                output = "Severe"
            else:
                output = "Non-severe"
            
            return render(request, "predictor/results.html", {'output':output})
    else:
        form = Model3Form()
    
    return render(request, "predictor/model3.html", {'form': form})
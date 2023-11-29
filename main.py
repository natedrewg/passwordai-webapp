import pandas as pd
import numpy as np
from pyscript import Element
from js import document, window
import pickle

#Disable warnings by pyscript appearing in the browser.
import warnings
warnings.filterwarnings("ignore")

#Load pickle file 
with open("rfc.pkl", "rb") as f:
  loaded_model = pickle.load(f)


def get_prediction():
#Insert password from HTML-User
  pWord = document.getElementById('password').value;

#Setting up array
  length = len(pWord)
  charNum = 0
  if (pWord.isalpha()==0 & pWord.isdigit()==0):
      charNum = 1
  capLetter = 0
  if (pWord.upper() != pWord and pWord.lower() != pWord):
    capLetter = 1
  specialChar = 1
  if(pWord.isalnum()==1):
    specialChar = 0
#Setting up array
  finale = np.array([length, charNum, capLetter, specialChar]).reshape(1, -1)

#Predicting on the array
  prediction = loaded_model.predict([finale])

  return prediction
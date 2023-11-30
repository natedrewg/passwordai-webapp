import pandas as pd
import numpy as np
from pyscript import Element
from js import document
import pickle


def print():
  result = document.getElementById('password').value;
  pyscript.write("result",result)

def check():
#Load pickle file 
  with open("rfc.pkl", "rb") as f:
    loaded_model = pickle.load(f)
  


#Insert password from HTML-User
  pWord = document.querySelector("#password").value

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
  result = loaded_model.predict(finale)

  pyscript.write("result",result[0])  
  
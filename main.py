import pandas as pd
import numpy as np
from pyscript import Element
from js import document
import pickle

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
  if result == 0:
    result = 'Weak'
    num = 33
    document.getElementsByClassName('progress-bar').item(0).setAttribute('style','width:'+str(num)+'%')
  elif result == 1:
    result = 'Okay'
    num = 66
    document.getElementsByClassName('progress-bar').item(0).setAttribute('style','width:'+str(num)+'%')
  else:
    result = 'Strong'
    num = 100
    document.getElementsByClassName('progress-bar').item(0).setAttribute('style','width:'+str(num)+'%')

  if pWord == '':
    num = 0
    result = 'None'
    document.getElementsByClassName('progress-bar').item(0).setAttribute('style','width:'+str(num)+'%')

  pyscript.write("result",result)  
  
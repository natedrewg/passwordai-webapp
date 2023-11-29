import xgboost as xgb
import pandas as pd
from pyscript import Element
from js import document, window
import numpy as np

classes = ["0","1","2"]

loaded_model = xgb.Booster()
loaded_model.load_model("xgb_model.json")

def transformPassword(pWord):
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
  return np.array([length, charNum, capLetter, specialChar]).reshape(1, -1)

def get_prediction():
  try:
    pas = str(Element("password").value)

  except:
    # window.alert("Please Enter valid values!")
    return 0
  
  sample_test_record = pd.DataFrame([{
      transformPassword(pas)
  }])
  prediction = loaded_model.predict(xgb.DMatrix(sample_test_record))

  # print("Predicted class for the above sample_test_record:",predicted_class)
  
  return prediction
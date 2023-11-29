import xgboost as xgb
import pandas as pd
from pyscript import Element
from js import document, window

classes = ["0","1","2"]

loaded_model = xgb.Booster()
loaded_model.load_model("xgb_model.json")

def get_predictions():
  try:
    sl = str(Element("sl").value)
    sw = str(Element("sw").value)
    pl = str(Element("pl").value)
  except:
    # window.alert("Please Enter valid values!")
    return 0
  
  sample_test_record = pd.DataFrame([{
      'sepal length (cm)': float(Element("sl").value),
      'sepal width (cm)': float(Element("sw").value),
      'petal length (cm)': float(Element("pl").value),
  }])
  prediction = loaded_model.predict(xgb.DMatrix(sample_test_record))

  # predicted_class = "SETOSA"

  predicted_class = classes[int(prediction.argmax())]
  document.querySelector("#iris_image").src = f"./images/{predicted_class}.png"
  document.querySelector("#prediction_result").innerHTML = f"The iris flower for the input data is : <b>{predicted_class}</b>"

  # print("Predicted class for the above sample_test_record:",predicted_class)
  
  return predicted_class
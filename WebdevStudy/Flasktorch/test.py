
import requests

resp = requests.post("http://3.94.132.146:5000/predict",
                     files={"file": open('./dog.jpg','rb')})
print(resp.json())
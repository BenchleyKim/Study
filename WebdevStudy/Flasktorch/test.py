
import requests

resp = requests.post("http://3.94.132.146:5000/predict",
                     files={"file": open('./kitten.jpg','rb')})
print(resp.json())
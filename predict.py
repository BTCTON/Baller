########## Classifier using the Clarifai API for fun ########################

## Can be used for anything not just the different types of balls as the functions are provided by Clarifai and are well trained! #######
from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

app = ClarifaiApp(api_key='{gotta get ur own}')

model = app.models.get('general-v1.3')

images = ClImage(file_obj=open('[LOCAL PATH TO IMAGE HERE].jpeg', 'rb'))

data = model.predict([images])

accuracy = data['outputs'][0]['data']['concepts'][0]['value']

label = data['outputs'][0]['data']['concepts'][0]['name']

percent = accuracy*100

print("The object you gave me is a {}, and I am {} percent confident!").format(label, percent)

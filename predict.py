########## Classifier using the Clarifai API 


from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

app = ClarifaiApp(api_key='{}')

model = app.models.get('general-v1.3')

images = ClImage(file_obj=open('[LOCAL PATH TO IMAGE HERE].jpeg', 'rb'))

data = model.predict([images])

accuracy = data['outputs'][0]['data']['concepts'][0]['value']

label = data['outputs'][0]['data']['concepts'][0]['name']

percent = accuracy*100

print("The object you gave me is a {}, and I am {} percent confident!").format(label, percent)

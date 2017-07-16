########## Classifier using the Clarifai API for fun ########################
from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

app = ClarifaiApp(api_key='{gotta get ur own}')

model = app.models.get('general-v1.3')

images = ClImage(file_obj=open('[LOCAL PATH TO IMAGE HERE].jpeg', 'rb'))

data = model.predict([images])


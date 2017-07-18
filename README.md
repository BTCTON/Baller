# Hoops

Hoops is a way for the computer determine what kind of ball is shown - whether it is a tennis ball, basketball, soccer ball or baseball. 

To run the program first clone the repository into your local directory and then cd to your working directory in terminal and execute by typing in 
```
python label_image.py [PATH_TO_IMAGE.JPG]
```
Also, not all training_summaries as well as the retrained_graph.pb uploaded due to size, and there is a bit redundacy that came up with the training images due to file organization. When cloning the repo, only use one set of your data - the folder that is tf_files/balls rather than the basketballs as the former one is more comprehensive. 

I also tested this using the Clarifai API to see if the results were approximately the same.
The script using the Clarifai API can be run by doing 
```
python predict.py
```
in the terminal.

Note: Don't forget to change the path in the file to the image you want. Also, being that it is an API it can classify much more than the different types of balls that I had originally built my classifier for.

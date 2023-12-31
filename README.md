APPLICATION SUMMARY:

This is a test application built to assess the capabilities of the keras adam optimizer. 
The model is trained on a bunch of random food recipes scrapped from the net. It then generates
new recipes. The best ones were consolidated into a list of favorite recipes and was hooked
to a Web Application that allows users to explore AI Generated Food Recipes. 

USAGE:

RUN the app.py file from the web subdirectory. This will run a webserver that shows
the web application that lists the AI generated recipes. 

PROJECT STRUCTURE:

a) data sub-directory: Read from the combined.txt file (AI/ML model's output file) 
   and return an array of recipes. Each recipe is a Dictionary wth three 
   key-value pairs: 1) title, 2) Ingredients, and 3) Steps.
b) preprocessing sub-directory: Preprocess a csv file (RAW_recipes.csv) containing 
   recipe text to generate the training data (training.txt).
c) sallygen sub-directory: Run the AI/ML Model (keras adam optimizer) to generate 
   new recipes.
b) web sub-directory: Flask-based web application that provides an interface to the 
   recipes in the favorites.txt file which were chosen from the recipes generated by
   the model.

### python -m venv .env
### 
### # Activate the virtual environment
### source .env/Scripts/activate OR source .env/bin/activate 
### # Deactivate the virtual environment
### source .env/Scripts/deactivate

### Run the following in the sallygen and web sub-directories to install 
### the required libraries into the python environment setup above
###
### pip install -r requirements.txt
###



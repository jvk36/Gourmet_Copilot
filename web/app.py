from flask import Flask, render_template, send_from_directory
import re
import datetime
import json

app = Flask(__name__)


@app.route('/')
def recipe_list():
    with open('data/favorites.txt') as f:
        favorites = f.read().split('\n')
    with open('data.json', 'r') as f:
        data = json.loads(f.read())
   
    blog_date = datetime.datetime.now().strftime("%m/%d/%Y")
    print(favorites)
    for x in favorites:
        if x == ' ':
            favorites.remove(' ')
        elif x == '':
            favorites.remove('')

    favorites = [{'name': x.replace('-', ' ').title(), 'date': blog_date} for x in favorites]

    recipies = [{'name': x.replace('-', ' ').title(), 'date': blog_date} for x in data]
    return render_template('home.html', 
            favorites=favorites,
            recipies=recipies)

@app.route('/static/<file>')
def serve_static(file):
    return send_from_directory('static', file)


@app.route('/recipe/<name>')
def recipe(name):
    print(name)
    try:
        with open('data.json', 'r') as f:
            data = json.loads(f.read())
    except:
        return '404 lol (but file)'

    name = name.lower()
    if name not in data:
        return '404 lol, recipe dne!'

    recipe = data[name]
    ingredients = recipe['ingredients']
    ingredients = re.split(r'\s*,\s*', ingredients)
    recipe_steps = recipe['steps']
    name = name.replace('-', ' ').title()
    print(ingredients)
    blog_date = datetime.datetime.now().strftime("%m/%d/%Y")
    return render_template('recipe.html', 
        name=name, 
        ingredients=ingredients, 
        recipe_steps=recipe_steps,
        blog_date=blog_date)


if __name__ == "__main__":
    app.run(debug=True)

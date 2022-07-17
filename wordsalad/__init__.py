# Flask development web server application factory for Word Salad flashcards project
#
# Reference: https://flask.palletsprojects.com/en/2.1.x/tutorial/factory/
#
# Import Flask, template, reverse URL class
from flask import Flask, render_template, url_for

import os

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'wordsalad.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Set root URL to index page
    @app.route('/')
    @app.route('/index.html')
    def index():
        return render_template('index.html')

    return app


#Create Database as flashcards.db
#dbName = "flashcards.db"
#sql = createDB.getSQL(".\dbScripts\MySQLCreate.sql")
#createDB.createDB(dbName, sql)
#print('Database', dbName, "created successfully")

#Populate tables with decks in Decks folder
#decks = ["GRE_vocab.csv", "LSAT_vocab.csv","SAT_vocab.csv"]
#initialPopulate.addWordSaladSuperUser("flashcards.db")
#for deck in decks:
#    initialPopulate.populateCards("flashcards.db", deck)
#    print(deck, "used to successfully populate tables")

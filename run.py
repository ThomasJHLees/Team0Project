import os
from unicodedata import name
# from flask import Flask
from wordsalad import create_app 

app = create_app()

if __name__== "__main_":
    app.run()
from flask import Flask
import os

# Make our app named app.
app = Flask(__name__)

# Imports the routes module where our pages are being created.
from app import routes
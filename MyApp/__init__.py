from flask import Flask

app = Flask(__name__)
print(__name__)
from MyApp import routes



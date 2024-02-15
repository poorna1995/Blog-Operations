from flask import Flask, jsonify, request

app = Flask(__name__)
app.db = "hello_world_db"

from app.routes.routes import *
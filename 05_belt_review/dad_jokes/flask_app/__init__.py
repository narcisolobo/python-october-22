from flask import Flask, render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'b8166a24cdedd39817729f2f14e4a4f5c252ceaf0aa85b8ed7ba247a0d399164'
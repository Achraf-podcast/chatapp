from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, EmailField
import random

def encrypt(text):
    encrypted_text = ""
    for c in text:
        try:
            encrypted_text += other[1][0][c.lower()]
        except:
            try:
                encrypted_text += random.choice([amazigh[0], arab[0], other[0][0], hind[0], nums[0]])[c.lower()]
            except:
                encrypted_text += c
    return encrypted_text[::-1]


amazigh = [{'a': 'ⴰ', 'b': 'ⴱ', 'c': 'ⴳ', 'd': 'ⴴ', 'e': 'ⴵ', 'f': 'ⴶ', 'g': 'ⴷ', 'h': 'ⵣ', 'i': 'ⵡ', 'j': 'ⴻ', 'k': 'ⴼ', 'l': 'ⴽ', 'm': 'ⴾ', 'n': 'ⵀ', 'o': 'ⵃ', 'p': 'ⵄ', 'q': 'ⵅ', 'r': 'ⵇ', 's': 'ⵉ', 't': 'ⵊ', 'u': 'ⵍ', 'v': 'ⵎ', 'w': 'ⵢ', 'x': 'ⵙ', 'y': 'ⵚ', 'z': 'ⵖ'}, {'ⴰ': 'a', 'ⴱ': 'b', 'ⴳ': 'c', 'ⴴ': 'd', 'ⴵ': 'e', 'ⴶ': 'f', 'ⴷ': 'g', 'ⵣ': 'h', 'ⵡ': 'i', 'ⴻ': 'j', 'ⴼ': 'k', 'ⴽ': 'l', 'ⴾ': 'm', 'ⵀ': 'n', 'ⵃ': 'o', 'ⵄ': 'p', 'ⵅ': 'q', 'ⵇ': 'r', 'ⵉ': 's', 'ⵊ': 't', 'ⵍ': 'u', 'ⵎ': 'v', 'ⵢ': 'w', 'ⵙ': 'x', 'ⵚ': 'y', 'ⵖ': 'z'}]
arab = [{'a': 'ج', 'b': 'ط', 'c': 'ظ', 'd': 'ز', 'e': 'ك', 'f': 'ح', 'g': 'خ', 'h': 'م', 'i': 'و', 'j': 'ة', 'k': 'ن', 'l': 'ص', 'm': 'ع', 'n': 'ت', 'o': 'ى', 'p': 'ء', 'q': 'ئ', 'r': 'ذ', 's': 'غ', 't': 'ف', 'u': 'ل', 'v': 'ؤ', 'w': 'ر', 'x': 'ب', 'y': 'ق', 'z': 'ث'}, {'ج': 'a', 'ط': 'b', 'ظ': 'c', 'ز': 'd', 'ك': 'e', 'ح': 'f', 'خ': 'g', 'م': 'h', 'و': 'i', 'ة': 'j', 'ن': 'k', 'ص': 'l', 'ع': 'm', 'ت': 'n', 'ى': 'o', 'ء': 'p', 'ئ': 'q', 'ذ': 'r', 'غ': 's', 'ف': 't', 'ل': 'u', 'ؤ': 'v', 'ر': 'w', 'ب': 'x', 'ق': 'y', 'ث': 'z'}]
other = [[{'a': '&', 'b': 'é', 'c': '"', 'd': "'", 'e': '(', 'f': '-', 'g': 'è', 'h': '_', 'i': 'ç', 'j': 'à', 'k': ')', 'l': '=', 'm': '*', 'n': '$', 'o': '^', 'p': 'ù', 'q': '!', 'r': ':', 's': ';', 't': ',', 'u': '£', 'v': '<', 'w': '>', 'x': '+', 'y': '/', 'z': '\\'}, {'&': 'a', 'é': 'b', '"': 'c', "'": 'd', '(': 'e', '-': 'f', 'è': 'g', '_': 'h', 'ç': 'i', 'à': 'j', ')': 'k', '=': 'l', '*': 'm', '$': 'n', '£': 'u', '^': 'o', 'ù': 'p', '!': 'q', ':': 'r', ';': 's', ',': 't', '<': 'v', '>': 'w', '+': 'x', '/': 'y', '\\': 'z'}], [{'&': '😀', 'é': '😁', '"': '😂', "'": '🤣', '(': '😃', '-': '😄', 'è': '😅', '_': '😆', 'ç': '😉', 'à': '😊', ')': '😋', '=': '😎', '*': '😍', '$': '😘', '^': '🥰', 'ù': '😗', '!': '😙', ':': '😚', ';': '🙂', ',': '🤗', '<': '🤩', '>': '🤔', '+': '🤨', '/': '😐', ' ': '😶', '\\': '😑', '0':'🤑', '1':'😲', '2':'🙁', '3':'😖', '4':'😞', '5':'😟', '6':'😤', '7':'😢', '8':'😭', '9':'😦'}, {'😀': '&', '😁': 'é', '😂': '"', '🤣': "'", '😃': '(', '😄': '-', '😅': 'è', '😆': '_', '😉': 'ç', '😊': 'à', '😋': ')', '😎': '=', '😍': '*', '😘': '$', '🥰': '^', '😗': 'ù', '😙': '!', '😚': ':', '🙂': ';', '🤗': ',', '🤩': '<', '🤔': '>', '🤨': '+', '😐': '/', '😶': ' ', '😑': '\\', '🤑': '0', '😲': '1', '🙁': '2', '😖': '3', '😞': '4', '😟': '5', '😤': '6', '😢': '7', '😭': '8', '😦': '9'}]]
hind = [{'a': 'ढ', 'b': 'ड', 'c': 'ठ', 'd': 'ट', 'e': 'ञ', 'f': 'प', 'g': 'झ', 'h': 'ज', 'i': 'छ', 'j': 'ो', 'k': '़', 'l': 'ा', 'm': 'ङ', 'n': 'घ', 'o': 'ग', 'p': 'ख', 'q': 'क', 'r': 'अ', 's': 'औ', 't': 'ऐ', 'u': 'ए', 'v': 'ऊ', 'w': 'उ', 'x': 'ई', 'y': 'इ', 'z': 'आ'}, {'ढ': 'a', 'ड': 'b', 'ठ': 'c', 'ट': 'd', 'ञ': 'e', 'प': 'f', 'झ': 'g', 'ज': 'h', 'छ': 'i', 'ो': 'j', '़': 'k', 'ा': 'l', 'ङ': 'm', 'घ': 'n', 'ग': 'o', 'ख': 'p', 'क': 'q', 'अ': 'r', 'औ': 's', 'ऐ': 't', 'ए': 'u', 'ऊ': 'v', 'उ': 'w', 'ई': 'x', 'इ': 'y', 'आ': 'z'}]
nums = [{'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7', 'i': '8', 'j': '9', 'k': '٠', 'l': '١', 'm': '٢', 'n': '٣', 'o': '٤', 'p': '٥', 'q': '٦', 'r': '٧', 's': '٨', 't': '٩', 'u': '一', 'v': '十', 'w': '九', 'x': '八', 'y': '七', 'z': '六'}, {'0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e', '5': 'f', '6': 'g', '7': 'h', '8': 'i', '9': 'j', '٠': 'k', '١': 'l', '٢': 'm', '٣': 'n', '٤': 'o', '٥': 'p', '٦': 'q', '٧': 'r', '٨': 's', '٩': 't', '一': 'u', '十': 'v', '九': 'w', '八': 'x', '七': 'y', '六': 'z'}]

class data(FlaskForm):
    fullname = StringField()
    username = StringField()
    email = EmailField()
    password = PasswordField()

class msg_form(FlaskForm):
    username = StringField()
    msg = StringField()
    date = StringField()

app = Flask(__name__)
app.config['SECRET_KEY'] = '&"vrfd"(jd$*^*m)'
msgs = []

@app.route('/', methods=['GET', 'POST'])
def main():
    form = data()
    if request.method == 'POST':
        fullname = encrypt(form.fullname.data)
        username = encrypt(form.username.data)
        email = encrypt(form.email.data)
        password = encrypt(form.password.data)

        with open('static\\database.db', 'ab') as db:
            db.write(bytes(fullname + '|', 'utf-8'))
            db.write(bytes(username + '|', 'utf-8'))
            db.write(bytes(email + '|', 'utf-8'))
            db.write(bytes(password + '|\n', 'utf-8'))

    return ""

@app.route('/database', methods=['GET', 'POST'])
def users():
    all = open('static\\database.db', 'rb').read()
    return all

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    form = msg_form()
    if request.method == 'POST':
        msgs.append({'username':encrypt(form.username.data), 'msg':encrypt(form.msg.data), 'date':encrypt(form.date.data)})

    return render_template('chat.html', msgs=msgs)

if __name__ == '__main__':
    app.run(debug=True)
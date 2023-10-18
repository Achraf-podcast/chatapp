from tkinter import *
from PIL import ImageTk, Image
import requests
from bs4 import BeautifulSoup
import lxml
from itertools import zip_longest
from tkinter import messagebox
import threading
import datetime
import time

amazigh = [{'a': 'ⴰ', 'b': 'ⴱ', 'c': 'ⴳ', 'd': 'ⴴ', 'e': 'ⴵ', 'f': 'ⴶ', 'g': 'ⴷ', 'h': 'ⵣ', 'i': 'ⵡ', 'j': 'ⴻ', 'k': 'ⴼ', 'l': 'ⴽ', 'm': 'ⴾ', 'n': 'ⵀ', 'o': 'ⵃ', 'p': 'ⵄ', 'q': 'ⵅ', 'r': 'ⵇ', 's': 'ⵉ', 't': 'ⵊ', 'u': 'ⵍ', 'v': 'ⵎ', 'w': 'ⵢ', 'x': 'ⵙ', 'y': 'ⵚ', 'z': 'ⵖ'}, {'ⴰ': 'a', 'ⴱ': 'b', 'ⴳ': 'c', 'ⴴ': 'd', 'ⴵ': 'e', 'ⴶ': 'f', 'ⴷ': 'g', 'ⵣ': 'h', 'ⵡ': 'i', 'ⴻ': 'j', 'ⴼ': 'k', 'ⴽ': 'l', 'ⴾ': 'm', 'ⵀ': 'n', 'ⵃ': 'o', 'ⵄ': 'p', 'ⵅ': 'q', 'ⵇ': 'r', 'ⵉ': 's', 'ⵊ': 't', 'ⵍ': 'u', 'ⵎ': 'v', 'ⵢ': 'w', 'ⵙ': 'x', 'ⵚ': 'y', 'ⵖ': 'z'}]
arab = [{'a': 'ج', 'b': 'ط', 'c': 'ظ', 'd': 'ز', 'e': 'ك', 'f': 'ح', 'g': 'خ', 'h': 'م', 'i': 'و', 'j': 'ة', 'k': 'ن', 'l': 'ص', 'm': 'ع', 'n': 'ت', 'o': 'ى', 'p': 'ء', 'q': 'ئ', 'r': 'ذ', 's': 'غ', 't': 'ف', 'u': 'ل', 'v': 'ؤ', 'w': 'ر', 'x': 'ب', 'y': 'ق', 'z': 'ث'}, {'ج': 'a', 'ط': 'b', 'ظ': 'c', 'ز': 'd', 'ك': 'e', 'ح': 'f', 'خ': 'g', 'م': 'h', 'و': 'i', 'ة': 'j', 'ن': 'k', 'ص': 'l', 'ع': 'm', 'ت': 'n', 'ى': 'o', 'ء': 'p', 'ئ': 'q', 'ذ': 'r', 'غ': 's', 'ف': 't', 'ل': 'u', 'ؤ': 'v', 'ر': 'w', 'ب': 'x', 'ق': 'y', 'ث': 'z'}]
other = [[{'a': '&', 'b': 'é', 'c': '"', 'd': "'", 'e': '(', 'f': '-', 'g': 'è', 'h': '_', 'i': 'ç', 'j': 'à', 'k': ')', 'l': '=', 'm': '*', 'n': '$', 'o': '^', 'p': 'ù', 'q': '!', 'r': ':', 's': ';', 't': ',', 'u': '£', 'v': '<', 'w': '>', 'x': '+', 'y': '/', 'z': '\\'}, {'&': 'a', 'é': 'b', '"': 'c', "'": 'd', '(': 'e', '-': 'f', 'è': 'g', '_': 'h', 'ç': 'i', 'à': 'j', ')': 'k', '=': 'l', '*': 'm', '$': 'n', '£': 'u', '^': 'o', 'ù': 'p', '!': 'q', ':': 'r', ';': 's', ',': 't', '<': 'v', '>': 'w', '+': 'x', '/': 'y', '\\': 'z'}], [{'&': '😀', 'é': '😁', '"': '😂', "'": '🤣', '(': '😃', '-': '😄', 'è': '😅', '_': '😆', 'ç': '😉', 'à': '😊', ')': '😋', '=': '😎', '*': '😍', '$': '😘', '^': '🥰', 'ù': '😗', '!': '😙', ':': '😚', ';': '🙂', ',': '🤗', '<': '🤩', '>': '🤔', '+': '🤨', '/': '😐', ' ': '😶', '\\': '😑', '0':'🤑', '1':'😲', '2':'🙁', '3':'😖', '4':'😞', '5':'😟', '6':'😤', '7':'😢', '8':'😭', '9':'😦'}, {'😀': '&', '😁': 'é', '😂': '"', '🤣': "'", '😃': '(', '😄': '-', '😅': 'è', '😆': '_', '😉': 'ç', '😊': 'à', '😋': ')', '😎': '=', '😍': '*', '😘': '$', '🥰': '^', '😗': 'ù', '😙': '!', '😚': ':', '🙂': ';', '🤗': ',', '🤩': '<', '🤔': '>', '🤨': '+', '😐': '/', '😶': ' ', '😑': '\\', '🤑': '0', '😲': '1', '🙁': '2', '😖': '3', '😞': '4', '😟': '5', '😤': '6', '😢': '7', '😭': '8', '😦': '9'}]]
hind = [{'a': 'ढ', 'b': 'ड', 'c': 'ठ', 'd': 'ट', 'e': 'ञ', 'f': 'प', 'g': 'झ', 'h': 'ज', 'i': 'छ', 'j': 'ो', 'k': '़', 'l': 'ा', 'm': 'ङ', 'n': 'घ', 'o': 'ग', 'p': 'ख', 'q': 'क', 'r': 'अ', 's': 'औ', 't': 'ऐ', 'u': 'ए', 'v': 'ऊ', 'w': 'उ', 'x': 'ई', 'y': 'इ', 'z': 'आ'}, {'ढ': 'a', 'ड': 'b', 'ठ': 'c', 'ट': 'd', 'ञ': 'e', 'प': 'f', 'झ': 'g', 'ज': 'h', 'छ': 'i', 'ो': 'j', '़': 'k', 'ा': 'l', 'ङ': 'm', 'घ': 'n', 'ग': 'o', 'ख': 'p', 'क': 'q', 'अ': 'r', 'औ': 's', 'ऐ': 't', 'ए': 'u', 'ऊ': 'v', 'उ': 'w', 'ई': 'x', 'इ': 'y', 'आ': 'z'}]
nums = [{'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7', 'i': '8', 'j': '9', 'k': '٠', 'l': '١', 'm': '٢', 'n': '٣', 'o': '٤', 'p': '٥', 'q': '٦', 'r': '٧', 's': '٨', 't': '٩', 'u': '一', 'v': '十', 'w': '九', 'x': '八', 'y': '七', 'z': '六'}, {'0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e', '5': 'f', '6': 'g', '7': 'h', '8': 'i', '9': 'j', '٠': 'k', '١': 'l', '٢': 'm', '٣': 'n', '٤': 'o', '٥': 'p', '٦': 'q', '٧': 'r', '٨': 's', '٩': 't', '一': 'u', '十': 'v', '九': 'w', '八': 'x', '七': 'y', '六': 'z'}]

def decrypt(text):
    decrypted_text = ""
    for c in text:
        try:
            decrypted_text += other[1][1][c]
        except:
            try:
                decrypted_text += arab[1][c]
            except:
                try:
                    decrypted_text += other[0][1][c]
                except:
                    try:
                        decrypted_text += amazigh[1][c]
                    except:
                        try:
                            decrypted_text += hind[1][c]
                        except:
                            try:
                                decrypted_text += nums[1][c]
                            except:
                                decrypted_text += c
    return decrypted_text

def extract_users():
    word = ""
    data = []
    users = []
    database = requests.get('http://127.0.0.1:5000/database')
    for info in database.iter_lines():
        for c in info.decode('utf-8'):
            if c == '\n':
                pass
            else:
                if c == '|':
                    data.append(word[::-1])
                    word = ""
                else:
                    word += c
        fullname = decrypt(data[0])
        username = decrypt(data[1])
        email = decrypt(data[2])
        password = decrypt(data[3])
        data = []
        users.append({'fullname':fullname, 'username':username, 'email':email, 'password':password})
    return users

def get_msgs():
    word = ""
    data = []
    msgs = []
    database = requests.get('http://127.0.0.1:5000/chat').content
    soup = BeautifulSoup(database, "lxml")
    all = soup.find_all("p")
    for info in all:
        for c in info.text:
            if c == '\n':
                pass
            else:
                if c == '|':
                    data.append(word[::-1])
                    word = ""
                else:
                    word += c
        username = decrypt(data[0])
        msg = decrypt(data[1])
        date = decrypt(data[2])
        data = []
        msgs.append({'username':username, 'msg':msg, 'date':date})
    return msgs

users = extract_users()
current_user = {}
y1 = 10
y2 = 10
y3 = 50
stop = False
num = len(get_msgs())

def chat():
    global current_user
    def show_msg(username, msg, date):
        global y1, y2, y3
        height = 75
        msg = '\n'.join(msg[i:i+85] for i in range(0, len(msg), 85))
        height += 14 * msg.count('\n')
        img4 = Image.open("Chatapp\\icons\\b_frame.png").resize((1097, height))
        b_frame = ImageTk.PhotoImage(img4)
        l = Label(frame, image=b_frame, bg='#eef7f1')
        l.image = b_frame
        l.pack()
        Label(frame, text=username, bg='#B4DEC3', font=('Calibri', 15)).place(x=10, y=y1)
        Label(frame, text=msg, bg='#B4DEC3', font=('Calibri', 15), fg='white').place(x=150, y=y2)
        Label(frame, text=date, bg='#B4DEC3', font=('Calibri', 10)).place(x=10, y=y3)
        y1 += 14 * msg.count('\n')
        y2 += 14 * msg.count('\n')
        y3 += 14 * msg.count('\n')
        y1 += 79
        y2 += 79
        y3 += 79

    def check():
        global num
        while stop == False:
            word = ""
            data = []
            msgs = BeautifulSoup(requests.get('http://127.0.0.1:5000/chat').content, "lxml").find_all("p")
            num = len(msgs)
            while len(msgs) == num:
                msgs = BeautifulSoup(requests.get('http://127.0.0.1:5000/chat').content, "lxml").find_all("p")
            try:
                num += 1
                for c in msgs[-1].text:
                    if c == '\n':
                        pass
                    else:
                        if c == '|':
                            data.append(word[::-1])
                            word = ""
                        else:
                            word += c
                username = data[0]
                username = decrypt(username)
                msg = data[1]
                msg = decrypt(msg)
                date = data[2]
                date = decrypt(date)
                data = []
                try:
                    show_msg(username, msg, date)
                except:
                    pass
                frame.update_idletasks()
                container.config(scrollregion=container.bbox("all"))
            except:
                pass

    def send_msg():
        msg = s1.get()
        if msg != "":
            date = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
            requests.post('http://127.0.0.1:5000/chat', data={'username':current_user['username'], 'msg':msg, 'date':date})
            s1.set('')
        else:
            pass

    def logout():
        global stop, num, y1, y2, y3
        stop = True
        num += 1
        y1 = 10
        y2 = 10
        y3 = 50
        current_user['username'] = ''
        wind.destroy()
        main()
    def on_enter(event):
        b1.config(fg='black')
    def on_leave(event):
        b1.config(fg='white')

    wind = Tk()
    wind.geometry("%dx%d+0+0" % (wind.winfo_screenwidth(), wind.winfo_screenheight()))
    wind.title('Chat room')
    wind.configure(background='#50b373')

    s1 = StringVar()

    img1 = ImageTk.PhotoImage(Image.open("Chatapp\\icons\\frame2.png"))
    img2 = Image.open("Chatapp\\icons\\t_input.png").resize((940, 40))
    t_input = ImageTk.PhotoImage(img2)
    img3 = ImageTk.PhotoImage(Image.open("Chatapp\\icons\\b_send.png"))

    Label(wind, text='Start Chatting', font=('Calibri', 25), bg='#50b373', fg='white').place(x=575, y=10)
    b1 = Button(wind, text='Log out', font=('Calibri', 25), bd=0, bg='#50b373', activebackground='#50b373', fg='white', activeforeground='black', command=logout)
    b1.place(x=10, y=0)
    b1.bind("<Enter>", on_enter)
    b1.bind("<Leave>", on_leave)

    Label(wind, image=img1, bg='#50b373').place(x=110, y=80)
    Label(wind, image=t_input, bg='#eef7f1').place(x=134, y=630)
    Entry(wind, bg='#B4DEC3', font=('Calibri', 16), width=84, bd=0, textvariable=s1).place(x=143, y=637)
    Button(wind, image=img3, bg='#eef7f1', bd=0, command=send_msg).place(x=1078, y=630)
    f1 = Frame(wind, bg='#50b373')
    scroll_y = Scrollbar(f1, orient=VERTICAL)
    container = Canvas(f1, bg='#eef7f1')
    scroll_y.config(command=container.yview)
    scroll_y.pack(side=RIGHT, fill=Y)
    container.configure(width=1097, height=520, yscrollcommand=scroll_y.set)
    frame = Frame(container)
    container.create_window((0, 0), window=frame, anchor=NW)
    f1.place(x=128, y=95)
    container.pack()

    for msg in get_msgs():
        show_msg(msg['username'], msg['msg'], msg['date'])
    try:
        threading.Thread(target=check).start()
    except:
        threading.Thread(target=check).start()

    frame.update_idletasks()
    container.config(scrollregion=container.bbox("all"))
    wind.mainloop()

def main():
    global current_user
    def login():
        username = s1.get()
        password = s2.get()

        error = True
        if username == '' or password == '':
            messagebox.showerror('Login', 'Please fill all fields.')
        else:
            for user in users:
                if username == user['username'] and password == user['password']:
                    current_user['username'] = user['username']
                    wind.destroy()
                    chat()
                    error = False
                elif username == user['username'] and password != user['password']:
                    messagebox.showerror('Login', 'This password is incorrect.')
                    error = False
                    s2.set('')
            if error:
                messagebox.showerror('Login', 'There is no account with this username.')
                s1.set('')
                s2.set('')

    def signup():
        global users
        fullname = s3.get()
        username = s4.get()
        email = s5.get()
        password1 = s6.get()
        password2 = s7.get()

        error = False
        if fullname == '' or username == '' or email == '' or password1 == '' or password2 == '':
            messagebox.showerror('Signup', 'Please fill all fields.')
        elif '@gmail.com' not in email:
            messagebox.showerror('Signup', 'Please enter a valid gmail.')
        elif len(username) > 12:
            messagebox.showerror('Signup', 'The username should be under or 12 characters.')
            s4.set('')
        elif len(password1) < 8:
            messagebox.showerror('Signup', 'The password should be more than 8 characters.')
            s6.set('')
            s7.set('')
        elif password1 != password2:
            messagebox.showerror('Signup', 'Please enter the same password.')
            s6.set('')
            s7.set('')
        else:
            for user in users:
                if username == user['username']:
                    messagebox.showinfo('Signup', 'This username already exist.')
                    error = True
                elif email == user['email']:
                    messagebox.showinfo('Signup', 'There is already an account with this gmail, you can login.')
                    error = True
                elif password1 == user['password']:
                    messagebox.showinfo('Signup', 'This password already exist. Choose another password.')
                    error = True
                    s6.set('')
                    s7.set('')
            if not error:
                requests.post('http://127.0.0.1:5000/', data={'fullname':fullname, 'username':username, 'email':email, 'password':password1})
                users = extract_users()
                s3.set('')
                s4.set('')
                s5.set('')
                s6.set('')
                s7.set('')
                messagebox.showinfo('Signup', 'Registred successfuly')

    def Input(text, image, bg, size, x1, y1, x2, y2, x3, y3):
        Label(wind, image=size, bg=bg).place(x=x1, y=y1)
        Label(wind, image=image, bg='#B4DEC3').place(x=x2, y=y2)
        Label(wind, text=text, bg='#B4DEC3', font=('Calibri', 12)).place(x=x3, y=y3)

    wind = Tk()
    wind.geometry("%dx%d+0+0" % (wind.winfo_screenwidth(), wind.winfo_screenheight()))
    wind.title('Login')
    wind.configure(background='#50b373')

    img1 = Image.open("Chatapp\\icons\\frame1.png").resize((1100, 600))
    img2 = Image.open("Chatapp\\icons\\b_input.png").resize((400, 70))
    img3 = Image.open("Chatapp\\icons\\login.png").resize((300, 60))
    img4 = Image.open("Chatapp\\icons\\user.png").resize((50, 50))
    img5 = Image.open("Chatapp\\icons\\lock.png").resize((50, 50))
    img6 = Image.open("Chatapp\\icons\\signup.png").resize((300, 60))
    img7 = Image.open("Chatapp\\icons\\arrow.png").resize((100, 65))
    img8 = Image.open("Chatapp\\icons\\s_input.png").resize((200, 70))
    img9 = Image.open("Chatapp\\icons\\mail.png").resize((50, 50))

    frame = ImageTk.PhotoImage(img1)
    b_input = ImageTk.PhotoImage(img2)
    s_input = ImageTk.PhotoImage(img8)
    submit1 = ImageTk.PhotoImage(img3)
    submit2 = ImageTk.PhotoImage(img6)
    user = ImageTk.PhotoImage(img4)
    lock = ImageTk.PhotoImage(img5)
    arrow = ImageTk.PhotoImage(img7)
    mail = ImageTk.PhotoImage(img9)

    s1 = StringVar()
    s2 = StringVar()
    s3 = StringVar()
    s4 = StringVar()
    s5 = StringVar()
    s6 = StringVar()
    s7 = StringVar()

    Label(wind, image=frame, bg='#50b373').place(x=130, y=50)
    Label(wind, text='Login to continue', bg='#035821', fg='white', font=('Calibri', 50)).place(x=200, y=100)
    Label(wind, text='do not have account ?', bg='#035821', fg='white', font=('Calibri', 20)).place(x=200, y=180)
    Label(wind, image=arrow, bg='#035821').place(x=583, y=173)

    Input('Username', user, '#035821', b_input, 200, 270, 536, 275, 230, 272)
    Entry(wind, bg='#B4DEC3', font=('Calibri', 20), width=23, bd=0, textvariable=s1).place(x=211, y=297)

    Input('Password', lock, '#035821', b_input, 200, 370, 536, 375, 230, 372)
    Entry(wind, bg='#B4DEC3', font=('Calibri', 20), width=23, bd=0, show='*', textvariable=s2).place(x=211, y=397)

    Button(wind, image=submit1, bg='#035821', activebackground='#035821', activeforeground='#03ff15', bd=0, command=login).place(x=253, y=500)

    Frame(wind, height=500, width=5).place(x=690, y=110)

    Label(wind, text='Sign-up', bg='#035821', fg='white', font=('Calibri', 50)).place(x=850, y=100)

    Input('Full name', None, '#035821', s_input, 720, 230, 855, 235, 750, 232)
    Entry(wind, bg='#B4DEC3', font=('Calibri', 20), width=13, bd=0, textvariable=s3).place(x=731, y=257)

    Input('Username', user, '#035821', s_input, 923, 230, 1058, 235, 953, 232)
    Entry(wind, bg='#B4DEC3', font=('Calibri', 20), width=9, bd=0, textvariable=s4).place(x=931, y=257)

    Input('Gmail', mail, '#035821', b_input, 720, 310, 1056, 315, 750, 312)
    Entry(wind, bg='#B4DEC3', font=('Calibri', 20), width=23, bd=0, textvariable=s5).place(x=731, y=337)

    Input('Create Password', lock, '#035821', s_input, 720, 390, 855, 395, 750, 392)
    Entry(wind, bg='#B4DEC3', font=('Calibri', 20), width=9, bd=0, show='*', textvariable=s6).place(x=731, y=417)

    Input('Confirm Password', lock, '#035821', s_input, 923, 390, 1058, 395, 948, 392)
    Entry(wind, bg='#B4DEC3', font=('Calibri', 20), width=9, bd=0, show='*', textvariable=s7).place(x=931, y=417)

    Button(wind, image=submit2, bg='#035821', activebackground='#035821', activeforeground='#03ff15', bd=0, command=signup).place(x=773, y=500)

    wind.mainloop()

main()
stop = True
num += 1

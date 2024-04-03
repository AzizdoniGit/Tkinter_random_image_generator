from tkinter import *
from PIL import ImageTk, Image
import requests
import json
from io import BytesIO


def fetch_random_image():
    response = requests.get(api_url)
    if response.status_code == requests.codes.ok:
        data = json.loads(response.text)
        img_url = data['urls']['regular']
        img_response = requests.get(img_url)
        img = Image.open(BytesIO(img_response.content))
        img = img.resize((480, 400))
        photo = ImageTk.PhotoImage(img)
        label.configure(image=photo)
        label.photo = photo
    else:
        print("Error:", response.status_code, response.text)


root = Tk()
root.title('Random Tkinter Images (Unsplash))')
root.geometry('1200x700+400+180')
root.resizable(False, False)
root.config(bg='black', pady=40)

access_key = 'Ybl8umC1OveJMdYBbN544KXr3qjYASdtY8yQ7ZlKwS4'
api_url = f'https://api.unsplash.com/photos/random/?client_id={access_key}'
response = requests.get(api_url)

if response.status_code == requests.codes.ok:
    data = json.loads(response.text)
    img_url = data['urls']['raw']
    img_response = requests.get(img_url)
    img = Image.open(BytesIO(img_response.content))
    img = img.resize((480, 400))
    photo = ImageTk.PhotoImage(img)
    label = Label(root, image=photo, width=480, height=400)
    label.photo = photo
    label.pack()
else:
    print("Error:", response.status_code, response.text)

btn_randomiser = Button(text="Click", width=10, height=2, relief="groove", command=fetch_random_image)
btn_randomiser.pack()

root.mainloop()

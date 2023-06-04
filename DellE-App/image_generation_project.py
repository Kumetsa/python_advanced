import os
import re
import urllib.request
from io import BytesIO
from PIL import Image, ImageTk
import openai
import tkinter as tk
import random

openai.api_key = "PUT_KEY_HERE"
MEDIA_FOLDER = "images/"


def get_image_url():
    response = openai.Image.create(
        prompt=input_field.get(),  # this will take whatever we write in the field and send it as request
        n=1,
        size="256x256"
    )
    image_url = response['data'][0]['url']

    return image_url


def covert_to_image_object(image_url):
    with urllib.request.urlopen(image_url) as url:
        image_data = url.read()

    image_stream = BytesIO(image_data)  # Това е информацията за снимката(не както можем да я видим) просто е в паметта
    image = Image.open(image_stream)

    return image


def display_image(image):
    tk_image = ImageTk.PhotoImage(image)  # създаваме снимката като реален обект

    image_label.configure(image=tk_image)
    image_label.image = tk_image  # за да не изтрие снимката, тъй като има garbage collector


def save_image(image, path):
    while os.path.isfile(path):
        image_name = re.match(r"images/(.* .?)\.jpg", path[1])
        new_name = image_name + str(random.randint(1, 1_000_000))
        path = path.replace(image_name, new_name)

    image.save(path)


def render_image():
    global save_button

    try:
        save_button.destroy()

        image_url = get_image_url()
        image_name = "_".join(input_field.get().split()) + ".jpg"

        input_field.delete(0, tk.END)

        image = covert_to_image_object(image_url)

        display_image(image)

        save_button = tk.Button(
            window,
            text="Save",
            height=1,
            command=lambda: save_image(image, os.path.join(MEDIA_FOLDER, image_name))
        )

        save_button.place(x=350, y=17)

    except openai.error.InvalidRequestError:
        error_label = tk.Label(window, text="Prompt cannot be empty!", fg="red")
        error_label.place(x=175, y=50)
    # else:
    #     display_image(image_url)


window = tk.Tk()
window.title("Best image generator")  # name of window
window.geometry("500x300")  # size of window

image_label = tk.Label(window)
image_label.place(y=125, x=75)

input_field = tk.Entry(window)  # input field
input_field.place(x=165, y=20)  # place of the input field

generate_button = tk.Button(window, text="Create", height=1,
                            command=render_image)  # funcion is placed without (), or we use lambda x: render_image(
# parameters)
generate_button.place(x=300, y=17)

save_button = tk.Button(window, text="Save", height=1)

window.mainloop()

import urllib.request
from io import BytesIO
from PIL import Image, ImageTk
import openai
import tkinter as tk

openai.api_key = "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"


def get_image_url():
    response = openai.Image.create(
        prompt=input_field.get(),  # this will take whatever we write in the field and send it as request
        n=1,
        size="256x256"
    )
    image_url = response['data'][0]['url']

    return image_url


def display_image(image_url):
    with urllib.request.urlopen(image_url) as url:
        image_data = url.read()

    image_stream = BytesIO(image_data)  # Това е информацията за снимката(не кактоможем да я видим) просто е в паметта

    image = ImageTk.PhotoImage(Image.open(image_stream))  # създаваме снимката като реален обект
    image_label.configure(image=image)
    image_label.image = image  # за да не изтрие снимката, тъй като има garbage collector


def render_image():
    try:
        image_url = get_image_url()
        input_field.delete(0, tk.END)
    except openai.error.InvalidRequestError:
        error_label = tk.Label(window, text="Prompt cannot be empty!", fg="red")
        error_label.place(x=175,y=50)
    else:
        display_image(image_url)


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

window.mainloop()

import tkinter as tk

from PIL import Image, ImageTk

from module.logger import logger
from submodule.AlasPlana.plana import Plana


def open_image():
    image = Image.open("./submodule/AlasPlana/assets/sc.png")
    global original_image, img
    img = ImageTk.PhotoImage(image)
    original_image = image.copy()


def on_click(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y
    logger.info("pressed: " + str(start_x) + " " + str(start_y))


def on_release(event):
    end_x = max(min(1280, event.x), 0)
    end_y = max(min(720, event.y), 0)
    global lx, rx, ly, ry
    lx, rx = min(start_x, end_x), max(start_x, end_x)
    ly, ry = min(start_y, end_y), max(start_y, end_y)
    logger.info("released: " + str(end_x) + " " + str(end_y))

    canvas.create_rectangle(0, 0, lx, 720, fill="black")
    canvas.create_rectangle(rx, 0, 1280, 720, fill="black")
    canvas.create_rectangle(lx, 0, rx, ly, fill="black")
    canvas.create_rectangle(lx, ry, rx, 720, fill="black")


def crop():
    cropped_image = original_image.crop((lx, ly, rx, ry))
    width, height = original_image.size
    black_image = Image.new('RGB', (width, height), (0, 0, 0))
    black_image.paste(cropped_image, (start_x, start_y))

    black_image.save("./submodule/AlasPlana/assets/sc_croped.png")


def clear_selection():
    canvas.delete("all")
    canvas.create_image(0, 0, image=img, anchor="nw")


def capture_screenshot():
    im = Image.fromarray(plana.device.screenshot())
    im.save("./submodule/AlasPlana/assets/sc.png")
    return im


plana = Plana()
capture_screenshot()
app = tk.Tk()
app.title("Photoshop Too Expensive")
app.geometry("1300x800")
open_image()

canvas = tk.Canvas(app, width=1280, height=720)
canvas.place(x=5, y=5)
clear_selection()
logger.hr("Entered", level=0)

canvas.bind("<ButtonPress-1>", on_click)
canvas.bind("<ButtonRelease-1>", on_release)

clear_button = tk.Button(app, text="Clear Selection", command=clear_selection)
clear_button.place(x=440, y=740)

crop_button = tk.Button(app, text="Crop", command=crop)
crop_button.place(x=540, y=740)

app.mainloop()

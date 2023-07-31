import os.path
import tkinter as tk
from PIL import Image, ImageTk
from module.logger import logger
from submodule.AlasPlana.module.config.config import PlanaConfig


class PlanaCapTool:
    canvas = None
    start_x = 0
    start_y = 0
    original_image = None
    img = None
    full_img_name = "sc.png"
    cropped_img_name = "sc_croped.png"
    app = None

    def __init__(self, config: PlanaConfig, device):
        self.config = config
        self.device = device

    def yeah(self):
        print("yeah")

    def capture_screenshot(self):
        im = Image.fromarray(self.device.screenshot())
        logger.info(im)
        if self.config.CapTool_SaveUncroppedImage:
            im.save(os.path.join(self.config.CapTool_SavedPath, self.full_img_name))
        self.img = ImageTk.PhotoImage(im)
        self.original_image = im.copy()

    def crop(self):
        cropped_image = self.original_image.crop((lx, ly, rx, ry))
        width, height = self.original_image.size
        black_image = Image.new('RGB', (width, height), (0, 0, 0))
        black_image.paste(cropped_image, (self.start_x, self.start_y))

        black_image.save(os.path.join(self.config.CapTool_SavedPath, self.cropped_img_name))
        if self.config.CapTool_CloseWindowAfterCropping:
            self.app.destroy()

    def on_click(self, event):
        self.start_x = event.x
        self.start_y = event.y
        logger.info("pressed: " + str(self.start_x) + " " + str(self.start_y))

    def on_release(self, event):
        end_x = max(min(1280, event.x), 0)
        end_y = max(min(720, event.y), 0)
        global lx, rx, ly, ry
        lx, rx = min(self.start_x, end_x), max(self.start_x, end_x)
        ly, ry = min(self.start_y, end_y), max(self.start_y, end_y)
        logger.info("released: " + str(end_x) + " " + str(end_y))

        self.canvas.create_rectangle(0, 0, lx, 720, fill="black")
        self.canvas.create_rectangle(rx, 0, 1280, 720, fill="black")
        self.canvas.create_rectangle(lx, 0, rx, ly, fill="black")
        self.canvas.create_rectangle(lx, ry, rx, 720, fill="black")

    def clear_selection(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.img, anchor="nw")

    def cap(self):
        self.config.bind('PlanaCapTool')
        self.app = tk.Tk()
        self.capture_screenshot()

        self.app.title("Photoshop Too Expensive")
        self.app.geometry("1300x800")

        self.canvas = tk.Canvas(self.app, width=1280, height=720)
        self.canvas.place(x=5, y=5)
        self.clear_selection()
        logger.hr("Entered", level=0)

        self.canvas.bind("<ButtonPress-1>", self.on_click)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        clear_button = tk.Button(self.app, text="Clear Selection", command=self.clear_selection)
        clear_button.place(x=440, y=740)

        crop_button = tk.Button(self.app, text="Crop", command=self.crop)
        crop_button.place(x=540, y=740)

        self.app.mainloop()

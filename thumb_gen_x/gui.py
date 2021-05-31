import tkinter as tk
import tkinter.ttk as ttk

from datetime   import datetime
from tkinter    import colorchooser
from tkinter.filedialog import askopenfilename
from PIL        import Image, ImageTk

from .worker    import Generator

class GUI:
    def __init__(self, root):
        self.root = root
        self.filename = None
        self.bg_color = "#000"
        self.font_color = "#fff"
        self.image_quality = 100

        self.compose_frames()
        self.app_main()
        self.boxes()
        self.buttons()
        self.configs()
        self.output_image()

    def boxes(self):
        self.file_path()
        self.custom_text_box()
        self.log_area_box()

    def buttons(self):
        self.button_open_file()
        self.button_run()

    def configs(self):
        self.setImageQuality()
        self.setImageCount()
        self.setBGColor()
        self.setFontColor()

    def app_main(self):
        logo_image = Image.open("thumb_gen_x/images/logo.png")
        logo_image = logo_image.resize((200, 60))
        logo = ImageTk.PhotoImage(logo_image)
        logo_label = tk.Label(image=logo)
        logo_label.image = logo
        logo_label.place(x=5, y=5)

    def compose_frames(self):
        canvas_options = tk.Canvas(self.root, height=500, width=1000, bg="#fff")
        canvas_options.pack()
        canvas_options.place(x=0, y=0)
        canvas_options.create_rectangle(5, 80, 495, 165, width=2)
        canvas_options.create_rectangle(5, 165, 160, 232, width=2)
        canvas_options.create_rectangle(160, 165, 255, 232, width=2)
        canvas_options.create_rectangle(255, 165, 375, 232, width=2)
        canvas_options.create_rectangle(375, 165, 495, 232, width=2)
        canvas_options.create_rectangle(5, 232, 495, 280, width=2)

    def file_path(self):
        if self.filename is None:
            self.filename = "No file selected"
        self.file_dir = ttk.Combobox(self.root, height=0, width=75, font=(0, 8))
        self.file_dir.insert(tk.END, self.filename)
        self.file_dir.pack()
        self.file_dir.place(x=10, y=95)
        self.file_dir.config(state=tk.DISABLED)

    def choose_file(self):
        self.filename = askopenfilename()
        self.file_dir.config(state=tk.NORMAL)
        self.file_dir.set("")
        self.file_dir.insert(tk.END, self.filename)
        self.log("File selected " + self.filename)

    def button_open_file(self):
        btn_open_file=ttk.Button(self.root, text="Open file", command=self.choose_file)
        btn_open_file.place(x=10, y=130)

    def button_run(self):
        btn_run=ttk.Button(self.root, text="Run", command=self.run)
        btn_run.place(x=100, y=130)

    def custom_text_box(self):
        font_color_label = tk.Label(self.root, text="Custom text", bg="white")
        font_color_label.pack()
        font_color_label.place(x=10, y=240)

        self.custom_text_area = tk.Text(self.root, height=2, width=65, font=(0, 8))
        self.custom_text_area.insert(tk.END, "")
        self.custom_text_area.pack()
        self.custom_text_area.place(x=90, y=240)

    def getCustomTextInput(self):
        self.custom_text = self.custom_text_area.get("1.0","end")
        return self.custom_text

    def setImageQuality(self):
        image_quality_label = tk.Label(self.root, text="Image quality")
        image_quality_label.pack()
        image_quality_label.place(x=10, y=170)

        scl_image_quality = ttk.Scale(self.root,
                      from_=10,
                      to=100,
                      orient=tk.HORIZONTAL,
                      command=self.getImageQuality)
        scl_image_quality.pack()
        scl_image_quality.place(x=10, y=200)
        scl_image_quality.config(value=self.image_quality)

        self.image_q = tk.Text(self.root, height=0, width=5, font=(0, 8))
        self.image_q.insert(tk.END, self.image_quality)
        self.image_q.pack()
        self.image_q.place(x=112, y=203)
        self.image_q.config(state=tk.DISABLED)

    def getImageQuality(self, value=85):
        self.image_quality = int(float(value))
        self.image_q.config(state=tk.NORMAL)
        self.image_q.delete('1.0', tk.END)
        self.image_q.insert(tk.END, self.image_quality)
        self.image_q.config(state=tk.DISABLED)

    def setImageCount(self):
        image_quality_label = tk.Label(self.root, text="Images count", bg="white")
        image_quality_label.pack()
        image_quality_label.place(x=165, y=170)

        image_counter_options = []
        for i in range(3, 60):
            if i%3 == 0:
                image_counter_options.append(i)

        self.variable = tk.StringVar(self.root)
        imageCountOptions = ttk.OptionMenu(self.root, self.variable,
                                    "12",
                                    *image_counter_options)
        imageCountOptions.pack()
        imageCountOptions.place(x=165, y=200)

    def getImageCount(self):
        return int(self.variable.get())

    def setBGColor(self):
        bg_color_label = tk.Label(self.root, text="Background color", bg="white")
        bg_color_label.pack()
        bg_color_label.place(x=260, y=170)

        self.canvas_bgc = tk.Canvas(self.root, height=25, width=25, bg="#fff")
        self.canvas_bgc.pack()
        self.canvas_bgc.place(x=260, y=199)
        self.rectangle_bgc = self.canvas_bgc.create_rectangle(0, 0, 25, 25,
                                                              outline="#000",
                                                              fill="#000")

        button = ttk.Button(self.root, text="Choose color", command=self.selectBGColor)
        button.pack()
        button.place(x=290, y=200)

    def selectBGColor(self):
        bg_color_code = colorchooser.askcolor(title="Choose background color")
        self.canvas_bgc.itemconfig(self.rectangle_bgc, fill=bg_color_code[1])
        self.bg_color = bg_color_code[1]

    def setFontColor(self):
        font_color_label = tk.Label(self.root, text="Font color", bg="white")
        font_color_label.pack()
        font_color_label.place(x=380, y=170)

        self.canvas_fc = tk.Canvas(self.root, height=25, width=25, bg="#fff")
        self.canvas_fc.pack()
        self.canvas_fc.place(x=380, y=199)
        self.rectangle_fc = self.canvas_fc.create_rectangle(0, 0, 25, 25,
                                                            outline="#000",
                                                            fill="#fff")

        button = ttk.Button(self.root, text="Choose color", command=self.selectFontColor)
        button.pack()
        button.place(x=410, y=200)

    def selectFontColor(self):
        font_color_code = colorchooser.askcolor(title="Choose font color")
        self.canvas_fc.itemconfig(self.rectangle_fc, fill=font_color_code[1])
        self.font_color = font_color_code[1]

    def log_area_box(self):
        self.log_box = tk.Text(self.root, height=18, width=81, font=(0, 8))
        self.log_box.insert(tk.END, "")
        self.log_box.pack()
        self.log_box.place(x=5, y=290)
        self.log_box.config(state=tk.DISABLED)

    def log(self, status):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.log_box.config(state=tk.NORMAL)
        self.log_box.insert(tk.END, "\n[" + current_time + "]" + status)
        self.log_box.config(state=tk.DISABLED)

    def output_image(self, image=False):
        if not image:
            self.out_image = Image.open("thumb_gen_x/images/no-image-available.png")
            output_image = ImageTk.PhotoImage(self.out_image)
            t_image = tk.Label(image=output_image)
            t_image.image = output_image
            t_image.place(x=650, y=140)

        else:
            self.out_image = Image.open(image)
            self.out_image = self.out_image.resize((480, 480))
            output_image = ImageTk.PhotoImage(self.out_image)
            t_image = tk.Label(image=output_image)
            t_image.image = output_image
            t_image.place(x=500, y=5)

    def run(self):
        if self.filename == "No file selected":
            self.log("Please select a video before run!")
        elif not self.filename.endswith(".mkv") and not self.filename.endswith(".mp4"):
            self.log("This file type is not supported.")
        else:
            if self.getCustomTextInput() == "":
                self.custom_text = str(True)
            self.log("Processing: " + self.filename)
            app = Generator(video_path=self.filename,
                            custom_text=self.custom_text,
                            font_dir='',
                            bg_colour=self.bg_color,
                            font_colour=self.font_color,
                            images=self.getImageCount(),
                            image_quality=self.image_quality
                            )
            app.run()
            self.output_image(self.filename[:-3] + "jpg")
            self.log("Thumbnail saved in: " + self.filename[:-3] + "jpg")

import tkinter as tk
from PIL import Image, ImageTk


# fungsi untuk membuka gambar
def open_image():
    global img, img_label, img_display

    # membuka gambar dari file
    img = Image.open("sri.jpg")

    # menampilkan gambar pada GUI
    img_display = ImageTk.PhotoImage(img)
    img_label = tk.Label(image=img_display)
    img_label.pack()


# fungsi untuk memperbaiki kontras
def contrast():
    global img, img_display, img_label

    # mengubah gambar ke mode grayscale
    img = img.convert('L')

    # memperbaiki kontras
    contrast_factor = 1.5
    img = img.point(lambda x: x * contrast_factor)

    # menampilkan gambar pada GUI
    img_display = ImageTk.PhotoImage(img)
    img_label.config(image=img_display)


# fungsi untuk memperbaiki brightness
def brightness():
    global img, img_display, img_label

    # mengubah gambar ke mode grayscale
    img = img.convert('L')

    # memperbaiki brightness
    brightness_factor = 50
    img = img.point(lambda x: x + brightness_factor)

    # menampilkan gambar pada GUI
    img_display = ImageTk.PhotoImage(img)
    img_label.config(image=img_display)


# membuat GUI
root = tk.Tk()
root.title("Perbaikan Citra SRI")

# tombol untuk membuka gambar
open_button = tk.Button(text="Buka Gambar", command=open_image)
open_button.pack()

# tombol untuk memperbaiki kontras
contrast_button = tk.Button(text="Perbaiki Kontras", command=contrast)
contrast_button.pack()

# tombol untuk memperbaiki brightness
brightness_button = tk.Button(text="Perbaiki Brightness", command=brightness)
brightness_button.pack()

# menjalankan GUI
root.mainloop()
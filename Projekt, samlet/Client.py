import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

from Processing import process_image
from LabelReturn import label_return

# TEMPORARY CLIENT, anvendes til test
def open_image():
    filepath = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.png *.jpeg")]
    )

    if not filepath:
        return

    # Vis billede
    img = Image.open(filepath)
    img.thumbnail((300, 300))
    photo = ImageTk.PhotoImage(img)

    image_label.config(image=photo)
    image_label.image = photo

    # Billedanalyse
    generated_text = process_image(filepath)

    # Behandler resultat
    responsTekst, l1, l2, l3, l4 = label_return(generated_text)

    # Opdater GUI
    response_label.config(text=responsTekst)

    label1.config(text=l1 or "")
    label2.config(text=l2 or "")
    label3.config(text=l3 or "")
    label4.config(text=l4 or "")


# GUI

root = tk.Tk()
root.title("Image Recognition API Demo")

# Venstre side
left_frame = tk.Frame(root)
left_frame.pack(side="left", padx=10, pady=10)

image_label = tk.Label(left_frame)
image_label.pack()

response_label = tk.Label(
    left_frame,
    text="",
    wraplength=300,
    justify="left"
)
response_label.pack(pady=10)

# Højre side
right_frame = tk.Frame(root)
right_frame.pack(side="right", padx=10, pady=10)

tk.Label(right_frame, text="Genkendte labels:").pack(anchor="w")

label1 = tk.Label(right_frame)
label1.pack(anchor="w")

label2 = tk.Label(right_frame)
label2.pack(anchor="w")

label3 = tk.Label(right_frame)
label3.pack(anchor="w")

label4 = tk.Label(right_frame)
label4.pack(anchor="w")

# Knap
btn = tk.Button(
    root,
    text="Vælg billede",
    command=open_image
)
btn.pack(pady=10)

root.mainloop()
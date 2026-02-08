import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

from Processing import process_image
from LabelReturn import label_return

class ImageRecognitionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Recognition")
        self.root.geometry("900x500")
        self.root.configure(bg="#d9d9d9")

        #Main frames
        self.left_frame = tk.Frame(root, bg="#d9d9d9")
        self.left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="n")

        self.right_frame = tk.Frame(root, bg="#d9d9d9")
        self.right_frame.grid(row=0, column=1, padx=20, pady=20, sticky="n")

        #Image display
        self.image_label = tk.Label(
            self.left_frame,
            text="[Billede]",
            width=40,
            height=20,
            bg="white",
            relief="solid"
        )
        self.image_label.pack(pady=10)

        #knap til at load image
        self.load_button = tk.Button(
            self.left_frame,
            text="Vælg billede",
            command=self.load_image
        )
        self.load_button.pack(pady=5)

        #text respone
        self.respone_label = tk.Label(
            self.left_frame,
            text="",
            bg="#e6b3ff",
            width=50,
            height=3,
            wraplength=350,
            justify="left"
        )
        self.respone_label.pack(pady=15)

        #labels og accuracy
        self.label_boxes = []

        for _ in range(4):
            row_frame = tk.Frame(self.right_frame, bg="#d9d9d9")
            row_frame.pack(pady=8)

            label_box = tk.Label(
                row_frame,
                text="",
                width=25,
                height=2,
                relief="solid",
                bg="#c0e0e0"
            )
            label_box.pack(side="left", padx=5)

            acc_box = tk.Label(
                row_frame,
                text="accuracy%",
                width=12,
                height=2,
                relief="solid",
                bg="#bfbfbf"
            )
            acc_box.pack(side="left", padx=5)
            self.label_boxes.append((label_box, acc_box))

    #image load funktion
    def load_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.png *.jpeg")]
        )

        if not file_path:
            return

        #show image
        image = Image.open(file_path)
        image.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(image)

        self.image_label.configure(image=photo, text="")
        self.image_label.image = photo

        #image processing
        generated_text = process_image(file_path)

        #Behandling af resultat
        response_text, l1, l2, l3, l4 = label_return(generated_text)

        #update respons
        self.respone_label.config(text=response_text)

        labels = [l1, l2, l3, l4]

        #update labels
        for i, (label_box, acc_box) in enumerate(self.label_boxes):
            label_box.config(text=labels[i] or "")
            acc_box.config(text="")  # Accuracy senere

#run application
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageRecognitionGUI(root)
    root.mainloop()
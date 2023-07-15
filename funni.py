import tkinter
import random

alpha = 1
root = tkinter.Tk()

root.resizable(False, False)
root.title("funiiii")
root.geometry("500x500")

label = tkinter.Label(root, text="XD", font="250")
label.place(relx=0.5, rely=0.5, anchor="center")

def DoTheFunni():
    global alpha

    if alpha <= 0:
        alpha = 1

        width = random.randint(0, root.winfo_screenwidth() / 2)
        height = random.randint(0, root.winfo_screenheight() / 2)
        root.geometry(f"+{width}+{height}")
    else:
        alpha = alpha - 0.1
        root.wm_attributes("-alpha", alpha)

    root.after(100, DoTheFunni)

DoTheFunni()
root.mainloop()


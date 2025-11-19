import random
import time
import tkinter as tk
from tkinter import ttk, font




#Import all the texts
f = open('Texts', 'r', encoding="utf-8")
sz = []
szvolt = []
for line in f:
    line = line.replace("\n", "")
    sz.append(line)

def norm_strings(s):
    return s.replace(' ', '')
def count_mistakes(given, users_input):
        s_given = norm_strings(given)
        s_typed = norm_strings(users_input)

        # Make it lowercase
        s_given = s_given.lower()
        s_typed = s_typed.lower()

        mistakes = 0
        # Compare up to the length of the longer string
        max_len = max(len(s_given), len(s_typed))
        for i in range(max_len):
            char_given = s_given[i] if i < len(s_given) else ''
            char_typed = s_typed[i] if i < len(s_typed) else ''

            if char_given != char_typed:
                mistakes += 1
        return mistakes

""""    

for line in sz:
    num = random.randint(0, len(sz))
    Curr_line = sz[num]

    #start timer
    input("Press Enter to start and to finish too!")
    print(Curr_line)
    start_time = time.time()

    #user input
    typed = input("Type here: ")

    #end timer
    end_time = time.time()
    elapsed_time = end_time - start_time #Calculate the time it took to type the sentence


    mistakes = count_mistakes(Curr_line, typed)

    if mistakes == 0:
        print(f"You typed the sentence correctly!\n")
    else:
        print(f"You typed the sentence incorrectly. {mistakes} characters were wrong.\n")


"""


class MyGUI:
    def __init__(self):

        self.root = tk.Tk()
        self.root.config(bg="#023047")
        #self.root.geometry("800x600")
        self.root.attributes("-fullscreen", True)
        self.root.title("Typing Speed Test")


        style = ttk.Style()

        style.configure("sb.TButton",
                        font=('Garamond', 25),
                        foreground="#ffb703",
                        background="#023047",
                        justify="center")

        style.configure("title.TLabel",
                        font=('Garamond', 40),
                        foreground="#ffb703",
                        background="#023047",
                        justify="center")

        style.configure("TLabel",
                        font=('Garamond', 25),
                        foreground="#ffb703",
                        background="#023047",
                        justify="center")

        self.res_frame = ttk.Frame(self.root)


        self.Name = ttk.Label(self.root, font=('Arial', 40), text="Typing Speed Test", style="title.TLabel")
        self.Name.pack(padx=20, pady=50)

        self.center_frame = ttk.Frame(self.root)
        self.center_frame.place(relx=0.5, rely=0.5, anchor='center')  # Center the frame

        # Now add widgets to the frame
        self.label = ttk.Label(self.center_frame, font=('Arial', 25), text="You will get a sentence and you will have to type it as fast as you can!", wraplength=600)
        self.label.pack(pady=(0, 10))  # Add some space below the label

        self.start_button = ttk.Button(self.center_frame, text="Start", command=self.on_start_button, style="sb.TButton")
        self.start_button.pack()

        self.root.mainloop()

    def on_start_button(self):
        self.center_frame.place_forget()
        self.res_frame.place_forget()

        # Clear the contents of res_frame so the next results show fresh
        for widget in self.res_frame.winfo_children():
            widget.destroy()

        if hasattr(self, "cntext"):
            self.cntext.destroy()

        num = random.randint(0, len(sz) - 1)
        Curr_line = sz[num]
        sz.remove(sz[num])
        self.start_time = time.time()

        self.cntext = ttk.Label(self.root, text=f"{Curr_line}")
        self.cntext.pack(pady=10)

        self.user_input = ttk.Entry(self.root)
        self.user_input.bind("<Return>", self.on_end_button)
        self.user_input.pack(pady=10)

        #print("Button was clicked!")
        #self.start_button.pack(pady=10) #I should reappear it when i finished the text...



    def on_end_button(self, event):
        self.user_input.unbind("<Return>")
        self.user_input.pack_forget()
        end_time = time.time()
        elapsed_time = end_time - self.start_time  # Calculate the time it took to type the sentence

        self.res_frame.place(relx=0.5, rely=0.5, anchor='center', background="000000")  # Center the frame

        # Count the mistakes: Original text, user input
        mistakes = count_mistakes(self.cntext["text"], self.user_input.get())


        if mistakes == 0:
            #print(f"You typed the sentence correctly!\n")
            self.result = ttk.Label(self.res_frame, text=f"You typed the sentence correctly and your time is: {elapsed_time:.2f} seconds!")
            self.result.pack(pady=10)
        else:
            #print(f"You typed the sentence incorrectly. {mistakes} characters were wrong.\n")
            self.result = ttk.Label(self.res_frame, text=f"You typed the sentence incorrectly. {mistakes} characters were wrong and your time is: {elapsed_time:.2f} seconds!")
            self.result.pack(pady=10)


        self.start_button = ttk.Button(self.res_frame, text="Start", command=self.on_start_button, style="sb.TButton")
        self.start_button.pack(pady=10)

        self.close_button = ttk.Button(self.res_frame, text="Close", command=self.root.quit, style="sb.TButton")
        self.close_button.pack(pady=10)



MyGUI()
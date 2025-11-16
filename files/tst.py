import random
import time
import tkinter as tk
import tkinter.ttk as ttk
from cProfile import label
from mimetypes import inited



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
        self.root.config(bg="#fff")
        self.root.geometry("600x500")
        self.root.title("Typing Speed Test")

        self.Name = tk.Label(self.root, font=('Arial', 40), text="Typing Speed Test")
        self.Name.pack(padx=20, pady=50)

        self.center_frame = tk.Frame(self.root)
        self.center_frame.place(relx=0.5, rely=0.5, anchor='center')  # Center the frame

        # Now add widgets to the frame
        self.label = tk.Label(self.center_frame, font=('Arial', 20), text="You will get a sentence and you will have to type it as fast as you can!")
        self.label.pack(pady=(0, 10))  # Add some space below the label

        self.start_button = tk.Button(self.center_frame, text="Start", command=self.on_start_button)
        self.start_button.pack()


        self.root.mainloop()

    def on_start_button(self):
        self.center_frame.place_forget()  # This hides the button

        num = random.randint(0, len(sz))
        Curr_line = sz[num]
        self.start_time = time.time()

        cntext = tk.Label(self.root, text=f"{Curr_line}")
        cntext.pack(pady=10)

        self.user_input = tk.Entry(self.root)
        self.user_input.bind("<Return>", self.on_end_button)
        self.user_input.pack(pady=10)

        print("Button was clicked!")
        #self.start_button.pack(pady=10) #I should reappear it when i finished the text...



    def on_end_button(self, event):
        self.user_input.pack_forget()
        end_time = time.time()
        elapsed_time = end_time - self.start_time  # Calculate the time it took to type the sentence
        print(elapsed_time)

        self.label = tk.Label(self.root, font=('Arial', 20), text=f"Nice work! Your time is: {round(elapsed_time, 2)}")
        self.label.pack(pady=20, padx=20)

MyGUI()
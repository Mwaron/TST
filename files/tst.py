import random
import time

#Import all the texts
f = open('Texts', 'r')
sz = []
szvolt = []
for line in f:
    line = line.replace("\n", "")
    sz.append(line)

for line in sz:


    # Get a random line then BUMMM
    num = random.randint(0, len(sz))
    Curr_line = sz[num]
    print("Type the following sentence and press Enter when done:")
    ready = input("Press Enter to start!")
    print(Curr_line)

    start_time = time.time()
    user_input = input("Type here: ")
    end_time = time.time()
    elapsed_time = end_time - start_time #Calculate the time it took to type the sentence

    # Give the user_input the max lenght so it won't be an error in the future that it isn't long enough
    user_input += len(Curr_line)*" "

    wrong = 0
    for i, c in enumerate(Curr_line):
        if c == user_input[i]:
            pass
        else:
            wrong += 1

    if wrong == 0:
        print(f"You typed the sentence correctly! Your time is {elapsed_time:.2f}!\n")
    else:
        print(f"You typed the sentence incorrectly. {wrong} characters were wrong. Your time is {elapsed_time:.2f}!\n")


    #print(f"Az első: {sz[num]}; A következő: {sz[num+1]}")
    sz.remove(sz[num])
    #print(f"Az első: {sz[num]}; A következő: {sz[num+1]}")






import random
from tkinter import *

SAVE_LIST = []


def randomly_generating():
    try:
        is_full = False
        min = int(min_entry.get())
        max = int(max_entry.get())
        res = (random.randint(min, max))

        if res in SAVE_LIST:
            is_duplicated = True
        else:
            is_duplicated = False

        if not is_duplicated:
            SAVE_LIST.append(res)
        else:
            while is_duplicated:
                res = (random.randint(min, max))

                if res in SAVE_LIST:
                    is_duplicated = True
                else: is_duplicated = False
            SAVE_LIST.append(res)

        result_label.config(text=str(res))
        print(res)
        print(SAVE_LIST)
        status_label.config(text=' ')
        label.config(text=SAVE_LIST)




        if len(SAVE_LIST) == (max - min + 1):
            status_label.config(text='Good job! You have gotten all the numbers.')
            is_full = True
        if is_full is True:
            generate_button["state"] = "disable"
    except:
        status_label.config(text='Invalid Input')


def reset_everything():
    if len(SAVE_LIST) != 0:
        min_entry.delete(0, 'end')
        max_entry.delete(0, 'end')
        result_label.config(text=" ")
        label.config(text=" ")
        status_label.config(text=" ")
        SAVE_LIST.clear()
        generate_button["state"] = "normal"


window = Tk()
window.title('Random Number Generator')
window.geometry('550x550')
window.resizable(False, False)

frame1 = Frame(window, width=100, height=100)
frame2 = Frame(window, width=100, height=100)
frame3 = Frame(window, width=100, height=100)
frame4 = Frame(window, width=100, height=100)

min_label = Label(frame1, text="Lower Bound: ", font=10)
min_label.pack(side="left")

min_entry = Entry(frame1, width=20, font=10)
min_entry.pack(side="left")

max_label = Label(frame2, text='Upper Bound: ', font=10)
max_label.pack(side="left")

max_entry = Entry(frame2, font=10)
max_entry.pack(side="right")

frame1.pack(pady=20)
frame2.pack(pady=20)

generate_button = Button(frame3, text="Generate", command=randomly_generating, width=20, height=2, font=15)
generate_button.pack(pady=10)

result_label = Label(frame3, text='Result here!', font=10)
result_label.pack(pady=20)

status_label = Label(frame3, text='', font=20)
status_label.pack()

label = Label(frame3, text='List', font=20)
label.pack(pady = 5)

reset_btn = Button(frame4, text='Reset', command=reset_everything, width=10, height=400, font=7)
reset_btn.pack(pady = 10)

frame3.pack(pady=60, side='top')
frame4.pack()
window.mainloop()

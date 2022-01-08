import tkinter as tk
from Tab_convert import tab_converting


# add menu bars, choosing file faster, add image, convert 2 ways, add converting music sheet, more options


def clear():
    entry1.delete(0, 'end')
    print('cleared')


def converting():
    input_link = entry1.get()
    print(input_link)
    note_file = open(input_link, 'r', encoding='utf8')
    tab_file = open('C:\\Users\\tankh\\OneDrive\\Documents\\tab_file.txt', 'w', encoding='utf8')
    for word in note_file:
        word = word.strip()
        print(word)
        words = word.split(' ')
        result = tab_converting(words)
        sentence = ' '.join(result)
        print(sentence)
        tab_file.write(f"{sentence} \n")
    text.set("C:\\Users\\tankh\\OneDrive\\Documents\\tab_file.txt")


root = tk.Tk(className=" Music41Me")
root.geometry("600x300")
root.resizable(False, False)
label1 = tk.Label(root, text="Welcome to Converting Application", bg='Yellow').grid(row=0, column=0, padx=180, pady=20,
                                                                                    columnspan=4)
label2 = tk.Label(root, text="Drop full path of file here...").grid(row=1, column=0)
entry1 = tk.Entry(root, width=80)
entry1.grid(row=2, column=0, pady=20, padx=50, columnspan=2)
button1 = tk.Button(root, text="Convert", command=converting).grid(row=3, column=0)
text = tk.StringVar()
button2 = tk.Button(root, text="Clear", command=clear).grid(row=3, column=1)
entry2 = tk.Entry(root, bd=0, state="readonly", textvariable=text, width=80)
entry2.grid(row=4, column=0, columnspan = 2, padx =40)
root.mainloop()

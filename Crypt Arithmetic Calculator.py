from tkinter import *
from itertools import chain, permutations
from string import digits

root = Tk()
root.title('Crypt Arithmetic Calculator')
root.minsize(width=550, height=350)
root.maxsize(width=550, height=350)
lframe = Frame(root)
lframe.grid(padx=30, pady=30)
rframe = Frame(root)
rframe.grid(pady=10, padx=20, row=7, column=0)
text = Text(rframe, width=60, height=4)

"""
   Print a solution to the cryptarithm, if any exists.
   Arguments are the list of addends and the result of the sum.
   
   For example:
   >>> solve_cryptarithm(['SEND', 'MORE'], 'MONEY')
   SEND(9567) + MORE(1085) = MONEY(10652)

"""
def solve_cryptarithm(addends, result):

        letters = ''.join(set(chain(result, *addends)))
        initial_letters = ''.join(set(chain(result[0], (a[0] for a in addends))))
        for perm in permutations(digits, len(letters)):
                decipher_table = str.maketrans(letters, ''.join(perm))

                def decipher(s):
                        return s.translate(decipher_table)

                if '0' in decipher(initial_letters):
                        continue  # leading zeros not allowed
                deciphered_sum = sum(int(decipher(addend)) for addend in addends)
                if deciphered_sum == int(decipher(result)):
                        def fmt(s):
                                return f"{s}({decipher(s)})"
                        
                        text.insert(INSERT, ' + '.join(map(fmt, addends)))
                        text.insert(INSERT, ' = ')
                        text.insert(INSERT, fmt(result))
                        text.insert(END, "\n\n\nThank you\n\n")
                    
                        #print(" + ".join(map(fmt, addends)), "=", fmt(result))
                        break

        else:
                text.insert(INSERT, "No Solution Found")
                text.insert(END, "\n\n\nThank You\n\n")
                #print(" + ".join(addends), "=", result, " : no solution")

def lab():
        a = entry1.get()
        b = entry2.get()
        c = entry3.get()
        solve_cryptarithm([a, b],  c)




free = Label(root, text='      ')
free.grid(column=0, row=11)

label1 = Label(lframe, text='   Word 1 : ')
label1.grid(row=3, column=1, pady=7)

entry1 = Entry(lframe)
entry1.grid(row=3, column=2)




label2 = Label(lframe, text='+ Word 2 : ')
label2.grid(row=7, column=1, pady=7)

entry2 = Entry(lframe)
entry2.grid(row=7, column=2)



label3 = Label(lframe, text='= Word 3 : ')
label3.grid(row=11, column=1, pady=10)


entry3 = Entry(lframe)
entry3.grid(row=11, column=2)

button = Button(lframe, text='calculate', command=lab)
button.grid(row=15, column=2)





text.grid()
root.mainloop()

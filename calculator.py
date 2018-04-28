from tkinter import*
root =Tk()

root.title("Calculator")
operator=""
text_input=StringVar()

Tops = Frame(root,width=600,height=600, bg="light green",relief=SUNKEN)
Tops.pack()

def btnClick(number):
    global operator
    operator=operator +str(number)
    text_input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_input.set(operator)
def btnEqualsDisplay():
    global operator
    ans =str(eval(operator))
    text_input.set(ans)
    operator =""

display = Entry(Tops,font=('arial',20,'bold'),textvariable=text_input,bd=30,insertwidth=4
                ,bg="light green",justify='right')
display.grid(columnspan=4)

btn7 = Button(Tops,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
              text="7",bg="light green",command=lambda:btnClick(7)).grid(row=2,column=0)
btn8 = Button(Tops,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
              text="8",bg="light green",command=lambda:btnClick(8)).grid(row=2,column=1)
btn9 = Button(Tops,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
              text="9",bg="light green",command=lambda:btnClick(9)).grid(row=2,column=2)
Add = Button(Tops,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
              text="+",bg="light green",command=lambda:btnClick('+')).grid(row=2,column=3)


btn4 = Button(Tops,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
              text="4",bg="light green",command=lambda:btnClick(4)).grid(row=3,column=0)
btn5 = Button(Tops,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
              text="5",bg="light green",command=lambda:btnClick(5)).grid(row=3,column=1)
btn6 = Button(Tops,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
              text="6",bg="light green",command=lambda:btnClick(6)).grid(row=3,column=2)
Sub = Button(Tops,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
              text="-",bg="light green",command=lambda:btnClick('-')).grid(row=3,column=3)


btn1 = Button(Tops,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
              text="1",bg="light green",command=lambda:btnClick(1)).grid(row=4,column=0)
btn2 = Button(Tops,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
              text="2",bg="light green",command=lambda:btnClick(2)).grid(row=4,column=1)
btn3 = Button(Tops,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
              text="3",bg="light green",command=lambda:btnClick(3)).grid(row=4,column=2)
Mul = Button(Tops,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
              text="*",bg="light green",command=lambda:btnClick('*')).grid(row=4,column=3)


btn0 = Button(Tops,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
              text="0",bg="light green",command=lambda:btnClick(0)).grid(row=5,column=0)
btnC = Button(Tops,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
              text="C",bg="light green",command=lambda:btnClearDisplay()).grid(row=5,column=1)
equal = Button(Tops,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
              text="=",bg="light green",command=lambda:btnEqualsDisplay()).grid(row=5,column=2)
Div = Button(Tops,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
              text="/",bg="light green",command=lambda:btnClick('/')).grid(row=5,column=3)

root.mainloop()

#CREATING QUIZ PORTAL USING TKINTER
"""MODEL STRUCTURE:
1. MAIN GUI WINDOW:
1.A. INTRODUCTION
1.B. INTERACTING SUBJECT BARS WHICH WILL DIRECT TO RESPECTIVE WINDOWS

2. PYTHON GUI QUIZ:
2.A. SHOW QUESTIONS IN ONE PAGE WITH OPTIONS
2.B. ALL OPTIONS GRADED WITH CORRECT AS 1, WRONG AS 0.
2.C. CHECK ANSWERS FROM DATA FILE AFTER FORM IS SUBMITTED, AND CALCULATE MARKS.
2.D. SHOW RESULT: MARKS, TOTAL WRONG AND TOTAL RIGHT.
"""

"""COLOR REFERENCE
1. DARK BLUE= #2B2B52
2. PINK=#FFF7F7
3. GREEN= #51B59F
4. RED=#EF3220
5. BLUE=#397DC9
6. YELLOW=#FFF222
7. WHITE=#FFFFFF"""

import tkinter
from tkinter import *
from tkinter import messagebox as mb
import random
import soc

root=tkinter.Tk()
root.title("LeapLearn")
root.geometry("1000x600")
root.config(background="#FFF7F7")
root.resizable(0,0)

img1=PhotoImage(file="C:\\Users\\Admin\\Desktop\\LNG\\Leap@Learn.png")
img2=PhotoImage(file="C:\\Users\\Admin\\Desktop\\LNG\\rib.png")
img3=PhotoImage(file="C:\\Users\\Admin\\Desktop\\LNG\\MAC.png")
img4=PhotoImage(file="C:\\Users\\Admin\\Desktop\\LNG\\GRP.png")
bg1=PhotoImage(file="C:\\Users\\Admin\\Desktop\\LNG\\bg1.png")
bg2=PhotoImage(file="C:\\Users\\Admin\\Desktop\\LNG\\bg2.png")

ind=[]
user_ans=[]
def ma():
    global ques,opt,ans,img,head
    ques,opt,ans=soc.ma()
    head="Mental Ability"
    img=bg1
    quizpanel(head)

def eg():
    global ques,opt,ans,img,head
    ques,opt,ans=soc.eg()
    head="Grammar"
    img=bg2
    quizpanel(head)
    
def gen():
    global ind
    while(len(ind)<10):
        x=random.randint(0,15)
        if x in ind:
            continue
        else:
            ind.append(x)

def calc():
    global ind,user_ans,ans,score,t1,f1,f2

    count,score=0,0
    for i in ind:
        if user_ans[count]==ans[i]:
            score+=1
        count+=1
        
    submit=Button(
    t1,
    text="Submit",
    font=("Ink Journal",30),
    bg="#FFF7F7",
    fg="#2B2B52",
    border=2,
    relief=GROOVE,
    padx=10,
    command=lambda:showresult(),
    )
    submit.pack(side=BOTTOM, anchor=SE, padx=100)


def showresult():
    global correct,wrong,score
    correct=score
    wrong=10-score
    score=score*10
    reswindow()

def reswindow():
    global root, res
    global correct,wrong,score
    root.destroy()
    
    res=tkinter.Tk()
    res.title("LeapLearn_Result")
    res.geometry("1000x600")
    res.config(background="#FFF7F7")
    res.resizable(0,0)
    
    img6=PhotoImage(file="C:\\Users\\Admin\\Desktop\\LNG\\Leap@Learn.png")
    img7=PhotoImage(file="C:\\Users\\Admin\\Desktop\\LNG\\rib.png")

    hd=Label(
        res,
        text="Leap@Learn",
        font=("Jokerman",50),
        fg="#2B2B52",
        bg="#FFF7F7",
        image=img6,
        compound=RIGHT,
        justify=CENTER,
        )
    hd.pack(side=TOP,fill=X,anchor=N)

    hd1=Label(
        res,
        image=img7,
        bg="#FFF7F7",
        )
    hd1.pack(fill=X)
    
    hd3=Label(
        res,
        text="RESULT",
        font=("Ink Journal",50),
        fg="#2B2B52",
        bg="#FFF7F7",
        justify=CENTER,
        )
    hd3.pack()

    hd4=Label(
        res,
        text="Correct: {} \nWrong: {}\nScore: {}".format(correct,wrong,score),
        font=("Ink Journal",40),
        fg="#2B2B52",
        bg="#FFF7F7",
        justify=CENTER,
        )
    hd4.pack()

    res.mainloop()
    
def quizpanel(head):
    global t1,f1,f2,img
    t1=tkinter.Toplevel()
    t1.title(head)
    t1.geometry("1000x600")
    t1.config(background="#FFF7F7")
    t1.resizable(0,0)
    #QUIZ IMAGE BACK]
    l1=Label(
        t1,
        image=img,
        justify=CENTER,
        )
    l1.place(x=0,y=0)

    f1=LabelFrame(
        t1,
        bg="#2B2B52",
        width=900,
        height=600)
    f1.pack(side=TOP,expand=True,ipady=20)

    f2=LabelFrame(
        f1,
        bg="#2B2B52",
        width=900,
        height=400)
    f2.pack(side=BOTTOM,expand=True, fill=X,ipady=20)
    
    gen()
    quiz()

q=1
def selected():
    global radiovar,user_ans,ind,ans
    global lblq,r1,r2,r3,r4,q
    y=radiovar.get()
    user_ans.append(y)
    if q<10:
        lblq.config(text=ques[ind[q]])
        r1['text']=opt[ind[q]][0]
        r2['text']=opt[ind[q]][1]
        r3['text']=opt[ind[q]][2]
        r4['text']=opt[ind[q]][3]
        q+=1
    else:
       calc()

def quiz():
    global t1,f1,f2
    global radiovar
    global lblq,r1,r2,r3,r4
    
    lblq=Label(
        f1,
        text=ques[ind[0]],
        font=("Ink Journal",20),
        fg="#FFFFFF",
        bg="#2B2B52",
        width=700,
        justify="center",
        wraplength=500,
        )
    lblq.pack(fill=X,anchor=N)

    radiovar=IntVar()
    radiovar.set(-1)

    r1=Radiobutton(
        f2,
        text=opt[ind[0]][0],
        font=("Ink Journal",20),
        bg="#397DC9",
        fg="#FFFFFF",
        value=0,
        variable=radiovar,
        pady=10,
        padx=10,
        justify=CENTER,
        command=selected,
        )
    r1.pack(side=LEFT,anchor=N,padx=5,pady=50,expand=True)

    r2=Radiobutton(
        f2,
        text=opt[ind[0]][1],
        font=("Ink Journal",20),
        bg="#51B59F",
        fg="#FFFFFF",
        value=1,
        variable=radiovar,
        pady=10,
        padx=10,
        justify=CENTER,
        command=selected,
        )
    r2.pack(side=LEFT,anchor=N,padx=5,pady=50,expand=True)
    
    r3=Radiobutton(
        f2,
        text=opt[ind[0]][2],
        font=("Ink Journal",20),
        bg="#FFF222",
        fg="#FFFFFF",
        value=2,
        variable=radiovar,
        pady=10,
        padx=10,
        justify=CENTER,
        command=selected,
        )
    r3.pack(side=LEFT,anchor=N,padx=5,pady=50,expand=True)

    r4=Radiobutton(
        f2,
        text=opt[ind[0]][3],
        font=("Ink Journal",20),
        bg="#EF3220",
        fg="#FFFFFF",
        value=3,
        variable=radiovar,
        pady=10,
        padx=10,
        justify=CENTER,
        command=selected,
        )
    r4.pack(side=LEFT,anchor=N,padx=5,pady=50,expand=True)
    
#MAIN WINDOW

lbl1=Label(root,
           text="Leap@Learn",
           font=("Jokerman",50),
           fg="#2B2B52",
           image=img1,
           bg="#FFF7F7",
           compound=RIGHT,
           justify=CENTER,
           )
lbl1.pack(side=TOP,fill=X,anchor=N)

lbl2=Label(root,
           image=img2,
           bg="#FFF7F7",
           )
lbl2.pack(fill=X)

lbl4=Label(
    root,
    text="<<Learn To Grow>>",
    font=("Ink Journal",40),
    fg="#2B2B52",
    bg="#FFF7F7",
    justify=CENTER,
    )
lbl4.pack()

lbl3=Label(
    root,
    text="The first step of success is the eagerness to learn!\nTake your first step, Ace your subject> ",
    font=("Ink Journal",30),
    fg="#2B2B52",
    bg="#FFF7F7",
    )
lbl3.pack()

btn1=Button(
    root,
    text="Mental Ability",
    font=("Ink Journal",30),
    bg="#D6FAF0",
    fg="#2B2B52",
    image=img3,
    height=180,
    width=180,
    border=2,
    relief=GROOVE,
    compound=TOP,
    padx=10,
    command=ma
    ).pack(side=LEFT, anchor=S,padx=150)

btn2=Button(
    root,
    text="Grammar",
    font=("Ink Journal",30),
    bg="#D6FAF0",
    fg="#2B2B52",
    image=img4,
    height=180,
    width=180,
    border=2,
    relief=GROOVE,
    compound=TOP,
    padx=10,
    command=eg
    ).pack(side=RIGHT, anchor=S, padx=150)


root.mainloop()

#credits: "https://www.vectorstock.com/royalty-free-vector/grammar-concept-icon-vector-36259429"







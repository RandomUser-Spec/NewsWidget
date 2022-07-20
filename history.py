from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Quiz on History")
root.geometry("600x600")

question1_radioButton = StringVar(value = "0")

Question1 = Label(root, text = "Q1 : What is the 5th Amendment for the Bill of Rights?")
Question1.pack()
question1_r1 = Radiobutton(root, text = "Testifying against yourself is optional", variable=question1_radioButton, value = "yes")
question1_r1.pack()
question1_r2 = Radiobutton(root, text = "Quartering Soldiers are not allowed during times of peace", variable = question1_radioButton, value = "no")
question1_r2.pack()

question2_radioButton = StringVar(value = "0")

Question2 = Label(root, text = "Q2 : What is the 1st Amendment for the Bill of Rights?")
Question2.pack()
question2_r1 = Radiobutton(root, text = "Always Trialed By Jury", variable=question2_radioButton, value = "yes")
question2_r1.pack()
question2_r2 = Radiobutton(root, text = "Freedom of Speech", variable = question2_radioButton, value = "no")
question2_r2.pack()

question3_radioButton = StringVar(value = "0")

Question3 = Label(root, text = "Q3 : Who was the so called 'president' at the Convention")
Question3.pack()
question3_r1 = Radiobutton(root, text = "James Madison", variable=question3_radioButton, value = "yes")
question3_r1.pack()
question3_r2 = Radiobutton(root, text = "Wai Hein", variable = question3_radioButton, value = "no")
question3_r2.pack()

question4_radioButton = StringVar(value = "0")

Question4 = Label(root, text = "Q4 : What caused the Convention")
Question4.pack()
question4_r1 = Radiobutton(root, text = "Shay's Rebellion", variable=question4_radioButton, value = "yes")
question4_r1.pack()
question4_r2 = Radiobutton(root, text = "Revoloutionary War", variable = question4_radioButton, value = "no")
question4_r2.pack()

question5_radioButton = StringVar(value = "0")

Question5 = Label(root, text = "Q5 : What did the law say about slavery?")
Question5.pack()
question5_r1 = Radiobutton(root, text = "They would abolish it", variable=question5_radioButton, value = "yes")
question5_r1.pack()
question5_r2 = Radiobutton(root, text = "It would not be discussed until 1808", variable = question5_radioButton, value = "no")
question5_r2.pack()

question6_radioButton = StringVar(value = "0")

Question6 = Label(root, text = "Q6 : How does the executive branch keep the legislative branch in check?")
Question6.pack()
question6_r1 = Radiobutton(root, text = "The executive branch vetos the law", variable=question6_radioButton, value = "yes")
question6_r1.pack()
question6_r2 = Radiobutton(root, text = "The executive branch impeaches the veto", variable = question6_radioButton, value = "no")
question6_r2.pack()

def test_score():
    score = 0
    if question1_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question2_radioButton.get()=="no":
        score = score+20
        print(score)
    if question3_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question4_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question5_radioButton.get()=="no":
        score = score+20
        print(score)
    if question6_radioButton.get()=="yes":
        score = score+20
        print(score)
        
    if score <= 20:
        messagebox.showinfo("Report", "Please study some more")
    elif score > 20 and score <= 80:
        messagebox.showinfo("Report","Good Job, you can do better though!")
    else :
        messagebox.showinfo("Report","Excellent work!")
        
btn = Button(root, text = "Results", command = test_score)
btn.pack()
root.mainloop()
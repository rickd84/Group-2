import tkinter

root = tkinter.Tk()
root.title("Two factor authentication")

def forgotPass():
   questions = tkinter.Tk()
   questions.title("Security Questions")
   tkinter.Label(questions, text = "Please Answer the Following Questions").place(x=80, y=15)
   tkinter.Label(questions, text = "Question 1:").place(x=50, y=50)
   tkinter.Entry(questions).place(x=120, y=50)
   tkinter.Label(questions, text = "Question 2:").place(x=50, y=90) 
   tkinter.Entry(questions).place(x=120, y=90)
   tkinter.Button(questions, text="Submit", command = Number).place(x=160, y=120)
   questions.geometry("450x200")
   forgotPass.mainloop()

   
def Number():
   number = tkinter.Tk()
   number.title("Phone Number Identification")
   tkinter.Label(number, text = "Please input your phone-number").place(x=80, y=15)
   tkinter.Label(number, text = "Phone Number:").place(x=80, y=50)
   tkinter.Entry(number).place(x=120, y=50)
   number.geometry("450x200")
   number.mainloop()
   
   

tkinter.Label(root, text = "Welcome to our two factor authentication program").place(x=80, y=15)

tkinter.Label(root, text = "Email:").place(x=80, y=50)

tkinter.Entry(root).place(x=120, y=50)

tkinter.Label(root, text = "Password:").place(x=60, y=90) 

tkinter.Entry(root).place(x=120, y=90)

tkinter.Button(root, text="Login").place(x=120, y=120)
tkinter.Button(root, text="Forgot My Password", command = forgotPass).place(x=160, y=120)
root.geometry("400x200")
root.mainloop()
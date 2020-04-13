import tkinter
import random

root = tkinter.Tk()
root.title("Two factor authentication")

def forgotPass():
   questions = tkinter.Tk()
   random1 = random.randint(0,4)
   random2 = random.randint(0,4)
   q1 = tkinter.StringVar()
   q2 = tkinter.StringVar()
   
   questions.title("Security Questions")
   tkinter.Label(questions, text = "Please Answer the Following Questions").place(x=80, y=15)
   tkinter.Label(questions, text = question[random1]+":").place(x=50, y=50)
   question1 = tkinter.Entry(questions, textvariable = q1)
   question1.place(x = 50, y = 80)
   tkinter.Label(questions, text = question[random2]+":").place(x=50, y=90) 
   question2 = tkinter.Entry(questions, textvariable = q2)
   question2.place(x = 50, y = 110)
   tkinter.Button(questions, text="Submit", command = get_data).place(x=160, y=120)
   questions.geometry("450x200")
   forgotPass.mainloop() 
   
def get_data():
   question1_data = q1.get()
   question2_data = q2.get()
   if question1_data == answers[random1]:
      if question2_data == answers[random2]:
         print("Continue")
         Number()
      else:
         print("Incorrect")
   else:
      print("Try Again")        

   
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

question = ['What was the first book I ever read?', 'What was the first company I ever worked for?', 'What High School did my mother attend?', 'In which city was my mother born?', 'In which city was my father born?']
answers = ['Cather in the Rye', 'Hyland', 'John Marshall', 'Cleveland', 'Toronto']
root.mainloop()
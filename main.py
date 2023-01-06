from tkinter import *
def menu():
    global m_screen
    m_screen = Tk()
    m_screen.geometry("2000x2000")
    m_screen.configure(background="light green")
    m_screen.title("Account Login")
    Label(text="Choose from the buttons below", bg="blue", width="300", height="2", font=("Calibri", 36)).pack()
    Label(text="",bg="light green").pack()
    Button(text="Check Camera", height="2", width="20",activebackground="red",font=("Calibri",20)).pack()
    Label(text="",bg="light green").pack()
    Button(text="Capture Faces", height="2", width="20",activebackground="red",font=("Calibri",20)).pack()
    Label(text="",bg="light green").pack()
    Button(text="Train Image", height="2", width="20",activebackground="red",font=("Calibri",20)).pack()
    Label(text="",bg="light green").pack()
    Button(text="Recognize and Attendance", height="2", width="20",activebackground="red",font=("Calibri",20)).pack()
    m_screen.mainloop()
menu()

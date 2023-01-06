import csv

import cv2
import os
from tkinter import *

# counting the numbers


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False



# Take image function

def takeinput():

    global cap_screen
    cap_screen=Toplevel()
    cap_screen.title("Capture Faces")
    cap_screen.geometry("900x700")
    cap_screen.configure(background="white")
    Label(cap_screen,text="Please enter details below to Capture Faces", bg="deepskyblue",fg="white", width="300", height="2", font=("Times", 36,"bold"),bd=5,relief=GROOVE).pack()
    Label(cap_screen, text="",bg="white").pack()

    global Id
    global name
    global sem
    global branch
    global sec

    Id = StringVar()
    name = StringVar()
    sem= StringVar()
    branch= StringVar()
    sec =  StringVar()

    global Id_entry
    global name_entry
    global sem_entry
    global branch_entry
    global sec_entry

    Label(cap_screen, text="Enter your ID ",bg="white",font=("Calibri", 26)).pack()
    Id_entry = Entry(cap_screen, textvariable=Id)
    Id_entry.pack()

    Label(cap_screen, text="",bg="white").pack()
    Label(cap_screen, text="Enter Your name ",bg="white",font=("Calibri", 26)).pack()
    name_entry = Entry(cap_screen, textvariable=name)
    name_entry.pack()
    Label(cap_screen, text="",bg="white").pack()

    Label(cap_screen, text="Enter Your Semester ",bg="white",font=("Calibri", 26)).pack()
    sem_entry = Entry(cap_screen, textvariable=sem)
    sem_entry.pack()
    Label(cap_screen, text="",bg="white").pack()

    Label(cap_screen, text="Enter Your Section ",bg="white",font=("Calibri", 26)).pack()
    sec_entry = Entry(cap_screen, textvariable=sec)
    sec_entry.pack()
    Label(cap_screen, text="",bg="white").pack()

    Label(cap_screen, text="Enter Your Branch ",bg="white",font=("Calibri", 26)).pack()
    branch_entry = Entry(cap_screen, textvariable=branch)
    branch_entry.pack()
    Label(cap_screen, text="",bg="white").pack()

    Button(cap_screen, activebackground="Red",bg="gold",text="Capture", width=15, height=2,command=takeImages,font=("Calibri", 26)).pack()

def takeImages():

        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0

        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                #incrementing sample number
                sampleNum = sampleNum+1
                #saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage" + os.sep +name_entry.get() + "."+Id_entry.get() + '.' +
                            str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
                #display the frame
                cv2.imshow('frame', img)
            #wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is more than 60
            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id_entry.get() + " Name : " + name_entry.get()
        row = [Id_entry.get(), name_entry.get()]
        with open("StudentDetails"+os.sep+"StudentDetails.csv", 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()

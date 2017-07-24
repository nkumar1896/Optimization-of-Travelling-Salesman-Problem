from __future__ import print_function
from tkinter import *
import os
import subprocess
import tkinter.messagebox
from PIL import Image
from subprocess import check_call
import sys
from random import randint
import math
root = Tk()
shape = Canvas(root,width=1100,height=500,bg='#6495ED')
shape.pack()
variable1 = IntVar()
var = IntVar()
var2 = IntVar()
def runall():
    file = open("outtsp.txt")
    q = file.read()
    file.close()
    try:
        if (q < "0"):
            tkinter.messagebox.showwarning('Error', 'First enter Number of cities')
        else:
            file = open("GAtime.txt")
            p1 = file.read()
            file.close()
            file1 = open("SAtime.txt")
            p2 = file1.read()
            file1.close()
            file2 = open("DMtime.txt")
            p3 = file2.read()
            file2.close()
            file3 = open("distLP.txt")
            p4 = file3.read()
            file3.close()
            try:
                if p1<"0" or p2<"0" or p3<"0" or p4<"0" :
                    tkinter.messagebox.showwarning('Error', 'First run all the Algorithms')
                else:
                    file = open("GAdistance.txt")
                    data = file.read()
                    file.close()
                    Results = Label(root, text=data)
                    Results.pack()
                    Results.place(x=10, y=300, width=200,height=30)
                    file = open("GAtime.txt")
                    data = file.read()
                    file.close()
                    Results = Label(root, text=data)
                    Results.pack()
                    Results.place(x=10, y=330, width=200,height=30)
                    file = open("SAdistance.txt")
                    data = file.read()
                    file.close()
                    Results = Label(root, text=data)
                    Results.pack()
                    Results.place(x=300, y=300, width=200,height=30)
                    file = open("SAtime.txt")
                    data = file.read()
                    file.close()
                    Results = Label(root, text=data)
                    Results.pack()
                    Results.place(x=300, y=330, width=200,height=30)
                    file = open("DMdistance.txt")
                    data = file.read()
                    file.close()
                    Results = Label(root, text=data)
                    Results.pack()
                    Results.place(x=590, y=300, width=200,height=30)
                    file = open("DMtime.txt")
                    data = file.read()
                    file.close()
                    Results = Label(root, text=data)
                    Results.pack()
                    Results.place(x=590, y=330, width=200,height=30)
                    file = open("distLP.txt")
                    data = file.read()
                    file.close()
                    Results = Label(root, text=data)
                    Results.pack()
                    Results.place(x=820, y=300, width=200)
                    file = open("timeLP.txt")
                    data = file.read()
                    file.close()
                    Results = Label(root, text=data)
                    Results.pack()
                    Results.place(x=820, y=330, width=200)
            except ValueError:
                tkinter.messagebox.showwarning('Error', 'First run all the Algorithms')
    except ValueError:
        tkinter.messagebox.showwarning('Error', 'First enter Number of cities')





def distGA():
    file = open("GAdistance.txt")
    data = file.read()
    file.close()
    Results = Label(root, text=data)
    Results.pack()
    Results.place(x=10,y=160,width=200,height=30)
def timeGA():
    file = open("outtsp.txt")
    q = file.read()
    file.close()
    try:
        if (q < "0"):
            tkinter.messagebox.showwarning('Error', 'First enter Number of cities')
        else:
            file = open("GAtime.txt")
            data = file.read()
            file.close()
            try:
                if (data < "0"):
                    tkinter.messagebox.showwarning('Error', 'First run GA')
                else:
                    Results = Label(root, text=data)
                    Results.pack()
                    Results.place(x=10, y=190, width=200,height=30)
                    distGA()
            except ValueError:
                tkinter.messagebox.showwarning('Error', 'First run GA')
    except ValueError:
        tkinter.messagebox.showwarning('Error', 'First enter Number of cities')
def imgga():
    image = Image.open('gatsp.png')
    image.show()

def imgGA():
    check_call(['dot', '-Tpng', 'GApath.dot', '-o', 'gatsp.png'])
    imgga()
def GA():
    file = open("outtsp.txt")
    p = file.read()
    file.close()
    try:
        if (p < "0"):
            tkinter.messagebox.showwarning('Error', 'First enter Number of cities')
        else:
            try:
                file = open("GAtime.txt")
                data = file.read()
                file.close()
                if (data < "0"):
                    tkinter.messagebox.showwarning('Error', 'First run GA')
                else:
                    a = open("GApath.txt")
                    c = a.readline()
                    c = c.split(",")
                    n = len(c) - 1
                    g = {}
                    for i in range(1, n):
                        g[str(i)] = {}
                        for j in range(i + 1, n + 1):
                            g[str(i)][str(j)] = "black"
                            # G.add_edge(str(i),str(j))
                    # print g

                    for i in range(1, len(c) - 1):
                        # print c[i-1],c[i]
                        try:
                            g[c[i - 1]][c[i]] = i
                        except KeyError:
                            g[c[i]][c[i - 1]] = i
                            # G.add_edge(c[i-1],c[i],color="red")

                    # G.add_edge(c[-2],c[0],color="red") #last to first
                    try:
                        g[c[-2]][c[0]] = len(c) - 1
                    except KeyError:
                        g[c[0]][c[-2]] = len(c) - 1
                    # print g

                    f = open("GApath.dot", "w")
                    f.write("graph G{\n")
                    for i in g:

                        for j in g[i]:
                            if g[i][j] == "black":
                                f.write(str(i) + "--" + str(j) + "[color=" + str(g[i][j]) + "]\n")
                            else:
                                f.write(str(i) + "--" + str(j) + "[color=" + "red" + ",label=" + str(g[i][j]) + "]\n")
                    f.write("}")
                    #  f.write_png('geneticpath2.png')
                    f.close()
                    imgGA()

            except ValueError:
                tkinter.messagebox.showwarning('Error', 'First run GA')

    except ValueError:
        tkinter.messagebox.showwarning('Error', 'First enter Number of cities')

def GAnum():
    file = open("outtsp15.txt")
    data = file.read()
    file.close()
    Results = Label(root, text=data)
    Results.pack()
    Results.place(x=10, y=45,width=200)

def run_g_program():
    n=str(var.get())
    try:
        if (n=="1"):
            base = os.path.dirname(os.path.dirname(__file__))
            path = os.path.join(base, "projecttsp")
            # we have to get drive:
            base = base.split(':')
            base = base[0]
            file_path_compile = os.path.join(path, 'sh_c.bat')
            file_path_run = os.path.join(path, 'sh_c_run.bat')
            batch_file_compile = open(file_path_compile, 'wt')
            batch_file_run = open(file_path_run, 'wt')
        # this is writing our commands to the batch files
        # Batch file to compile the code. I am taking the output of commands to the files.
            file_data = 'cd ' + path + '\n' + base + ':\n' + 'g++ -o GAtsp GAtsp.cpp 2>compile.txt'
            batch_file_compile.write(file_data)
            batch_file_compile.close()
            file_data = 'cd ' + path + '\n' + base + ':\n' + 'GAtsp.exe ' + ' >run.txt'
            batch_file_run.write(file_data)
            batch_file_run.close()
        # we use the subprocess to execute the batch file
            p = subprocess.Popen(file_path_compile)
            p.wait()
            file_path = os.path.join(path, 'compile.txt')
            compile_txt = open(file_path)
        # if no compilation error then only run the code for executing the C program.
            if compile_txt.read() == "":
                p = subprocess.Popen(file_path_run)
            GAnum()
        else:
             tkinter.messagebox.showwarning('Error', 'First select method')
    except ValueError:
        tkinter.messagebox.showwarning('Error', 'First select method')






def GArun():
    file = open("outtsp.txt")
    p = file.read()
    file.close()
    try:
        if (p < "0"):
            tkinter.messagebox.showwarning('Error', 'First enter Number of cities')
        else:
            button2 = Button(root, text="RUN", command=run_g_program, width=10, bd=5, fg='green')
            button2.pack()
            button2.place(x=450, y=450)
    except ValueError:
        tkinter.messagebox.showwarning('Error', 'First enter Number of cities')



R1 = Radiobutton(root, text="GA ", variable=var, value=1,width=15, bd=1, bg='green',
                  command=GArun)
R1.pack( anchor = W )
R1.place(x=10,y=90)
R7 = Radiobutton(root, text="Distance and Time ", variable=var, value=2,width=15, bd=1, bg='green',
                  command=timeGA)
R7.pack( anchor = W )
R7.place(x=10,y=130)


R2 = Radiobutton(root, text="GA image show", variable=var, value=3,width=15, bd=1, bg='green',
                  command=GA)
R2.pack( anchor = W)
R2.place(x=10,y=230)

def distSA():
    file = open("SAdistance.txt")
    data = file.read()
    file.close()
    Results = Label(root, text=data)
    Results.pack()
    Results.place(x=300,y=160,width=200,height=30)
def timeSA():
    file = open("outtsp.txt")
    q = file.read()
    file.close()
    try:
        if (q < "0"):
            tkinter.messagebox.showwarning('Error', 'First enter Number of cities')
        else:
            file = open("SAtime.txt")
            data = file.read()
            file.close()
            try:
                if (data < "0"):
                    tkinter.messagebox.showwarning('Error', 'First run SA')
                else:
                    Results = Label(root, text=data)
                    Results.pack()
                    Results.place(x=300, y=190, width=200,height=30)
                    distSA()
            except ValueError:
                tkinter.messagebox.showwarning('Error', 'First run SA')

    except ValueError:
        tkinter.messagebox.showwarning('Error', 'First enter Number of cities')

def imgsa():
    image = Image.open('satsp.png')
    image.show()
def imgSA():
    check_call(['dot', '-Tpng', 'SApath.dot', '-o', 'satsp.png'])
    imgsa()
def SA():
    file = open("outtsp.txt")
    p = file.read()
    file.close()
    try:
        if (p < "0"):
            tkinter.messagebox.showwarning('Error', 'First enter Number of cities')
        else:
            try:
                file = open("SAtime.txt")
                data = file.read()
                file.close()
                if (data < "0"):
                    tkinter.messagebox.showwarning('Error', 'First run SA')
                else:
                    a = open("SApath.txt")
                    c = a.readline()
                    c = c.split(",")
                    n = len(c) - 1
                    g = {}
                    for i in range(1, n):
                        g[str(i)] = {}
                        for j in range(i + 1, n + 1):
                            g[str(i)][str(j)] = "black"
                            # G.add_edge(str(i),str(j))
                    # print g

                    for i in range(1, len(c) - 1):
                        # print c[i-1],c[i]
                        try:
                            g[c[i - 1]][c[i]] = i
                        except KeyError:
                            g[c[i]][c[i - 1]] = i
                            # G.add_edge(c[i-1],c[i],color="red")

                    # G.add_edge(c[-2],c[0],color="red") #last to first
                    try:
                        g[c[-2]][c[0]] = len(c) - 1
                    except KeyError:
                        g[c[0]][c[-2]] = len(c) - 1
                    # print g

                    f = open("SApath.dot", "w")
                    f.write("graph G{\n")
                    for i in g:

                        for j in g[i]:
                            if g[i][j] == "black":
                                f.write(str(i) + "--" + str(j) + "[color=" + str(g[i][j]) + "]\n")
                            else:
                                f.write(str(i) + "--" + str(j) + "[color=" + "red" + ",label=" + str(g[i][j]) + "]\n")
                    f.write("}")
                    #  f.write_png('geneticpath2.png')
                    f.close()
                    imgSA()

            except ValueError:
                tkinter.messagebox.showwarning('Error', 'First run DM')

    except ValueError:
        tkinter.messagebox.showwarning('Error', 'First enter Number of cities')



    #distSA()
    #timeSA()
    # import pygraphviz as pgv

def SAnum():
    file = open("outtsp15.txt")
    data = file.read()
    file.close()
    Results = Label(root, text=data)
    Results.pack()
    Results.place(x=300, y=45,width=200)
def run_s_program():
    n=str(var.get())
    try:
        if (n=="4"):
            base = os.path.dirname(os.path.dirname(__file__))
            path = os.path.join(base, "projecttsp")
            base = base.split(':')
            base = base[0]
            file_path_compile = os.path.join(path, 'sh1_c.bat')
            file_path_run = os.path.join(path, 'sh1_c_run.bat')
            batch_file_compile = open(file_path_compile, 'wt')
            batch_file_run = open(file_path_run, 'wt')
        # this is writing our commands to the batch files
        # Batch file to compile the code. I am taking the output of commands to the files.
            file_data = 'cd ' + path + '\n' + base + ':\n' + 'g++ -o SAtsp SAtsp.cpp 2>compile1.txt'
            batch_file_compile.write(file_data)
            batch_file_compile.close()
            file_data = 'cd ' + path + '\n' + base + ':\n' + 'SAtsp.exe ' + ' >run1.txt'
            batch_file_run.write(file_data)
            batch_file_run.close()
        # we use the subprocess to execute the batch file
            p = subprocess.Popen(file_path_compile)
            p.wait()
            file_path = os.path.join(path, 'compile1.txt')
            compile_txt = open(file_path)
        # if no compilation error then only run the code for executing the C program.
            if compile_txt.read() == "":
                p = subprocess.Popen(file_path_run)
            SAnum()
        else:
            tkinter.messagebox.showwarning('Error', 'First select method')
    except ValueError:
        tkinter.messagebox.showwarning('Error', 'First select method')


def SArun():
    file = open("outtsp.txt")
    p = file.read()
    file.close()
    try:
        if (p < "0"):
            tkinter.messagebox.showwarning('Error', 'First enter Number of cities')
        else:
            button3 = Button(root, text="RUN", command=run_s_program, width=10, bd=5, fg='green')
            button3.pack()
            button3.place(x=450, y=450)
    except ValueError:
        tkinter.messagebox.showwarning('Error', 'First input Number of cities')

R3 = Radiobutton(root, text="SA ", variable=var, value=4,width=15, bd=1, bg='green',
                  command=SArun)
R3.pack( anchor = W )
R3.place(x=300,y=90)
R8 = Radiobutton(root, text="Distance and Time ", variable=var, value=5,width=15, bd=1, bg='green',
                  command=timeSA)
R8.pack( anchor = W )
R8.place(x=300,y=130)

R4 = Radiobutton(root, text="SA image show", variable=var, value=6,width=15, bd=1, bg='green',
                  command=SA)
R4.pack( anchor = W)
R4.place(x=300,y=230)



def distDM():
    file = open("DMdistance.txt")
    data = file.read()
    file.close()
    Results = Label(root, text=data)
    Results.pack()
    Results.place(x=590,y=160,width=200,height=30)
def timeDM():
    file = open("outtsp.txt")
    q = file.read()
    file.close()
    try:
        if(q<"0"):
            tkinter.messagebox.showwarning('Error', 'First enter Number of cities')
        else:
            file = open("DMtime.txt")
            data = file.read()
            file.close()
            try:
                if (data < "0"):
                    tkinter.messagebox.showwarning('Error', 'First run DM')
                else:
                    Results = Label(root, text=data)
                    Results.pack()
                    Results.place(x=590, y=180, width=200,height=30)
                    distDM()
            except ValueError:
                tkinter.messagebox.showwarning('Error', 'First run DM')
    except ValueError:
        tkinter.messagebox.showwarning('Error', 'First enter Number of cities')

def imgdm():
    image = Image.open('dmtsp.png')
    image.show()
def imgDM():
    check_call(['dot', '-Tpng', 'DMpath.dot', '-o', 'dmtsp.png'])
    imgdm()
def DM():
    file = open("outtsp.txt")
    p = file.read()
    file.close()
    try:
        if (p <"0"):
            tkinter.messagebox.showwarning('Error', 'First enter Number of cities')
        else:
            try:
                file = open("DMtime.txt")
                data = file.read()
                file.close()
                if (data < "0"):
                    tkinter.messagebox.showwarning('Error', 'First run DM')
                else:
                    a = open("DMpath.txt")
                    c = a.readline()
                    c = c.split(",")
                    n = len(c) - 1
                    g = {}
                    for i in range(1, n):
                        g[str(i)] = {}
                        for j in range(i + 1, n + 1):
                            g[str(i)][str(j)] = "black"
                            # G.add_edge(str(i),str(j))
                    # print g

                    for i in range(1, len(c) - 1):
                        # print c[i-1],c[i]
                        try:
                            g[c[i - 1]][c[i]] = i
                        except KeyError:
                            g[c[i]][c[i - 1]] = i
                            # G.add_edge(c[i-1],c[i],color="red")

                    # G.add_edge(c[-2],c[0],color="red") #last to first
                    try:
                        g[c[-2]][c[0]] = len(c) - 1
                    except KeyError:
                        g[c[0]][c[-2]] = len(c) - 1
                    # print g

                    f = open("DMpath.dot", "w")
                    f.write("graph G{\n")
                    for i in g:

                        for j in g[i]:
                            if g[i][j] == "black":
                                f.write(str(i) + "--" + str(j) + "[color=" + str(g[i][j]) + "]\n")
                            else:
                                f.write(str(i) + "--" + str(j) + "[color=" + "red" + ",label=" + str(g[i][j]) + "]\n")
                    f.write("}")
                    #  f.write_png('geneticpath2.png')
                    f.close()
                    imgDM()

            except ValueError:
                tkinter.messagebox.showwarning('Error', 'First run DM')

    except ValueError:
        tkinter.messagebox.showwarning('Error', 'First enter Number of cities')


            # distDM()
    #timeDM()
    # import pygraphviz as pgv

def DMnum():
    file = open("outtsp15.txt")
    data = file.read()
    file.close()
    Results = Label(root, text=data)
    Results.pack()
    Results.place(x=590, y=45,width=200)

def run_d_program():
    n = str(var.get())
    try:
        if (n == "7"):
            base = os.path.dirname(os.path.dirname(__file__))
            path = os.path.join(base, "projecttsp")
            base = base.split(':')
            base = base[0]
            file_path_compile = os.path.join(path, 'sh2_c.bat')
            file_path_run = os.path.join(path, 'sh2_c_run.bat')
            batch_file_compile = open(file_path_compile, 'wt')
            batch_file_run = open(file_path_run, 'wt')
            # this is writing our commands to the batch files
            # Batch file to compile the code. I am taking the output of commands to the files.
            file_data = 'cd ' + path + '\n' + base + ':\n' + 'g++ -o DMtsp DMtsp.cpp 2>compile2.txt'
            batch_file_compile.write(file_data)
            batch_file_compile.close()
            file_data = 'cd ' + path + '\n' + base + ':\n' + 'DMtsp.exe ' + ' >run2.txt'
            batch_file_run.write(file_data)
            batch_file_run.close()
            # we use the subprocess to execute the batch file
            p = subprocess.Popen(file_path_compile)
            p.wait()
            file_path = os.path.join(path, 'compile2.txt')
            compile_txt = open(file_path)
            # if no compilation error then only run the code for executing the C program.
            if compile_txt.read() == "":
                p = subprocess.Popen(file_path_run)
            DMnum()
        else:
            tkinter.messagebox.showwarning('Error', 'First select method')
    except ValueError:
        tkinter.messagebox.showwarning('Error', 'First select method')

        # get the path to the currunt file.Assuming python code and C code to be    #executed are in same Folder



#R20 = Radiobutton(root, text="Path DM ", variable=var, value="20",
                #  command=pathdm)
#R20.pack( anchor = W )
#R20.place(x=10,y=450)

def DMrun():
    file = open("outtsp.txt")
    p = file.read()
    file.close()
    try:
        if(p<"0"):
            tkinter.messagebox.showwarning('Error', 'First enter Number of cities')
        #elif(p>"11"):
          #  tkinter.messagebox.showwarning('Error', 'Usually does not work for large number of cities')
        else:
            button4 = Button(root, text="RUN", command=run_d_program, width=10, bd=5, fg='green')
            button4.pack()
            button4.place(x=450, y=450)
    except ValueError:
        tkinter.messagebox.showwarning('Error', 'First enter Number of cities')
R5 = Radiobutton(root, text="DM ", variable=var, value=7,width=15, bd=1, bg='green',
                  command=DMrun)
R5.pack( anchor = W )
R5.place(x=590,y=90)
R9 = Radiobutton(root, text="Distance and Time ", variable=var, value=8,width=15, bd=1, bg='green',
                  command=timeDM)
R9.pack( anchor = W )
R9.place(x=590,y=130)


R10 = Radiobutton(root, text="DM image show", variable=var, value=9,width=15, bd=1, bg='green',
                  command=DM)
R10.pack( anchor = W)
R10.place(x=590,y=230)
def timeLP():
    file = open("timeLP.txt")
    data = file.read()
    file.close()
    Results = Label(root, text=data)
    Results.pack()
    Results.place(x=820,y=190,width=200)
def distLP():
    file = open("outtsp.txt")
    p = file.read()
    file.close()

    try:
        if (p<"0"):
            tkinter.messagebox.showwarning('Error', 'First enter Number of cities')
        else:
            file = open("distLP.txt")
            data = file.read()
            file.close()
            try:
                if (data < "0"):
                    tkinter.messagebox.showwarning('Error', 'First run LP')
                else:
                    Results = Label(root, text=data)
                    Results.pack()
                    Results.place(x=820, y=160, width=200)
                    timeLP()
            except ValueError:
                tkinter.messagebox.showwarning('Error', 'First run LP')
    except ValueError:
        tkinter.messagebox.showwarning('Error', 'First enter Number of cities')


R15 = Radiobutton(root, text="Distance and Time", variable=var, value=10, width=15, bd=1, bg='green',
                  command=distLP)
R15.pack( anchor = W )
R15.place(x=820,y=130)
def LPnum():
    file = open("outtsp15.txt")
    data = file.read()
    file.close()
    Results = Label(root, text=data)
    Results.pack()
    Results.place(x=820, y=45,width=200)
def opl():
    n=str(var.get())
    try:
        if (n=="11"):
            subprocess.check_call(["oplrun", "F:/projecttsp/projectlp/projectlp.mod","F:/projecttsp/projectlp/projectlp.dat"])
            LPnum()
        else:
            tkinter.messagebox.showwarning('Error', 'First select method')
    except ValueError:
        tkinter.messagebox.showwarning('Error', 'First select method')
def LPrun():
    file = open("outtsp.txt")
    p = file.read()
    file.close()

    try:
        if (p < "0"):
            tkinter.messagebox.showwarning('Error', 'First enter Number of cities')
        #elif p > "25":
           # tkinter.messagebox.showwarning('Error', 'Usually does not work for large number of cities')

        else:
            button8 = Button(root, text="RUN", command=opl, width=10, bd=5, fg='green')
            button8.pack()
            button8.place(x=450, y=450)
    except ValueError:
        tkinter.messagebox.showwarning('Error', 'First enter Number of cities')
R11 = Radiobutton(root, text="LP ", variable=var, value=11,width=15, bd=1, bg='green',
                  command=LPrun)
R11.pack( anchor = W )
R11.place(x=820,y=90)



root.title('TSP ')
def RandomFunction():
   # if variable1==int:

    # print(n)
    try:
        n =variable1.get()
        if(n>0):
            orig_stdout = sys.stdout
            sys.stdout = open('outtsp.txt', 'w')
            print(n)
            sys.stdout.close()
            orig_stdout = sys.stdout
            sys.stdout.close()
            sys.stdout = open('outtsp15.txt', 'w')
            print('')
            sys.stdout.close()
            file = open("outtsp15.txt")
            data = file.read()
            file.close()
            Results = Label(root, text=data)
            Results.pack()
            Results.place(x=10, y=45, width=200)
            file = open("outtsp15.txt")
            data = file.read()
            file.close()
            Results = Label(root, text=data)
            Results.pack()
            Results.place(x=300, y=45, width=200)
            file = open("outtsp15.txt")
            data = file.read()
            file.close()
            Results = Label(root, text=data)
            Results.pack()
            Results.place(x=590, y=45, width=200)
            file = open("outtsp15.txt")
            data = file.read()
            file.close()
            Results = Label(root, text=data)
            Results.pack()
            Results.place(x=820, y=45, width=200)
            sys.stdout = open('outtsp15.txt', 'w')
            print('Running For=',n,'Cities')
            sys.stdout.close()
            sys.stdout = open('GAdistance.txt', 'w')
            print('')
            sys.stdout.close()
            sys.stdout = open('SAdistance.txt', 'w')
            print('')
            sys.stdout.close()
            sys.stdout = open('DMdistance.txt', 'w')
            print('')
            sys.stdout.close()
            sys.stdout = open('GAtime.txt', 'w')
            print('')
            sys.stdout.close()
            sys.stdout = open('SAtime.txt', 'w')
            print('')
            sys.stdout.close()
            sys.stdout = open('DMtime.txt', 'w')
            print('')
            sys.stdout.close()
            sys.stdout = open('GApath.txt', 'w')
            print('')
            sys.stdout.close()
            sys.stdout = open('SApath.txt', 'w')
            print('')
            sys.stdout.close()
            sys.stdout = open('DMpath.txt', 'w')
            print('')
            sys.stdout.close()
            sys.stdout = open('distLP.txt', 'w')
            print('')
            sys.stdout.close()
            sys.stdout = open('timeLP.txt', 'w')
            print('')
            sys.stdout.close()
            file = open("GAdistance.txt")
            data = file.read()
            file.close()
            Results = Label(root, text=data)
            Results.pack()
            Results.place(x=10, y=160, width=200, height=30)
            file = open("GAtime.txt")
            data = file.read()
            file.close()
            Results = Label(root, text=data)
            Results.pack()
            Results.place(x=10, y=190, width=200, height=30)
            file = open("SAdistance.txt")
            data = file.read()
            file.close()
            Results = Label(root, text=data)
            Results.pack()
            Results.place(x=300, y=160, width=200, height=30)
            file = open("SAtime.txt")
            data = file.read()
            file.close()
            Results = Label(root, text=data)
            Results.pack()
            Results.place(x=300, y=190, width=200, height=30)
            file = open("DMdistance.txt")
            data = file.read()
            file.close()
            Results = Label(root, text=data)
            Results.pack()
            Results.place(x=590, y=160, width=200, height=30)
            file = open("DMtime.txt")
            data = file.read()
            file.close()
            Results = Label(root, text=data)
            Results.pack()
            Results.place(x=590, y=190, width=200, height=30)
            file = open("distLP.txt")
            data = file.read()
            file.close()
            Results = Label(root, text=data)
            Results.pack()
            Results.place(x=820, y=160, width=200, height=30)
            file = open("timeLP.txt")
            data = file.read()
            file.close()
            Results = Label(root, text=data)
            Results.pack()
            Results.place(x=820, y=190, width=200, height=30)
            # random.seed(1)
            file = open("GAdistance.txt")
            data = file.read()
            file.close()
            Results = Label(root, text=data)
            Results.pack()
            Results.place(x=10, y=300, width=200, height=30)
            file = open("GAtime.txt")
            data = file.read()
            file.close()
            Results = Label(root, text=data)
            Results.pack()
            Results.place(x=10, y=330, width=200, height=30)
            file = open("SAdistance.txt")
            data = file.read()
            file.close()
            Results = Label(root, text=data)
            Results.pack()
            Results.place(x=300, y=300, width=200, height=30)
            file = open("SAtime.txt")
            data = file.read()
            file.close()
            Results = Label(root, text=data)
            Results.pack()
            Results.place(x=300, y=330, width=200, height=30)
            file = open("DMdistance.txt")
            data = file.read()
            file.close()
            Results = Label(root, text=data)
            Results.pack()
            Results.place(x=590, y=300, width=200, height=30)
            file = open("DMtime.txt")
            data = file.read()
            file.close()
            Results = Label(root, text=data)
            Results.pack()
            Results.place(x=590, y=330, width=200, height=30)
            file = open("distLP.txt")
            data = file.read()
            file.close()
            Results = Label(root, text=data)
            Results.pack()
            Results.place(x=820, y=300, width=200)
            file = open("timeLP.txt")
            data = file.read()
            file.close()
            Results = Label(root, text=data)
            Results.pack()
            Results.place(x=820, y=330, width=200)
            # distance={}
            distance = [[0 for x in range(n)] for y in range(n)]
            points = []
            # matrix=[[]]
            # points = []
            # n = 10
            for i in range(n):
                points.append((randint(0, 100), randint(0, 100)))
            for k in range(n):
                distance[k][k] = 0
                for j in range(k + 1, n):
                    dx = points[k][0] - points[j][0]
                    dy = points[k][1] - points[j][1]
                    distance[k][j] = int(math.sqrt(dx * dx + dy * dy))
                    distance[j][k] = distance[k][j]

            orig_stdout = sys.stdout
            sys.stdout = open('matrixtsp.txt', 'w')
            matrix = '\n'.join('\t'.join(str(distance[p][q]) for p in range(n)) for q in range(n))
            # print(np.matrix(distance))
            # single = genfromtxt('single.csv')
            print(matrix)
            # print('\n')
            sys.stdout.close()
            sys.stdout = open('F:/projecttsp/projectlp/projectlp.dat', 'w')
            matrix = '],\n['.join("\t".join(str(distance[p][q]) for p in range(n)) for q in range(n))
            # print("Gas=[")
            print("n=", n, ";")
            print("C=[")
            # print('[')
            # print(np.matrix(distance))
            print('[', matrix, ']')
            print('];')
            sys.stdout.close()
        else:
            tkinter.messagebox.showwarning('Error', 'Please enter positive integer')
    except ValueError:
        tkinter.messagebox.showwarning('Error', 'Please enter positive integer')

L1 = Label(root, text="Number of cities")
L1.pack( side = RIGHT)
L1.place(x=300,y=10)
EntryBox = Entry(root, textvariable = variable1)
EntryBox .pack()
EntryBox .place(x=400,y=10)
button = Button(root, text="Enter", command=RandomFunction)
button.pack()
button.place(x=500,y=10)

button2 = Button(root, text="ALL ", width=10, bd=5, fg='green',command=runall)
button2.pack()
button2.place(x=820,y=230)


def run():
    file = open("outtsp.txt")
    p = file.read()
    file.close()

    try:
        if (p < "0"):
            tkinter.messagebox.showwarning('Error', 'First enter Number of cities')
        else:
            try:
                file = open("DMdistance.txt")
                p1 = file.read()
                file.close()
                if (p1<"0"):
                    tkinter.messagebox.showwarning('Error', 'Please select method')
            except ValueError:
                tkinter.messagebox.showwarning('Error', 'Please select method')

    except ValueError:
        tkinter.messagebox.showwarning('Error', 'First enter Number of cities')

    #tkinter.messagebox.showwarning('Error','Please enter number of cities')

button2 = Button(root, text="RUN", width=10, bd=5, fg='green',command=run)
button2.pack()
button2.place(x=450,y=450)
def doSomething():
    # check if saving
    # if not:
    sys.stdout = open('GAdistance.txt', 'w')
    print(-1)
    sys.stdout.close()
    sys.stdout = open('SAdistance.txt', 'w')
    print(-1)
    sys.stdout.close()
    sys.stdout = open('DMdistance.txt', 'w')
    print(-1)
    sys.stdout.close()
    sys.stdout = open('GAtime.txt', 'w')
    print(-1)
    sys.stdout.close()
    sys.stdout = open('SAtime.txt', 'w')
    print(-1)
    sys.stdout.close()
    sys.stdout = open('DMtime.txt', 'w')
    print(-1)
    sys.stdout.close()
    sys.stdout = open('GApath.txt', 'w')
    print(-1)
    sys.stdout.close()
    sys.stdout = open('SApath.txt', 'w')
    print(-1)
    sys.stdout.close()
    sys.stdout = open('DMpath.txt', 'w')
    print(-1)
    sys.stdout.close()
    sys.stdout = open('distLP.txt', 'w')
    print(-1)
    sys.stdout.close()
    sys.stdout = open('timeLP.txt', 'w')
    print(-1)
    sys.stdout.close()
    sys.stdout = open('outtsp.txt', 'w')
    print(-1)
    sys.stdout.close()

    root.destroy()
root.protocol('WM_DELETE_WINDOW', doSomething)  # root is your root window


#button2.pack()
root.mainloop()
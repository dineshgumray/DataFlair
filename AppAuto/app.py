# modules to be imported.
import tkinter as tk
from tkinter import filedialog, Text 
import os

# creating object root for handling TK window.
root = tk.Tk()

# apps list is created to accomodate all the path details.
apps = []

# print(os.getcwd())

# change the current working directory
os.chdir(os.path.dirname(os.path.realpath(__file__))) 

# in current directory checking if save.txt file is there or not to open.
if os.path.isfile('save.txt'):
    # open the file named save.txt, where we saved our app path.
    with open('save.txt','r') as f:
        # reading files with read_file variable.
        tempApps = f.read()
        # split the read text to list based on common as seperator.
        tempApps = tempApps.split(',')
        # for strip empty string from list tempApps which got readed when reading save.txt file.
        apps = [x for x in tempApps if x.strip()]

def addApp():
    '''
    addApp is used to add selected application path to the frame
    '''
    # clearing the frame when new application path got selected.
    # by this we can avoid duplication of details getting posted on frame.
    for widget in frame.winfo_children():
        widget.destroy()

    # to catch/copy the selected application/file name in filename variable and append it to app list.
    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables","*.exe"),("all files","*.*")))
    # if nothing got selected then don't append to apps list.
    # to avoid creating an empty string in list.
    if filename:
        apps.append(filename)

    # for creating label of selected app and displaying it on frame.
    for app in apps:
        # for creating label of selected app.
        label = tk.Label(frame, text=app, bg="gray")
        # for displaying it on frame.
        label.pack()

def runApps():
    '''
    runApp is used to run application from the path mentioned on frame
    '''
    # to start displaying apps on frame.
    for app in apps:
        os.startfile(app)

# creating canvas on which our frame resides.
canvas = tk.Canvas(root, height = 700, bg ="#263D42")
# attaching canvas to our tk window.
canvas.pack()

# creating frame on whilch we will display our app details.
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# creating Open File button, used to open the window to select path of our app/file.
# calls addApp function to get the app/file path deatails.
openApps = tk.Button(root, text = "Open App", padx=10, pady=5, fg="white", bg="gray", command = addApp)
# attaching Open File button to our tk window.
openApps.pack()

# creating Run App button, used to run the app/file from select path.
# calls runApps to run the displayed file.
runApps = tk.Button(root, text="Run App", padx=10, pady=5, fg="white", bg ="gray", command = runApps)
# attaching Run App button to our tk window.
runApps.pack()

# creating and attaching labels of selecetd app/file name on displaying frame 
# which are already there in save.txt and where selected in past run.
for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

# for starting the tk application/window.
root.mainloop()

# to open the save.txt file and write the app/file path details which user selects.
with open('save.txt', 'w') as f:
    for app in apps:
        # write the details to save.txt by appending common after each file path.
        f.write(app + ',')
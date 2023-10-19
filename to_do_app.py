# import all functions from the tkinter 
from tkinter import *
from tkinter import messagebox

# global list is declare for storing all the task
tasks_list = []

# global variable is declare for counting the task
counter = 1

# Function for checking input error when
def inputError() :
	
	
	if enterTaskField.get() == "" :
		messagebox.showerror("Input Error")
		return 0
	
	return 1


def clear_taskNumberField() :
	
	taskNumberField.delete(0.0, END)


def clear_taskField() :

	enterTaskField.delete(0, END)
	
# Function for inserting the contents
def insertTask():

	global counter
	
	value = inputError()

	if value == 0 :
		return

	content = enterTaskField.get() + "\n"

	# store task in the list
	tasks_list.append(content)

	TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)

	counter += 1

	# function calling for deleting the content of task field
	clear_taskField()

# function for deleting the specified task
def delete() :
	
	global counter
	
	if len(tasks_list) == 0 :
		messagebox.showerror("No task")
		return

	number = taskNumberField.get(1.0, END)

	if number == "\n" :
		messagebox.showerror("input error")
		return
	
	else :
		task_no = int(number)

	clear_taskNumberField()
	
	tasks_list.pop(task_no - 1)

	counter -= 1
	
	TextArea.delete(1.0, END)

	# rewriting the task after deleting one task at a time
	for i in range(len(tasks_list)) :
		TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])
	

# Driver code 
if __name__ == "__main__" :

	gui = Tk()

	gui.configure(background = "light green")

	#title of GUI window
	gui.title("ToDo App")

	#configuration of GUI window 
	gui.geometry("250x300")

	# create a label : Enter Your Task
	enterTask = Label(gui, text = "Enter Your Task", bg = "light green")

	# create a text entry box 
	enterTaskField = Entry(gui)

	# create a Submit Button and place into the root window
	Submit = Button(gui, text = "Submit", fg = "Black", bg = "light blue", command = insertTask)

	# create a text area for the root
	TextArea = Text(gui, height = 5, width = 25, font = "lucida 13")

	# create a label : Delete Task Number
	taskNumber = Label(gui, text = "Delete Task Number", bg = "light green")
						
	taskNumberField = Text(gui, height = 1, width = 2, font = "lucida 13")

	# create a Delete Button and place into the root window
	delete = Button(gui, text = "Delete", fg = "Black", bg = "light blue", command = delete)

	# create a Exit Button and place into the root window
	Exit = Button(gui, text = "Exit", fg = "Black", bg = "light blue", command = exit)

	# grid method is used for placing 
	# the widgets at respective positions 
	enterTask.grid(row = 0, column = 2)
			 
	enterTaskField.grid(row = 1, column = 2, ipadx = 50)
						
	Submit.grid(row = 2, column = 2)
		
	TextArea.grid(row = 3, column = 2, padx = 10, sticky = W)
						
	taskNumber.grid(row = 4, column = 2, pady = 5)
						
	taskNumberField.grid(row = 5, column = 2)

				 
	delete.grid(row = 6, column = 2, pady = 5)
						
	Exit.grid(row = 7, column = 2)

	# start the GUI 
	gui.mainloop()

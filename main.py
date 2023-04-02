
#importing libraires to create window and stage 1
import tkinter as tk
from tkinter import ttk
import stage1

# main class - holds the elementst that need to be displayed on the window
class main(ttk.Frame):
    #first function that must be executed whn main is called
    def __init__(self,container):
            super().__init__(container)

            #the title of the project and the position 
            project_name = ttk.Label(text="Physics beam", font=("Calibri", 30),)
            project_name.grid(row=4,column=3,)

            #button to move onto stage 1 and enter the data for the beam.
            create_beam = ttk.Button(text=" Begin")
            #when the button is clicked it will run the function calling stage 1 
            create_beam['command'] = lambda:self.calling_stage1()
            create_beam.grid(row=5,column=3)

            
    # this function will import stage 1 once the user has clicked the button.
    def calling_stage1(self):
        # it will close the main window and then open stage 1 
        app.destroy()
        st1Window= stage1_window()
        stage1.stage1_interface(st1Window)

# this class is to create the window for stage 1 and to import stage 1 into this window instead of the main window
class stage1_window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Stage 1")     
        
# this class creates the window for the main window and the elements for the main window are displayed in here
class main_window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("main")
        #this is a fixed size so there is a smooth transition to stage 1
        self.geometry("700x300")

# this displays the window when the program is running.
if __name__ == "__main__":
    #it is storing the main window in app so we can place the main window elements into the main window.
    app = main_window()
    main(app)
    #closing the main loop
    app.mainloop()



      


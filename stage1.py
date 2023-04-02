
# imports for stage 1 
import tkinter as tk
from tkinter import W, StringVar, ttk

# importing other modules
import stage1_validations
import database as db
# importing stage 2
# import stage2

# global variables
global length
global pivot
global dis_piv_1
global dis_piv_2
global weight
global app


#stage 1 class

s1 = stage1_validations.validations()
class stage1_interface(ttk.Frame):

    # initialis function has the layout and the interface for the window
    def __init__(self, container):
        super().__init__(container)

        options = {'padx':5, 'pady':5,}

        #the window title

        stage_name = ttk.Label(text="Creating the beam", font=("Calibri", 30),)
        stage_name.grid(row=0, column=2)

        # reteriving the length of the beam
        lable1 = ttk.Label(text="Length of beam:", font=("Calibri", 20),)
        lable1.grid(row=1, column=0, padx=0, pady=10)

        #storing the value as a string because the user may enter a word instead of a string 
        #this value is later converted to a string.
        length_value = tk.StringVar()

        length = ttk.Entry(width=20, textvariable=length_value)
        length.grid(row=1, column=2, padx=0, pady=0)

        lable1 = ttk.Label(text="meter(s)", font=("Calibri", 20),)
        lable1.grid(row=1, column=3, padx=0, pady=0)

        # creating the enterie for the number of pivots
        label2 = ttk.Label(text="number of pivots", font=("Calibri", 20))
        label2.grid(row=2, column=0, sticky=W)

        # the data type here is an integer because the user is only selecting form 2 options
        # we check they have choses a value 
        # then we store the value of the pivot into the database.
        pivot = tk.IntVar()

        #they are radial buttons becue you can only choose one option
        pivot1 = ttk.Radiobutton(
            text="pivot 1", width=20, variable=pivot, value=1)
        pivot1.grid(row=3, column=0, padx=0, pady=0,)

        pivot2 = ttk. Radiobutton(
            text="pivot 2", width=20, variable=pivot, value=2)

        pivot2.grid(row=4, column=0, padx=0, pady=0,)

        #user is entering the position of the pivot from the left end to the right

        label3 = ttk.Label(text="support location", font=("Calibri", 20),)
        label3.grid(row=2, column=2)

        label3 = ttk.Label(text="pivot 1 location", font=("Calibri", 20),)
        label3.grid(row=3, column=1)

        # stoeing the vaulus as a string incase the user has entered an invalid input.
        distance1 = tk.StringVar()

        dis_piv_1 = ttk.Entry(textvariable=distance1)
        dis_piv_1.grid(row=3, column=2)

        label3 = ttk.Label(text="meter(s)", font=("Calibri", 20),)
        label3.grid(row=3, column=3)

        label3 = ttk.Label(text="pivot 2 loction", font=("Calibri", 20),)
        label3.grid(row=4, column=1)

        # there a two distance incase the user has chossen to have 2 pivots they must enter 2 locations
        distance2 = tk.StringVar()

        dis_piv_2 = ttk.Entry(textvariable=distance2)
        dis_piv_2.grid(row=4, column=2)

        label3 = ttk.Label(text="meter(s)", font=("Calibri", 20),)
        label3.grid(row=4, column=3)

        # entering the weigh of the beam
        #uniform beam this means that the weigh is in the center of the beam
        label4 = ttk.Label(text="weight of beam", font=("Calibri", 20),)
        label4.grid(row=5, column=0, padx=0, pady=0)

        # storing the value of the weigh is this variable
        # is a string incase the user has not entered a number
        beamweight = StringVar()

        weight = ttk.Entry(textvariable=beamweight)
        weight.grid(row=5, column=1)

        label4 = ttk.Label(text="Newtons", font=("Calibri", 20),)
        label4.grid(row=5, column=2)

        # submitting the data
        #when the button is clicked it will call the functions to check the validations
        #and to add elements to the database.
        create_beam = ttk.Button(text="Create the beam")
        # create_beam['command'] = lambda: [self.calling_checks(length_value, pivot, distance1, distance2, beamweight),
        # self.delete_beam_data(),
        # self.insert_beam_Data(length_value, beamweight, pivot, distance1, distance2)
        # ]
        create_beam['command'] = lambda: [self.calling_checks(length_value, pivot, distance1, distance2, beamweight), ]
        # create_beam['command']=lambda:self.insert_beam_Data(length_value,beamweight,)
        create_beam.grid(row=6, column=3)

        # self.pack(options)

    # calling stage 1 validations to check user has entered correct data 
    def calling_checks(self, length_value, pivot, distance1, distance2, beamweight):
        # passing in the variables which data is stored in
        # passing them into the functions in the sepreate file 
        # s1 is the vaiable name i used retreive stage 1 validation functions
        # s1 = stage1_validations.validations()
        print("calling stage 1 checks")
        s1.length_check(length_value)
        s1.pivot_check(pivot,)
        s1.pivot_distance_check(distance1, distance2, length_value, pivot)
        s1.weigth_check(beamweight)
        s1.validation_result()

    # calling database querying function andd adding the users inputs into the database.
    def insert_beam_Data(self, length_value, beamweight, pivot, distance1, distance2):
    
        #check if the function from stage 1 validations returns false
        result = s1.validation_result()
        # here i was checking the value of result
        # print(result)
        # if ther eare no error is error will be false 
        if result == False:
            self.delete_beam_data()
            # thsi is the quwry we are passing into the datbase
            data_query = "INSERT into beam_table VALUES (?, ?, ?, ?, ?, ?)"
            # we need to calculate the beam mid point this is were the weight is placed.
            beam_mid = (float(length_value.get())/2)
            # these are the values we are passing into the database
            data_tuple = [
                (1, length_value.get(), beamweight.get(), beam_mid, 0, 0)]
            # then i called insert data and passes the nam eof the database the query and the data that needs to be inserted into the table
            Data.insert_data("db_physics_beam.db",  data_query, data_tuple)

            # here i have another variable with the query to store the pivot data 
            pivot_query = "INSERT into pivot_table VALUES (?,?,?,?)"
            # there are two rows in this database
            # i need to store the inforamtion for the fist pivot and the second pivot
            # i set y as the distance of the first pivot
            y = distance1.get()
            # then i create a for loop because I need to add the data twice
            # the range is 1 to pivot +1 because it would usually start at 0 
            # the value of pivot needs to be 1 and 2 
            for piv in range(1, pivot.get()+1):
                # this is the data that needs to be entered
                pivot_tuple = [(piv, y, 0, 0)]
                # then i inset this data 
                Data.insert_data("db_physics_beam.db",
                                 pivot_query, pivot_tuple)
                # i change the value of y to be the second distance and add this to the database.
                y = distance2.get()

            # now calling stage 2 because all the data is stored
            # app.destroy()
            # st2Window= stage2_window()
            # stage2.Capture_objects(st2Window)

    # this is the function to delete the previos elements in the database
    # this is because there are pervious enteries of data
    def delete_beam_data(self):
        # these are the querys to delet the data 
        data_query = "DELETE FROM beam_table"
        pivot_query = "DELETE FROM pivot_table"
        # i then call the function within database and pass in my querys
        Data.delete_data("db_physics_beam.db", data_query)
        Data.delete_data("db_physics_beam.db", pivot_query)

# this class is used to create the window for stage 1 
class stage1(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Stage 1")

class stage2_window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Stage 2")  


# this runs stage 1
if __name__ == "__main__":
    # i have stored the class of stage one in app 
    app = stage1()
    # stored the command to call functions from the database file
    Data = db.database()
    # storing the command to call stage 1 validations
    # s1 = stage1_validations.validations(app)
    # this runs the class stage 1 into stage 1 which is a window
    frame = stage1_interface(app)
    app.mainloop()


# importing libraries
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import warnings

# variables
# error message hold the message if the user has entered an incorrect value
error_messages = ""
#this is a vaiable to check if there is an error message
is_error = False

# this is the class for validationg the inputs 
class validations():
    def __init__(self):
     pass
   
    # this function validates the length of the beam
    def length_check(self, beam_length,):
        print("inside Stage 1 checks")
        # this retreives the value of the beam
        beam_length = beam_length.get()
        # i am declaring my global valiables
        # this is so i can change the value of the variables
        global is_error
        global error_messages

        # this is to check the input is correct
        try:
            # i am checking that the value is a floating point number
            float(beam_length)
            # if the value entered is a float or an integer then we will check the value
            if ((float(beam_length) >= 1 and float(beam_length) <= 10000) == True):
                pass
            # if the value entered is not within the range then we add an error message to the variable
            else:
                error_messages = error_messages + \
                    " Length Of Beam : Please enter a number within the range 1 and 10 000"
                # we make is error true because we have an error 
                is_error = True

        except:
            # if the value entered is not  a float or integer then will display an error 
            error_messages = error_messages+" Length Of Beam : Please enter a number "
            is_error = True

    # function check that the user has chosen a number of pivot
    def pivot_check(self, num_pivot,):
        # calling the global variables
        global is_error
        global error_messages
        num_pivot = num_pivot.get()

        # if the value of the vaiable has not changed then nothing was entered
        if num_pivot == 0:
            # adding error message 
            error_messages = error_messages + \
                "\n Number of pivots : please select a number of pivots"
            is_error = True

    # function to check that the user has entered the correct distances for the pivots
    def pivot_distance_check(self, distance1, distance2, beam_length, pivotNum,):
        # retreiving all the vaiable
        distance1 = distance1.get()
        distance2 = distance2.get()
        beam_length = beam_length.get()
        pivotNum = pivotNum.get()
        global is_error
        global error_messages

        # first check the user has entered a number
        try:
            float(distance1)
            # checking the first distance is within the range of the length of the beam
            if (float(distance1) >= 0 and float(distance1) <= float(beam_length)):
                # then checking if the user wanted 2 pivots
                if pivotNum == 2:
                    try:
                        #checking if the distance 2 is a number
                        float(distance2)
                        # checking if the beam within the reange of the beam
                        # also checking if distance 1 and 2 are different
                        if float(distance2) >= 0 and float(distance2) <= float(beam_length) and (distance1 != distance2):
                            pass
                        else:
                            # if it doesnt meet the conditions then add error message
                            error_messages = error_messages + \
                                "\n Distance 2 : make sure the pivot length is an number within the range 0 and length of the beam \n you can't have two pivots in the same place  "
                    # error message if it is not a number
                    except:
                        error_messages = error_messages + \
                            "\n Distance 2 : make sure the pivot length is an number within the range 0 and length of the beam   "
                # if i pivot distance 2 should have no enteries
                else:
                    if (distance2) == "":
                        pass
                    else:
                        # if there was an entry for distance 2 then display error 
                        error_messages = error_messages + \
                            "\n Distance 2 : you not enter a value pivot 2 if you choose to have one pivot"
            else:
                # the value for distance does not meet the conditions above
                error_messages = error_messages + \
                    "\n Distance 1: make sure the distance is an intger within range 0 and length of beam "
        except:
            # if distance 1 is not a number, error message
            error_messages = error_messages+"\n Enter correct values for pivot distances "

    # function checking if weight enery is correct
    def weigth_check(self, beamWeight,):
        # declaring variables
        beamWeight = beamWeight.get()
        global error_messages
        global is_error

        try:
            # checking that the weight entered is an number
            float(beamWeight)

            # checking the condition 
            if float(beamWeight) >= 0 and float(beamWeight) <= 100000:
                pass
            else:
                # the entery did not meet the conditions, add error message
                is_error = True
                error_messages = error_messages + \
                    "\n Beam Weight: Make sure the weight is number within the range 0 and 100 000 "
        # if not a number then display a error message
        except:
            is_error = True
            error_messages = error_messages + \
                "\n Beam Weight: Make sure the weight is number within the range 0 and 100 000 "

    # displaying the warning message
    def validation_result(self):
        # declaring the variables
        global is_error
        global error_messages
        # if there are error message show the warning box
        if is_error == True:
            messagebox.showwarning('warning', error_messages)
        # if no eror messages then dont show waning box
        # return the value of error message 
        # were there any errors
        error_messages=""
        is_error=False

        return is_error

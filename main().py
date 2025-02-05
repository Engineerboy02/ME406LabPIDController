# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 22:18:43 2025

@author: John Lindquist
"""

import serial
import time
from datetime import datetime
import pytz

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Configure serial port settings for serial adapter
port = 'COM3'  # Update to your serial port
baudrate = 9600  # Adjust this if needed
timeout = .1   # Timeout for serial read/write operations
serRS232 = serial.Serial(port, baudrate, timeout=timeout, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Configure serial port settings for arduino
#port = 'COM6'  # Update to your serial port
#baudrate = 115300 # Adjust this if needed
#timeout = .1   # Timeout for serial read/write operations
#serRelay = serial.Serial(port, baudrate, timeout=timeout)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
timebetweenruns = 60 #time delay to let tank drain fully in sec
TankLowValue = 0.690 #Tank Low value for tank drain reset

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def main():
    inputValues = inputs()
    #serialWrite(inputValues)
    serialGetParmaters(inputValues)
    
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def inputs():
    #print("Please enter the new values:")
    PValue = 1 #float(input("P value float from 0.000 to 3.999: "))
    IValue = 1 #float(input("I value float from 0000 to 3999: "))
    DValue = 1 #float(input("D value float from 000.0 to 399.9: "))

    print()

    Endtime = float(input("Please enter the end time in sec: ")) #number of secounds to collect data for (starts at 0)
    numberofsamples = int(input("Please enter the Number of Samples: ")) #Number of data points within the set time
    
    print()
    
    numberofTrials = int(input("Please enter the Number of Trials: ")) #Number of trials from empty to full

    print()

    outputFileName = str(input("Please enter the output filename: ")) #output file name the data for all trials just gets appended on the end
    
    inputvalues = [PValue, IValue, DValue, Endtime, numberofsamples, numberofTrials, outputFileName] #Puts all the Inputs into and array
    
    print()

    whenReadytoRun = input("Varibles set When ready to run hit enter: ") #Verifys that the user ir ready to run the experiment

    return(inputvalues) #returns the Input array to be used in other functions
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def serialWrite(inputValues): #Sends the PID Values CURRENTLY DOSEN'T WORK commands are wrong
    
    #------------------------------------------------------------------------
    set_command = f'*P503 {inputValues[0]}<CR>'
    serRS232.write(set_command.encode())
    time.sleep(0.1)  # Allow some time for the command to be processed
    
    #------------------------------------------------------------------------
    set_command = f'*P504 {inputValues[1]}<CR>'
    serRS232.write(set_command.encode())
    time.sleep(0.1)  # Allow some time for the command to be processed
    
    #------------------------------------------------------------------------
    set_command = f'*P505 {inputValues[2]}<CR>'
    serRS232.write(set_command.encode())
    time.sleep(0.1)  # Allow some time for the command to be processed
    
    return
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def serialGetParmaters(inputValues):

    timeStep = inputValues[3] / inputValues[4] #Finds the Time delay between data collections

    runsLeft = 0 #Sets a varible to be used to enabel or disable the tank drain delay time
                    #on the last trial it just exits and assumes the tank is empty before you start the scriot again
    
    for j in range( inputValues[5] ): #For loop to run for the desired number of trials
        
        fileName = inputValues[6]  + ".txt" #+ str(j+1) #Builds the file name and adds .txt to make it openable

        with open(fileName, "a") as f: #Writes the Headers to the file includes data lable and run number
                #f.write(f"Run Number = {j+1} \n")
                f.write(f"Date  formatted_time  TrialNumber   timestep    value \n")

        print()
        print("Starting new run", j+1) #User feedback as to what trial it is on

        #relaytrigger(1) #Used to trigger the realy to turn the pump on and off (not used if the controller is being set to standby)
        SetResponse = omegaResponse(4) #Sets the controller to run mode
        print(SetResponse) #Prints confirmation that the controller was set to run mode

        for i in range( inputValues[4] ): #for loop for the indivisual samples to be taken
    
            response = omegaResponse(0) #Gets the response from the omega controller
            
            #responseClean = float(response.replace("X04","",1)) #response[3:] #used to clean the command from the response not used if ECHO is off
            
            #if(responseClean > 10.0): #used to bring the float back down to under 10.0 (additional data cleaning)
                #responseClean = round(responseClean - 10, 4)

            #Created Time
            # Get the current time in UTC
            current_time_utc = time.time()
            # Create a timezone object for PST
            pst_timezone = pytz.timezone('America/Los_Angeles')
            # Convert the UTC time to PST
            current_time_pst = datetime.fromtimestamp(current_time_utc, pst_timezone)
            # Format the time as a string
            formatted_time = current_time_pst.strftime('%Y-%m-%d %H:%M:%S ')

            #print(responseClean)

            print(" -> -> -> -> ->",i , end = '', flush=True) #User feed back that data is being collected
            
            with open(fileName, "a", encoding="utf-8") as f: #writes data to the file to be saved 
                f.write(f"{formatted_time}   {j}    {i}    {response}\r")

            time.sleep(timeStep) #delay between samples to be taken
        
        print()

        #relaytrigger(2)  #Used to trigger the realy to turn the pump on and off (not used if the controller is being set to standby)
        SetResponse = omegaResponse(3) #Sets the controller to standby mode
        print(SetResponse) #Send the respones the the controller being set to stand by
        
        if inputValues[5] - runsLeft > 1: #decides weather or not to delay between trials (skips the last one)
            print("delay between runs")
            
            while float(response) > TankLowValue: #Function waiting till the delay has been compleated
                                                #One idea is that this could be changed to for (response > TankLowValue): .....
                
                print("-> -> -> -> -> ", end = '', flush=True) #User feed back that the delay is happening
                response = float(omegaResponse(0))
                time.sleep(1)
            
            runsLeft = runsLeft + 1
        
        print()
        print("Current run compleated and saved to file") #User feed back that the Run was compleated and saved to file

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#def relaytrigger(value): #Function used to run relay module

    #relay = f'{value}'
    #serRelay.write(relay.encode())

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def omegaResponse(input): #Used to send and receive the serial commands to the PID contoller
    command = [f'*X04\r\n', f'*W01400000\r\n', f'*W01400320\r\n', f'*D03\r\n', f'*E03\r\n']
    #commandRead = f'*X04\r\n' #Read Command
    #commandSet0 = f'*W01400000\r\n' #set 0.000
    #commandSet8 = f'*W01400320\r\n' #set 0.800
    #commandSetESB = f'*D03\r\n' #enable stand by
    #commandSetDSB = f'*E03\r\n' #disable stand by

    serRS232.write(command[input].encode())
    CommandResponse = serRS232.read_until('\r').decode('utf-8', errors='ignore').strip()#readline().decode()

    #print(SetResponse)

    return(CommandResponse)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
main() #calls the main function
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
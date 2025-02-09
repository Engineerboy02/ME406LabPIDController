# ME406LabPIDController
ME 406 PID lab serial communication

This guide is for Windows 10 and 11 if you have another operating system you will need to make special changes to the installation and setup.

## How to Use the Python Script

1.	Once loaded into Visual Studio Code with the required libraries you should be ready to run after a few settings that need to be checked.

![VSC Terminal](/Python%20PID%20Control%20Screenshots/FDFGH_18_VSC%20screen%20with%20terminal.png "VSC Terminal")

2.	First start by plugging in the serial interface to any USB port on your laptop does require a USB Type A port.

![Serial Interface](/Python%20PID%20Control%20Screenshots/HTUTPS_2_Serial%20Interface.png "Serial Interface")

3.	Second hit “Windows key” and search for “device manager”.

![Device Manager](/Python%20PID%20Control%20Screenshots/HTUTPS_3_Device%20maneger%20search.png "Device Manager")

4.	Scroll down the list a look for “Ports(COM & LPT)” click the drop down and look for the “USB Serial Port (COMx)” this should be the required serial device before moving on take note of the COM port number (in this example it is “COM5”) you will need to add that information to the Python Script.

![COM Port Number](/Python%20PID%20Control%20Screenshots/HTUTPS_4_Device%20manager%20look%20for%20the%20COMport%20number.png "COM Port Number")

5.	Now head back to Visual Studio Code and navigate to the “Main().py” file.

![Back To VSC main().py](/Python%20PID%20Control%20Screenshots/HTUTPS_5_Heading%20Back%20to%20VSC.png "Back To VSC main().py")

6.	Now on Line 16 it says `port = 'COM3'  # Update to your serial port` change the “COM3” to what you found in device manager so in my example the line will now read `port = 'COM5'  # Update to your serial port`

![COM Port Number in VSC](/Python%20PID%20Control%20Screenshots/HTUTPS_6_Updating%20the%20COM%20number%20in%20VSC.png "COM Port Number in VSC")

7.	To run hit the Triangle  ![Run button](/Python%20PID%20Control%20Screenshots/SUVS_10_run%20button.png "Run Button")   in the top of the window to run. 

![Run Button Global](/Python%20PID%20Control%20Screenshots/HTUTPS_7_Run%20Button%20location%20in%20VSC.png "Run Button Global")

8.	You will then be asked a series of prompts in the terminal at the bottom of the screen the first prompt is ether the number of seconds you want to collect data for (see procedure for recommended time) when done hit enter to go to the next prompt.

![Run Time](/Python%20PID%20Control%20Screenshots/HTUTPS_8_VSC%20Terminal%20during%20run%20time.png "Run Time")

9.	The next prompt is for the desired number of samples to be taken during to timeline (see procedure for recommended number of samples) when done hit enter to go to the next prompt.

![Number of samples](/Python%20PID%20Control%20Screenshots/HTUTPS_9_VSC%20Terminal%20during%20run%20time%20number%20of%20samples.png "Number of samples")

10.	The next prompt is for the desired number of trials to be performed. The number of trials is the number of tank fills and empties (see procedure for recommended number of trials) when done hit enter to go to the next prompt.

![Number of trials](/Python%20PID%20Control%20Screenshots/HTUTPS_10_VSC%20Terminal%20during%20run%20time%20number%20of%20trials.png "Number of trials")

11.	The next prompt is the Output File Name this can be whatever you want it to be and it will save to the same folder as the “Main().py” file.

![File Name](/Python%20PID%20Control%20Screenshots/HTUTPS_11_VSC%20Terminal%20during%20run%20time%20output%20file%20name.png "File Name")

12.	The Final prompt is to make sure you are ready to run the experiment when ready hit enter.

![Ready to Run](/Python%20PID%20Control%20Screenshots/HTUTPS_12_VSC%20Terminal%20during%20run%20time%20enter%20to%20start%20sampiling.png "Ready to Run")

13.	Once you hit run you should get the output below and the number will slowly count up to the final number of samples.

![Initial Run](/Python%20PID%20Control%20Screenshots/HTUTPS_13_VSC%20Terminal%20during%20run%20time%20initial%20output.png "Initial Run")

14.	After the run there will be a delay after the run to let the tank drain. The script polls data from the controller until the tank is “Empty” then stats again appending to the existing python file.

![Tank Drain Delay](/Python%20PID%20Control%20Screenshots/HTUTPS_14_VSC%20Terminal%20during%20first%20delay.png "Tank Drain Delay")
![alt text](image-1.png)
15.	Now you just need to wait till the trials have been completed.

![Clock GIFF](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmUzcGpvazBidmg5bDYwZW92c3B2MWhldW94aGxzZWttbnlqaTJ6cCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3oz8xKaR836UJOYeOc/giphy.gif "Clock GIFF")

16.	Once the trials have been completed you can open the .txt file named in step 11 in Excel.

![Compleated Text File](/Python%20PID%20Control%20Screenshots/HTUTPS_16_VSC%20Terminal%20after%20completion.png "Compleated Text File")
![alt text](image.png)
17.	That is how the python script runs and how the script will execute


## Importing the data to Excel

1.	Now you might be wondering about how to view the data well, fear not this is the section for you


2.	First open Excel and get to the home page like below

![Excel Home](/Python%20PID%20Control%20Screenshots/EFC_2_Excel%20Home%20page.png "Excel Home")

3.	Next hit “Open” then browse and navigate to the save folder

![Excel Open Page](/Python%20PID%20Control%20Screenshots/EFC_3_Excel%20open%20page.png "Excel Open Page")

4.	In this folder you won’t see anything

![Blank Folder](/Python%20PID%20Control%20Screenshots/EFC_4_Blank%20File%20explorer.png "Blank Folder")

5.	Next change the file type to “All files” in the bottom right corner

![All Files](/Python%20PID%20Control%20Screenshots/EFC_5_filled%20File%20explorer.png "All Files")

6.	Next select the run you want to open and click “open” in my case I am opening the “Example.txt”

![Selected File](/Python%20PID%20Control%20Screenshots/EFC_6_selected%20File%20explorer.png "Selected File")

7.	Next you will be prompted by the Text import Wizard. In the first window you want to select “Delimited” and “Next”

![Text Import Wizard 1](/Python%20PID%20Control%20Screenshots/EFC_7_Text%20import%20window.png "Text Import Wizard 1")

8.	Next Uncheck “Tab” and Check “Space” and hit “Finish”

![Text Import Wizard 2](/Python%20PID%20Control%20Screenshots/EFC_8_Text%20import%20finish%20window.png "Text Import Wizard 2")

9.	Congrats you have now imported the Text file to Excel

![Data Page](/Python%20PID%20Control%20Screenshots/EFC_9_imported%20data.png "Data Page")


![](/Python%20PID%20Control%20Screenshots "")


## Finding The COM port Manualy

1.	First hit “Windows key” and search for “device manager”.

![Device Manager](/Python%20PID%20Control%20Screenshots/HTUTPS_3_Device%20maneger%20search.png "Device Manager")

2.	next scroll down the list a look for “Ports(COM & LPT)” click the drop down and look for the “USB Serial Port (COMx)” this should be the required serial device before moving on take note of the COM port number (in this example it is “COM5”) you will need to add that information to the Python Script.

![COM Port Number](/Python%20PID%20Control%20Screenshots/HTUTPS_4_Device%20manager%20look%20for%20the%20COMport%20number.png "COM Port Number")
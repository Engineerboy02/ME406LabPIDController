# ME406 Lab PID Controller
ME 406 PID lab serial communication

This guide is for Windows 10 and 11 if you have another operating system you will need to make special changes to the installation and setup.


## How to Use the Python Script

1.	Head to the GitHub and Click on the “mainV1.1.exe”

![GitHub download Page](/Python%20PID%20Control%20Screenshots/HTUTPS/HTUTPS_1_download%20the%20exe%20part%201.png "GitHub download Page")

2.	Next download the “mainV1.1.exe” file and save to what ever folder you would like.

![GitHub exe download](/Python%20PID%20Control%20Screenshots/HTUTPS/HTUTPS_2_download%20the%20exe%20part%202.png "GitHub exe download")

3.	Next start by plugging in the serial interface to any USB port on your laptop the interface does require a USB Type A port.

![Serial Interface](/Python%20PID%20Control%20Screenshots/HTUTPS/HTUTPS_3_Serial%20Interface.png "Serial Interface")

4.	After plugging the interface in launch, the exe by double clicking on it after a small delay you should be prompted with a window that says, “Serial adapter selected and ready to run Please enter the end time in sec:” If you get this message move to step 5 if not head to trouble shooting the serial interface section of this document [(LINK to Manual COM port selection)](https://github.com/Engineerboy02/ME406LabPIDController/tree/main?tab=readme-ov-file#finding-the-com-port-manualy)

![exe serial interface sucess](/Python%20PID%20Control%20Screenshots/HTUTPS/HTUTPS_4_exe%20serial%20adapter%20sucess.png "exe serial interface sucess")

5.	You will then be asked a series of prompts in the terminal. The first prompt is the number of seconds you want to collect data for (see procedure for recommended time) when done hit “Enter” to go to the next prompt.

![Run Time](/Python%20PID%20Control%20Screenshots/HTUTPS/HTUTPS_5_end%20time.png "Run Time")

6.	The next prompt is for the desired number of samples to be taken during the timeline (see procedure for recommended number of samples) when done hit “Enter” to go to the next prompt.

![Number of samples](/Python%20PID%20Control%20Screenshots/HTUTPS/HTUTPS_6_number%20of%20samples.png "Number of samples")

7.	The next prompt is for the desired number of trials to be performed. The number of trials is the number of tank fills and empties (see procedure for recommended number of trials) when done hit “Enter” to go to the next prompt.

![Number of trials](/Python%20PID%20Control%20Screenshots/HTUTPS/HTUTPS_7_number%20of%20trials.png "Number of trials")

8.	The next prompt is the Output File Name this can be whatever you want it to be, and it will save to the same folder as the “MainV1.1.exe” file.

![File Name](/Python%20PID%20Control%20Screenshots/HTUTPS/HTUTPS_8_filename.png "File Name")

9.	The Final prompt is to make sure you are ready to run the experiment when ready hit “Enter”.

![Ready to Run](/Python%20PID%20Control%20Screenshots/HTUTPS/HTUTPS_9_ready%20to%20run%20confirmation.png "Ready to Run")

10.	Once you hit run you should get the output below and the number will slowly count up to the final number of samples.

![Initial Run](/Python%20PID%20Control%20Screenshots/HTUTPS/HTUTPS_10_Run%20Sampiling.png "Initial Run")

11.	After the run there will be a delay after the run to let the tank drain. The script polls data from the controller until the tank is “Empty” then stats again appending to the existing python file.

![Tank Drain Delay](/Python%20PID%20Control%20Screenshots/HTUTPS/HTUTPS_11_VSC%20Terminal%20during%20first%20delay.png "Tank Drain Delay")

12.	Now you just need to wait till the trials have been completed.

![Clock GIFF](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmUzcGpvazBidmg5bDYwZW92c3B2MWhldW94aGxzZWttbnlqaTJ6cCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3oz8xKaR836UJOYeOc/giphy.gif "Clock GIFF")

13.	Once the trials have been completed you can open the .txt file named in step 11 in Excel.

![Compleated Text File](/Python%20PID%20Control%20Screenshots/HTUTPS/HTUTPS_13_VSC%20Terminal%20after%20completion.png "Compleated Text File")

14.	That is how the python script runs and how the script will execute


## Importing the data to Excel

1.	Now you might be wondering about how to view the data well, fear not this is the section for you


2.	First open Excel and get to the home page like below

![Excel Home](/Python%20PID%20Control%20Screenshots/Excel/EFC_2_Excel%20Home%20page.png "Excel Home")

3.	Next hit “Open” then browse and navigate to the save folder

![Excel Open Page](/Python%20PID%20Control%20Screenshots/Excel/EFC_3_Excel%20open%20page.png "Excel Open Page")

4.	In this folder you won’t see anything

![Blank Folder](/Python%20PID%20Control%20Screenshots/Excel/EFC_4_Blank%20File%20explorer.png "Blank Folder")

5.	Next change the file type to “All files” in the bottom right corner

![All Files](/Python%20PID%20Control%20Screenshots/Excel/EFC_5_filled%20File%20explorer.png "All Files")

6.	Next select the run you want to open and click “open” in my case I am opening the “Example.txt”

![Selected File](/Python%20PID%20Control%20Screenshots/Excel/EFC_6_selected%20File%20explorer.png "Selected File")

7.	Next you will be prompted by the Text import Wizard. In the first window you want to select “Delimited” and “Next”

![Text Import Wizard 1](/Python%20PID%20Control%20Screenshots/Excel/EFC_7_Text%20import%20window.png "Text Import Wizard 1")

8.	Next Uncheck “Tab” and Check “Space” and hit “Finish”

![Text Import Wizard 2](/Python%20PID%20Control%20Screenshots/Excel/EFC_8_Text%20import%20finish%20window.png "Text Import Wizard 2")

9.	Congrats you have now imported the Text file to Excel

![Data Page](/Python%20PID%20Control%20Screenshots/Excel/EFC_9_imported%20data.png "Data Page")


![](/Python%20PID%20Control%20Screenshots "")


## Finding The COM port Manualy

1.	First hit “Windows key” and search for “device manager”.

![Device Manager](/Python%20PID%20Control%20Screenshots/COM/COM_3_Device%20maneger%20search.png "Device Manager")

2.	next scroll down the list a look for “Ports(COM & LPT)” click the drop down and look for the “USB Serial Port (COMx)” this should be the required serial device before moving on take note of the COM port number (in this example it is “COM5”) you will need to add that information to the Python Script.

![COM Port Number](/Python%20PID%20Control%20Screenshots/COM/COM_4_Device%20manager%20look%20for%20the%20COMport%20number.png "COM Port Number")

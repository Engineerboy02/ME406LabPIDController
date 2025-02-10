# ME406 Lab PID Controller
ME 406 PID lab serial communication

This guide is for Windows 10 and 11 if you have another operating system you will need to make special changes to the installation and setup.


## How to Use the Python Script

1.  Navigate to the releases section of this Github and download the Source code (zip) file:

![image](https://github.com/user-attachments/assets/596fd35e-56a0-452c-bb92-30650369579d)

2.	Locate the 'ME406LabPIDController-ME406.zip' file and extract this into a desired folder for this class (ME406). 

![image](https://github.com/user-attachments/assets/00335b1d-320d-4746-bf5c-5efcdb70adb7)

3. After the *.zip file has been extracted, ensure that the serial interface is plugged into any USB A port on your device. 

![Serial Interface](/Python%20PID%20Control%20Screenshots/HTUTPS/HTUTPS_3_Serial%20Interface.png "Serial Interface")

4.	Inside the extracted folder, the user can then run the 'ME406 PID Controller - Data Collection Script.exe' application:

![image](https://github.com/user-attachments/assets/3e050b5e-3f78-4984-a3c6-fa4433675a9a)

If the COM Port was able to detect properly, the following terminal window should appear with the following prompt: "Serial adapter selected and ready to run. Please enter the end time in sec:". Move to the next step if this is the case.

![exe serial interface sucess](/Python%20PID%20Control%20Screenshots/HTUTPS/HTUTPS_4_exe%20serial%20adapter%20sucess.png "exe serial interface sucess")

**Note**: If the "USB COM Port NOT found. Double check connections" appears, refer to the following instructions to locate and input the COM port manually: [(Instructions for COM Port Selection)](https://github.com/Engineerboy02/ME406LabPIDController/tree/main?tab=readme-ov-file#finding-the-com-port-manualy)

5.	In the first prompt, "Please enter the end time in sec: ", refer to the Group 1 Procedure Report for the recommended time. Press **Enter** on your keyboard to go to the next prompt.

![Run Time](/Python%20PID%20Control%20Screenshots/HTUTPS/HTUTPS_5_end%20time.png "Run Time")

6.	For the "Please enter the Number of Samples:" prompt, enter the number of samples to collect for each sample. Refer to the Group 1 Procedure Report for the recommended number. Press **Enter** on your keyboard to go to the next prompt.

![Number of samples](/Python%20PID%20Control%20Screenshots/HTUTPS/HTUTPS_6_number%20of%20samples.png "Number of samples")

7.	In the "Please enter the Number of Trials:" prompt, enter the number of trials to perform. Trials are run automatically and are based on how long you set the end time to be. When the end time is reached, the program will automatically wait until the tank drains and then immediately start the next trial. Refer to the Group 1 Procedure Report for the recommended number. Press **Enter** on your keyboard to go to the next prompt.

![Number of trials](/Python%20PID%20Control%20Screenshots/HTUTPS/HTUTPS_7_number%20of%20trials.png "Number of trials")

8.	A prompt asking for the Output File Name will be asked next. This can be whatever you want it to be. The file will be saved in the same folder as the 'ME406LabPIDController' folder. Press **Enter** on your keyboard to go to the next prompt.

![File Name](/Python%20PID%20Control%20Screenshots/HTUTPS/HTUTPS_8_filename.png "File Name")

9.	The last prompt will confirm if you are ready to start the data collection. Press **Enter** on your keyboard to continue.

![Ready to Run](/Python%20PID%20Control%20Screenshots/HTUTPS/HTUTPS_9_ready%20to%20run%20confirmation.png "Ready to Run")

10.	At this point, the pump should be running and an output counting to the final number of samples will display. 

![Initial Run](/Python%20PID%20Control%20Screenshots/HTUTPS/HTUTPS_10_Run%20Sampiling.png "Initial Run")

11.	When the final number of samples is reached, the program will suspend until the tank is drained to a preset value. Once the script determines that the tank is "empty," the next trial will begin with the pump turning on again. The collected data will append onto the existing *.txt file. 

![Tank Drain Delay](/Python%20PID%20Control%20Screenshots/HTUTPS/HTUTPS_11_VSC%20Terminal%20during%20first%20delay.png "Tank Drain Delay")

12.	Now you just need to wait till the trials have been completed.

![Clock GIFF](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmUzcGpvazBidmg5bDYwZW92c3B2MWhldW94aGxzZWttbnlqaTJ6cCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3oz8xKaR836UJOYeOc/giphy.gif "Clock GIFF")

13.	After all trials are complete, the *.txt file named in Step 11 can then be opened and imported into Excel (see the next section).

![CompletedText File](/Python%20PID%20Control%20Screenshots/HTUTPS/HTUTPS_13_VSC%20Terminal%20after%20completion.png "Compleated Text File")

14.	At this point, the application should be closed. Open a new instance of the app to start collecting new data, as needed.


## Importing the data to Excel
Now... you may also be wondering how to import the data into Excel. Fear not, this is the section for you!! (or you can just google it)

1.	First, open Excel and click on the **File** Tab.

![Excel Home](/Python%20PID%20Control%20Screenshots/Excel/EFC_2_Excel%20Home%20page.png "Excel Home")

2.	Next, click on **Open** to then browse and navigate to where the *.txt file is that was made in the previous data collecting section.

![Excel Open Page](/Python%20PID%20Control%20Screenshots/Excel/EFC_3_Excel%20open%20page.png "Excel Open Page")

3.	Inside the folder (without having selected anything yet), ensure that **All Files (*.*)** is seleced, in the Bottom Right Corner.

![All Files](/Python%20PID%20Control%20Screenshots/Excel/EFC_5_filled%20File%20explorer.png "All Files")

6.	Select the *.txt file to run and click on **Open** to open the file inside Excel. For this example, we are using "Example.txt"

![Selected File](/Python%20PID%20Control%20Screenshots/Excel/EFC_6_selected%20File%20explorer.png "Selected File")

7.	Through Excel's _Text Import Wizard_, ensure that **Delimited**. Click on **Next** to contiue.

![Text Import Wizard 1](/Python%20PID%20Control%20Screenshots/Excel/EFC_7_Text%20import%20window.png "Text Import Wizard 1")

8.	In the next window, ensure that ONLY **Space** under the _Delimiters_ section. Click **Finish** to continue. 

![Text Import Wizard 2](/Python%20PID%20Control%20Screenshots/Excel/EFC_8_Text%20import%20finish%20window.png "Text Import Wizard 2")

9.	Congrats!! You have now imported the Text file to Excel.

![Data Page](/Python%20PID%20Control%20Screenshots/Excel/EFC_9_imported%20data.png "Data Page")

10.	[_**IMPORTANT!!**_](https://media.istockphoto.com/id/1315339539/photo/red-stamp-with-megaphone-important.jpg?s=612x612&w=0&k=20&c=GpG7P_-hz9uCHkAdisa0fJqzaWOBcm_MpqtfDKr0B24=) Be sure to SAVE AS the Excel file as an .xlsx file. The file opened here will remain as a .txt file otherwise, making it hard to reopen in the future. Have fun!


## Finding The COM port Manualy

1.	First hit “Windows key” and search for “device manager”.

![Device Manager](/Python%20PID%20Control%20Screenshots/COM/COM_3_Device%20maneger%20search.png "Device Manager")

2.	Next, scroll down the list a look for “Ports(COM & LPT)” click the drop down and look for the “USB Serial Port (COMx)” this should be the required serial device before moving on take note of the COM port number (in this example it is “COM5”) you will need to add that information to the Python Script.

![COM Port Number](/Python%20PID%20Control%20Screenshots/COM/COM_4_Device%20manager%20look%20for%20the%20COMport%20number.png "COM Port Number")

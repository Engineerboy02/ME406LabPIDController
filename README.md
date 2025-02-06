# ME406LabPIDController
ME 406 PID lab Serial communication

This guide it for Windows 10 and 11 if you have another operating system you will need to make special changes to the installation and setup

## Install Visual studio
Only required if you don't have Visual studio installed already

1.	Download the installer [Visual Studio Code Download link](https://code.visualstudio.com/Download)

![Download VSC](/Python%20PID%20Control%20Screenshots/IVS_0_Download%20VSC.jpg "Download VSC")

2.	Once downloaded launch the installer
3.	Once launched it will ask for setting see screen shots for the info

![Licence Agreement](/Python%20PID%20Control%20Screenshots/IVS_1_LicenceAgreemanet.png "Licence Agreement")
![Install Path](/Python%20PID%20Control%20Screenshots/IVS_2_Select%20install%20Path.png "install path")
![Start menu folder](/Python%20PID%20Control%20Screenshots/IVS_3_Select%20start%20menue%20folder.png "Start menu folder")

**Desktop shortcut not required**

![Desktop short cut](/Python%20PID%20Control%20Screenshots/IVS_4_creat%20desktop%20icon.png "Desktop shortcut")
![Ready to install](/Python%20PID%20Control%20Screenshots/IVS_5_ready%20to%20install.png "Ready to install")

4.	Finish and launch VSC

![Installing](/Python%20PID%20Control%20Screenshots/IVS_6_Installing.png "Installing")

5.	Done end image

![Install finished](/Python%20PID%20Control%20Screenshots/IVS_7_VSC%20installed%20finish.jpg "Install finished")

6. Congrats you have now installed  Visual Studio Code


## Set up Visual Studio Code for python
   The interpreter and the Python extension must be installed in addition to the Visual Studio program. If you have previously installed the interpreter prior to this lab continue to step 8 to install the Python extension.  If both have been previously installed continue to step 15 with a new .py file opened. In the event neither the interpreter and Python extension have not been installed follow the steps below.


1.	Open Visual Studio code to the main page

![Main Window](/Python%20PID%20Control%20Screenshots/SUVS_1_Main%20window.png "Main Window")

2.	File -> New text file

![New Text File](/Python%20PID%20Control%20Screenshots/SUVS_2_newtextfile.png "New Text File")

3.	Select a language

![Select a Language](/Python%20PID%20Control%20Screenshots/SUVS_2A_LanguageSelection.png "Select a Language")

4.	Search “Python” and hit enter

![Language selection 2](/Python%20PID%20Control%20Screenshots/SUVS_2b_LanguageSelection.png "Language selection 2")

5.	In the bottom right a box should appear asking to install the “Python extension for Visual Studio Code” hit Install

![extension install](/Python%20PID%20Control%20Screenshots/SUVS_3_install%20python%20extension.png "extension install")

6.	After hitting enter you should be brought to a page like below click install and wait for it to insall before moving on

![Extension install page](/Python%20PID%20Control%20Screenshots/SUVS_4_click%20to%20the%20untitiled%20tab.png "Extension install page")

7.	After installation go back to the untitled-1 file by clicking it in the file tabs

![File Tabs](/Python%20PID%20Control%20Screenshots/SUVS_4b_click%20to%20the%20untitiled%20tab.png "File Tabs")

8.	Next go to the bottom right of the screen and click on the “Select interpreter”

![interperter selection](/Python%20PID%20Control%20Screenshots/SUVS_5b_interpreterselection.png "interperter selection")

9.	Next in the top middle click on "python not installed click for instructions"

![Click for instructions](/Python%20PID%20Control%20Screenshots/SUVS_6_python%20click%20for%20instructions.jpg "Click for instructions")

10.	It will open the Microsoft store click "install" and wait for it to complete

![python install](/Python%20PID%20Control%20Screenshots/(13)%20Python%20Install.jpg "python install")

11.	After it has been installed exit the Microsoft store and head back to VSC

![Back to VSC](/Python%20PID%20Control%20Screenshots/SUVS_6a_back%20to%20VSC.png "Back to VSC")

12.	Again, go to the bottom right of the screen and click on the “Select interpreter”

![interperter selection](/Python%20PID%20Control%20Screenshots/SUVS_5b_interpreterselection.png "interperter selection")

13.	In the top middle click on “Python 3.11.x …."

![Selecting the Interpreter](/Python%20PID%20Control%20Screenshots/SUVS_6_after%20python%20instalation.png "Selecting the Interpreter")

14.	The text that once said “Select interpreter” should now say “3.11.9 Microsoft store”

![Interpreter selected](/Python%20PID%20Control%20Screenshots/SUVS_8_interpreter%20selected.png "Interpreter selected")

15.	To test the installation copy or type ```print(“Hello, world”)``` into the unnamed python file we created in step 1

![Test Script](/Python%20PID%20Control%20Screenshots/SUVS_9_test%20script.png "Test Script")

16.	To run hit the Triangle  ![Run Button](/Python%20PID%20Control%20Screenshots/SUVS_10_run%20button.png "Run Button")   in the top of the window to run

![Run Button Global](/Python%20PID%20Control%20Screenshots/SUVS_10b_runbutton%20location.png "Run Button Global")

17.	When prompted to save the file to a place of your choosing (ex. Downloads folder)

18.	After which you should get the following output in the terminal on the bottom of your screen

![Successfull run](/Python%20PID%20Control%20Screenshots/SUVS_11_output%20of%20sucessfull%20run.png "Sucessfull Run")

19.	Congratulations you have set python up in Visual Studio Code


## File download from GitHub

1.	Navigate to the GitHub Page at this [GitHub link](https://github.com/Engineerboy02/ME406LabPIDController/tree/main?tab=readme-ov-file#set-up-vsc-for-python)

![GitHub Page](/Python%20PID%20Control%20Screenshots/FDFGH_1_navigate%20to%20the%20git%20hub%20page.png "GitHub Page")

2.	Once there click on the Green “<>Code” button

![Code Button](/Python%20PID%20Control%20Screenshots/FDFGH_2_click%20on%20the%20green%20Button.png "Code Button")

3.	Then click on Download zip and save it to a place you can find later

![Download button](/Python%20PID%20Control%20Screenshots/FDFGH_3_click%20on%20download%20zip.png "Download button")

4.	Next navigate to the folder you saved the zip to

![Zip Folder Loaction](/Python%20PID%20Control%20Screenshots/FDFGH_4_navigate%20to%20the%20save%20folder.png "Zip Folder Loaction")

5.	Next right click on the zip and hit extract all 

![Extract](/Python%20PID%20Control%20Screenshots/FDFGH_5_Extract%20zip.png "Extract")

6.	Next you should be prompted for a save location select a place for it to extract to and hit extract

![Extract Location](/Python%20PID%20Control%20Screenshots/FDFGH_6_exctract%20location.png "Extract Location")

7.	Next it should open a new file explorer with the extracted files

![NEWFX](/Python%20PID%20Control%20Screenshots/FDFGH_7_exctract%20location%20in%20FEX.png "NEWFX")

8.	Enter the displayed folder and it should give you what is seen below

![Displayed folder](/Python%20PID%20Control%20Screenshots/FDFGH_8A_VSC%20Home%20page.png "Displayed folder")

9.	Take note of the save location by right clicking on the file tree and clicking “copy address” then head to Visual Studio Code

![Save Location](/Python%20PID%20Control%20Screenshots/FDFGH_9b_save%20location.png "Save Location")

![VSC Home Screen](/Python%20PID%20Control%20Screenshots/FDFGH_8_VSC%20Home%20page.png "VSC Home Screen")

10.	once in visual studio code click on “File” then “Open Folder”

![VSC open folder](/Python%20PID%20Control%20Screenshots/FDFGH_10_VSC%20navigat%20to%20folder%20path.png "VSC open folder")

11.	Next navigate to the folder by pasting the file path you copied earlier and click “select folder”

![VSC open folder](/Python%20PID%20Control%20Screenshots/FDFGH_11_VSC%20navigat%20to%20folder%20path.png "VSC open folder")

12.	Once opened you should see something like this

![VSC Opened folder](/Python%20PID%20Control%20Screenshots/FDFGH_12_VSC%20something%20like%20this.png "VSC Opened folder")

13.	Click on the “main().py” on the left task bar and it should open the file in the tabs

![VSC Open Main.py](/Python%20PID%20Control%20Screenshots/FDFGH_13_VSC%20something%20like%20this.png "VSC Open Main.py")

14.	Now you should see the file open just like below

![VSC Open File](/Python%20PID%20Control%20Screenshots/FDFGH_14_VSC%20something%20like%20this%20opened.png "VSC Open File")

15.	Double check that your interpreter is selected before moving on

![VSC Interpreter check](/Python%20PID%20Control%20Screenshots/FDFGH_15_VSC%20correct%20interpreter.png "VSC Interpreter check")

16.	Next time to install the required libraries click on “Terminal” in the top ribbon

![VSC Termianl](/Python%20PID%20Control%20Screenshots/FDFGH_16_VSC%20terminal.png "VSC Termianl")

17.	Then hit “New Terminal”

![VSC New Terminal](/Python%20PID%20Control%20Screenshots/FDFGH_17_VSC%20new%20terminal.png "VSC New Terminal")

18.	In the terminal type or copy ```pip install -r requirements.txt```(paste by right clicking in the terminal) and hitting enter

![VSC PIP Reqs](/Python%20PID%20Control%20Screenshots/FDFGH_18_VSC%20screen%20with%20terminal.png "VSC PIP Reqs")

 If the command above creates a file not found error replace the "requirements.txt" with the relative path of the file by right clicking "requirements.txt" file in the left menu and selecting "Copy Relative Path" then past into the terminal replacing the "Requirements.txt" and hit enter and the requirements should install.

 ![VSC PIP Reqs solution](/Python%20PID%20Control%20Screenshots/FDFGH_18a_VSC%20pip%20install%20command%20relative%20path.png "VSC PIP Reqs solution")


19.	When it is done you should get something like the following with no errors

![VSC Terminal Done](/Python%20PID%20Control%20Screenshots/FDFGH_19_VSC%20pip%20install%20command.png "VSC Terminal Done")

20.	Now you are ready to go see the next section on how to set the parameters and run the script


## How to Use the Python Script

1.	Once loaded into Visual studio Code with the required libraries you should be ready to run after a few settings that need to be checked.

![VSC Terminal](/Python%20PID%20Control%20Screenshots/FDFGH_18_VSC%20screen%20with%20terminal.png "VSC Terminal")

2.	First start by plugging in the serial interface to any USB port on your laptop does require a USB Type A port.

![Serial Interface](/Python%20PID%20Control%20Screenshots/HTUTPS_2_Serial%20Interface.png "Serial Interface")

3.	Second hit “Windows key” and search for “device manager”

![Device Manager](/Python%20PID%20Control%20Screenshots/HTUTPS_3_Device%20maneger%20search.png "Device Manager")

4.	Scroll down the list a look for “Ports(COM & LPT)” click the drop down and look for the “USB Serial Port (COMx)” this should be the required serial device before moving on take note of the COM port number (in this example it is “COM5”) you will need to add that information to the Python Script.

![COM Port Number](/Python%20PID%20Control%20Screenshots/HTUTPS_4_Device%20manager%20look%20for%20the%20COMport%20number.png "COM Port Number")

5.	Now head back to Visual Studio Code and navigate to the “Main().py” file

![Back To VSC main().py](/Python%20PID%20Control%20Screenshots/HTUTPS_5_Heading%20Back%20to%20VSC.png "Back To VSC main().py")

6.	Now on Line 16 it says `port = 'COM3'  # Update to your serial port` change the “COM3” to what you found in device manager so in my example the line will now read `port = 'COM5'  # Update to your serial port`

![COM Port Number in VSC](/Python%20PID%20Control%20Screenshots/HTUTPS_6_Updating%20the%20COM%20number%20in%20VSC.png "COM Port Number in VSC")

7.	To run hit the Triangle  ![Run button](/Python%20PID%20Control%20Screenshots/SUVS_10_run%20button.png "Run Button")   in the top of the window to run 

![Run Button Global](/Python%20PID%20Control%20Screenshots/HTUTPS_7_Run%20Button%20location%20in%20VSC.png "Run Button Global")

8.	You will then be asked a series of prompts in the terminal at the bottom of the screen the first prompt is ether the number of seconds you want to collect data for (see procedure for recommended time) when done hit enter to go to the next prompt

![Run Time](/Python%20PID%20Control%20Screenshots/HTUTPS_8_VSC%20Terminal%20during%20run%20time.png "Run Time")

9.	The next prompt is for the desired number of samples to be taken during to timeline (see procedure for recommended number of samples) when done hit enter to go to the next prompt

![Number of samples](/Python%20PID%20Control%20Screenshots/HTUTPS_9_VSC%20Terminal%20during%20run%20time%20number%20of%20samples.png "Number of samples")

10.	The next prompt is for the desired number of trials to be performed. The number of trials is the number of tank fills and empties (see procedure for recommended number of trials) when done hit enter to go to the next prompt

![Number of trials](/Python%20PID%20Control%20Screenshots/HTUTPS_10_VSC%20Terminal%20during%20run%20time%20number%20of%20trials.png "Number of trials")

11.	The next prompt is the Output File Name this can be whatever you want it to be and it will save to the same folder as the “Main().py” file 

![File Name](/Python%20PID%20Control%20Screenshots/HTUTPS_11_VSC%20Terminal%20during%20run%20time%20output%20file%20name.png "File Name")

12.	The Final prompt is to make sure you are ready to run the experiment when ready hit enter

![Ready to Run](/Python%20PID%20Control%20Screenshots/HTUTPS_12_VSC%20Terminal%20during%20run%20time%20enter%20to%20start%20sampiling.png "Ready to Run")

13.	Once you hit run you should get the output below and the number will slowly count up to the final number of samples

![Initial Run](/Python%20PID%20Control%20Screenshots/HTUTPS_13_VSC%20Terminal%20during%20run%20time%20initial%20output.png "Initial Run")

14.	After the run there will be a delay after the run to let the tank drain. The script polls data from the controller until the tank is “Empty” then stats again appending to the existing python file

![Tank Drain Delay](/Python%20PID%20Control%20Screenshots/HTUTPS_14_VSC%20Terminal%20during%20first%20delay.png "Tank Drain Delay")

15.	Now you just need to wait till the trials have been completed

![Clock GIFF](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmUzcGpvazBidmg5bDYwZW92c3B2MWhldW94aGxzZWttbnlqaTJ6cCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3oz8xKaR836UJOYeOc/giphy.gif "Clock GIFF")

16.	Once the trials have been completed you can open the .txt file named in step 11 in Excel

![Compleated Text File](/Python%20PID%20Control%20Screenshots/HTUTPS_16_VSC%20Terminal%20after%20completion.png "Compleated Text File")

17.	You will need to select "delimited" by **SPACE** in order to get the data organized

![](/Python%20PID%20Control%20Screenshots "")

18.	That is how the python script runs and what things you need to change to get your data

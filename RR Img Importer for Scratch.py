#Instalations
import pyautogui #For prompts & keyboard controls
import time #For delays in order to stabalize
import ctypes #To get resolution

#Initialization:
userRes = (ctypes.windll.user32.GetSystemMetrics(78), ctypes.windll.user32.GetSystemMetrics(79)) #Supposed to get total res if has multi monitor set up, probaly just better to manually setup with the prompts, but ye
halfWidth = int(userRes[0] * 0.5) #Used more than once, so precalculated
taskbarKeys = "win"

#Preset to defaults
mouseLocations = [
    (int(userRes[0] * 0.6036585365853658), int(userRes[1] * 0.1291913214990138)), #Enter Scratch
    (int(userRes[0] * 0.5482261640798226), int(userRes[1] * 0.26528599605522685)), #Copy
    (int(userRes[0] * 0.01164079822616408), int(userRes[1] * 0.5)), #Enter Rec/Submit
    (halfWidth, int(userRes[1] * 0.3116370808678501)), #Paste
    (halfWidth, int(userRes[1] * 0.9674556213017751)), #Browser
]

#Setup:
#Set mouse locations
texts = [
    "the tab running scratch (NOT the project itself)",
    "the item read bay in scratch (make sure it's RIGHT infront)",
    "near the left edge of your screen (make sure it's not on the item input menu)",
    "the item input box in Rec",
    "your browser in the task bar"
]
for i in range(5):
    input = pyautogui.prompt(title="RR Img Importer: Mouse Locations Setup",text="Press \"Enter\" when mouse is hovering over " + texts[i] + ". (Enter \"d\" for default, anything else to skip the rest of setup}")
    if input == "" or input == "d":
        mouseLocations[i] = mouseLocations[i] if input == "d" else pyautogui.position()
    else:
        break
#Inputs
if input == "" or input == "d":
    taskbarKeys = (pyautogui.prompt(title="Image Data Importer: Setup", text="Enter the key name or key combination that reveals the taskbar\n\nFor example, Windows: win"))
count = int(pyautogui.prompt(title="Image Data Importer: Setup", text="Enter scratch list length after loading compiled"))
delay = float(pyautogui.prompt(title="Image Data Importer: Setup", text="Enter delay (0.1 is recommended). (helps success of data being transfered)\n\n* AUTOMATION WILL BEGIN ONCE SUBMITTED:\nMake sure you;re in the data importer seat with trigger in right & Makerpen set to \"Connect\" in the left hand, & the browser is open with the scratch project active"))

#Automation:
for i in range(count):
    #Copy Data from Scratch:
    pyautogui.leftClick(mouseLocations[0][0], mouseLocations[0][1]) #Enter Scratch project
    pyautogui.press("h") #Get item (Scratch exclusive)
    time.sleep(delay)
    pyautogui.tripleClick(mouseLocations[1][0], mouseLocations[1][1], button="left") #Select entire item
    pyautogui.hotkey("ctrl", "c") #Copy

    #Paste Data into Rec:
    pyautogui.doubleClick(mouseLocations[2][0], mouseLocations[2][1], button="left") #Enetr Rec, Open Rec Item
    time.sleep(delay)
    pyautogui.leftClick(mouseLocations[3][0], mouseLocations[3][1]) #Edit item text feild
    pyautogui.hotkey("ctrl", "v") #Paste
    pyautogui.leftClick(mouseLocations[2][0], mouseLocations[2][1]) #Submit
    pyautogui.rightClick() #Move down a port (should be using the data importer seat)
    pyautogui.hotkey(taskbarKeys) #Show taskbar to enter browser
    pyautogui.leftClick(mouseLocations[4][0], mouseLocations[4][1]) #Open Browser
pyautogui.leftClick(mouseLocations[2][0], mouseLocations[2][1]) #Enter Rec
pyautogui.press("space") #Exit seat
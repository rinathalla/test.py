import pyautogui
pyautogui.size()
#Size(width=1366, height=768)
pyautogui.position()
#Point(x=169, y=639)
pyautogui.moveTo(10,10, duration=1.5)    #move mouse cursor to upperleft corner
pyautogui.moveRel(200,0,duration=2)      #move mouse cursor to horizontal X-axis
pyautogui.moveRel(0,-100,duration=2)     #move mouse cursor to vertically Y-axis
pyautogui.position()   #execute this by placing cursor the position you want
#Point(x=448, y=31)
pyautogui.click(448,31)
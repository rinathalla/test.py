import pyautogui

pyautogui.click()  # click to put drawing program in focus
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=1)  # move right
    distance = distance - 25
    pyautogui.dragRel(0, distance, duration=1)  # move down
    pyautogui.dragRel(-distance, 0, duration=1)  # move left
    distance = distance - 25
    pyautogui.dragRel(0, -distance, duration=1)  # move up

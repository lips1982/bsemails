import pyautogui as pyau
import time
linea="HOLAAAAAAAAAAAAAAAAAAAAAAA"
#pyau.mouseInfo()

time.sleep(3)
pyau.moveTo(448,116)
time.sleep(1)
time.sleep(2)
pyau.moveTo(237,183)
pyau.click(237,183)
time.sleep(1)
pyau.moveTo(448,116)
time.sleep(1)
pyau.moveTo(448,116)
time.sleep(1)
pyau.click(448,116)
time.sleep(1)
pyau.hotkey('ctrl', 'c')
time.sleep(1)
pyau.hotkey('alt', 'f4')
time.sleep(2)
pyau.moveTo(448,77)
time.sleep(1)
pyau.moveTo(448,77)
pyau.click(448,77)
time.sleep(2)
pyau.hotkey('ctrl', 'v')
pyau.hotkey('enter')
time.sleep(5)
pyau.moveTo(1019,372)
pyau.click(1019,372)
pyau.click(1019,372)
time.sleep(1)
pyau.hotkey('tab')
time.sleep(1)
pyau.hotkey('tab')
time.sleep(1)
pyau.hotkey('enter')
pyau.moveTo(1019,372)
pyau.moveTo(1019,372)
pyau.click(1019,372)
pyau.click(1019,372)
pyau.hotkey('pgdn')
time.sleep(1)
pyau.hotkey('pgdn')
time.sleep(1)
pyau.hotkey('pgdn')
time.sleep(1)
pyau.moveTo(760,570)
pyau.moveTo(760,570)

pyau.click(760,570)
pyau.click(760,570)
pyau.click(760,570)
time.sleep(10)
with open("gcloud.txt", "a") as f:
    f.write(f"{linea}\n")
    f.close()  
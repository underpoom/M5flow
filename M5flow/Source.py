from m5stack import *
from m5ui import *
from uiflow import *
import wifiCfg
import urequests

setScreenColor(0x222222)




label0 = M5TextBox(8, 105, "Text", lcd.FONT_DejaVu40,0xFFFFFF, rotate=0)


wifiCfg.doConnect('Longinus', 'ppppppppp')
try:
  req = urequests.request(method='GET', url='https://m5flow.firebaseio.com/Test1/text.json')
  if (req.text).replace('"\\"', '').replace('\\""', '')=='#ff05f7':
    setScreenColor(0xcc66cc)
  elif (req.text).replace('"\\"', '').replace('\\""', '')=='#1789ff':
    setScreenColor(0x3366ff)
  elif (req.text).replace('"\\"', '').replace('\\""', '')=='#0000ff':
    setScreenColor(0x3333ff)
  elif (req.text).replace('"\\"', '').replace('\\""', '')=='#00ff00':
    setScreenColor(0x33cc00)
  elif (req.text).replace('"\\"', '').replace('\\""', '')=='#ffff00':
    setScreenColor(0xffff00)
  elif (req.text).replace('"\\"', '').replace('\\""', '')=='#ffc800':
    setScreenColor(0xff6666)
  elif (req.text).replace('"\\"', '').replace('\\""', '')=='#ff0000':
    setScreenColor(0xff0000)
  else:
    pass
except:
  pass
try:
  req = urequests.request(method='GET', url='https://m5flow.firebaseio.com/Test1/color.json')
  if (req.text).replace('"\\"', '').replace('\\""', '')=='#00ffff':
    label0.setColor(0x33ccff)
  elif (req.text).replace('"\\"', '').replace('\\""', '')=='#ffddfc':
    label0.setColor(0xffddfc)
  elif (req.text).replace('"\\"', '').replace('\\""', '')=='#ffafaf':
    label0.setColor(0xffafaf)
  elif (req.text).replace('"\\"', '').replace('\\""', '')=='#cccccc':
    label0.setColor(0xcccccc)
  elif (req.text).replace('"\\"', '').replace('\\""', '')=='#ffffff':
    label0.setColor(0xffffff)
  elif (req.text).replace('"\\"', '').replace('\\""', '')=='#dbffdc':
    label0.setColor(0xdbffdc)
  elif (req.text).replace('"\\"', '').replace('\\""', '')=='#000000':
    label0.setColor(0x000000)
  else:
    pass
except:
  pass
while True:
  try:
    req = urequests.request(method='GET', url='https://m5flow.firebaseio.com/Test1/data.json')
    label0.setText(str((req.text).replace('"\\"', '').replace('\\""', '')))
  except:
    pass
  wait_ms(2)
import os
from datetime import date, timedelta, datetime
import tkinter as tk
from tkinter import filedialog

import variables as var

dateToday = date.today()

def updateLogVariable(stringToAdd):
  var.jobLog = var.jobLog + str(stringToAdd) + '\n'
  print(stringToAdd)

# Writes a local file with the content and filename as parameters
def writeToFile(output, fileName):
  fileName = dateToday.strftime('%Y-%m-%d') + ' ' + fileName + '.txt'
  if os.path.exists(fileName):
    os.remove(fileName)
  f = open(fileName, "x")
  f.write(output)
  f.close()
  print('"' + fileName + '" saved to local directory...')

def getFilePath():
  root = tk.Tk()
  root.withdraw()
  file_path = filedialog.askopenfilename()
  return file_path
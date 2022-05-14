import os
import tkinter as tk
from tkinter import filedialog

jobLog = ''

def updateLogVariable(stringToAdd):
  global jobLog
  jobLog = jobLog + str(stringToAdd) + '\n'

# Writes a local file with the content and filename as parameters
def writeTotxtFile(output, fileName):
  #fileName = dateToday.strftime('%Y-%m-%d') + ' ' + fileName + '.txt'
  fileName = fileName + '.txt'
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
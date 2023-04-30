import PySimpleGUI as sg
import serial
import time
 
ser = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)

sg.theme('LightBlue2')  # Set the theme
mes='1'
# Define the layout
layout = [[sg.Button('Show', font=('Arial', 12), button_color=('white', '#4CAF50'), key='process'),
           sg.Button('Hyper', font=('Arial', 12), button_color=('white', '#4CAF50'), key='button')],
          [sg.Output(s=(40,10), key='outputt')]]

# Create the window
window = sg.Window('ЕГЭ архив', layout,size=(1000,300))

# Event loop
while True:
    event, values = window.read()

    # Exit the app when the window is closed
    if event == sg.WINDOW_CLOSED:
        break

    # Process the input and update the output when the button is clicked
    if event == 'process':
        ser.write(mes.encode())
        if mes=='1':mes='0'
        else: mes='1'
        
        ser.flushInput()
        ser.flushOutput()

        
        
    if event == 'button':
        status=0
        mess='2'
        ser.write(mess.encode())
        L=''
        while status==0:
            line = ser.readline()
            L+=line.decode()
            print(L)
            L=L [L.index('x'):-2]
            if len(L)==4:
                status=1
                window['outputt'].update(L)
                L=''
        ser.flushInput()
        ser.flushOutput()

# Close the window
ser.close()
window.close()

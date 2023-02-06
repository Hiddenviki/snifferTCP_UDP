import PySimpleGUI as sg
import send



layout = [
    [sg.Text('Адресс отправителя'), sg.InputText()],
    [sg.Text('Адрес получателя'), sg.InputText()],
    [sg.Checkbox("TCP")],
    [sg.Checkbox("UDP")],
    [sg.Output(size=(88, 20))],
    [sg.Submit(), sg.Cancel()]
]
window = sg.Window('Генерация IPV4', layout)


def someIp(someShit):
    some_ip = "'" + someShit + "'"
    print(some_ip)
    return some_ip


while True:  # The Event Loop
    event, values = window.read()
    print(event, values)  # debug
    # 0 = ipFrom
    # 1 = ipTo
    # 2 = tcp true/false
    # 3= udp true/false

    if event == 'Submit':

        send.send(values[0], values[1])
        #192.168.43.44
        #00:F4:8D:EF:72:8D

    else:
        print("ЭЭ")

#
# window.close()

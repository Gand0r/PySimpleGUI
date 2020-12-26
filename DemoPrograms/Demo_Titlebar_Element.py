import PySimpleGUI as sg

"""
    The Custom Titlebar Demo
    Two ways of getting a custom titlebar:
    1. set_options - will create a titlebar that every window will have based on theme
    2. Titlebar element - Adds custom titlebar to your window
"""

sg.set_options(use_custom_titlebar=True)

def main():

    layout = [
              # [sg.Titlebar('My Custom Titlebar', background_color='light blue', text_color='red', k='-T-')],
              [sg.Text('My Window')],
              [sg.Input(k='-IN1-')],
              [sg.Input(k='-IN2-')],
              [sg.Input(k='-IN3-')],
              [sg.Button('Clear'), sg.Button('Popup'), sg.Button('Exit')]]

    # Use the same title so that when the window minimizes, the title will be the same as the custom titlebar title
    window = sg.Window('My Custom Titlebar', layout)

    while True:
        event, values = window()
        print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Clear':
            [window[k]('') for k in ('-IN1-', '-IN2-', '-IN3-')]
        elif event == 'Popup':
            sg.popup('This is a popup')

    window.close()

main()

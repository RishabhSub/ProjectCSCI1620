from gui_area import *


def main():
    """
    This function displays a window using tkinter GUI
    """
    window = Tk()
    widgets = GUI(window)

    window.title('Final Project')
    window.geometry('500x300')
    window.resizable(True, True)

    window.mainloop()


if __name__ == '__main__':
    main()

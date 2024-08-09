import tkinter
from view.plugin_name_frame import PluginNameFrame

def main():
    print("starting plugin name!")

    # show the view
    root = tkinter.Tk()
    frame = PluginNameFrame(root)
    frame.grid(column=0, row=0)
    root.mainloop()


if __name__ == "__main__":
    main()
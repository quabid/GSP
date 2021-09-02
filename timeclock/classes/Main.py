from tkinter import *
from tkinter import Tk
from threading import Thread
from custom_modules.index import CONSOLE_MESSENGER_SWITCH as cms, DIALOG_MESSENGER_SWITCH as dms, save_config, get_config, handle_window_open


class MainWindow(Tk):
    def __init__(this):
        super().__init__()
        this.h_scroller = Scrollbar(orient="horizontal")
        this.minsize(700, 500)
        this.maxsize(700, 500)
        this.parent = this
        # this.option__add('*tearOff', False)
        this.__contentpane = Frame(this)
        this.__contentpane.grid(column=1, row=1, sticky=E + W)
        this.__config = {}
        this.__WINDOW_TITLE_SWITCH = {
            'default': 'timer',
            'timer': 'timer',
            'stopwatch': 'stopwatch',
            'countdown': 'countdown'
        }
        this.title(this.__WINDOW_TITLE_SWITCH['default'])
        this.__menu_radio_var = StringVar()
        this.option_add('*tearOff', False)
        this.create_menu()
        this.check_config_thread()
        this.protocol("WM_DELETE_WINDOW", this.exit_prog)

    def create_menu(this):
        menubar = Menu(this)
        this['menu'] = menubar

        menu_file = Menu(menubar)
        menu_config = Menu(menubar)

        menubar.add_cascade(menu=menu_file, label='File')
        menubar.add_cascade(menu=menu_config, label='Config')

        menu_file.add_command(label='exit'.title(), command=this.exit_prog)

        menu_config.add_radiobutton(label='countdown'.title(),
                                    variable=this.__menu_radio_var,
                                    value='countdown',
                                    command=this.select_menu_radio_thread)

        menu_config.add_radiobutton(label='stopwatch'.title(),
                                    variable=this.__menu_radio_var,
                                    value='stopwatch',
                                    command=this.select_menu_radio_thread)

        menu_config.add_radiobutton(label='timer'.title(),
                                    variable=this.__menu_radio_var,
                                    value='timer',
                                    command=this.select_menu_radio_thread)

    def select_menu_radio_thread(this):
        select_radio_thread = Thread(target=this.select_menu_radio, args=())
        select_radio_thread.start()
        select_radio_thread = None

    def select_menu_radio(this):
        selected = this.__menu_radio_var.get()
        print('Selected Menu Option:\t{}'.format(selected))
        this.__config['mode'] = selected.strip()
        save_config(this.__config)
        # this.create_gui()

    def check_config_thread(this):
        config_thread = Thread(target=this.check_config, args=())
        config_thread.start()
        config_thread.join()
        config_thread = None

    def check_config(this):
        this.__config = get_config()

        if this.__config == None:
            save_config({'mode': 'timer'})
            this.check_config_thread()
        else:
            print("App Configuration:\t{}".format(this.__config))

    def start(this):
        this.create_gui()
        this.mainloop()

    def exit_prog(this):
        this.update_location()
        save_config(this.__config)
        this.parent.destroy()

    def create_gui(this):
        if 'coordinates' in this.__config:
            handle_window_open(this, this.__config['coordinates'])
        this.build_panel()

    def update_location(this):
        this.__config['coordinates'] = {
            'x': this.parent.winfo_rootx(),
            'y': this.parent.winfo_rooty()
        }
        success = cms['success']
        print("\n\t\t{}\n\n".format(
            success('Window\'s coordinates were updated')))

    def build_panel(this):
        mode = this.__config['mode']
        print('\n\tBuilding {} panel\n'.format(mode))

        if mode == 'timer':
            this.build_timer_panel_thread()
        elif mode == 'countdown':
            this.build_countdown_panel_thread()
        else:
            this.build_stopwatch_panel_thread()

    def build_timer_panel_thread(this):
        thread = Thread(target=this.build_timer_panel, args=())
        thread.start()
        thread.join()
        thread = None

    def build_countdown_panel_thread(this):
        thread = Thread(target=this.build_countdown_panel, args=())
        thread.start()
        thread.join()
        thread = None

    def build_stopwatch_panel_thread(this):
        thread = Thread(target=this.build_stopwatch_panel, args=())
        thread.start()
        thread.join()
        thread = None

    def build_timer_panel(this):
        mode = this.__config['mode']
        print('\t{} panel built\n'.format(mode))

    def build_countdown_panel(this):
        mode = this.__config['mode']
        print('\t{} panel built\n'.format(mode))

    def build_stopwatch_panel(this):
        mode = this.__config['mode']
        print('\t{} panel built\n'.format(mode))

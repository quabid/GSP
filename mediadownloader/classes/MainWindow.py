from tkinter import *
from threading import Thread
from custom_modules.index import CONSOLE_MESSENGER_SWITCH, handle_window_open, cls, save_config, get_config, be, DIALOG_MESSENGER_SWITCH as dms
from classes.WebScraper import Scraper as scr


class main(Tk):
    __main_window_title = "resource scraper"
    __scrape_frame = None
    __media_downloader_frame = None
    __config = {}
    __scrape_results = None
    __current_result_selected_item = None
    __current_result = None
    __current_tag = None
    __domain = None
    __domain_path = None

    def __init__(this):
        super().__init__()
        # cls()
        # Config main window
        this.scraper = scr()
        this.h_scroller = Scrollbar(orient="horizontal")
        this.minsize(700, 500)
        this.maxsize(700, 500)
        this.title(this.__main_window_title.title())
        this.parent = this
        this.option_add('*tearOff', False)
        # Initialize component vars
        this.__radio_var = StringVar()
        this.__spinbox_options_var = StringVar()
        this.__url_entry_var = StringVar()
        this.__scrape_results_frame = None
        this.__scrape_results_detail_frame = None
        this.create_menu()
        # Check for app's configuration file
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

        menu_config.add_radiobutton(label='scraper'.title(),
                                    variable=this.__radio_var,
                                    value='scraper',
                                    command=this.select_menu_radio_thread)
        menu_config.add_radiobutton(label='downloader'.title(),
                                    variable=this.__radio_var,
                                    value='downloader',
                                    command=this.select_menu_radio_thread)

    def check_config_thread(this):
        config_thread = Thread(target=this.check_config, args=())
        config_thread.start()
        config_thread.join()
        config_thread = None

    def check_config(this):
        this.__config = get_config()

        if this.__config == None:
            save_config({'mode': 'scraper'})
            this.check_config()
        print("App Configuration:\t{}".format(this.__config))

    def create_gui(this):
        if 'coordinates' in this.__config:
            handle_window_open(this, this.__config['coordinates'])

        if 'mode' in this.__config:
            if this.__config['mode'] == 'scraper':
                if None != this.__media_downloader_frame:
                    this.__media_downloader_frame.destroy()
                this.create_scraper()
                this.parent.title("scraper".title())
            else:
                if None != this.__scrape_frame:
                    this.__scrape_frame.destroy()
                this.create_downloader()
                this.parent.title("downloader".title())

    def start(this):
        this.create_gui()
        this.devmode()
        this.mainloop()

    def create_scraper(this):
        parent = this.parent

        this.__scrape_frame = Frame(parent)
        # this.__scrape_frame.grid(column=1, row=1, pady=5, padx=5)
        # this.__scrape_frame.pack(side=LEFT, fill=Y, padx=10)
        this.__scrape_frame.grid(column=1, row=1, sticky=N)

        label_frame = LabelFrame(this.__scrape_frame, text="url".upper())
        label_frame.grid(column=1, row=1, padx=18)
        # label_frame.pack(side=TOP)

        button_scrape = Button(label_frame,
                               text="scrape".title(),
                               font=("Helvetica", 13, 'bold'),
                               command=this.scrape_thread)

        url_entry = Entry(label_frame,
                          textvariable=this.__url_entry_var,
                          font=("Helvetica", 13, 'normal'),
                          width=55)

        url_entry.focus_set()

        # url_entry.pack(side=LEFT, padx=5, ipady=5, pady=5)
        url_entry.grid(column=1, row=1, ipady=5, pady=5, padx=4)

        # button_scrape.pack(side=RIGHT, padx=5, pady=5)
        button_scrape.grid(column=2, row=1, pady=5, padx=5)

    def create_downloader(this):
        this.__spinbox_options_var = StringVar()
        spinbox_options = ('playlist'.title(), 'video'.title())

        parent = this.parent

        this.__media_downloader_frame = Frame(parent)
        this.__media_downloader_frame.grid(column=1, row=1)

        url_frame = LabelFrame(this.__media_downloader_frame,
                               text="url".upper())
        url_frame.grid(column=2, columnspan=2, row=1, ipadx=5)

        spinbox_frame = LabelFrame(this.__media_downloader_frame,
                                   text="options".capitalize())
        spinbox_frame.grid(column=1, row=1, padx=5)

        url_entry = Entry(url_frame,
                          textvariable=this.__url_entry_var,
                          font=("Helvetica", 11, 'normal'),
                          width=40)
        url_entry.grid(column=1, row=1, columnspan=2, ipady=6, padx=5, pady=5)

        spinbox_options = Spinbox(spinbox_frame,
                                  values=spinbox_options,
                                  textvariable=this.__spinbox_options_var)
        spinbox_options.grid(column=1, row=1, columnspan=2, ipady=6, pady=5)

        button_download = Button(this.__media_downloader_frame,
                                 text="download".title(),
                                 font=("Helvetica", 11, 'bold'))
        button_download.grid(column=4, row=1, padx=10, pady=10, ipady=2)

    def spinbox_options_handler(this, selected_option):
        this.__spinbox_options_var.set(selected_option)

    def exit_prog(this):
        this.update_location()
        save_config(this.__config)
        this.parent.destroy()

    def update_location(this):
        this.__config['coordinates'] = {
            'x': this.parent.winfo_rootx(),
            'y': this.parent.winfo_rooty()
        }
        success = CONSOLE_MESSENGER_SWITCH['success']
        print("\n\t\t{}\n\n".format(
            success('Window\'s coordinates were updated')))

    def select_menu_radio_thread(this):
        select_radio_thread = Thread(target=this.select_menu_radio, args=())
        select_radio_thread.start()
        select_radio_thread = None

    def select_menu_radio(this):
        selected = this.__radio_var.get()
        print('Selected Option:\t{}'.format(selected))
        this.__config['mode'] = selected.strip()
        save_config(this.__config)
        this.create_gui()

    # https://www.youtube.com/watch?v=bmVhQT1SDdE

    def scrape(this):
        if this.__url_entry_var.get():
            print('\n\n\t\tScraping {}\n'.format(this.__url_entry_var.get()))

            # Clear the scrape results frame
            this.refresh_scrape_results_frame()

            #  Set URL
            this.scraper.set_url(this.__url_entry_var.get())

            # Set the scrape results to class' instance variable
            this.__scrape_results = this.scraper.scrape_file()

            # Check the scrape results status
            if this.__scrape_results['status']:
                this.__scrape_results_frame = Frame(this.__scrape_frame,
                                                    relief=SUNKEN)

                this.__scrape_results_frame.grid(column=1, row=2, sticky=NW)

                listbox_results = Listbox(this.__scrape_results_frame,
                                          cursor="hand2",
                                          font=("Helvitica", 11, "bold"))

                listbox_results.grid(column=1,
                                     row=1,
                                     sticky=W,
                                     padx=10,
                                     pady=5)
                listbox_results.bind("<<ListboxSelect>>",
                                     this.listbox_results_mouse_click)

                values = list(this.__scrape_results.keys())
                values.sort()

                for i, r in enumerate(values):
                    if r.lower() == 'domain list':
                        this.__domain = this.__scrape_results[r][0].rsplit(
                            '/', 1)[0]
                        this.__domain_path = this.__scrape_results[r][1]
                    listbox_results.insert(i, r.title())

    def scrape_thread(this):
        scrape_thread = Thread(target=this.scrape, args=())
        scrape_thread.start()
        scrape_thread = None

    # Listbox on the far left
    def listbox_results_mouse_click(this, e):
        listbox = e.widget
        cls()
        this.devmode()

        if len(listbox.curselection()) > 0:
            selected_line = listbox.get(listbox.curselection())

            print("\n\tFar left listbox selected line: {}\n".format(
                selected_line))

            result = this.__scrape_results[selected_line.lower()]
            this.__current_result = result

            # Clear the scrape results detail frame
            this.refresh_scrape_results_detail_frame()

            this.__scrape_results_detail_frame = Frame(
                this.__scrape_results_frame)
            this.__scrape_results_detail_frame.grid(column=2,
                                                    row=1,
                                                    sticky=NE,
                                                    padx=10)

            data_frame = Frame(this.__scrape_results_detail_frame)
            data_frame.grid(column=2, row=1, ipadx=5)

            this.show_result_thread(result, data_frame)

    # Second listbox
    def show_result(this, result, data_frame):

        if type(result) == list:
            result_listbox = Listbox(data_frame,
                                     cursor="hand2",
                                     font=("Helvetica", 12, "bold"),
                                     width=44)

            result_listbox.grid(column=1, row=1, pady=5, ipady=5, sticky=E)
            result_listbox.bind("<<ListboxSelect>>",
                                this.current_selected_result_thread)

            for n, r in enumerate(result):
                if not type(r) == str:
                    print('{}.\t{}'.format(n + 1, r.tag))
                else:
                    print('{}.\t{}'.format(n + 1, r))
                result_listbox.insert(n, r)

    def show_result_thread(this, result, data_frame):
        result_thread = Thread(target=this.show_result,
                               args=(result, data_frame))
        result_thread.start()
        result_thread = None

    def current_selected_result_thread(this, e):
        cur_thread = Thread(target=this.current_selected_result, args=(e, ))
        cur_thread.start()
        cur_thread = None

    def current_selected_result(this, e):
        listbox = e.widget
        selected_line = listbox.get(listbox.curselection())
        this.__current_result_selected_item = selected_line

        print('\n\tCurrent Selected Item From Second Listbox:\t{}\n\n'.format(
            selected_line))

        for i, cr in enumerate(this.__current_result):
            if str(cr) == selected_line:
                this.__current_tag = cr
                continue

        this.current_tag()

    def current_tag(this):
        cls()
        this.devmode()
        print('Current Tag:\t{}'.format(this.__current_tag))
        if not type(this.__current_tag) == str:
            tag = this.__current_tag.tag
        else:
            tag = this.__current_tag

        if tag == 'link':
            link = this.__current_tag.xpath('//@href')
            if type(link) == list:
                for i, l in enumerate(link):
                    print('{}.\t{}'.format(i, l))
            else:
                print('{}'.format(link))
        elif tag == 'script':
            print('{}'.format(this.__current_tag.text_content()))
        elif tag == 'img':
            src = this.__current_tag.xpath('//@src')

            print('Domain:\t{}\n'.format(this.__domain))

            img_path = "{}{}".format(this.__domain, src[0])

            print('{} source: {}\n'.format(
                tag.title(),
                this.__current_tag.xpath('//@src')[0]))
            print('{} Full Path:\t{}\n'.format(tag.title(), img_path))
        else:
            if not type(this.__current_tag) == str:
                print('{}'.format(this.__current_tag.text_content()))
            else:
                print('{}'.format(this.__current_tag))

    """ Maintenance """

    def refresh_scrape_results_frame(this):
        if this.__scrape_results_frame != None:
            this.__scrape_results_frame.destroy()

    def refresh_scrape_results_detail_frame(this):
        if this.__scrape_results_detail_frame != None:
            this.__scrape_results_detail_frame.destroy()

    def devmode(this):
        print("\n\t\tURL:\t{}\n\t\t{}\n\n".format(
            "https://www.youtube.com/watch?v=bmVhQT1SDdE",
            "http://www.howtowebscrape.com/examples/simplescrape1.html"))

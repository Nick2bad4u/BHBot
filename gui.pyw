import threading
import uuid

from bot import (
    BELOW_NORMAL_PRIORITY_CLASS,
    BrawlhallaBot,
    BrawlhallaProcess,
    CONNECTION_LEVELS,
    Character,
    Client,
    ClientConfig,
    Config,
    DangerZoneError,
    GUIConfig,
    GUIHotkeys,
    Hotkeys,
    Image,
    InvalidStateError,
    LevelDefiner,
    LevelNotDetected,
    MAP_VK_TO_CHAR,
    MAP_VSC_TO_VK,
    Mode,
    MyFileHandler,
    MyFormatter,
    MyStreamHandler,
    NotRespondingError,
    Path,
    QueuedRecalculation,
    ResizedError,
    Settings,
    Sg,
    Singleton,
    SteamClient,
    SteamExeNotFound,
    VirtualInput,
    bar_bbox,
    bar_colors,
    box,
    build_character_matrix,
    ceil,
    character_matrix,
    character_matrix_width,
    characters,
    choice,
    chunks,
    compare,
    copy,
    ctypes,
    datetime,
    display_changelog,
    excepthook,
    find_char,
    find_element,
    first_digit_dict,
    floor,
    font_color,
    format_time,
    get_duration_gold,
    get_duration_xp,
    get_font_name,
    get_menu_pixels,
    get_rotation,
    get_text,
    get_window,
    global_settings,
    gold_levels,
    hdlr,
    importlib,
    json,
    keyboard,
    level_bbox,
    level_character_matrix,
    level_character_matrix_width,
    level_hundred_conditions,
    levels_xp,
    load_font,
    locked_color,
    locked_pixel,
    log,
    logger,
    logging,
    map_to_char,
    my_emit,
    os,
    parse_pos,
    psutil,
    pywintypes,
    queue,
    re,
    regenerate_layout,
    requests,
    rewards_bar_bbox,
    rewards_bar_colors,
    rfh,
    second_digit_dict,
    second_digit_diff,
    set_text,
    single_digit_dict,
    single_digit_diff,
    sleep,
    subprocess,
    sys,
    time,
    timedelta,
    win32api,
    win32con,
    win32gui,
    win32process,
    winreg,
    winxpgui,
)


class Handler(logging.StreamHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def emit(self, record):
        colors = {logging.DEBUG: "grey10", logging.INFO: "white"}
        if isinstance(record.msg, str) and record.msg in global_settings.messages:
            record.msg = global_settings.messages[record.msg]
        Sg.cprint(self.format(record), text_color=colors.get(record.levelno, "red"))


class GUI:
    def __init__(self):
        self.queue = queue.Queue()
        self.bot_thread = None
        self.downloading_new_version = False

        self.last_window_check = time()

        self.window = self.create_window()

        display_changelog()

        handler = Handler()
        handler.setFormatter(MyFormatter())
        global_settings.gui_handler = handler
        global_settings.set_debug_state()
        logger.addHandler(handler)

        Config.load()  # Display old config warning on bot launch and not on settings opened

    @staticmethod
    def create_window():
        Sg.theme("DarkGrey10")
        layout = [
            [Sg.Text(" ", size=(1, 1), key="title", font=(global_settings.font, 20))],
            [Sg.Text(" ", size=(1, 1), key="version", font=(global_settings.font, 13))],
            [
                Sg.Text(
                    " ",
                    size=(1, 1),
                    key="press_start",
                    font=(global_settings.font, 14),
                    metadata=0,
                )
            ],
            [
                Sg.Multiline(
                    size=(90, 10),
                    key="log",
                    disabled=True,
                    autoscroll=True,
                    write_only=True,
                    reroute_cprint=True,
                    reroute_stderr=global_settings.compiled,
                    font=(global_settings.font, 12),
                    text_color="red",
                )
            ],
        ]

        buttons = [
            [
                Sg.Button(
                    "", key="toggle", font=(global_settings.font, 12), metadata=0
                ),
                Sg.Button("", key="instructions", font=(global_settings.font, 12)),
                Sg.Button("", key="settings", font=(global_settings.font, 12)),
                Sg.Button("", key="exit", font=(global_settings.font, 12)),
            ],
            [
                Sg.Button(
                    "",
                    key="delayed_stop",
                    font=(global_settings.font, 12),
                    metadata=0,
                    visible=False,
                ),
                Sg.Button("", key="take_screenshot", font=(global_settings.font, 12)),
            ],
        ]
        if not global_settings.compiled:
            buttons[0].append(
                Sg.Button("", key="test", font=(global_settings.font, 12))
            )

        layout += buttons
        layout.append([Sg.Text(" ", font="Any 50")])

        if global_settings.new_version:
            global_settings.new_version.cleanup()
            update_column_layout = [
                [
                    Sg.Text(
                        " ",
                        size=(1, 1),
                        key="update_available_title",
                        font=(global_settings.font, 25),
                    )
                ],
                [
                    Sg.Text(
                        " ",
                        size=(1, 1),
                        key="update_available_version",
                        font=(global_settings.font, 15),
                    )
                ],
                [
                    Sg.Button(
                        "",
                        key="update_available_button",
                        font=(global_settings.font, 12),
                    )
                ],
                [Sg.Text(" ", font="Any 50")],
            ]
            layout.append([Sg.Column(update_column_layout)])

        window = Sg.Window(
            "", layout, icon=global_settings.icon, metadata="main_window_title"
        ).Finalize()
        global_settings.update_window(window)
        return window

    def toggle_bot(self):
        if self.bot_thread and self.bot_thread.is_alive():
            logger.info("stop_bot")
            self.queue.put_nowait("STOP")
        else:
            logger.info("start_bot")
            config = Config.load()
            logger.debug(global_settings)
            logger.debug(config)
            bot = BrawlhallaBot(config, Hotkeys.load(), self.queue)
            self.bot_thread = threading.Thread(target=bot.main_loop, daemon=True)
            self.bot_thread.start()

    def clear_queue(self):
        while not self.queue.empty():
            try:
                self.queue.get_nowait()
            except queue.Empty:
                continue
            self.queue.task_done()

    def delayed_stop(self):
        if self.bot_thread and self.bot_thread.is_alive():
            if self.window["delayed_stop"].metadata:
                logger.info("cancel_stop")
                self.clear_queue()
            else:
                logger.info("delayed_stop")
                self.queue.put_nowait("DELAYED_STOP")
            self.window["delayed_stop"].metadata = not self.window[
                "delayed_stop"
            ].metadata

    def refresh_buttons(self):
        if self.downloading_new_version:
            self.window["toggle"].update(disabled=True)
            self.window["delayed_stop"].update(visible=False)
            self.window["instructions"].update(disabled=True)
            self.window["settings"].update(disabled=True)
            self.window["update_available_button"].update(disabled=True)
            self.window["exit"].update(disabled=True)
        elif self.bot_thread and self.bot_thread.is_alive():
            self.window["toggle"].metadata = 1
            self.window["press_start"].metadata = 1
            self.window["delayed_stop"].Update(visible=True)
            self.window["instructions"].Update(disabled=True)
            self.window["settings"].Update(disabled=True)
        else:
            self.window["toggle"].metadata = 0
            self.window["press_start"].metadata = 0
            self.window["delayed_stop"].metadata = 0
            self.window["delayed_stop"].Update(visible=False)
            self.window["instructions"].Update(disabled=False)
            self.window["settings"].Update(disabled=False)
            self.clear_queue()

    @staticmethod
    def display_instructions():
        contents = global_settings.language.LAYOUT_MAPPING.get(
            "instructions_contents",
            global_settings.get_language("English").LAYOUT_MAPPING.get(
                "instructions_contents", "Should be stuff here"
            ),
        )
        Sg.popup(
            *contents,
            font=(global_settings.font, 13),
            title=global_settings.language.LAYOUT_MAPPING.get(
                "instructions_window_title", "Instructions"
            ),
            icon=global_settings.icon,
        )

    def configure(self):
        settings = GUIConfig()
        self.window.disable()
        self.window.hide()
        settings.start_loop()
        self.window.enable()
        self.window.un_hide()

    def autostart(self):
        if not global_settings.autostart:
            return
        if self.bot_thread and self.bot_thread.is_alive():
            self.last_window_check = time()
        elif time() - self.last_window_check > 120:
            logger.debug("autostart_check")
            bh = BrawlhallaProcess.find()
            if not bh:
                self.toggle_bot()
            self.last_window_check = time()

    def main_loop(self):
        while True:
            event, values = self.window.Read(timeout=50)
            if event in (Sg.WINDOW_CLOSED, "exit"):
                break
            elif event == "toggle":
                self.toggle_bot()
            elif event == "delayed_stop":
                self.delayed_stop()
            elif event == "instructions":
                self.display_instructions()
            elif event == "settings":
                self.configure()
            elif event == "test":
                logger.info("test")
                logger.debug("test")
            elif event == "take_screenshot":
                bh = BrawlhallaProcess.find()
                if bh is None:
                    logger.error("bh_not_running")
                else:
                    screenshot_name = f"screenshot-{uuid.uuid4()}.png"
                    screenshot_path = (
                        Path(os.getenv("LOCALAPPDATA")) / "BHBot" / screenshot_name
                    )
                    bh.make_screenshot().save(screenshot_path)
                    logger.info("took_screenshot", str(screenshot_path))

            elif event == "update_available_button":
                global_settings.new_version.download(background=True)
                self.downloading_new_version = True
            elif not self.downloading_new_version:
                self.autostart()
            if (
                global_settings.compiled
                and global_settings.new_version
                and self.downloading_new_version
                and global_settings.new_version.is_downloaded()
            ):
                global_settings.new_version.extract_restart()
            self.refresh_buttons()
            global_settings.update_window(self.window)

        self.window.close()


if __name__ == "__main__":
    Singleton()
    gui = GUI()
    gui.main_loop()

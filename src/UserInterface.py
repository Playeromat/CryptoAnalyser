from simple_term_menu import TerminalMenu


class UserInterface:

    def multi_select(self, options):
        terminal_menu = TerminalMenu(options, multi_select=True)
        return terminal_menu.show()

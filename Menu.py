class Menu:
    def __init__(self, options=None, title='---- MENU ----'):
        if options is None:
            options = []
        self.options = options
        self.title = title

    def __str__(self):
        st = f'\n{self.title}\n'
        for i, option in enumerate(self.options):
            st += f"{i + 1}.\t{option[0]}\n"
        return st

    def is_valid_input(self, choice):
        return choice.isdigit() and int(choice) in range(1, len(self.options) + 1)

    def show(self):
        if self.options:
            print(self.__str__())
            choice = input(f'Enter your choice (1 - {len(self.options)}): ')
            if self.is_valid_input(choice):
                option = self.options[int(choice) - 1]
                if option[2] is None:
                    option[1]()
                else:
                    option[1](option[2])
            else:
                print(f'Invalid input! Please choose number option from the menu: (1 - {len(self.options)})')
        else:
            print('Sorry, but no options provided...')
            exit()

# Peer Group 10: Restaurant
# Charles Seidel
# Chad Fortune


class Order:
    def __init__(self, argOrder):
        self.__order = argOrder

    def __str__(self):
        return str(self.__order)

    def get_order(self):
        return self.__order

    def print_receipt(self, bill):
        print('\n%15s' % 'Receipt')
        print('%-20s %5s' % ('item(s)', 'price'))
        print('%-19s %5s' % ('----------', '-------'))
        receipt_item = bill[0]  # fill in later
        receipt_price = bill[1]  # fill in later
        for i in range(len(receipt_item)):
            print('%-20s %5.2f' % (receipt_item[i], receipt_price[i]))
        total = 0  # fill in later
        print('%27s' % '-------')
        print('%26.2f' % total)


    def take_orders(self, argMenu={}):
        menu1 = argMenu
        validCommands = ['a', 'b', 'c', 'd', 'e', 'o']
        command = input("Enter commands separated by spaces, or c to close: ")
        total = 0.00
        while command.lower() != "c":
            command = command.split(' ')
            for cm in range(0, len(command), 1):
                if command[cm] in validCommands and command[cm].lower() != 'c':
                    if command[cm].lower() == 'a':
                        print(menu1['a1'], menu1['a2'])
                        total += (menu1['a1']['Price:']) + (menu1['a2']['Price:'])
                    elif command[cm].lower() == 'b':
                        print(menu1['b1'], menu1['b2'])
                        total += (menu1['b1']['Price:']) + (menu1['b2']['Price:'])
                    elif command[cm].lower() == 'd':
                        print(menu1['d1'], menu1['d2'])
                        total += menu1['d1']['Price:'] + menu1['d2']['Price:']
                    elif command[cm].lower() == 'e':
                        print(menu1['e1'], menu1['e2'])
                        total += (menu1['e1']['Price:']) + (menu1['e2']['Price:'])
                elif command[cm].lower() in menu1:
                    print(menu1[command[cm]])
                    total += menu1[command[cm]]['Price:']
                elif command[cm].lower() == 'o':
                    print("")
                elif command[cm].lower() == 'c':
                    exit(1)
                else:
                    print("Error: " + command[cm] + " is not a valid command!")
            print("Total: $" + str(total))
            command = input("Enter commands separated by spaces, or c to cancel: ")
            total = 0.00


class Table:
    __available = True

    def __init__(self, arg_table, arg_max, arg_guests=0, arg_order=''):
        self.__table = arg_table
        self.__maxSeats = arg_max
        self.__guests = arg_guests
        self.__order = list(arg_order)

    def __str__(self):
        if len(self.__order) == 0:
            ordering = 'nothing'
        else:
            ordering = self.__order

        return 'Table: ' + str(self.__table) + ' has ' + str(self.__maxSeats) + ' seats, with ' + \
               str(self.__guests) + ' guests and has ordered ' + str(ordering) + '.'

    def is_available(self):
        return self.__available

    def seat_guest(self):
        self.__available = False

    def unseat_guest(self):
        self.__available = True


class MenuItem:
    def __init__(self, arg_item_code, arg_name, arg_price):  # instantiates object
        self.__code = arg_item_code
        self.__name = arg_name
        self.__price = arg_price

    def __str__(self):
        return self.__code + ' ' + self.__name + ' ' + str(self.__price)


class Menu:
    def __init__(self, arg_menu=[]):
        self.__menu = arg_menu
        self.readMenu()

    # def __add__(self, other):
    #    self.__menu.append(other)

    def getMenu(self):
        return self.__menu

    def readMenu(self):
        try:
            rFile = open("Menu.txt", 'rb')
        except IOError:
            print("missing menu menu.txt file.")
            return []

        # splits menu.txt by line
        rawData = rFile.readlines()
        rFile.close()

        list1 = []
        for i in rawData:
            i = i.splitlines()
            list1.append(i)  # puts all orders in an array

        # this loop cleans up the text in menu.txt and puts the items in a new array
        list2 = []
        for item in list1:
            item = str(item)
            item = item.split(' ')
            item[0] = item[0].strip(' \'[')
            item[0] = item[0][2:len(item[0])]
            item[2] = item[2].strip(' \']')
            item[2] = float(item[2])
            list2.append(item)

        # this loop turns all orders into MenuItems
        for k in range(0, len(list2), 1):
            argCode = list2[k][0]
            argName = list2[k][1]
            argPrice = list2[k][2]
            newMenuItem = MenuItem(argCode, argName, argPrice)
            # print(newMenuItem)
            self.__menu.append(newMenuItem)

        return self.__menu

    def __str__(self):
        for m in range(0, len(self.__menu), 1):
            print(m)


def read_tables():
    # open table config file
    try:
        config = open('config.txt', 'r')
    except IOError:
        print("Missing table config.txt file.")
        return []

    # Read in table information
    raw_data = config.readlines()
    config.close()

    # Clean up raw data
    for i in range(len(raw_data) - 1):
        raw_data[i] = raw_data[i].strip('\n')
        raw_data[i] = raw_data[i].rstrip(' ')

    # convert raw_data into Table Object
    table = []
    for item in raw_data:
        temp = item.split(' ')
        table.append(Table(int(temp[0]), int(temp[1])))

    return table


def print_table():
    table1 = read_tables()
    for i in table1:
        print(i)


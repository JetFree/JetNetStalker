import sys
from datetime import datetime, timedelta
from colorama import Fore
from requests_controller import is_host_available


def print_start_welcome():
    print("""
             _      _   _   _      _   ____  _        _ _             
            | | ___| |_| \ | | ___| |_/ ___|| |_ __ _| | | _____ _ __ 
         _  | |/ _ \ __|  \| |/ _ \ __\___ \| __/ _` | | |/ / _ \ '__|
        | |_| |  __/ |_| |\  |  __/ |_ ___) | || (_| | |   <  __/ |   
         \___/ \___|\__|_| \_|\___|\__|____/ \__\__,_|_|_|\_\___|_| 
         """)


def select_target():
    choices = {1: "https://www.rghost.net", 2: "https://www.imgur.com", 3: "https://www.print.sc"}
    print(Fore.GREEN + "\nAvailable targets:" + Fore.RESET,
          "1) rghost.net", "2) imgur.com", "3) print.sc", sep="\n")
    try:
        choice = int(input("Your choice: "))
        if choice in range(1, 4):
            if is_host_available(choices[choice]):
                return choices[choice]
            else:
                print(f"Host {choices[choice]} is unavailable. Please select another target")
                return select_target()
        else:
            raise ValueError
    except ValueError:
        print("Incorrect value entered. Please use only numbers 1, 2, 3")
        return select_target()
    except KeyboardInterrupt:
        print("Program was stopped by user.")
        sys.exit(0)


def select_threads():
    try:
        choice = int(input(Fore.GREEN + "\nSelect number of threads: " + Fore.RESET))
        if choice > 0:
            return choice
        else:
            raise ValueError
    except ValueError:
        print("Incorrect value entered. Please use only numbers")
        return select_threads()
    except KeyboardInterrupt:
        print("Program was stopped by user.")
        sys.exit(0)


def select_method():
    choices = {1: "time", 2: "links", 3: "size"}
    print(Fore.GREEN + "\nChoose method:" + Fore.RESET,
          "1) time", "2) links count", "3) target size", sep="\n")
    try:
        choice = int(input("Your choice: "))
        if choice in range(1, 4):
            return choices[choice]
        else:
            raise ValueError
    except ValueError:
        print("Incorrect value entered. Please use only numbers 1, 2, 3")
        return select_method()
    except KeyboardInterrupt:
        print("Program was stopped by user.")
        sys.exit(0)


def select_time():
    try:
        time = input(Fore.GREEN + "\nEnter time in format [HH:mm:ss] :" + Fore.RESET)
        hours, minutes, seconds = [int(i) for i in time.split(":")]
        future_date = datetime.now() + timedelta(hours=hours, minutes=minutes, seconds=seconds)
        return future_date
    except ValueError:
        print("Incorrect format for entered time. Use format [HH:mm:ss]")
        return select_time()
    except KeyboardInterrupt:
        print("Program was stopped by user.")
        sys.exit(0)


def select_links():
    try:
        qnt = int(input(Fore.GREEN + "\nSelect links quantity: " + Fore.RESET))
        if qnt > 0:
            return qnt
        else:
            raise ValueError
    except ValueError:
        print("Incorrect value entered. Please use only numbers > 0")
        return select_links()
    except KeyboardInterrupt:
        print("Program was stopped by user.")
        sys.exit(0)


def select_size():
    try:
        size = float(input(Fore.GREEN + "\nEnter size in kilobytes: " + Fore.RESET))
        if size > 0:
            return size
        else:
            raise ValueError
    except ValueError:
        print("Incorrect value entered. Please use only numbers > 0")
        return select_size()
    except KeyboardInterrupt:
        print("Program was stopped by user.")
        sys.exit(0)


def print_income_data(target, threads_amount, trigger_type, trigger):
    if trigger_type == "size":
        trigger_str = f"until size is {Fore.CYAN + str(trigger) + ' megabytes' + Fore.RESET}"
    elif trigger_type == "links":
        trigger_str = f"for {Fore.CYAN + str(trigger) + ' links' + Fore.RESET}"
    else:
        trigger_str = f"until time: {Fore.CYAN + datetime.strftime(trigger, '%H:%M:%S') + Fore.RESET}"
    print(f"Target: {Fore.CYAN + target.split('www.')[-1] + Fore.RESET} with "
          f"{Fore.CYAN + str(threads_amount) + ' threads ' + Fore.RESET}" + trigger_str)

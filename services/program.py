from colorama import Fore
import services.program_guests
from services import program_hosts
import data.mongo_setup as mongo_setup

def main():
    mongo_setup.global_init()

    print_header()

    try:
        while True:
            if find_user_intent() == 'book':
                program_guests.run()

            else:
                program_hosts.run()

    except KeyboardInterrupt:
        return

def print_header():
    snake = \
import multiprocessing
from functools import partial
from scripts.requests_controller import *
from scripts.linkbruteforcer import generate
from scripts import os_utils
from scripts.custom_iterator import MyIterator
from scripts.menu import *
from scripts.os_utils import open_downloads_resources, get_dir_size


def run_pool(threads, condition, link_counter, event, url):
    try:
        pool = multiprocessing.Pool(threads)
        iter_list = generate()
        for perm_iter in iter_list:
            list(pool.imap(partial(check_url, condition, link_counter, event,
                                   url), MyIterator(perm_iter, event)))
    except KeyboardInterrupt:
        print("Program was stopped by user.")
        sys.exit(0)
    except OSError as os_e:
        print(os_e.strerror)


def print_statistics(start, links):
    print("=" * 50, end="\n\n")
    time_delta = datetime.now() - start
    hours, remainder = divmod(time_delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(Fore.MAGENTA + f"Ready for: {hours:> 3d} hours {minutes} minutes"
                         f" {seconds} seconds")
    print(Fore.MAGENTA + f"Found links: {links}")
    print(Fore.MAGENTA + f"Folder size: {int(get_dir_size())}kb")


def main():
    os_utils.create_folder()
    os_utils.clean_folder()
    method_dict = {"time": select_time, "links": select_links,
                   "size": select_size}
    print_start_welcome()
    url = select_target()
    threads = select_threads()
    method = select_method()
    method_value = method_dict[method]()
    print_income_data(url, threads, method, method_value)
    condition = {method: method_value}
    manager = multiprocessing.Manager()
    event = manager.Event()
    link_counter = manager.Value("i", 0)
    start_time = datetime.now()
    run_pool(threads, condition,link_counter, event, url)
    print_statistics(start_time, link_counter.value)
    open_downloads_resources()


if __name__ == '__main__':
    main()

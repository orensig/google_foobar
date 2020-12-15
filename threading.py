import logging
import threading
import time
import concurrent.futures


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    lst = [5, "in", 0.4]
    threads_lst = []
    # for x in lst:
    #     logging.info("Main    : type of {:s} is {:s}".format(str(x),str(type(x))))
    # logging.info("Main    : type of entire list is {:s}".format(str(type(lst))))

    # for i in range(1,4):
    #     x = threading.Thread(target=thread_function, args=(i,))
    #     logging.info("Main    : before running threads")
    #     x.start()
    #     logging.info("Main    : wait for the thread to finish")
    #     threads_lst.append(x)
    #
    # for thread in threads_lst:
    #     thread.join()
    # logging.info("Main    : all done")
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, lst)
    exit(0)


if __name__ == '__main__':
    main()
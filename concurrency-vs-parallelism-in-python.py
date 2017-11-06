# In CPython, the most popular implementation of Python, the GIL is a mutex
# that makes things thread-safe
# Due to the GIL, we can't achieve true parallelism via multithreading
# Two different native threads of the same process can't run Python code at
# once

# What is a PROCESS?
# A process is just a program that is in execution
# A single process can have multiple threads

# Processes don't share memory
# Threads share memory

# Switching processes is expensive
# Switching threads is less expensive

# Processes require more resources
# Threads require less resources

# Concurrency is often misunderstood and mistaken for parallelism
# Concurrency implies the scheduling of independent code to be executed in a
# cooperative manner

# From a parallelization perspective, using threads or greenlets is equivalent
# because neither actually runs in parallel
# Greenlets are even less expensive to create than threads

import time
import logging
import requests

class WebsiteDownException(Exception):
    pass

def ping_website(address, timeout=20):
    """
    Check if a website is down. A website is considered down
    if either the status_code >= 400 or if the timeout expires

    Throw a WebsiteDownException if any of the website down conditions are met
    """
    try:
        response = requests.head(address, timeout=timeout)
        if response.status_code >= 400:
            logging.warning("Website %s returned status_code=%s" % (address,
                                                                    response.status_code))
            raise WebsiteDownException()
    except requests.exceptions.RequestException:
        logging.warning("Timing expired for website %s" % address)
        raise WebsiteDownException()

def notify_owner(address):
    """
    Send the owner of the address a notification that their website is down
    For now, we're just going to sleep for 0.5 seconds but this is where
    you would send an email, push notification or text-message
    """
    logging.info("Notifying the owner of %s website" % address)
    time.sleep(0.5)


def check_website(address):
    """
    Utility function: check if a website is down, if so, notify the user
    """
    try:
        ping_website(address)
    except WebsiteDownException:
        notify_owner(address)

# Continue with this tutorial
# https://code.tutsplus.com/articles/introduction-to-parallel-and-concurrent-programming-in-python--cms-28612

## Intro to FUNCTOOLS

## LRU Cache
## Wraps a function in a memoizing callable that saves up to the maxsize
## most recent calls
## It can save time when an expensive or I/O bound function is periodically
## called with the same arguments

## LRU Caches work best when the most recent calls are the best predictors of
## upcoming calls

import urllib.error
import urllib.request
from functools import lrucache
from functools import partial

@lrucache(maxsize=24)
def get_webpage(module):
    webpage = "https://docs.python.org/3/library/{}.html".format(module)
    try:
        with urllib.request.urlopen(webpage) as request:
            return request.read()
    except urllib.error.HTTPError:
        return None

if __name__ == "__main__":
    modules = ['functools', 'collections', 'os', 'sys']
    for module in modules:
        page = get_webpage(module)
    if page:
        print('{} module not found'.format(module))

def add(x,y):
    return x + y

p_add = partial(add, 2)
print(p_add(4))

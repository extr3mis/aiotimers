# aiotimers
<img src='https://img.shields.io/badge/Python-3.5+-blue'> <img src='https://img.shields.io/badge/license-MIT-green'> <img src='https://img.shields.io/badge/async-enabled-blue'>

An asynchronous implementation of background timers in Python3.
_Requires Python 3.5+_

# Installation

Install this package using `pip`.
```console
$ pip install git+https://github.com/extr3mis/aiotimers.git
```

# Usage
Import the package using the given import statement.

```console
>>> from aiotimers import Timer
```

Now you can simply make a `Timer` object and initialize it with the time (in seconds) you want to wait until, and the callback function/coroutine that you want to be called once the timer is complete. Optionally, you can also pass args and kwargs as a `tuple` and a `dict` respectively. 

```console
>>> timer = Timer(30.00, mycallback)
```

# This file will be executed every time a new IPython session is started.
# goes in startup folder of ipython profile dir (terminal: ipython profile locate)


try:
    get_ipython().run_line_magic('load_ext', 'autoreload')
    get_ipython().run_line_magic('autoreload', '2')
except NameError:
    # This will happen if get_ipython() is not defined (e.g., in a plain Python script)
    pass # Do nothing, autoreload is not for non-IPython environments

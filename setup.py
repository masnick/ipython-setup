#    _____ ______ _______ _    _ _____
#   / ____|  ____|__   __| |  | |  __ \
#  | (___ | |__     | |  | |  | | |__) |
#   \___ \|  __|    | |  | |  | |  ___/
#   ____) | |____   | |  | |__| | |
#  |_____/|______|  |_|   \____/|_|


import pprint # Pretty printing for debugging
pp = pprint.PrettyPrinter(indent=4) # Usage: `pp.pprint(varname)`

from IPython.display import display
from IPython.display import HTML
import IPython.core.display as di # Example: di.display_html('<h3>%s:</h3>' % str, raw=True)

# Function for easily outputting HTML
def d(html):
    di.display_html(html, raw=True)

# Function for displaying a flagged paragraph tag
def p_flag(html):
    d("""<p style="background-color: yellow;">%s</p>""" % html)

# This line will hide code by default when the notebook is exported as HTML
di.display_html('<script>jQuery(function() {if (jQuery("body.notebook_app").length == 0) { jQuery(".input_area").toggle(); jQuery(".prompt").toggle();}});</script>', raw=True)

# This line will add a button to toggle visibility of code blocks, for use with the HTML export version
di.display_html('''<button onclick="jQuery('.input_area').toggle(); jQuery('.prompt').toggle();">Toggle code</button>''', raw=True)

#######################################################################################

# Can only be run once, at beginning
import matplotlib
matplotlib.use('TkAgg') # select a backend for plots: http://matplotlib.org/faq/usage_faq.html#what-is-a-backend
%matplotlib inline

import re # regex

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import epipy as epi

plt.ion() # turn on interactive mode: http://matplotlib.org/faq/usage_faq.html#what-is-interactive-mode

#######################################################################################

# iPython notebook configuration
# http://stackoverflow.com/questions/11707586/python-pandas-widen-output-display
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

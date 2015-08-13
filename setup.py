################################ > S E T U P < #################################

# 1. SciPy setup
#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # http://matplotlib.org/faq/usage_faq.html
import matplotlib.gridspec as gs # http://bit.ly/1U6YKGm

# Other potentially useful libraries
# import re # regex
# import epipy as epi # specific for epidemiology research
# from scipy import stats # statistical testing


%matplotlib inline
# This displays matplotlib graphics inline
# See http://stackoverflow.com/a/24884342/173351

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
# iPython notebook configuration to increase output width
# See http://stackoverflow.com/a/11711637/173351



# 2. Display raw HTML in IPython notebooks
#
#    Ability to write raw HTML that will be displayed
#    with a cell's output.
#
#    Example:
#      di.display_html('<h3>%s:</h3>' % str, raw=True)
#
import IPython.core.display as di

def d(html): # Function for easily outputting HTML
    di.display_html(html, raw=True)
def p(html): # Function for easily outputting HTML inside <p> tags
    di.display_html("<p>%s</p>" % html, raw=True)
def p_flag(html): # Function for displaying a flagged paragraph tag
    d("""<p style="background-color: yellow;">%s</p>""" % html)



# 3. Button to hide code
#
# The line below will hide code by default when the notebook
# is exported as HTML.
#
# See how this works:
# http://protips.maxmasnick.com/hide-code-when-sharing-ipython-notebooks
#
di.display_html('<script>jQuery(function() {if (jQuery("body.notebook_app").length == 0) { jQuery(".input_area").toggle(); jQuery(".prompt").toggle();}});</script>', raw=True)

# The line below will add a button to toggle visibility of code blocks,
# for use with the HTML export version.
#
di.display_html('''<button onclick="jQuery('.input_area').toggle(); jQuery('.prompt').toggle();">Toggle code</button>''', raw=True)



# 4. Better output for debugging
#
#    Usage: `pp.pprint(varname)`
import pprint
pp = pprint.PrettyPrinter(indent=4)

################################################################################

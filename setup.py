################################ > S E T U P < #################################

# 1. SciPy setup
#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # http://matplotlib.org/faq/usage_faq.html
import matplotlib.gridspec as gs # http://bit.ly/1U6YKGm
import seaborn

# Other potentially useful libraries
# import re # regex
# import epipy as epi # specific for epidemiology research
# from scipy import stats # statistical testing
# import xlrd # Needed for pd.read_excel()
# import feather # pip install feather-format; see https://github.com/wesm/feather
import datetime as dt

# Sane font sizes for matplotlib figures
import matplotlib as mpl
mpl.rc('axes', labelsize="large", titlesize="x-large")
# Size options are: [size in points | ‘xx-small’ | ‘x-small’ | ‘small’ | ‘medium’ | ‘large’ | ‘x-large’ | ‘xx-large’ ] - http://matplotlib.org/api/text_api.html#matplotlib.text.Text.set_size

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

# 5. Retina image support
get_ipython().magic(u"config InlineBackend.figure_format = 'retina'")

# 6. 2x2 table helper methods
def _2by2(df, row_name, column_name):
    df = df.copy()
    df['one'] = 1
    x = df.pivot_table(columns=[column_name], values=['one'], index=[row_name], aggfunc=[np.sum], margins=True)
    x.columns = x.columns.droplevel([0,1]) # Delete superflurious index levels
    return x.astype(int)

def _2by2_cell_percent(df, row_name, column_name):
    counts = _2by2(df, row_name, column_name)
    return (counts / counts.iloc[-1][-1].astype(float) * 100).round(1)

def _2by2_row_percent(df, row_name, column_name):
    counts = _2by2(df, row_name, column_name)
    return (counts.divide(list(counts.T.iloc[-1]), axis='rows') * 100).round(1)

def _2by2_column_percent(df, row_name, column_name):
    counts = _2by2(df, row_name, column_name)
    return (counts.divide(list(counts.iloc[-1]), axis='columns') * 100).round(1)
################################################################################

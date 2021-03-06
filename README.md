This is the code I use to set up IPython notebooks. I generally put it in the first cell in the notebook.

You can easily do this with `%load` magic. In a code cell, put the following:

    %load /path/to/ipython-setup/setup.py

...and then run the cell. The cell will be auto-filled with the contents of `setup.py`. Note that you will need to run the cell again after it is auto-filled.

## Auto-create `.py` and `.html` files when saving

IPyton/Jupyter notebooks [can do this automatically](http://protips.maxmasnick.com/ipython-notebooks-automatically-export-py-and-html), which is very useful for version control. The `.html` output from this is what the [toggle HTML button](https://github.com/masnick/ipython-setup/blob/cf703c6dec0fa6f5e41533a87665d7716e759cdb/setup.py#L43-L56) is for.

## License (MIT)

Copyright (c) 2015 Max Masnick

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

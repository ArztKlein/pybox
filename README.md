# pybox
Create terminal boxes with python

# Installation
Pybox is not yet on pypi, so you must manually download the package.
## Manual
- Clone this repository `git clone "https://github.com/ArztKlein/pybox.git"`
- Place the pybox folder (not the root folder) into your project.

# Usage
```py
from pybox import Pybox

box = Pybox()

box.print("Terminal boxes in Python")
```

## Change the box style
There are three box styles -- single, double, curved.  
When initialising the pybox, set the keyword `style`.
```
box = Pybox(style="curved")
```


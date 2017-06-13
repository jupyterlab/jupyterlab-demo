# Markdown+Python Example

This is a regular markdown file. In JupyterLab you can open and edit
the file in the file editor, or in the markdown viewer. As you edit the
file the rendered markdown will automatically update.

# Including Python code

Here is a block of Python code in the markdown file:

```python
a = 10
```

Let's attach a Python 3 Kernel and Console to this markdown file. Then
we can select lines of code in the markdown file and run them in the 
console by pressing `Shift+Enter`. Let's do something more complicated:

First import `matplotlib`, `numpy` and `pandas`, and create a data frame:

```python
%matplotlib inline
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd
data = {
    'x': np.random.rand(100),
    'y': np.random.rand(100),
    'color': np.random.rand(100),
    'size': 100.0*np.random.rand(100)
}
df = pd.DataFrame(data)
df.head()
```

And make a scatter plot:

```python
style.use('seaborn-whitegrid')

plt.scatter('x', 'y', c='color', s='size', data=df, cmap=plt.cm.Blues)
plt.xlabel('x')
plt.ylabel('y')

plt.title("The data that we collected")
```

All of the Python objects are live in the console and can be explored
further.
# JupyterLab update

JupyterLab is a new web-based frontend that brings together many tools in an extensible, performant, open-source environment. We plan to release the beta in a few weeks, which should be usable for day-to-day work.

## JupyterLab

This is JupyterLab. Create a new tab by clicking the + button or using the File | New menu. We can then start a notebook with a specific kernel, a console, terminal, or text editor.

## Notebook

The notebook is a completely new implementation of the same Jupyter notebook interface that we know and love. Here is an example notebook from Jake's data science book. You still have markdown including math, code, rich output, interactive jupyter widgets, etc.

Since this is a complete rewrite, we've taken the opportunity to add a few things, like collapsible and draggable cells and a vastly better extension mechanism.

One of the design goals for JupyterLab is to make it easy for components to interact with each other. For example, we can right-click to open a console talking to the same kernel as this notebook. We can drag these so that they are side-by-side. As we execute cells in the notebook, we see the log of executions in the console. In the console, we can investigate the computation environment without messing up the notebook. Two tools, talking to the same kernel, in an integrated environment.

So that's the notebook. The same interface that you know and love, more powerful and integrated into the extensible JupyterLab environment.

## Editor

Let's see the editor. Here is an example markdown file. We can also preview it. We can again arrange these side-by-side.

We have some code in this markdown file. We can right-click and open a console associated with any editor file. This time, pressing shift-enter inside of a markdown code block will send the text to the console to execute. We can easily check our examples, or if we were in a code file, could check our scripts.

## Single document mode

You can see that our workspace can have many things on it. Sometimes we want to focus on a single tab, for example this console. With any tab active, we can toggle the new "Single document mode" command with shift-cmd-enter. And we can toggle back.

# File types

We can also write our own file viewer plugins. Some others include images, geojson maps, vega and vegalite.

These are easy to create. For example, last night we thought it would be great to have a Fasta sequence viewer in JupyterLab. We built a prototype in with a couple dozen lines of code in half an hour wrapping the msa viewer.

*open fasta file*

I see that it looks like the top sequence is not aligned properly. Since all viewers use the same underlying file, it's easy to open the file and align it, and the view automatically updates.

*update the fasta file*

# Data grid

Another file that many of us deal with is CSV files, or other files that can be represented as a grid.

**open smaller.csv**

This viewer uses an alpha version of a new fast datagrid component written by Chris Colbert as part of the JupyterLab collaboration. It's in the PhosphorJS javascript library, on which jlab is built, and can be used outside of JupyterLab.

It also handles larger data files. Here is a 200MB csv file with 1.2 million rows. Excel and LibreOffice can't load it - it's too big, and it is very slow to scroll around what it can load. Let's see how our data grid component works. It takes a few seconds to transfer 200MB through to the web browser, but it *does* open. And scrolling is as smooth as butter. Chris has another example with one TRILLION rows and one TRILLION columns, still smooth as butter.

Thanks Chris. We look forward to the many more planned features.

# Extensibility

So that's some of the new exciting things in JupyterLab, an extensible, performant, comprehensive environment.

Did I mention that JupyterLab is extensible? Everything you see is a plugin, and your plugins are on equal footing to extend or replace any of ours.

That's the genius of open-source - you can customize your own tools and help the community. I'm most excited about what *you* will do with this tool and the extensions that *you* write.

If you want to learn more about Jupyter, please come to [JupyterCon! August 23-25](https://conferences.oreilly.com/jupyter/jup-ny), August 23-25, in New York City. See the NumFOCUS booth for discount codes for tickets. And come to the sprint day of JupyterCon, Saturday Aug 26, following the conference.

Thank you

For more information, see the [PyData Seattle JupyterLab talk](https://channel9.msdn.com/Events/PyData/Seattle2017/BRK11)

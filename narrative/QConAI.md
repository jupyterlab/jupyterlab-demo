# Slides

# JupyterLab update

JupyterLab is a new web-based frontend that brings together many tools in an extensible, performant, open-source environment. We announced it to be ready for users about a month ago. We are calling it "beta" since the extension developer APIs for making extensions are still evolving.

## JupyterLab

This is JupyterLab. Create a new tab by clicking the + button or using the File | New menu. We can then start a notebook with a specific kernel, a console, terminal, or text editor.

## Notebook

The notebook is a completely new implementation of the same Jupyter notebook interface that we know and love. Here is an example notebook from Jake's data science book. You still have markdown including math, code, rich output, interactive jupyter widgets, etc.

Since this is a complete rewrite, we've taken the opportunity to add a few things, like collapsible and draggable cells and a vastly better extension mechanism.

Another workflow supported by JupyterLab is creating a new view of a file by right-clicking on the tab, so it is easy to look at different parts at the same time. Of course, you can still drag and drop between these views.

One of the design goals for JupyterLab is to make it easy for components to interact with each other. For example, we can right-click to open a console talking to the same kernel as this notebook. We can drag these so that they are side-by-side. As we execute cells in the notebook, we see the log of executions in the console. In the console, we can investigate the computation environment without messing up the notebook. Two tools, talking to the same kernel, in an integrated environment.

Here is another notebook demonstrating Jupyter widgets. Just as it is easy to get components to talk to each other, we've also made it easy to pull out components. Right-click to create a new view of this output, which then is like your prototypical dashboard.

TODO: bqplot example.

So that's the notebook. The same interface that you know and love, more powerful and integrated into the extensible JupyterLab environment.

## Editor

Let's see the editor. Here is an example markdown file. For any file, we may have multiple viewers open. For example, we can also preview this file by right-clicking on it. We can again arrange these side-by-side. These views are live, talking to the same underlying in-memory model of the file, which means live preview happens automatically *type some text*.

We have some code in this markdown file. We can right-click and open a console associated with any editor file. This time, pressing shift-enter inside of a markdown code block will send the text to the console to execute. We can easily check our examples.

This enables a fluent workflow executing code from a script or code file: open the file, open an associated console with any kernel, and step through the lines of code with shift-enter, or highlight several lines and press shift-enter.

## Single document mode

You can see that our workspace can have many things on it. Sometimes we want to focus on a single tab, for example this console here in the corner. With any tab active, we can toggle the new "Single document mode" command with the View menu option. Once in single-document mode, we can navigate the documents with the Tabs side panel or the Tabs menu. It's easy to jump back to our full layout again.

## Terminal

The terminal is a full-blown terminal. We can run emacs or vi. We can even quit vi.

## Customization

We have a number of settings to customize your JupyterLab environment. Some settings are accessible from the menu, such as theme (change theme), the text editor keyboard handling, etc. Other settings such as the keyboard shortcuts for the system are accessible in the advanced settings.

# File types

Many of us deal with many types of files. JupyterLab comes with many different viewers for files. For example:
* images
* pdf
* geojson
* vega/vegalite

As with the markdown file, these models are live. We can open a single file like this Vega file with the JSON viewer, and with the text editor, and changes in one will reflect in the others. *Change the mark type*

# Data grid

Another file that many of us deal with is CSV files, or other files that can be represented as a grid.

**open smaller.csv**

This viewer uses an alpha version of a new fast datagrid component written by Chris Colbert as part of the JupyterLab collaboration. It's in the PhosphorJS javascript library, on which jlab is built, and can be used outside of JupyterLab.

It also handles larger data files. Here is a 200MB csv file with 1.2 million rows.

**open big.csv**

Excel and LibreOffice can't load this file - it's too big. Let's see how our data grid component works. It takes a few seconds to transfer 200MB through to the web browser, but it *does* open. And scrolling is as smooth as butter.

**close big.csv**

Chris has another example with one TRILLION rows and one TRILLION columns, still smooth as butter.

*open datagrid example*

Thanks Chris. We look forward to the many more planned features.

# Extensibility

## Extending JLab

### File viewers

It is also straightforward to add your own file viewer. For example, last year at Scipy someone said it would be great to have a FASTA sequence file viewer for their biology work. We found a javascript library for rendering FASTA information, and wrapped it in a couple of dozen lines of code in a few hours. The result is a small JupyterLab extension that both lets us open Fasta files

*open Fasta file*

and the same extension also automatically enables the notebook to render Fasta information inline.

*open Fasta notebook*

As another example, in January Wolf Vollprecht at QuantStack wanted to embed the excellent draw.io diagram editor in JupyterLab. A few days later, we had a working plugin for creating and editing diagrams.

*create new draw.io file*

### New activities

The GitHub file browser allows you to browse any GitHub organization. For example, we can open the bloomberg organization and run the bqplot examples straight from GitHub, no need to download anything. We can also launch the binder if the repo has a binder associated with it.


### Wrapup

So that's some of the new exciting things in JupyterLab, an extensible, performant, comprehensive environment.

Did I mention that JupyterLab is extensible? 

*open package.json*

Everything you see is a plugin, and your plugins are on equal footing to extend or replace any of ours.

That's the genius of open-source - you can customize your own tools and help the community. I'm most excited about what *you* will do with this tool and the extensions that *you* write.

If you want to learn more about Jupyter, please come to [JupyterCon](https://conferences.oreilly.com/jupyter/jup-ny), August 21-25, in New York City. And come to the free Jupyter Community sprint day of JupyterCon, Saturday Aug 25, following the conference.

Thank you

For more information, see the Jupyter Blog post, and the JupyterLab documentation, and try it out today!
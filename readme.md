# Flask Blueprints


Creates a directory for a Flask application with options for different facets of template customization.

The driving concept is to allow a quick-start of a Flask application given a pip install of the **requirements.txt** file and a few lines of code.

*Note that this is just one of the structurings of how a Flask application directory can be built.*

See the GitHub repository for the [Workout-Tracker](https://github.com/clickityKlein/Workout-Tracker) featuring a Flask application built using this directory structuring. Website deployed [here](https://workout-tracker-9m3l.onrender.com/) *(at the time of this README creation)*.


## Table of Contents

- [Acknowledgements](#acknowledgements)
- [Libraries](#libraries)
- [File Descriptions](#file-descriptions)
- [Create a Directory](#create-a-directory)
- [Attributes](#attributes)
- [Under the Hood](#under-the-hood)


## Acknowledgements

The main framework revolves around the following systems:

- [Bootswatch](https://bootswatch.com/)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Bootstrap](https://getbootstrap.com/)
- [WTForms](https://wtforms.readthedocs.io/en/3.1.x/)
- [Python and Flask Bootcamp: Create Websites using Flask! - Jose Portilla & Pierian Training](https://www.udemy.com/course/python-and-flask-bootcamp-create-websites-using-flask/?couponCode=ST19MT61724)
    - [Specifically the Structuring in the Final Project](https://www.udemy.com/course/python-and-flask-bootcamp-create-websites-using-flask/learn/lecture/11084618#content) *(at the time of this README creation)*
- [Beautiful Interactive Tables for your Flask Templates - Miguel Grinberg](https://blog.miguelgrinberg.com/post/beautiful-interactive-tables-for-your-flask-templates)


[Table of Contents](#table-of-contents)


## Libraries

See `requirements.txt` for the full build of libraries and versions.


[Table of Contents](#table-of-contents)


## File and Folder Descriptions

Proceed by eithering forking this repository, or by downloading the zip-file **flask-blueprints**, and unzipping the file in the directory designated for the Flask project.

- **bootswatch/**
- **flask_generate_directories.py**
- **requirements.txt**
- **template_pages.py**

<div class="container">
<table class="table table-striped">
    <thead>
        <tr>
            <th>Name</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>bootswatch/</td>
            <td>Contains the css files for Bootswatch themes.</td>
        </tr>
        <tr>
            <td>create_templates.py</td>
            <td>Contains a form-like structure to create and modify the BlueprintDirectory object and then generates the directory.</td>
        </tr>
        <tr>
            <td>flask_generate_directories.py</td>
            <td>Contains the directory generation class.</td>
        </tr>
        <tr>
            <td>requirements.txt</td>
            <td>Contains modules and their respective version numbers.</td>
        </tr>
        <tr>
            <td>template_pages.py</td>
            <td>Contains the supporting functions imported in the flask_generate_directories.py file.</td>
        </tr>
    </tbody>
</table>
</div>

---

[Table of Contents](#table-of-contents)


## Create a Directory

1. Create a virtual environment in a chosen folder (make sure to `cd` into folder in terminal).
2. Download the zip-file **flask-blueprints**.
3. Place and unpack the zip-file within the folder containing where the virtual environment is located.
4. Run `pip install -r requirements.txt` in the terminal.
5. Create templates:
    - Recommended:
        - follow instructions in **create_templates.py**
        - there are 3 listed different ways to create a directory
    - Custom:
        - `import flask_generate_directories as fgd`
        - `project_directory = fgd.BlueprintDirectory()`
        - can pass arguments and options within `fgd.BlueprintDirectory()` or pass them manually via attributes
        - `project_directory.create_project_directory()`
        - run `python app.py` in terminal

*Note that* `fgd` *and* `project_directory` *are arbitrary naming.*


[Table of Contents](#table-of-contents)


## Attributes

```{python}
import flask_generate_directories as fgd

project_directory = fgd.BlueprintDirectory(
    app_directory='.',
    app_name='project',
    project_name='project_name',
    models=[],
    pages=[],
    populate=True,
    fancy_options={
        'fancy_tables':False,
        'bootswatch_theme':None,
        },
    page_model_links=None
)
```

### app_directory

Directory to place the Flask application in. If following the [Create a Directory](#create-a-directory) above, leave this as default.

### app_name

Main folder containing **project_name** folder, **.env** file, **.gitignore** file, **app.py** file, and **requirements.txt** file.

`cd` into specified **app_name** and then run `python app.py`.

### project_name

Secondary folder containing **model** folders, **static** folder, **templates** folder, **__init__.py**, and **models.py**

### models

List which contains specified models to start out with.

### pages

List which contains specified pages to start out with.

### populate

Boolean:
- **True**: produces filled **.html** and **.py** files with starting template code.
- **False**: produces empty **.html** and **.py** files (i.e. just the directory).

### fancy_options

Dictionary Options:
- **fancy_tables**:
    - Boolean:
        - **True**: produces customized css and js styled and dynamic/reactive tables. See [Beautiful Interactive Tables for your Flask Templates - Miguel Grinberg](https://blog.miguelgrinberg.com/post/beautiful-interactive-tables-for-your-flask-templates) for details.
        - **False**: produces standard html / bootstrap styled tables.
- **bootswatch_theme**:
    - **None**: produces a website with standard html / bootstrap theme.
    - **\<bootswatch_theme\>**: produces a website with a specified [Bootswatch](https://bootswatch.com/) theme *(enter as a lowercase string)*.
        - use `fgd.BlueprintDirectory().bootswatch_themes()` to display optional themes.
        - see the above mentioned documentation for theme-specific schematics.
- **page_model_links**: dictionary to specify page - model link
    - `fgd.BlueprintDirectory().page_model_links = {"page": "model", ...}`


[Table of Contents](#table-of-contents)


## Under the Hood

### Methods

- **create_project_directory**: creates the Flask application directory with specified options.
- **\_\_repr\_\_** (i.e. `print(fgd.BlueprintDirectory())`): prints information about the customization of the **BlueprintDirectory** object.
- **bootswatch_themes** (i.e. `fgd.BlueprintDirectory().bootswatch_themes()`): returns a list with the possible Bootswatch themes for website stying.


### Supporting Functions

Located under **template_pages.py**, these functions are called into **flask_generate_directories.py** prior to the **BlueprintDirectory** class.

- `create_file_folder(path, structure)`: creates either a file or folder given a path and structure list.
- `ignore_page_links(page_model_links, pages, models)`: checks if pages and models are valid and acceptable links
- `populate_base(pages=[])`: populates the base html page
- `populate_html_extension()`: populates most other html pages
- `populate_error_page(error_code)`: populates error pages html
- `populate_model_views(project_name, model)`: populates views.py files for models
- `populate_core_views(project_name, model='core')`: populates views.py file for core
- `populate_init(project_name, models)`: populates \_\_init\_\_.py file
- `populate_app(project_name)`: populates app.py file
- `populate_error_handlers()`: populates handlers.py file under error_pages model
- `populate_model_script(project_name, models)`: populates models.py file
- `populate_index()`: populates index page html *(landing page)*
- `populate_info()`: populates info page html *(about page)*
- `populate_template(file_path, lines_list)`: takes in lines returned from the other functions and writes them into a file
- `populate_forms()`: populates forms.py files for models
- `populate_requirements()`: populates requirements.txt file
- `populate_ignore()`: populates the .gitignore file
- `populate_env()`: populates the .env file
- `get_bootswatch(theme, path)`: checks validity of Bootswatch theme passed in


[Table of Contents](#table-of-contents)
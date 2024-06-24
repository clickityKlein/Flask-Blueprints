'''
IMPORTANT: DON'T RUN THE ENTIRE SCRIPT, JUST RUN ONE SECTION

1. make sure to cd into chosen folder via terminal
2. if in a virtual environment and/or not sure on requirements, run in terminal:
    pip install requirement.txt
3. follow the directions below, there are three versions listed (only run one section):
    - 1. The Most Basic Application (defaults)
    - 2. The Customized Application I (options to fully customize - prior options)
    - 3. The Customized Application II (options to fully customize - after options)
4. after having ran project_directory.create_project_directory(), run in terminal:
    python app.py
5. recommended to delete the folders created during this process if another build is desired
'''


'''
The Most Basic Application
'''
# import the module
import flask_generate_directories as fgd
# create the object
project_directory = fgd.BlueprintDirectory()
# check customization
print(project_directory)
# create the Flask directory
project_directory.create_project_directory()


'''
The Customized Application I

Choose all options up front.
'''
# import the module
import flask_generate_directories as fgd

# app_directory (default recommended)
app_directory = "."

# app_name (main folder)
# example: app_name = "store"
app_name = "project"

# project_name (secondary folder)
# example: project_name = "store_app"
project_name = "project_name"

# models (i.e. CRUD databases)
# example: models = ["merchandise", "employees", "customers", "departments", "distributors"]
models = []

# pages (i.e. pages to view)
# example: pages = ["products", "staff", "partners"]
pages = []

# populate (default recommended)
populate = True

# fancy_options (table and page styling)
# example: fancy_options = {"fancy_tables": True, "bootswatch_theme": "flatly"}
fancy_options = {"fancy_tables": False, "bootswatch_theme": None}

# page_model_links (specify links between pages and models; dict(page: model, ...))
# example: page_model_links = {"products": "merchandise", "staff": "employees", "partners": "distributors"}
page_model_links = {}

# create the object
project_directory = fgd.BlueprintDirectory(
    app_directory=app_directory,
    app_name=app_name,
    project_name=project_name,
    models=models,
    pages=pages,
    populate=populate,
    fancy_options=fancy_options,
    page_model_links=page_model_links)

# check customization
print(project_directory)

# create the Flask directory
project_directory.create_project_directory()


'''
The Customized Application II

Change options after creation

Can always use a print(object) to check customization
'''
# import the module
import flask_generate_directories as fgd
# create the object
project_directory = fgd.BlueprintDirectory()

# app_directory (default recommended)
app_directory = "."
project_directory.app_directory = app_directory

# app_name (main folder)
# example: app_name = "store"
app_name = "project"
project_directory.app_name = app_name

# project_name (secondary folder)
# example: project_name = "store_app"
project_name = "project_name"
project_directory.project_name = project_name

# models (i.e. CRUD databases)
# example: models = ["merchandise", "employees", "customers", "departments", "distributors"]
models = []
project_directory.models = models

# pages (i.e. pages to view)
# example: pages = ["products", "staff", "partners"]
pages = []
project_directory.pages = pages

# populate (default recommended)
populate = True
project_directory.populate = populate

# fancy_options (table and page styling)
# example: fancy_options = {"fancy_tables": True, "bootswatch_theme": "flatly"}
fancy_options = {"fancy_tables": False, "bootswatch_theme": None}
project_directory.fancy_options = fancy_options

# page_model_links (specify links between pages and models; dict(page: model, ...))
# example: page_model_links = {"products": "merchandise", "staff": "employees", "partners": "distributors"}
page_model_links = {}
project_directory.page_model_links = page_model_links

# check customization
print(project_directory)

# if project customization isn't up to par, change the respective options above

# create the Flask directory
project_directory.create_project_directory()

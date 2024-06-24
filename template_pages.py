'''
flask_generate_directories:
    - create_file_folder(path, structure)
    - ignore_page_links(page_model_links, pages, models)
    - populate_base(pages=[])
    - populate_html_extension()
    - populate_error_page(error_code)
    - populate_model_views(project_name, model)
    - populate_core_views(project_name, model='core')
    - populate_init(project_name, models)
    - populate_app(project_name)
    - populate_error_handlers()
    - populate_model_script(project_name, models)
    - populate_index()
    - populate_info()
    - populate_template(file_path, lines_list)
    - populate_forms()
    - populate_requirements()
    - populate_ignore()
    - populate_env()
    - get_bootswatch(theme, path)
'''

import os
import logging
import shutil

# folder or file creation function
def create_file_folder(path, structure):
    for item in structure:
        if '.' in item:
            with open(f'{path}/{item}', 'w') as file:
                pass
        else:
            sub_path = f'{path}/{item}'
            if not os.path.exists(sub_path):
                os.makedirs(sub_path)

# checks if pages and models are valid and acceptable links
def ignore_page_links(page_model_links, pages, models):
    
    logger = logging.getLogger(__name__)
    link_exclude = set()
    
    # logger warnings
    for link_count, page in enumerate(page_model_links.keys()):
        if page not in pages:
            logger.warning(f'"{page}" not a specified page.\nUse `ngl_object.pages()` to see and edit specified pages.\nThis will not be linked.\n')
            link_exclude.add(link_count)
    for link_count, model in enumerate(page_model_links.values()):
        if model not in models:
            logger.warning(f'"{model}" not a specified model.\nUse `ngl_object.models()` to see and edit specified pages.\nThis will not be linked.\n')
            link_exclude.add(link_count)
            
    return list(link_exclude)

# populates the base html page
def populate_base(pages=[], fancy_tables=False, bootswatch=None, page_model_links=None, models=None):
    # initial block
    lines = ['<!DOCTTYPE html>']
    lines.append(f'<html lang="en" dir="ltr">')
    lines.append(f'{" "*4}<head>')
    lines.append(f'{" "*8}<meta charset="utf-8">')
    lines.append(f'{" "*8}<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">')
    # fancy tables
    if fancy_tables:
        lines.append(f'{" "*8}<!-- Dynamic Table Options -->')
        lines.append(f'{" "*8}<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.25/css/dataTables.bootstrap5.css">')
    
    # bootswatch
    if bootswatch is not None:
        lines.append(f'{" "*8}<!-- Bootswatch Options -->')
        lines.append(f'{" "*8}<link rel="stylesheet" type="text/css" href="/static/css/bootstrap.min.css">')
        
    lines.append(f'{" "*8}<title></title>')
    lines.append(f'{" "*4}</head>')
    lines.append(f'{" "*4}<body>')
    lines.append(f'{" "*4}<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>')
    lines.append(f'{" "*8}<ul class="nav">')
    lines.append(f'{" "*12}<li class="nav-link">')
    lines.append(f'{" "*16}''<a href=\"{{url_for(\'core.index\')}}\">Home</a>')
    lines.append(f'{" "*12}</li>')
    lines.append(f'{" "*12}<li class="nav-link">')
    lines.append(f'{" "*16}''<a href=\"{{url_for(\'core.info\')}}\">About</a>')
    lines.append(f'{" "*12}</li>')
    
    # custom links
    linked_pages = []
    link_pages = [page.replace('.html', '') for page in pages]
    if page_model_links is not None:
        ignore_links = ignore_page_links(page_model_links=page_model_links, pages=link_pages, models=models)
        for link_count, page in enumerate(page_model_links):
            if link_count not in ignore_links:
                model = page_model_links[page]
                linked_pages.append(page)
                link_string = f"'{model}.{page}'"
                link_start = '<a href="{{url_for('
                link_end_1 = ")}}"
                link_end_2 = f'">{page.replace("_", " ").title()}</a>'
                # lines.append('<!--')
                lines.append(f'{" "*12}<li class="nav-link">')
                lines.append(f'{" "*16}'f'{link_start+link_string+link_end_1+link_end_2}')
                # lines.append('-->')
    
    # page section
    nav_pages = [page.replace('.html', '').replace('_', ' ').title() for page in pages if page.replace('.html', '') not in linked_pages]
    for page in nav_pages:
        lines.append(f'{" "*12}<li class="nav-link">')
        lines.append(f'''{" "*16}<a href="#">{page}</a>''')
        lines.append(f'{" "*12}</li>')
        
        
    lines.append(f'{" "*8}</ul>')
    
    # extension capability section
    lines.append(f'{" "*8}<div class="container">')
    lines.append(f'{" "*12}''{% block content %}')
    lines.append('\n')
    lines.append(f'{" "*12}''{% endblock %}')
    lines.append(f'{" "*8}</div>')
    # fancy tables
    if fancy_tables:
        lines.append(f'{" "*8}<!-- Dynamic Table Options -->')
        lines.append(f'{" "*8}<script type="text/javascript" charset="utf8" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>')
        lines.append(f'{" "*8}<script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.25/js/jquery.dataTables.js"></script>')
        lines.append(f'{" "*8}<script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.25/js/dataTables.bootstrap5.js"></script>')
        lines.append(f'{" "*8}''{% block scripts %}{% endblock %}')
        
    # closing block
    lines.append(f'{" "*4}</body>')
    lines.append(f'</html>')
    
    # return
    return(lines)

# template html for other html pages
def populate_html_extension(page):
    lines = ['{% extends "base.html" %}']
    lines.append('{% block content %}')
    lines.append(f'{" "*4}<div class="container">')
    lines.append(f'{" "*8}<h1>{page.replace("_", " ").replace(".html", "").title()}</h1>')
    lines.append(f'{" "*4}</div>')
    lines.append('{% endblock %}')
    return(lines)

# template html for error_pages within templates folder
def populate_error_page(error_code):
    lines = ['{% extends "base.html" %}']
    lines.append('{% block content %}')
    lines.append(f'{" "*4}<div class="jumbotron">')
    if error_code == 403:
        lines.append(f'{" "*8}<h1>403 ACCESS FORBIDDEN</h1>')
    elif error_code == 404:
        lines.append(f'{" "*8}<h1>404 PAGE NOT FOUND</h1>')
    lines.append(f'{" "*4}</div>')
    lines.append('{% endblock %}')
    return(lines)

# template python code for views.py files
def populate_model_views(project_name, pages, model, models, page_model_links):
    # standard
    lines = [f'#{model}/views.py']
    lines.append('from flask import render_template, redirect, url_for, request, Blueprint, flash')
    lines.append(f'from {project_name} import db')
    lines.append('from flask_login import current_user, login_required')
    lines.append(f'# from {project_name}.models import <specified models>')
    lines.append(f'# from {project_name}.{model}.forms import ExampleForm')
    lines.append(f"\n{model} = Blueprint('{model}', __name__)")
    # page model links
    link_pages = [page.replace('.html', '') for page in pages]
    ignore_links = ignore_page_links(page_model_links=page_model_links, pages=link_pages, models=models)
    for link_count, page in enumerate(page_model_links):
        if (link_count not in ignore_links) and (page_model_links[page]==model):
            lines.append('\n')
            lines.append(f"@{model}.route('/{page}')")
            lines.append(f'def {page}():')
            lines.append(f"{' '*4}return render_template('{page}.html')")

    return lines

# template python code for views.py core file
def populate_core_views(project_name, model='core'):
    lines = [f'#{model}/views.py']
    lines.append('from flask import render_template, redirect, url_for, request, Blueprint, flash')
    lines.append(f"{model} = Blueprint('{model}', __name__)")
    lines.append('\n')
    lines.append("@core.route('/')")
    lines.append('def index():')
    lines.append(f"{' '*4}return render_template('index.html')")
    lines.append('\n')
    lines.append("@core.route('/info')")
    lines.append('def info():')
    lines.append(f"{' '*4}return render_template('info.html')")
    return lines

# template python code for main __init__.py file
def populate_init(project_name, models):
    lines = [f'#{project_name}/__init__.py']
    lines.append('from flask import Flask')
    lines.append('from flask_sqlalchemy import SQLAlchemy')
    lines.append('from flask_migrate import Migrate')
    lines.append('import os')
    lines.append('from flask_login import LoginManager')
    lines.append('\n')
    lines.append('app = Flask(__name__)')
    lines.append('\n')
    lines.append("# app.config['SECRET_KEY'] = 'mysecret'")
    lines.append("app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')")
    lines.append('\n')
    
    ### database setup ###
    lines.append('### database setup ###')
    lines.append('basedir = os.path.abspath(os.path.dirname(__file__))')
    lines.append("app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')")
    lines.append("app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False")
    lines.append('\n')
    lines.append('db = SQLAlchemy(app)')
    lines.append('Migrate(app, db)')
    lines.append('### database setup ###')
    ### database setup ###
    lines.append('\n')
    
    ### login manager ###
    lines.append('### login manager ###')
    lines.append('#login_manager = LoginManager()')
    lines.append('#login_manager.init_app(app)')
    lines.append("#login_manager.login_view = 'users.login'")
    lines.append('### login manager ###')
    ### login manager ###
    lines.append('\n')
    
    ### blueprint registrations ###
    blueprints = ['core.views', 'error_pages.handlers', ]
    lines.append('### blueprint registrations ###')
    # imports
    lines.append(f'from {project_name}.core.views import core')
    lines.append(f'from {project_name}.error_pages.handlers import error_pages')
    for model in models:
        lines.append(f'from {project_name}.{model}.views import {model}')
    # registration
    lines.append('app.register_blueprint(core)')
    lines.append('app.register_blueprint(error_pages)')
    for model in models:
        lines.append(f'app.register_blueprint({model})')
    lines.append('### blueprint registrations ###')
    ### blueprint registrations ###
    return lines

# template python code for main app.py file
def populate_app(project_name):
    lines = [f'from {project_name} import app']
    # lines.append('\n')
    lines.append("if __name__ == '__main__':")
    lines.append(f'{" "*4}app.run(debug=True)')
    return lines

# template python code for error handlers
def populate_error_handlers():
    lines = ['# error_pages/handlers.py']
    lines.append('from flask import Blueprint, render_template')
    lines.append("error_pages = Blueprint('error_pages', __name__)")
    lines.append('\n')
    lines.append('@error_pages.app_errorhandler(404)')
    lines.append('def error_404(error):')
    lines.append(f"{' '*4}return render_template('error_pages/404.html'), 404")
    lines.append('\n')
    lines.append('@error_pages.app_errorhandler(403)')
    lines.append('def error_403(error):')
    lines.append(f"{' '*4}return render_template('error_pages/403.html'), 404")
    return lines

# template python code for models.py
def populate_model_script(project_name, models):
    lines = ['#models.py']
    lines.append(f'from {project_name} import db, login_manager')
    lines.append(f'#from {project_name} import login_manager')
    lines.append('#from from werkzeug.security import generate_password_hash, check_password_hash')
    lines.append('#from flask_login import UserMixin')
    lines.append('from datetime import datetime')
    lines.append('\n')
    lines.append('#@login_manager.user_loader')
    lines.append('#def load_user(user_id):')
    lines.append(f'#{" "*4}return User.query.get(user_id)')
    for model in models:
        lines.append('\n')
        model_name = model.replace('_', ' ').title().replace(' ','')
        lines.append(f'class {model_name}(db.Model):')
        lines.append(f'#class {model_name}(db.Model, UserMixin):')
        lines.append(f'{" "*4}# table name')
        lines.append(f"{' '*4}__tablename__ = '{model}'")
        lines.append('\n')
        lines.append(f'{" "*4}# specific columns')
        lines.append('\n')
        lines.append(f'{" "*4}# relationships')
        lines.append('\n')
        lines.append(f'{" "*4}# instance')
        lines.append(f'{" "*4}def __init__(self):')
        lines.append(f'{" "*8}pass')
        lines.append('\n')
        lines.append(f'{" "*4}# functions')
        lines.append('\n')
    
    return lines

# template html for index.html page
# rest of the pages will have the standard extension, this will use something to appear
def populate_index():
    lines = ['{% extends "base.html" %}']
    lines.append('{% block content %}')
    lines.append(f'{" "*4}<div class="container">')
    lines.append(f'{" "*8}<h1>Welcome!</h1>')
    lines.append(f'{" "*4}</div>')
    lines.append('{% endblock %}')
    return(lines)

# template html for info.html page
# rest of the pages will have the standard extension, this will use something to appear
def populate_info():
    lines = ['{% extends "base.html" %}']
    lines.append('{% block content %}')
    lines.append(f'{" "*4}<div class="container">')
    lines.append(f'{" "*8}<h1>About</h1>')
    lines.append(f'{" "*4}</div>')
    lines.append('{% endblock %}')
    return(lines)
        
# after calling a populate function for lines_list, write to the respective file_path
def populate_template(file_path, lines_list):
    with open(file_path, 'w') as file:
        for line in lines_list:
            file.write(f'{line}\n')
    file.close()

# template python code for forms
def populate_forms():
    lines = ['from flask_wtf import FlaskForm']
    lines.append('from wtforms import BooleanField, DateField, DateTimeField, DecimalField, FileField, MultipleFileField, FloatField, RadioField, SelectField, SelectMultipleField, SubmitField, StringField')
    lines.append('\n# example form')
    lines.append('class ExampleForm(FlaskForm):')
    lines.append(f'{" "*4}string_entry = StringField("Example String")')
    lines.append(f'{" "*4}date_entry = DateField("Example Date")')
    lines.append(f'{" "*4}submit = SubmitField("Submit Example")')
    return(lines)
    
# template txt code for requirements.txt
def populate_requirements():
    lines = ['alembic==1.13.1']
    lines.append('blinker==1.8.2')
    lines.append('click==8.1.7')
    lines.append('colorama==0.4.6')
    lines.append('dnspython==2.6.1')
    lines.append('email_validator==2.1.1')
    lines.append('Flask==3.0.3')
    lines.append('Flask-Login==0.6.3')
    lines.append('Flask-Migrate==4.0.7')
    lines.append('Flask-SQLAlchemy==3.1.1')
    lines.append('Flask-WTF==1.2.1')
    lines.append('greenlet==3.0.3')
    lines.append('gunicorn==22.0.0')
    lines.append('idna==3.7')
    lines.append('itsdangerous==2.2.0')
    lines.append('Jinja2==3.1.4')
    lines.append('Mako==1.3.5')
    lines.append('MarkupSafe==2.1.5')
    lines.append('numpy==1.26.4')
    lines.append('packaging==24.1')
    lines.append('pandas==2.2.2')
    lines.append('python-dateutil==2.9.0.post0')
    lines.append('pytz==2024.1')
    lines.append('setuptools==69.5.1')
    lines.append('six==1.16.0')
    lines.append('SQLAlchemy==2.0.30')
    lines.append('typing_extensions==4.12.2')
    lines.append('tzdata==2024.1')
    lines.append('Werkzeug==3.0.3')
    lines.append('wheel==0.43.0')
    lines.append('WTForms==3.1.2')
    
    return(lines)
    
# template txt code for .gitignore
def populate_ignore():
    lines = ['.env']
    return(lines)

# template txt code for .gitignore
def populate_env():
    lines = ['SECRET_KEY="mysecret"']
    return(lines)

# copy correct bootswatch file
def get_bootswatch(theme, path):
    possible_themes = [
    'cerulean',
    'cosmo',
    'cyborg',
    'darkly',
    'flatly',
    'journal',
    'litera',
    'lumen',
    'lux',
    'materia',
    'minty',
    'morph',
    'pulse',
    'quartz',
    'sandstone',
    'simplex',
    'sketchy',
    'slate',
    'solar',
    'spacelab',
    'superhero',
    'united',
    'vapor',
    'yeti',
    'zephyr',
    ]
    if theme in possible_themes:
        source_path = f'bootswatch/{theme}/bootstrap.min.css'
        destination_path = os.path.join(path, 'bootstrap.min.css')
        shutil.copyfile(source_path, destination_path)
    else:
        logger = logging.getLogger(__name__)
        logger.warning('Specified Bootswatch Theme Not Found!\nUse `ngl_object.bootswatch_themes()` for possible designations.')

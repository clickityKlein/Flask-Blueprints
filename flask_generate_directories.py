'''
class to create the 
'''

## Generate Directory ##
# import template_pages
from template_pages import *
 
class BlueprintDirectory:

    def __init__(self,
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
                 page_model_links=None):
        
        self.app_directory = app_directory
        self.app_name = app_name
        self.project_name = project_name
        self.models = models
        self.pages = pages
        self.populate = populate
        self.fancy_options = fancy_options
        self.page_model_links = page_model_links
        self.generate_count = 0
        

    # full function to create the directory
    def create_project_directory(self):
        # warning
        if self.generate_count == 1:
            gen_count = 'time'
        else:
            gen_count = 'times'
        if input(f'This object has been used to generate a directory structure {self.generate_count} {gen_count}.\nContinuing could overwrite existing folders and files.\nARE YOU SURE YOU WOULD LIKE YOU CONTINUE?\n(y/n)\n').lower()[0] != 'y':
            return 'Generation Process Exited'
        
        # main project path
        main_path = f'{self.app_directory}/{self.app_name}'
        
        # main app folder
        if not os.path.exists(main_path):
            os.makedirs(main_path)
        
        # constants
        initial_tier_constants = ['app.py', 'requirements.txt', self.project_name, '.gitignore', '.env']
        secondary_tier_constants = ['core', 'error_pages', 'static', 'templates', '__init__.py', 'models.py']
        model_constants = ['__init__.py', 'forms.py', 'views.py']
        core_constants = ['__init__.py', 'views.py']
        error_pages_constants = ['handlers.py']
        templates_constants = ['error_pages', 'base.html', 'index.html', 'info.html']
        error_pages_sub_constants = ['403.html', '404.html']
        
        # templates append
        # proper file name and add html to all pages
        for num, page in enumerate(self.pages):
            # proper file naming (lowercase and underscores)
            page = page.replace(' ', '_').lower()
            # ensure .html suffix
            if '.html' not in self.pages:
                page = f'{page}.html'
            self.pages[num] = page
        # combine templates_constants and pages       
        templates_all = templates_constants + self.pages
        
        # models appending
        # proper folder naming and remove any suffix
        for num, model in enumerate(self.models):
            # proper folder naming (lower, underscores, remove periods)
            model = model.replace(' ', '_').replace('.', '').lower()
            self.models[num] = model
        # combine secondary_tier_constants with models
        secondary_tier_all = secondary_tier_constants + self.models
        
        # initial tier creation
        # app.py, requirements.txt, project_name folder, .gitignore, .env
        create_file_folder(main_path, initial_tier_constants)
       
        if self.populate:
            # populate main app.py
            lines_list = populate_app(project_name=self.project_name)
            file_path = f'{main_path}/app.py'
            populate_template(file_path=file_path, lines_list=lines_list)
            
            # populate requirement.txt
            lines_list = populate_requirements()
            file_path = f'{main_path}/requirements.txt'
            populate_template(file_path=file_path, lines_list=lines_list)
            
            # poulate .gitignore
            lines_list = populate_ignore()
            file_path = f'{main_path}/.gitignore'
            populate_template(file_path=file_path, lines_list=lines_list)
            
            # populate .env
            lines_list = populate_env()
            file_path = f'{main_path}/.env'
            populate_template(file_path=file_path, lines_list=lines_list)
        
        
        # secondary tier creation
        # 'core', 'error_pages', 'static', 'templates', '__init__.py', 'models.py', model folders
        sub_path = f'{main_path}/{self.project_name}'
        create_file_folder(sub_path, secondary_tier_all)
        # populate main __init__.py
        if self.populate:
            lines_list = populate_init(project_name=self.project_name, models=self.models)
            file_path = f'{sub_path}/__init__.py'
            populate_template(file_path=file_path, lines_list=lines_list)
        # populate models.py
        if self.populate:
            lines_list = populate_model_script(project_name=self.project_name, models=self.models)
            file_path = f'{sub_path}/models.py'
            populate_template(file_path=file_path, lines_list=lines_list)
        # populate static (if bootswatch is selected)
        if self.fancy_options['bootswatch_theme'] is not None:
            # create css folder
            css_path = f'{sub_path}/static'
            create_file_folder(css_path, ['css'])
            # create copy of specified bootswatch theme
            get_bootswatch(self.fancy_options['bootswatch_theme'], f'{css_path}/css')
            
                
        # tertiary tier plus creation
        # core
        tertiary_path = f'{main_path}/{self.project_name}/core'
        create_file_folder(tertiary_path, core_constants)
        # populate core folder views.py
        if self.populate:
            file_path = f'{sub_path}/core/views.py'
            lines_list = populate_core_views(project_name=self.project_name)
            populate_template(file_path=file_path, lines_list=lines_list)
            
        # error_pages
        tertiary_path = f'{main_path}/{self.project_name}/error_pages'
        create_file_folder(tertiary_path, error_pages_constants)
        # populate handlers.py
        if self.populate:
            file_path = f'{tertiary_path}/handlers.py'
            lines_list = populate_error_handlers()
            populate_template(file_path=file_path, lines_list=lines_list)
        
        # templates
        tertiary_path = f'{main_path}/{self.project_name}/templates'
        plus_path = f'{tertiary_path}/error_pages'
        create_file_folder(tertiary_path, templates_all)
        create_file_folder(plus_path, error_pages_sub_constants)
        # populate pages in templates
        if self.populate:
            # lines_list = populate_html_extension() # deprecated
            lines_list_base = populate_base(pages=self.pages,
                                            fancy_tables=self.fancy_options['fancy_tables'],
                                            bootswatch=self.fancy_options['bootswatch_theme'],
                                            page_model_links=self.page_model_links,
                                            models=self.models)
            lines_list_index = populate_index()
            lines_list_info = populate_info()
            lines_list_403 = populate_error_page(403)
            lines_list_404 = populate_error_page(404)
            for page in templates_all:
                if page == 'error_pages':
                    file_path_403 = f'{plus_path}/403.html'
                    file_path_404 = f'{plus_path}/404.html'
                    populate_template(file_path=file_path_403, lines_list=lines_list_403)
                    populate_template(file_path=file_path_404, lines_list=lines_list_404)
                elif page == 'base.html':
                    file_path = f'{tertiary_path}/{page}'
                    populate_template(file_path=file_path, lines_list=lines_list_base)
                elif page == 'index.html':
                    file_path = f'{tertiary_path}/{page}'
                    populate_template(file_path=file_path, lines_list=lines_list_index)
                elif page == 'info.html':
                    file_path = f'{tertiary_path}/{page}'
                    populate_template(file_path=file_path, lines_list=lines_list_info)
                else:
                    file_path = f'{tertiary_path}/{page}'
                    lines_list = populate_html_extension(page)
                    populate_template(file_path=file_path, lines_list=lines_list)
        
        # models - populate built in (still allows boolean selection)
        for model in self.models:
            tertiary_path = f'{main_path}/{self.project_name}/{model}'
            create_file_folder(tertiary_path, model_constants)
            
            if self.populate:
                # views
                file_path = f'{tertiary_path}/views.py'
                lines_list = populate_model_views(project_name=self.project_name,
                                                  model=model,
                                                  pages=self.pages,
                                                  models=self.models,
                                                  page_model_links=self.page_model_links)
                populate_template(file_path=file_path, lines_list=lines_list)
                # forms
                file_path = f'{tertiary_path}/forms.py'
                lines_list = populate_forms()
                populate_template(file_path=file_path, lines_list=lines_list)
                
        # version count
        self.generate_count += 1
            
                
    def __repr__(self):
        # initial section
        lines = []
        lines.append('A Flask Directory Blueprint Object:\n\n')
        lines.append(f'The directory will placed in this folder: "{self.app_directory}"\n')
        lines.append(f'The directory will begin with: "{self.app_name}"\n')
        lines.append(f'Most of the components will be under: "{self.project_name}"\n')
        lines.append('Basic folders and files will be created...\n\n')
        
        # models section
        if len(self.models) > 0:
            lines.append('Templates for the following "models" will be created:\n')
            for model in self.models:
                lines.append(f'{"-"*3}> {model}\n\n')
        else:
            lines.append('No "models" were specified\n\n')
        
        # pages section
        if len(self.pages) > 0:
            lines.append('Templates for the following "pages" will be created:\n')
            for page in self.pages:
                lines.append(f'{"-"*3}> {page}\n\n')
        else:
            lines.append('No "pages" were specified\n\n')
        
        # populated section
        if self.populate:
            lines.append('"populate" was specified as True:\n')
            lines.append(f'{"-"*3}> python and html files will have basic templating\n\n')
        else:
            lines.append('"populate" was specified as false:\n')
            lines.append(f'{"-"*3}> python and html files will not have basic templating\n\n')
            
        # fancy options
        lines.append('Fancy Options:\n')
        lines.append(f'{"-"*3}> Fancy Tables Enabled: {self.fancy_options["fancy_tables"]}\n\n')
        lines.append(f'{"-"*3}> Bootswatch Theme: {self.fancy_options["bootswatch_theme"]}\n\n')
            
        # generation count
        if self.generate_count == 1:
            gen_count = 'time'
        else:
            gen_count = 'times'
        lines.append(f'This object has been used to generate a directory structure {self.generate_count} {gen_count}.')
        
        # print the customization options
        print_lines = ''.join(lines)
        return print_lines
    
    def bootswatch_themes(self):
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
        
        return possible_themes

import jinja2
from pathlib import Path


class TeX_Template():

    def __init__(self, template_folder:Path, template_name:str, environment_variables_dict:dict = None):
        # TODO is the current_directory appropriate name?
        self._environment = jinja2.Environment(loader = jinja2.FileSystemLoader(template_folder))
        # If configuration dictionary is defined, set environment variables.
        if environment_variables_dict:
            self.set_environment_variables(environment_variables_dict)
        # Load a template by name - filename of the template with extension eg. get_template("template.tex")
        self._template = self._environment.get_template(template_name)


    def set_environment_variables(self,environment_variables_dict:dict):
        conf = environment_variables_dict
        for conf_variable in conf.keys():
            match conf_variable:
                case "VARIABLE_START_STRING":
                    self._environment.variable_start_string = conf[conf_variable]
                case "VARIABLE_END_STRING" :
                    self._environment.variable_end_string = conf[conf_variable]
                case "BLOCK_START_STRING" :
                    self._environment.block_start_string = conf[conf_variable]
                case "BLOCK_END_STRING" :
                    self._environment.block_end_string = conf[conf_variable]
                case "COMMENT_START_STRING":
                    self._environment.comment_start_string =conf[conf_variable]
                case "COMMENT_END_STRING":
                    self._environment.comment_end_string = conf[conf_variable]
                case _:
                    print(f"Configuration variable {conf_variable} not recognized")

    def set_template(self, template_name:str):
        '''Utility method sets template from the templates available in the environment folder'''
        self._template = self._environment.get_template(template_name)
   
    def load_configuration_file(self, filename:Path)->dict:
        '''Utility method get configuration from external file'''
        # TODO Get configuration from external file preferably json
        configuration_variables_dictionary = {}
        return configuration_variables_dictionary
    def render(self,**kwargs) -> str:
        # TODO needs testing
        return self._template.render(**kwargs)
    def __str__(self):
        return self.filename

    def __repr__(self):
        return f"TeX_Template : {self.filename}"




if __name__ == '__main__':
    print("TESTING")
    print("At least it runs")
    # Test if file exists
    static_dir = Path(__file__).resolve().parent.parent / 'static'
    print(static_dir)
    # Test if file can be read
    template_file=static_dir / 'template.tex'

    test_if_file_exists = False
    if test_if_file_exists:
        with open(template_file,"r") as file:
            for line in file:
                print(line)
    # Environment variables
    conf = dict(
        BLOCK_START_STRING = r"\begin{jinja_block}",
        BLOCK_END_STRING =  r"\end{jinja_block}",
        VARIABLE_START_STRING = r"\begin{jinja}",
        VARIABLE_END_STRING = r"\end{jinja}",
        COMMENT_START_STRING = r"\begin{jinja_comment}",
        COMMENT_END_STRING = r"\end{jinja_comment}",
    )
    # Create template object
    my_template = TeX_Template(static_dir,"template.tex", conf)
    print("Template created")
    # Check information
    print(my_template._environment.variable_start_string)
    # Render
    print(my_template.render(var1 = "Successssssss"))
    
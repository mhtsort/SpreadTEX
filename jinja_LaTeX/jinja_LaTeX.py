import jinja2
from pathlib import Path


class TeX_Template(jinja2.Template):
    '''Objects of this class contain the text of a jinja2 Template of a LaTeX document
    '''
    '''DELETE WHEN READY
    def __init__(self, template, filename:str = "template.tex" ):
        self.template = jinja2.Template(template)
        self.filename = filename
        #Define template parameters
        # Define your custom delimiters
        self.template.environment.BLOCK_START_STRING = r"\begin{jinja_block}"
        self.template.environment.BLOCK_END_STRING = r"\end{jinja_block}"
        self.template.environment.VARIABLE_START_STRING = r"\begin{jinja}"
        self.template.environment.VARIABLE_END_STRING = r"\end{jinja}"
        self.template.environment.COMMENT_START_STRING = r"\begin{jinja_comment}"
        self.template.environment.COMMENT_END_STRING = r"\end{jinja_comment}"
        # Create an environment with your custom delimiters
        self.env = self.template.Environment(
        variable_start_string = jj.environment.VARIABLE_START_STRING,
        variable_end_string = jj.environment.VARIABLE_END_STRING
        )
        text = r"This is \begin{jinja} myvar1 \end{jinja} and \begin{jinja} myvar2 \end{jinja}"
        # Create the template using the custom environment
        template_inside = env.from_string(text)
    '''
    def __init__(self,current_directory):
        # TODO is the current_directory apropriate name?
        self._environment = jinja2.Environment(loader = jinja2.FileSystemLoader(current_directory))
        pass
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
                    print(f"Configuration variable {_} not recognized")
    def __str__(self):
        return self.filename

    def __repr__(self):
        return f"TeX_Template : {self.filename}"



class Data_to_Template():
    
    # data defined as a list of tuples. Each tuple contains one row of variables for the template
    def __init__(self, data:list[tuple] =[], columns_list=[]):
        self.data = data
        
if __name__ == '__main__':
    print("Works fine")
    # Test if file exists
    static_dir = Path(__file__).resolve().parent.parent / 'static'
    print(static_dir)
    # Test if file can be read
    template_file=static_dir / 'template.tex'
    with open(template_file,"r") as file:
        for line in file:
            print(line)
    # Test if data goes into template
    var1 = "Jinja Works!"
    
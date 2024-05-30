import jinja2
from pathlib import Path


class TeX_Template(jinja2.Template):
    '''Objects of this class contain the text of a jinja2 Template of a LaTeX document
    '''
    def __init__(self, template, filename:str = "tex_template.tex" ):
        self.template = jinja2.Template(template)
        self.filename = filename
        
    def __str__(self):
        return self.filename

    def __repr__(self):
        return f"TeX_Template : {self.filename}"



class Data_to_Template():
    
    # data defined as a list of tuples. Each tuple contains one row of variables for the template
    def __init__(self, data:list[tuple] =[], columns_list=[]):
        self.data = data
        

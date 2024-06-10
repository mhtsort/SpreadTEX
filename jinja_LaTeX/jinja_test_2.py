from jinja2 import Template, Environment, FileSystemLoader
from pathlib import Path
# Basic usage of Template.
'''
Template creates a template object that can be rendered
template.render -> final text

'''
var = "++ D A T A ++"
template_text = "This is {{ input1}} and {{input2}}"
template = Template(template_text)
out = template.render(
    input1 = var,
    input2 = "Sparta",
)
print(out)

# Basic usage of Environment

# Get the absolute path to the directory containing this script
current_directory = Path(__file__).resolve().parent

env = Environment(loader = FileSystemLoader(current_directory))
# Load a template by name
template = env.get_template('template.tex')
# Render the template with context data
output = template.render(var1="++ Jinja2 Environment ++")
print(output)

# TODO Usage of environment changing Environment parameters

# Get the absolute path to the directory containing this script
current_directory = Path(__file__).resolve().parent

env :Environment = Environment(loader = FileSystemLoader(current_directory))
env.variable_start_string = r"\begin{jinja}"
env.variable_end_string = r"\end{jinja}"
# Load a template by name
template :Template= env.get_template('template.tex')
# Render the template with context data
output = template.render(xx ="++ Jinja2 Environment ++")
print(output)
import jinja2 as jj

# Define your custom delimiters
jj.environment.BLOCK_START_STRING = r"\begin{jinja_block}"
jj.environment.BLOCK_END_STRING = r"\end{jinja_block}"
jj.environment.VARIABLE_START_STRING = r"\begin{jinja}"
jj.environment.VARIABLE_END_STRING = r"\end{jinja}"
jj.environment.COMMENT_START_STRING = r"\begin{jinja_comment}"
jj.environment.COMMENT_END_STRING = r"\end{jinja_comment}"


# Create an environment with your custom delimiters
env = jj.Environment(
    variable_start_string = jj.environment.VARIABLE_START_STRING,
    variable_end_string = jj.environment.VARIABLE_END_STRING
)

# Define your template text
text = r"This is \begin{jinja} myvar \end{jinja}"

# Create the template using the custom environment
template = env.from_string(text)
#TODO use jj.Template()
# Render the template with your context variables
rendered = template.render(myvar="Athens")
print(rendered)

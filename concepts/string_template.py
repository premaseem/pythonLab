# Form a string template which can be interpolated or substituted
# Read more
# https://stackabuse.com/formatting-strings-with-the-python-template-class/
# @Author Aseem Jain


from string import Template
template = Template('Hi $name, welcome to $site')

# by passing var
final_string = template.substitute(name="Aseem",site="premaseem.me")
print(final_string)
# Hi John Doe, welcome to StackAbuse.com

# By using unpacked dict
mapping = {'name': 'John Doe', 'site': 'StackAbuse.com'}
final_string = template.substitute(**mapping)
print(final_string)
# 'Hi John Doe, welcome to StackAbuse.com'
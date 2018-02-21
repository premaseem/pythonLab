__author__ = 'Aseem Jain'

# The get() method on dicts
# and its "default" argument

name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")

""" Sample output

>>> greeting(382)
"Hi Alice!"

>>> greeting(333333)
"Hi there!"

"""
"""
@Author: Aseem Jain
@Linkedin: https://www.linkedin.com/in/premaseem/
@Github: https://github.com/premaseem/pythonLab/tree/master/challenge

Need to find the coupon if exists from the product Category.

"""
Coupons = [
    {"Category Name":"Comforter Sets", "Coupon Name":"Comforters Sale","Modified date": "2019-11-20"},
    {"Category Name":"Bedding", "Coupon Name":"Savings on Bedding","Modified date": "2019-11-20"},
    {"Category Name":"Bed Bath", "Coupon Name":"Low price for Bed Bath","Modified date": "2019-11-20"},
    {"Category Name":"Toy", "Coupon Name":"Savings", "Modified date": "2019-11-20"},
    {"Category Name":"Toy", "Coupon Name":"Savings on top", "Modified date": "2018-11-20"},
    {"Category Name":"Toy", "Coupon Name":"Savings on top", "Modified date": "2018-11-10"},
]

print(Coupons)
Categories = [
    {"Category Name":"Comforter Sets",
     "Category Parent Name":"Bedding"},
    {"Category Name":"Bedding",
     "Category Parent Name":"Bed Bath"},
    {"Category Name":"Bed Bath", "Category Parent Name":None},
    {"Category Name":"Soap Dispensers", "Category Parent Name":"Bathroom Accessories"},
    {"Category Name":"Bathroom Accessories", "Category Parent Name":"Bed Bath"},
    {"Category Name":"Toy Organizers", "Category Parent Name":"Baby And Kids"},
    {"Category Name":"Baby And Kids", "Category Parent Name":None}
]

# get parent or return None
def get_parent(ui):
    for element in Categories:
        if ui == element["Category Name"]:
            return element["Category Parent Name"]

    return None

# print(get_parent("Bathroom Accessories"))

# 1. simple input
# 2. no key found
# 3. Find in parent
# ui = "Comforter Sets"
ui = "Bathroom Accessories"
ui = "Bed Bath"
ui = "Toy Organizers"

def get_coupon(ui):
    for element in Coupons:
        if ui == element["Category Name"]:
            return element["Coupon Name"]
    prt = get_parent(ui)
    # print("retry parent",prt)
    if prt:
        get_coupon(prt)

print(get_coupon(ui))

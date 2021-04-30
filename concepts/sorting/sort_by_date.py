"""
@Author: Aseem Jain
@Linkedin: https://www.linkedin.com/in/premaseem/
@Github: https://github.com/premaseem/pythonLab/tree/master/challenge

"""


from datetime import datetime

# sorting list of date strings
my_dates = ['5-Nov-18', '25-Mar-17', '1-Nov-18', '7-Mar-17']
my_dates.sort(key=lambda x: datetime.strptime(x, "%d-%b-%y"))

# sorting list of map with dates
coupons =[ {"Category Name":"Dhoom1",  "Modified date": "2018-11-20"},
{"Category Name":"Dhoom2",  "Modified date": "2018-11-10"} ]
coupons.sort(key=lambda x: datetime.strptime(x["Modified date"], "%Y-%m-%d"))


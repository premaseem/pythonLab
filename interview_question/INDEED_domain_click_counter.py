# Asked by Indeed
# You are in charge of a display advertising program.
# Your ads are displayed on websites all over the internet.
# You have some CSV input data that counts how many times that users have clicked on an ad on each individual domain.
# Every line consists of a click count and a domain name, like this:

# counts = [ "900,google.com",
#      "60,mail.yahoo.com",
#      "10,mobile.sports.yahoo.com",
#      "40,sports.yahoo.com",
#      "300,yahoo.com",
#      "10,stackoverflow.com",
#      "20,overflow.com",
#      "2,en.wikipedia.org",
#      "1,m.wikipedia.org",
#      "1,mobile.sports",
#      "1,google.co.uk"]

# Write a function that takes this input as a parameter and returns a data structure containing the number of clicks that were recorded on each domain AND each subdomain under it.
# For example, a click on "mail.yahoo.com" counts toward the totals for "mail.yahoo.com", "yahoo.com", and "com".
# (Subdomains are added to the left of their parent domain. So "mail" and "mail.yahoo" are not valid domains.
# Note that "mobile.sports" appears as a separate domain near the bottom of the input.)

# Sample output (in any order/format):

# calculateClicksByDomain(counts) =>
# com:                     1340
# google.com:              900
# stackoverflow.com:       10
# overflow.com:            20
# yahoo.com:               410
# mail.yahoo.com:          60
# mobile.sports.yahoo.com: 10
# sports.yahoo.com:        50
# org:                     3
# wikipedia.org:           3
# en.wikipedia.org:        2
# m.wikipedia.org:         1
# mobile.sports:           1
# sports:                  1
# uk:                      1
# co.uk:                   1
# google.co.uk:            1

# n: number of domains in the input
# (individual domains and subdomains have a constant upper length)



def get_domains(dm):
    dms = set()
    while "." in dm:
        i = dm.index(".")
        dms.add(dm)
        dm = dm[i+1:]
    dms.add(dm)
    return dms


# print(dms)

def map_it(counts):
    mm ={}
    for c in counts:
        p =c.split(",")
        mm[p[1]] = p[0]
    return mm



counts = ["900,google.com",
          "60,mail.yahoo.com",
          "10,mobile.sports.yahoo.com",
          "40,sports.yahoo.com",
          "300,yahoo.com",
          "10,stackoverflow.com",
          "20,overflow.com",
          "2,en.wikipedia.org",
          "1,m.wikipedia.org",
          "1,mobile.sports",
          "1,google.co.uk"]



# print(mymap)

def create_domain_set(domain_list):
    ms = set()
    for d in domain_list:
        for dms in get_domains(d):
            ms.add(dms)
    return ms

# domain_set = create_domain_set(mymap)
# print(domain_set)

def calculate_click_count(domain_set,click_map):
    nm = {}
    for domain in domain_set:
        t = 0
        for k,v in click_map.items():
            if domain == k:
                t = t + int(v)
        nm[domain] = t
    return nm


def calculateClicksByDomain(counts):
    mymap = map_it(counts)
    dms = create_domain_set(mymap.keys())
    ans = calculate_click_count(dms,mymap)
    for k,v in ans.items():
        print("{}:  \t  {} ".format(k,v).expandtabs(50))

calculateClicksByDomain(counts)









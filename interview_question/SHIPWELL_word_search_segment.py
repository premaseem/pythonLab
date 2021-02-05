"""
@Author: Aseem Jain
Problem: find the search terms in the string
and return the shortest segment containing the search terms.
"""


def search(doc, terms):
    """
    :arg document or String
    :arg list of search terms

    """
    d = {}
    for term in terms:
        d[term] = []

    words = doc.split()
    for i, word in enumerate(words):
        if word in terms:
            d[word].append(i)

    l1 = d.get(terms[0])
    l2 = d.get(terms[1])
    ans = None
    gap = float("inf")
    for le1 in l1:
        for le2 in l2:
            g = abs(le1 - le2)
            if g < gap:
                gap = g
                ans = (le1, le2)
    if not ans:
        return "Terms {} not found ".format(terms)

    le1 = ans[0]
    le2 = ans[1]

    if le1 < le2:
        return " ".join(words[le1:le2 + 1])
    else:
        return " ".join(words[le2:le1 + 1])


input = "austin is away from dallas, but price for dallas and austin are best."
terms = ["austin", "dallas"]
print(search(input, terms))

# Match the brackets

a = []
def comp(b):
    if b is "[":
        return "]"
    if b is "(":
        return ")"
    if b is "{":
        return "}"

    if b is "]":
        return "["
    if b is ")":
        return "("
    if b is "}":
        return "{"

def solution(brs):
    # Type your solution here
    for i, b in enumerate(brs):
        if b in ["[","{","("]:
            a.append(b)
        else:
            if(comp(a.pop()) != b):
                return False
    if len(a) != 0:
        return False
    return True

assert solution("()")
assert solution("{}[]{}()")
assert solution("{{}{[([]{})](){{}}}(((({}){()[]}((){})))())}")

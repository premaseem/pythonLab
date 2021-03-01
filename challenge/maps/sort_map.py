"""
@Author: Aseem Jain
@Linkedin: https://www.linkedin.com/in/premaseem/
@Github: https://github.com/premaseem/pythonLab/tree/master/challenge

Sort map/dictionary by keys and values

"""
map = { 3:15, 0:10, 5:50, 7:25 }
sorted_key = { 0:10, 3:15, 5:50, 7:25 }
sorted_values = { 5:50, 7:25, 0:10, 3:15}

def sol(m):
    s_k ={}
    s_v ={}
    # On 1
    for k in sorted(m.keys()):
        s_k[k] = m.get(k)

    for v in sorted(m.values()):
        for k in m:
            if v == m.get(k):
                s_v[k] = v

    return (s_k,s_v)


def sol1(m):
    s_k_t = sorted(m.items(),key=lambda i:i[0])
    s_v_t = sorted(m.items(),key=lambda i:i[1])

    s_k_m = {}
    for k,v in s_k_t: s_k_m[k]=v

    s_v_m = {}
    for k,v in s_v_t: s_v_m[k]=v

    return (s_k_m,s_v_m)

def sol2(m):
    s_k_t = sorted(m.items(),key=lambda i:i[0])
    s_v_t = sorted(m.items(),key=lambda i:i[1])
    def tuple_to_map(t):
        new_m = {}
        for k,v in t:
            new_m[k]=v
        return new_m
    return (tuple_to_map(s_k_t),tuple_to_map(s_v_t))


test_data = [
    (map, (sorted_key,sorted_values) )
]

for given, expected in test_data:
    assert sol(given) == expected
    assert sol1(given) == expected
    print(f"Test passed for: given {given} and expected = {expected}")

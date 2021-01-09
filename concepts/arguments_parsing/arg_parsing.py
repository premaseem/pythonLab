import argparse

o = argparse.ArgumentParser(description="__doc__")
o.add_argument("arg" )
o.add_argument("--brg",required=False, help="please enter bra size",dest="abc")
o.add_argument("--crg",required=True, help="please enter bra size")
# o.add_argument(help="help",)
o = o.parse_args()
print(o)
from optparse import OptionParser

prep_mode = None

parser = OptionParser()
parser.add_option("-m", "--mode",  dest="prep_mode", metavar="MYVAR",
    help="(REQUIRED)")

(options, args) = parser.parse_args()

print(options.prep_mode)
prep_mode = options.prep_mode

if prep_mode is not None :
    print("only prepping")
else:
    print("executing for real")


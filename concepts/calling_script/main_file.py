from optparse import OptionParser

def call_method(arg = None):
    print("method called with arg", arg)

if __name__ == '__main__':
    # provide options
    parser = OptionParser()
    parser.add_option("-d", "--database", dest="database", metavar="DATABASE",
        help="Database product name (REQUIRED)")
    parser.add_option("-e", "--environment", dest="environment", metavar="ENVIRONMENT",
        help="Database product name (REQUIRED)")
    parser.add_option("-p", "--patchfile", dest="patchfile", metavar="PATCHFILE",
        help="Patch file path in S3 to execute. Should be TAR file.(REQUIRED)")
    parser.add_option("-m", "--max_thread", dest="max_thread", metavar="MAX_THREAD",
        help="Max number of con current processes.(OPTIONAL)")

    (options, args) = parser.parse_args()
    print(options)
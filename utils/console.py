class bColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def header(string):
        return bColors.HEADER + str(string) + bColors.ENDC

    def blue(string):
        return bColors.OKBLUE + str(string) + bColors.ENDC

    def green(string):
        return bColors.OKGREEN + str(string) + bColors.ENDC

    def bold(string):
        return bColors.BOLD + str(string) + bColors.ENDC
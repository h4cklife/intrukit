"""
IntruKit Colors Class

This is used in majority of the framework code but termcolors may be seen.
termcolors.colored did not want to play nice with ljust in the show commands
"""
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
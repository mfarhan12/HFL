DEBUG_LEVEL = 1

def print_log(level, info):

    if level >= DEBUG_LEVEL:
        print("%d %s" % (level, info))




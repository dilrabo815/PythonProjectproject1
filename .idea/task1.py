def kwargsAcceptFun(**kwargs):
    for major, course in kwargs.items():
        print("%s major has the course %s" % (major, course))

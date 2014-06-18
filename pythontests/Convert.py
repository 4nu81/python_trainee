class Convert(object):
    def str2Num(self, args):
        result = []
        try:
            for arg in args:
                result.append(float(arg))
        except:
            result = None
        return result

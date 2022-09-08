import sys


def test_with_range_func():
    return range(1, 10000)

def test_with_xrange_func():
    return xrange(1, 10000)


print "range() has used ", sys.getsizeof(test_with_range_func()), "bytes"
print "xrange() has used ", sys.getsizeof(test_with_xrange_func()), "bytes"

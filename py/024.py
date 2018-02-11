#!/usr/bin/env python

import itertools
print [''.join(x) for x in list(itertools.permutations('0123456789'))][999999]

import math
import pprint
from typing import Tuple
print('Hello, World!')

def foo(x:int)->Tuple[int, float]:
    return x, math.pi

pprint.pprint('Hello')

pprint.pprint(foo(4))
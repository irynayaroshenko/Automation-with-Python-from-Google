#!/usr/bin/env python

import sys
import random


value = random.randint(0, 3)
print(f'Returning: {str(value)}')
sys.exit(value)

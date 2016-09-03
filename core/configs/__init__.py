# -*- coding: utf-8 -*-

try:
    from .product import *
except ImportError as e:
    try:
        from .develop import *
    except ImportError as e:
        from .default import *

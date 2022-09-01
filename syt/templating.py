from itertools import product
from typing import Optional, Dict, Tuple
from yacs.config import load_cfg
import re

VALUES_RE = re.compile(r'^.*?\[\[(.*)]].*$')


def eval_line(line: str) -> Optional[str]:
    m = VALUES_RE.match(line)
    if m:
        expr = m.group(1)
        return expr
    return None



def read_template(filename: str):
    with open(filename) as f:
        lines = f.readlines()

    permuted: Dict[str, list] = dict()
    counted: Dict[str, str] = dict()
    for i, line in enumerate(lines):
        expr = eval_line(line)
        if expr:
            k = f'[[{expr}]]'
            expr = expr.strip()
            if expr.startswith('!'):
                counted[k] = expr
            else:
                permuted[k] = expr.split(', ')

    template = ''.join(lines)

    variants = []
    for i, p in enumerate(product(*permuted.values())):
        variant = template
        for k, sub in zip(permuted.keys(), p):
            variant = variant.replace(k, sub)

        for k, v in counted.items():
            if v == '!ID':
                sub = str(i)
            else:
                raise ValueError
            variant = variant.replace(k, sub)
        variants.append(variant)

    return variants

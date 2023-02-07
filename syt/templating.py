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


def escaping_split(s: str):
    parts = []
    part = ''
    escapes = ''
    for c in s:
        if c == ',' and not escapes:
            parts.append(part)
            part = ''
        else:
            if c in '"\'':
                if escapes.endswith(c):
                    escapes = escapes[:-1]
                else:
                    escapes += c
            elif c in '({[':
                escapes += c
            elif c in ')}]':
                op = dict(zip(')}]', '({['))[c]
                assert escapes[-1] == op
                escapes = escapes[:-1]
            part += c
    assert not escapes
    if part:
        parts.append(part)
    return parts


def read_template(filename: str):
    with open(filename) as f:
        lines = f.readlines()

    permuted: Dict[str, list] = dict()
    counted: Dict[str, str] = dict()
    for i, line in enumerate(lines):
        expr = eval_line(line)
        if expr:
            k = (i, f'[[{expr}]]')
            expr = expr.strip()
            if expr.startswith('!'):
                counted[k] = expr
            else:
                permuted[k] = escaping_split(expr)

    variants = []
    for i, p in enumerate(product(*permuted.values())):
        variant = list(lines)
        for (j, k), sub in zip(permuted.keys(), p):
            variant[j] = variant[j].replace(k, sub)

        for k, v in counted.items():
            if v == '!ID':
                sub = str(i)
            else:
                raise ValueError
            variant = variant.replace(k, sub)
        variants.append(''.join(variant))

    return variants

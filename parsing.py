from lark import Lark
from lark import Transformer

from core import *

simply_typed_grammar = r"""
    ?term: NAME -> var
        | "(" "\\" NAME "." term ")" -> abs
        | "(" term term ")" -> app
    %import common.CNAME -> NAME
    %import common.WS
    %ignore WS
"""

class LambdaTransformer(Transformer):
    def NAME(self, name):
        return name.value

    def var(self, t):
        term = TermVar()
        term.name = t[0]
        return term

    def app(self, t):
        term = TermApp()
        term.t1 = t[0]
        term.t2 = t[1]
        return term

    def abs(self, t):
        term = TermAbs()
        term.var = t[0]
        term.t = t[1]
        return term

def parse_term(input):
    parser = Lark(simply_typed_grammar, start='term')
    tree = parser.parse(input)
    term = LambdaTransformer().transform(tree)
    return term


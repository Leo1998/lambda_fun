#!/usr/bin/env python3

from core import *
from parsing import parse_term

def test(input):
    term = parse_term(input)
    print(f"Input: {input}")
    print(f"Term: {term}")
    print(f"Free vars: {term.fv()}")
    print(f"Normalform: {term.is_nf()}")
    print(f"Beta step: {term.beta_multistep()}")
    print("\n")

test("x")
test("(\\x.x)")
test("((\\x.x) y)")
test("((\\y.a) b)")
test("((\\x.x) (\\y.y))")
test("(((\\x.(\\y.x)) a) b)")
test("((\\x.(x x)) a)")
test("((\\x.(x x)) (\\x.(x x)))")
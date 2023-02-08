#!/usr/bin/env python3

from core import *
from parsing import parse_term

def test(input):
    term = parse_term(input)
    fv = term.fv()
    #print(f"Input: {input}")
    print(f"Term: {term}")
    print("Free vars: " + (str(fv) if len(fv) != 0 else "{}"))
    print(f"Is Normalform: {term.is_nf()}")
    print(f"Normalform: {term.beta_multistep()}")
    print("")

test("x") #var
test("(\\x.x)") #id
test("((\\x.x) y)") #id applied to var
test("((\\y.a) b)") #drops applicant
test("((\\x.x) (\\y.y))") #id applied to id
test("(((\\x.(\\y.x)) a) b)") #K (or true) applied to a, b
test("((\\x.(x x)) a)") #omega applied to a
test("((\\x.(x x)) (\\x.(x x)))") #Big omega (omega applied to itself)
test("(\\x.(\\y.y))") #false
test("(\\z.((z (\\x.(\\y.y))) (\\x.(\\y.x))))") # not operator
test("((\\z.((z (\\x.(\\y.y))) (\\x.(\\y.x)))) (\\x.(\\y.x)))") # not applied to true
test("((\\z.((z (\\x.(\\y.y))) (\\x.(\\y.x)))) (\\x.(\\y.y)))") # not applied to false
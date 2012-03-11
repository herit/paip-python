import logging
from paip import logic

def main():
    x = logic.Var('x')
    y = logic.Var('y')
    a = logic.Var('a')
    more = logic.Var('more')

    member_first = logic.Fact(
        logic.Relation('member', (x, logic.Relation('pair', (x, more)))))

    member_last = logic.Fact(
        logic.Relation('member', (x, logic.Relation('pair', (y, x)))))
    
    member_rest = logic.Rule(
        logic.Relation('member', (x, logic.Relation('pair', (y, more)))),
        [logic.Relation('member', (x, more))])

    db = logic.Database()
    db.store(member_first)
    db.store(member_rest)

    foo = logic.Atom('foo')
    logic.prolog_prove([logic.Relation('member', (foo, x))], db)

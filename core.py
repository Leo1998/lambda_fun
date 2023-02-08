
class Term:
    def copy(self):
        pass

    def subst(self, var, term):
        pass

    def fv(self):
        pass

    def is_nf(self):
        pass

    def is_redex(self):
        return isinstance(self, TermApp) and isinstance(self.t1, TermAbs)

    def beta_multistep(self, max_iter=100):
        pass

class TermVar(Term):
    name: str

    def __str__(self):
        return f"{self.name}"
    
    def copy(self):
        r = TermVar()
        r.name = self.name
        return r

    def subst(self, var, term):
        if self.name == var:
            return term.copy()
        else:
            return self.copy()

    def fv(self):
        return set([self.name])

    def is_nf(self):
        return True
    
    def beta_multistep(self, max_iter=100):
        return self.copy()

class TermApp(Term):
    t1: Term
    t2: Term
    
    def __str__(self):
        return f"({self.t1} {self.t2})"
    
    def copy(self):
        r = TermApp()
        r.t1 = self.t1
        r.t2 = self.t2
        return r

    def subst(self, var, term):
        s1 = self.t1.subst(var, term)
        s2 = self.t2.subst(var, term)
        r = TermApp()
        r.t1 = s1
        r.t2 = s2
        return r
    
    def fv(self):
        vars = self.t1.fv().union(self.t2.fv())
        return vars
    
    def is_nf(self):
        if self.is_redex():
            return False
        else:
            return self.t1.is_nf() and self.t2.is_nf()

    def beta_multistep(self, max_iter=100):
        r = self.copy()
        steps = 0
        while steps <= max_iter and not r.is_nf():
            steps += 1
            if r.is_redex():
                var = r.t1.var
                r = r.t1.t.subst(var, r.t2)
            else:
                r.t1 = r.t1.beta_multistep(max_iter=max_iter)
                r.t2 = r.t2.beta_multistep(max_iter=max_iter)
        return r


class TermAbs(Term):
    var: str
    t: Term
    
    def __str__(self):
        return f"(\\{self.var}.{self.t})"
    
    def copy(self):
        r = TermAbs()
        r.var = self.var
        r.t = self.t
        return r

    def subst(self, var, term):
        if self.var == var:
            return self.copy()
        else:
            if self.var == var:
                return self.copy()
            elif self.var not in term.fv():
                s = self.t.subst(var, term)
                r = TermAbs()
                r.var = self.var
                r.t = s
                return r
    
    def fv(self):
        vars = self.t.fv()
        vars.discard(self.var)
        return vars
    
    def is_nf(self):
        return self.t.is_nf()

    def beta_multistep(self, max_iter=100):
        r = self.copy()
        r.t = r.t.beta_multistep(max_iter=max_iter)
        return r
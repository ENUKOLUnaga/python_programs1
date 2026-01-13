class Employee:
    raise_amount=1.05
    def __init__(self,fn,ln,pay):
        self.fn=fn
        self.ln=ln
        self.pay=pay
    @property
    def email(self):
        return f"{self.fn}.{self.ln}@gmail.com"
    @property
    def name(self):
        return f"{self.fn}.{self.ln}"
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)
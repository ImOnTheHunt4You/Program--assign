import numpy as np
def funk1(x): return x**3-3*x**2+x
def der1(x): return 3**x**2-6*x+1
a=0
h=0.001

num_forward1=(funk1(a+h)-funk1(a))/h
num_backward1=(funk1(a)-funk1(a-h))/h
numcentral=(funk1(a+h)-funk1(a-h))/(2*h)
num_fivepoint1=(-funk1(a+2*h)+8*funk1(a+h)-8*funk1(a-h)+funk1(a-2*h))/(12*h)

print(f"Exakta värdet av derivatan i x={a} är {der1(a)}. \n")
print(f"Mitt approximativa värde av derivatan i x={a} med\n"
      f"framåt differenskvot och h={h} är {num_forward1}- \n")
print(f"Mitt approximativa värde av derivatan i x={a} med \n"
      f"bakåt differenskvot och h={h} är {num_backward1}. \n")
print(f"Mitt approximativa värde av derivatan i x={a} med\n"
      f"central differenskvot och h={h} är {numcentral}. \n")
print(f" Mitt approximativa värde av derivatan i x={a} med\n"
      f"fempunktsmetoden och h={h} är {num_fivepoint1}. \n")
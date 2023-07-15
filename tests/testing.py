from hypothesis import given, assume, strategies as st
from calculator_gkukse.calculator_gkukse import calculator

@given(a = st.floats(min_value=-10000, max_value=10000),
       n = st.integers(min_value=0, max_value=10000)
       )

def unit_test(a, n):
    assume(abs(a) >= 0.0001)
    assume(abs(n) != 0)
    assert sum([calculator.Addition(a)]) == calculator.Overall_sum
    assert sum([calculator.Subtraction(a)]) == calculator.Overall_sum
    assert sum([calculator.Multiplication(a)]) == calculator.Overall_sum
    assert sum([calculator.Division(a)]) == calculator.Overall_sum
    assert sum([calculator.Root(n)]) == calculator.Overall_sum



if __name__ == '__main__':
    unit_test()
    print("Everything passed")


from .variable import Variable


class Number(Variable):
    value = None

    def __init__(self, input):
        self.value = float(str(input))

    def __str__(self):
        return f"Number({self.value})"

    def add(self, value):
        # self._log_op(value, "+")

        if type(value) == Number:
            return Number(self.value + value.value)
        if type(value) == float or type(value) == int:
            return Number(self.value + value)
        raise SystemExit(
            TypeError(f"Value of type ${type(value)} cannot be used in number.add")
        )

    def sub(self, value):
        # self._log_op(value, "-")

        if type(value) == Number:
            return Number(self.value - value.value)
        if type(value) == float or type(value) == int:
            return Number(self.value - value)
        raise SystemExit(
            TypeError(f"Value of type ${type(value)} cannot be used in number.sub")
        )

    def mult(self, value):
        # self._log_op(value, "*")

        if type(value) == Number:
            return Number(self.value * value.value)
        if type(value) == float or type(value) == int:
            return Number(self.value * value)
        raise SystemExit(
            TypeError(f"Value of type ${type(value)} cannot be used in number.mult")
        )

    def div(self, value):
        # self._log_op(value, "/")

        if type(value) == Number:
            return Number(self.value / value.value)
        if type(value) == float or type(value) == int:
            return Number(self.value / value)
        raise SystemExit(
            TypeError(f"Value of type ${type(value)} cannot be used in number.div")
        )

    def _log_op(self, value, op):
        print(f"Operation {op} -- {value} on self {self}")


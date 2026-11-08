import math
import operator
from collections.abc import Mapping
from pathlib import Path

from lark import Lark, Token, Tree

_builtins = {
    "add": operator.add,
    "sub": operator.sub,
    "mul": operator.mul,
    "div": operator.truediv,
    "mod": operator.mod,
}
_functions = {
    **_builtins,
    "abs": abs,
    "round": round,
    "min": min,
    "max": max,
    "sqrt": math.sqrt,
}


class Parser:
    def __init__(self):
        self.parser = Lark(
            Path(__file__).parent.joinpath("arithmp.lark").read_text(), parser="lalr"
        )

        self._variables: Mapping[str, float] = {"pi": math.pi, "e": math.exp(1)}

    def _eval(self, tree: Tree[Token] | Token, variables: Mapping[str, float]) -> float:
        if isinstance(tree, Token):
            if tree.type == "NUMBER":
                return float(tree.value)
            else:
                raise ValueError(f"Unexpected token type: {tree.type}")
        match tree.data:
            case "number":
                return self._eval(tree.children[0], variables)
            case "add" | "sub" | "mul" | "div" | "mod":
                return _builtins[tree.data](
                    self._eval(tree.children[0], variables),
                    self._eval(tree.children[1], variables),
                )
            case "pos":
                return self._eval(tree.children[0], variables)
            case "neg":
                return -self._eval(tree.children[0], variables)
            case "power":
                return self._eval(tree.children[0], variables) ** self._eval(
                    tree.children[1], variables
                )
            case "function_call":
                name = str(tree.children[0])
                if name not in _functions:
                    raise ValueError(f"Unknown function: '{name}'")
                arguments = tree.children[1]  # None si aucun argument
                values = (
                    []
                    if arguments is None
                    else [self._eval(arg, variables) for arg in arguments.children]
                )
                try:
                    return float(_functions[name](*values))
                except (TypeError, ValueError) as error:
                    raise ValueError(f"Invalid call to {name}(): {error}") from error
            case _:
                raise ValueError(f"Unexpected tree data: {tree.data}")

    def parse(self, expression: str, *, variables: Mapping[str, float] = {}) -> float:
        return self._eval(
            self.parser.parse(expression), {**self._variables, **variables}
        )

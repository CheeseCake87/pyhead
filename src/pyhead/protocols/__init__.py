from typing import Protocol, runtime_checkable


@runtime_checkable
class CompileDelayed(Protocol):
    def compile(self) -> str: ...

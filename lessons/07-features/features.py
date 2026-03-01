"""Small feature helpers for undo and hints."""
from typing import List, Dict


def push_undo(stack: List, state) -> List:
    return stack + [state]


def pop_undo(stack: List):
    if not stack:
        return None, stack
    return stack[-1], stack[:-1]


def hint(state: Dict):
    # Placeholder: return None or a simple suggestion
    return None

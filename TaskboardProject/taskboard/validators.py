from constants import *
from django.core.exceptions import ValidationError


def task_state_validator(state):
    if state in TASK_STATES: return
    for s in TASK_STATES:
        if state in s: return
    raise ValidationError(
        str(state) + " is not a correct state",
        params={"state": state})

from . import constants
from django.core.exceptions import ValidationError


def task_state_validator(state):
    if state not in constants.TASK_STATES:
        raise ValidationError(
            f"{state} is not a correct state", params={"state": state}
        )


def task_action_validator(action):
    if action not in constants.TASK_STATES:
        raise ValidationError(
            f"{action} is not a correct state", params={"action": action}
        )

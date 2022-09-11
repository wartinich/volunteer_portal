from enum import Enum


class AssistanceStatus(Enum):
    ASSISTANCE_SETUP = "Setup"
    ASSISTANCE_PAUSE = "PAUSE"
    ASSISTANCE_IPS = "In progress"
    ASSISTANCE_CPD = "Completed"

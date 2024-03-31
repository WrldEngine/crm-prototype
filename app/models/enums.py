import enum


class GenderStatus(str, enum.Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"


class Positions(str, enum.Enum):
    HUMAN_RESOURCE = "HUMAN_RESOURCE"
    MARKETING = "MARKETING"
    DESIGN = "DESIGN"
    FRONTEND = "FRONTEND"
    BACKEND = "BACKEND"
    TESTING = "TESTING"


class PollingTypes(str, enum.Enum):
    VOTE = "VOTE"
    RATE = "RATE"
    OPINION = "OPINION"

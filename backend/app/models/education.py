# Standard library
from pydantic import BaseModel
from enum import Enum


class Institution(str, Enum):
    urjc = "urjc"
    ucy = "ucy"

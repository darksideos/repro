# Constants
IMMEDIATE = "immediate"
REGISTER = "register"
MEMORY = "memory"
INPUT = "input"
OUTPUT = "output"


class Section:
    """A section of an executable binary."""

    def __init__(self, size, data, flags):
        """Initialize a section."""
        self.size = size
        self.data = data
        self.flags = flags


class Executable:
    """An executable binary."""

    def __init__(self, architecture, sections, entry):
        """Initialize an executable."""
        self.architecture = architecture
        self.sections = sections
        self.entry = entry


class Operand:
    """An operand to a binary instruction."""

    TYPES = (IMMEDIATE, REGISTER, MEMORY)

    def __init__(self, type, value, direction):
        """Initialize an instruction operand."""
        self.type = type
        self.value = value
        self.direction = direction
    

class Instruction:
    """A single binary instruction."""

    def __init__(self, name, operands):
        """Initialize an instruction."""
        self.name = name
        self.operands = operands


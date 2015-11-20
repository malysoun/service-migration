import copy

default = {
    "Command": "",
    "CommitOnSuccess": False
}

def deserialize(data):
    """
    Deserializes a list of Commands.
    """
    if not data:
        return []
    commands = []
    for k, v in data.iteritems():
        command = Command()
        command._Command__data = v
        command.name = k
        command.command = v.get("Command", command.command)
        command.commitOnSuccess = v.get("CommitOnSuccess",
                                        command.commitOnSuccess)
        commands.append(command)
    return commands

def serialize(commands):
    """
    Serializes a list of commands.
    """
    data = {}
    for command in commands:
        data[command.name] = command._Command__data
        data[command.name]["Command"] = command.command
        data[command.name]["CommitOnSuccess"] = command.commitOnSuccess
    return data


class Command(object):
    """
    Wraps a single service command.
    """
    def __init__(self, name="", command="", commitOnSuccess=False):
        self.__data = copy.deepcopy(default)
        self.name = name
        self.command = command
        self.commitOnSuccess = commitOnSuccess

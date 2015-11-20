import copy

default = {
    "Owner": "",
    "Permission": "",
    "ResourcePath": "",
    "ContainerPath": "",
    "Type": ""
}

def deserialize(data):
    """
    Deserializes a list of volumes.
    """
    if not data:
        return []
    volumes = []
    for volume in data:
        v = Volume()
        v._Volume__data = volume
        v.owner = volume.get("Owner", v.owner)
        v.permission = volume.get("Permission", v.permission)
        v.resourcePath = volume.get("ResourcePath", v.resourcePath)
        v.containerPath = volume.get("ContainerPath", v.containerPath)
        volumes.append(v)
    return volumes

def serialize(volumes):
    """
    Serializes a list of volumes.
    """
    data = []
    for volume in volumes:
        v = volume._Volume__data
        v["Owner"] = volume.owner
        v["Permission"] = volume.permission
        v["ResourcePath"] = volume.resourcePath
        v["ContainerPath"] = volume.containerPath
        data.append(v)
    return data

class Volume(object):
    """
    Wraps a single service volume.
    """
    def __init__(self, owner="", permission="", resourcePath="", containerPath=""):
        self.__data = copy.deepcopy(default)
        self.owner = owner
        self.permission = permission
        self.resourcePath = resourcePath
        self.containerPath = containerPath


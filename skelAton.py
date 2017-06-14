import animation as am
import xml.etree.ElementTree as ET # fone home
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def make_lines(filename):
    """
    looks at the file
    :return an array of arrays of 3 arrays of floats. The outer array represents all of the different joints.
    The inside frames contain 25 different arrays, which are each of the different body parts in the array.
    """
    lines = []
    d = {}
    signs = ET.parse(filename).getroot()
    for sign in signs:
        for frame in sign:
            for joint in frame:
                body_part = joint.get('name')
                if body_part not in d:
                    d[body_part] = [[], [], []]
                d[body_part][0].append(float(joint.get("x")))
                d[body_part][1].append(float(joint.get("y")))
                d[body_part][2].append(float(joint.get("z")))
    return d

def getxyzplot( body, frame):
        return [dict[body][0][frame],dict[body][1][frame],dict[body][2][frame]]

def bodypart(body, body2, frame):
    plt.plot([getxyzplot(body,  frame)[0], getxyzplot(body2, frame)[0]],
             [getxyzplot(body,  frame)[1], getxyzplot(body2, frame)[1]],
             [getxyzplot(body, frame)[2], getxyzplot(body2, frame)[2]])
dict= make_lines("DINOSAUR_716.xml")
def makebody(frame):
    ## head
    bodypart("Head", "Neck", frame)
    bodypart("SpineShoulder", "Neck", frame)
    bodypart("SpineShoulder", "SpineMid", frame)
    bodypart("SpineBase", "SpineMid", frame)
    # leg left
    bodypart("SpineBase", "HipLeft", frame)
    bodypart("HipLeft", "KneeLeft", frame)
    bodypart("AnkleLeft", "KneeLeft", frame)
    bodypart("AnkleLeft", "FootLeft", frame)
    # arm left
    bodypart("SpineShoulder", "ShoulderLeft", frame)
    bodypart("ElbowLeft", "ShoulderLeft", frame)
    bodypart("ElbowLeft", "WristLeft", frame)
    bodypart("HandLeft", "WristLeft", frame)
    bodypart("HandLeft", "HandTipLeft", frame)
    bodypart("WristLeft", "ThumbLeft", frame)

    ## right arm
    bodypart("SpineShoulder", "ShoulderRight", frame)
    bodypart("ElbowRight", "ShoulderRight", frame)
    bodypart("ElbowRight", "WristRight", frame)
    bodypart("HandRight", "WristRight", frame)
    bodypart("WristRight", "ThumbRight", frame)
    bodypart("HandRight", "HandTipRight", frame)

    # leg right
    bodypart("SpineBase", "HipRight",  frame)
    bodypart("HipRight", "KneeRight", frame)
    bodypart("AnkleRight", "KneeRight", frame)
    bodypart("AnkleRight", "FootRight", frame)
dict= make_lines("DINOSAUR_716.xml")
makebody(0)
plt.show()
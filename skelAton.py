#import animation as am
import xml.etree.ElementTree as ET # fone home
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
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

def bodypart(body, body2, frame,width_line):
            #x
     ax.plot([getxyzplot(body,  frame)[0], getxyzplot(body2, frame)[0]],
            #y from                             to
              [getxyzplot(body,  frame)[1], getxyzplot(body2, frame)[1]],
        #z
             zs=[getxyzplot(body, frame)[2], getxyzplot(body2, frame)[2]],linewidth=width_line)
    #ax.setp(lines,linewidth=3.0)

def bodypart_sphere(body, body2, frame, width_line):  # x
        avg_x = (getxyzplot(body, frame)[0] + getxyzplot(body2, frame)[0])/2
        avg_y = (getxyzplot(body, frame)[1] + getxyzplot(body2, frame)[1])/2
        avg_z = (getxyzplot(body, frame)[2] + getxyzplot(body2, frame)[2])/2
        ax.Cir(avg_x,avg_y,avg_z)

        #ax.plot([getxyzplot(body, frame)[0], getxyzplot(body2, frame)[0]],
        # y from                             to
        #[getxyzplot(body, frame)[1], getxyzplot(body2, frame)[1]],
        # z
        #zs=[getxyzplot(body, frame)[2], getxyzplot(body2, frame)[2]], linewidth=width_line)


# ax.setp(lines,linewidth=3.0)


def makebody(frame):
    ax.clear()
    ## head
              #from    to?
    bodypart("Head", "Neck", frame,10)
    bodypart("SpineShoulder", "Neck", frame,10)
    bodypart("SpineShoulder", "SpineMid", frame,25)
    bodypart("SpineBase", "SpineMid", frame,25)
    # leg left
    bodypart("SpineBase", "HipLeft", frame,5)
    bodypart("HipLeft", "KneeLeft", frame,5)
    bodypart("AnkleLeft", "KneeLeft", frame,5)
    bodypart("AnkleLeft", "FootLeft", frame,5)
    #arm left
    bodypart("SpineShoulder", "ShoulderLeft", frame,5)
    bodypart("ElbowLeft", "ShoulderLeft", frame,5)
    bodypart("ElbowLeft", "WristLeft", frame,5)
    bodypart("HandLeft", "WristLeft", frame,1)
    bodypart("HandLeft", "HandTipLeft", frame,1)
    bodypart("WristLeft", "ThumbLeft", frame,1)

    ## right arm
    bodypart("SpineShoulder", "ShoulderRight", frame,5)
    bodypart("ElbowRight", "ShoulderRight", frame,5)
    bodypart("ElbowRight", "WristRight", frame,5)
    bodypart("HandRight", "WristRight", frame,1)
    bodypart("WristRight", "ThumbRight", frame,1)
    bodypart("HandRight", "HandTipRight", frame,1)

    # leg right
    bodypart("SpineBase", "HipRight",  frame,5)
    bodypart("HipRight", "KneeRight", frame,5)
    bodypart("AnkleRight", "KneeRight", frame,5)
    bodypart("AnkleRight", "FootRight", frame,5)
dict= make_lines("DINOSAUR_716.xml")

fig = plt.figure()
ax = p3.Axes3D(fig)
ax.view_init(270,270)

def updatefig(i):
    makebody(i)
    #ax.canvas.draw_idle()
   # plt.pause(1000)
anim = animation.FuncAnimation(fig, updatefig,frames= len(dict["Head"][0]), interval=1000/30)
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
import threading



plt.show()
#def thread():
#    while True:
#        for i in range (len(dict["Head"][0])):
 #           updatefig(i)

#t = threading.Thread(target=thread)
#t.daemon = False
#t.start()


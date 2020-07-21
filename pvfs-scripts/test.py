import os, time, random
import rosbag
import sys
import rospy
import time

bag2topic = {"imu": "/imu",
        "image": "/camera/depth/image",
        "image_color":"/camera/rgb/image_color"}

def _open(path, bora):
    bag = rosbag.Bag(path, borafs=bora)
    return bag

def long_time_task(path):
    start = time.time()
    filesystem = ""	
    if int(sys.argv[3]) == 0:
        bag = _open(path, True) 
        filesystem="bora-pvfs"
    elif int(sys.argv[3]) == 1:
        bag = _open(path, True) 
        filesystem="bora-ext4"
    elif int(sys.argv[3]) == 2:
        bag = _open(path, True) 
        filesystem="bora-xfs"
    elif int(sys.argv[3]) == 3:
        bag = _open(path, False)
        filesystem="ext4"
    elif int(sys.argv[3]) == 4:
        bag = _open(path, False)
        filesystem="xfs"
    elif int(sys.argv[3]) == 5:
        bag = _open(path, False)
        filesystem="pvfs"

    open_end = time.time()
    print(filesystem + '_time open_time: ' + str(open_end - start))
    msg_count = 0 
    start_t = None
    end_t = None
    if len(sys.argv) > 4:
        start_t = rospy.Time.from_sec(int(sys.argv[4]))
        end_t = rospy.Time.from_sec(int(sys.argv[5]))
    for topic, m, t in bag.read_messages(topics=[sys.argv[2]], start_time=start_t, end_time=end_t):
        msg_count+=1

    read_end = time.time()
    if start_t != None and end_t != None:
        print(filesystem + '_time read_time: ' + str(read_end - open_end) + " time_interval: " + sys.argv[4] +"-" +  sys.argv[5])
    else:
        print(filesystem + '_time read_time: ' + str(read_end - open_end))

    print(msg_count)
    bag.close()
    end = time.time()
    print(filesystem + '_time Task %s runs %0.2f seconds.' % (path, (end - start)))

if __name__=='__main__':
    start = time.time()
    long_time_task(sys.argv[1])
    end = time.time()
    print('All Tasks runs %0.2f seconds.' % (end - start))

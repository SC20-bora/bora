import os, time, random
import rosbag
import sys
import rospy
import time
import argparse

bag2topic = {"imu": "/imu",
        "image": "/camera/depth/image",
        "image_color":"/camera/rgb/image_color"}
topics = ["/camera/depth/camera_info", "/camera/depth/image", "/camera/rgb/camera_info", 
            "/camera/rgb/image_color", "/cortex_marker_array", "/imu", "/tf"]

def parse_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="bag path")
    parser.add_argument("fs_type", help="file system type", type=int)
    parser.add_argument("-s", "--start_time", help="query start time", type=int)
    parser.add_argument("-e", "--end_time", help="query end time", type=int)
    parser.add_argument("-t", '--topics', nargs='+', default=[])
    return parser.parse_args()

def _open(path, bora):
    bag = rosbag.Bag(path, borafs=bora)
    return bag

def choose_fs(args):
    is_bora = False
    fs = ""
    if args.fs_type == 0:
        is_bora = True
        fs="bora-pvfs"
    elif args.fs_type == 1:
        is_bora = True
        fs="bora-ext4"
    elif args.fs_type == 2:
        is_bora = True
        fs="bora-xfs"
    elif args.fs_type  == 3:
        fs="ext4"
    elif args.fs_type  == 4:
        fs="xfs"
    elif args.fs_type  == 5:
        fs="pvfs"

    return (is_bora, fs)


def random_pick_topics():
    random_topics = []
    for i in random.sample(range(0,7), 3):
        random_topics.append(topics[i])
    return random_topics

def do_task(args, num = 1):
    open_time = 0
    read_time = 0
    task_time = 0
    for t in range(num) :

        if num > 1:
            args.topics = random_pick_topics()

        is_bora= False
        filesystem = ""
        is_bora, filesystem = choose_fs(args);

        start = time.time()

        bag = _open(args.path, is_bora)

        open_end = time.time()
        open_time += (open_end - start)

        msg_count = 0
        start_t = None
        end_t = None
        if args.start_time and args.end_time:
            start_t = rospy.Time.from_sec(args.start_time)
            end_t = rospy.Time.from_sec(args.end_time)

        print("start read topic: " + str(args.topics))
        for _, m, t in bag.read_messages(topics=args.topics, start_time=start_t, end_time=end_t):
            msg_count+=1

        read_end = time.time()
       
        read_time += (read_end - open_end)
        bag.close()
        end = time.time()
        print("finish, read msg num: " + str(msg_count))
        task_time +=  (end - start)
        os.system("sudo sh ./clear-cache.sh")

    print(filesystem + '_time open_time: ' + str(open_time / num))

    if start_t != None and end_t != None:
        print(filesystem + '_time read_time: ' + str(read_time / num) + " time_interval: " + 
                str(args.start_time) +"-" + str(args.end_time) + " read_intelval: " + str(args.end_time -args.start_time))
    else:
        print(filesystem + '_time read_time: ' + str(read_time / num))


    print(filesystem + '_time Task %s runs %0.2f seconds, do %d times' % (args.path,(task_time / num), num))

def long_time_task(args):
    num = 1
    if len(args.topics) == 0:
        num = 10
    os.system("sudo sh ./clear-cache.sh")
    do_task(args, num)


if __name__=='__main__':
    args = parse_arg()
    start = time.time()
    long_time_task(args)
    end = time.time()
    print('All Tasks runs %0.2f seconds.' % (end - start))

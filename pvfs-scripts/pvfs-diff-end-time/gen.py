
import os, sys, stat

path = "diff-end-time.sh"
bags = ["test-42g.bag"]
topics = ["/camera/depth/image", "/cortex_marker_array", "/imu", "/camera/depth/camera_info"]

PVFS_TYPE = 5
fs_name="pvfs"
fs_path="/pvfsmnt_ssd/"
default_start_time="1311875133"

def write_fs_content(f, end_time, fs_type, fs_name, fs_path, bag, topic):

    f.write("echo '---------------" + fs_name + " start, bag:' " + bag + "', topic: '" + topic + "' -------------'\n")
    f.write("sudo sh ../clear-cache.sh\n")
    f.write("sudo python ../test.py "+ fs_path + bag+ " " + topic + " " + str(fs_type) + " "+ default_start_time + " " + str(end_time) +"\n")
    f.write("echo '---------------" + fs_name + " exit ------------'\n")

f = open(path, "wb+")

start_time = 1311875133
total_time = 1311875180

for topic in topics:
    for bag in bags:
        end_time = start_time + 3
        while end_time < total_time:
            write_fs_content(f, end_time, PVFS_TYPE, fs_name, fs_path, bag, topic)
            end_time += 3

f.close()
os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)




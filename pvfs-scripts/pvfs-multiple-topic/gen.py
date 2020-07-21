
import os, sys, stat

path = "pvfs-multiple-topic.sh"
bags = ["test-21g.bag", "test-42g.bag"]
topics = ["/camera/depth/image /camera/rgb/image_color", 
       "/camera/depth/image /camera/rgb/image_color /imu", 
       "/tf /camera/rgb/image_color /camera/rgb/camera_info /cortex_marker_array", "random"]

PVFS_TYPE = 5

def write_fs_content(f, fs_type, fs_name, fs_path):
    for bag in bags:
        for topic in topics:
            f.write("echo '---------------" + fs_name + " start, bag:' " + bag + "', topics: '" + topic + "' -------------'\n")
            if topic == "random":
                f.write("sudo python ../test-multiple.py "+ fs_path + bag  + " " + str(fs_type) +"\n")
            else:
                f.write("sudo python ../test-multiple.py "+ fs_path + bag  + " " + str(fs_type) + " -t " + topic +"\n")
            f.write("echo '---------------" + fs_name + " exit ------------'\n")

fs_name="pvfs"
fs_path="/pvfsmnt_ssd/"

f = open(path, "wb+")

write_fs_content(f, PVFS_TYPE, fs_name, fs_path)

f.close()
os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)




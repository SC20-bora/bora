
import os, sys, stat

path = "pvfs-diff-topic.sh"
bags = ["test-21g.bag", "test-42g.bag"]
topics = ["/camera/depth/image", "/camera/rgb/image_color", 
            "/camera/depth/camera_info", "/camera/rgb/camera_info",  
                "/cortex_marker_array", "/imu", "/tf"]
PVFS_TYPE = 5

def write_fs_content(f, fs_type, fs_name, fs_path):
    for bag in bags:
        for topic in topics:
            f.write("echo '---------------" + fs_name + " start, bag:' "+ bag + "', topic: '" + topic + "' -------------'\n")
            f.write("sudo sh ../clear-cache.sh\n")
            f.write("sudo python ../test.py "+ fs_path + bag + " " + topic + " "+ str(fs_type) +"\n")
            f.write("echo '---------------" + fs_name + " exit ------------'\n")

fs_name="pvfs"
fs_path="/pvfsmnt_ssd/"

f = open(path, "wb+")

write_fs_content(f, PVFS_TYPE, fs_name, fs_path)

f.close()
os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)




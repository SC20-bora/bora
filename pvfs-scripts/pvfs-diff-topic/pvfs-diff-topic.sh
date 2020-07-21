echo '---------------pvfs start, bag:' test-21g.bag', topic: '/camera/depth/image' -------------'
sudo sh ../clear-cache.sh
sudo python ../test.py /pvfsmnt_ssd/test-21g.bag /camera/depth/image 5
echo '---------------pvfs exit ------------'
echo '---------------pvfs start, bag:' test-21g.bag', topic: '/camera/rgb/image_color' -------------'
sudo sh ../clear-cache.sh
sudo python ../test.py /pvfsmnt_ssd/test-21g.bag /camera/rgb/image_color 5
echo '---------------pvfs exit ------------'
echo '---------------pvfs start, bag:' test-21g.bag', topic: '/camera/depth/camera_info' -------------'
sudo sh ../clear-cache.sh
sudo python ../test.py /pvfsmnt_ssd/test-21g.bag /camera/depth/camera_info 5
echo '---------------pvfs exit ------------'
echo '---------------pvfs start, bag:' test-21g.bag', topic: '/camera/rgb/camera_info' -------------'
sudo sh ../clear-cache.sh
sudo python ../test.py /pvfsmnt_ssd/test-21g.bag /camera/rgb/camera_info 5
echo '---------------pvfs exit ------------'
echo '---------------pvfs start, bag:' test-21g.bag', topic: '/cortex_marker_array' -------------'
sudo sh ../clear-cache.sh
sudo python ../test.py /pvfsmnt_ssd/test-21g.bag /cortex_marker_array 5
echo '---------------pvfs exit ------------'
echo '---------------pvfs start, bag:' test-21g.bag', topic: '/imu' -------------'
sudo sh ../clear-cache.sh
sudo python ../test.py /pvfsmnt_ssd/test-21g.bag /imu 5
echo '---------------pvfs exit ------------'
echo '---------------pvfs start, bag:' test-21g.bag', topic: '/tf' -------------'
sudo sh ../clear-cache.sh
sudo python ../test.py /pvfsmnt_ssd/test-21g.bag /tf 5
echo '---------------pvfs exit ------------'
echo '---------------pvfs start, bag:' test-42g.bag', topic: '/camera/depth/image' -------------'
sudo sh ../clear-cache.sh
sudo python ../test.py /pvfsmnt_ssd/test-42g.bag /camera/depth/image 5
echo '---------------pvfs exit ------------'
echo '---------------pvfs start, bag:' test-42g.bag', topic: '/camera/rgb/image_color' -------------'
sudo sh ../clear-cache.sh
sudo python ../test.py /pvfsmnt_ssd/test-42g.bag /camera/rgb/image_color 5
echo '---------------pvfs exit ------------'
echo '---------------pvfs start, bag:' test-42g.bag', topic: '/camera/depth/camera_info' -------------'
sudo sh ../clear-cache.sh
sudo python ../test.py /pvfsmnt_ssd/test-42g.bag /camera/depth/camera_info 5
echo '---------------pvfs exit ------------'
echo '---------------pvfs start, bag:' test-42g.bag', topic: '/camera/rgb/camera_info' -------------'
sudo sh ../clear-cache.sh
sudo python ../test.py /pvfsmnt_ssd/test-42g.bag /camera/rgb/camera_info 5
echo '---------------pvfs exit ------------'
echo '---------------pvfs start, bag:' test-42g.bag', topic: '/cortex_marker_array' -------------'
sudo sh ../clear-cache.sh
sudo python ../test.py /pvfsmnt_ssd/test-42g.bag /cortex_marker_array 5
echo '---------------pvfs exit ------------'
echo '---------------pvfs start, bag:' test-42g.bag', topic: '/imu' -------------'
sudo sh ../clear-cache.sh
sudo python ../test.py /pvfsmnt_ssd/test-42g.bag /imu 5
echo '---------------pvfs exit ------------'
echo '---------------pvfs start, bag:' test-42g.bag', topic: '/tf' -------------'
sudo sh ../clear-cache.sh
sudo python ../test.py /pvfsmnt_ssd/test-42g.bag /tf 5
echo '---------------pvfs exit ------------'

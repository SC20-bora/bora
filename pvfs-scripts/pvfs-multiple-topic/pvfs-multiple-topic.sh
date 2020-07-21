echo '---------------pvfs start, bag:' test-21g.bag', topics: '/camera/depth/image /camera/rgb/image_color' -------------'
sudo python ../test-multiple.py /pvfsmnt_ssd/test-21g.bag 5 -t /camera/depth/image /camera/rgb/image_color
echo '---------------pvfs exit ------------'
echo '---------------pvfs start, bag:' test-21g.bag', topics: '/camera/depth/image /camera/rgb/image_color /imu' -------------'
sudo python ../test-multiple.py /pvfsmnt_ssd/test-21g.bag 5 -t /camera/depth/image /camera/rgb/image_color /imu
echo '---------------pvfs exit ------------'
echo '---------------pvfs start, bag:' test-21g.bag', topics: '/tf /camera/rgb/image_color /camera/rgb/camera_info /cortex_marker_array' -------------'
sudo python ../test-multiple.py /pvfsmnt_ssd/test-21g.bag 5 -t /tf /camera/rgb/image_color /camera/rgb/camera_info /cortex_marker_array
echo '---------------pvfs exit ------------'
echo '---------------pvfs start, bag:' test-21g.bag', topics: 'random' -------------'
sudo python ../test-multiple.py /pvfsmnt_ssd/test-21g.bag 5
echo '---------------pvfs exit ------------'
echo '---------------pvfs start, bag:' test-42g.bag', topics: '/camera/depth/image /camera/rgb/image_color' -------------'
sudo python ../test-multiple.py /pvfsmnt_ssd/test-42g.bag 5 -t /camera/depth/image /camera/rgb/image_color
echo '---------------pvfs exit ------------'
echo '---------------pvfs start, bag:' test-42g.bag', topics: '/camera/depth/image /camera/rgb/image_color /imu' -------------'
sudo python ../test-multiple.py /pvfsmnt_ssd/test-42g.bag 5 -t /camera/depth/image /camera/rgb/image_color /imu
echo '---------------pvfs exit ------------'
echo '---------------pvfs start, bag:' test-42g.bag', topics: '/tf /camera/rgb/image_color /camera/rgb/camera_info /cortex_marker_array' -------------'
sudo python ../test-multiple.py /pvfsmnt_ssd/test-42g.bag 5 -t /tf /camera/rgb/image_color /camera/rgb/camera_info /cortex_marker_array
echo '---------------pvfs exit ------------'
echo '---------------pvfs start, bag:' test-42g.bag', topics: 'random' -------------'
sudo python ../test-multiple.py /pvfsmnt_ssd/test-42g.bag 5
echo '---------------pvfs exit ------------'

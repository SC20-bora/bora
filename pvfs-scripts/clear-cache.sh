echo 3 | ssh node1 "tee /proc/sys/vm/drop_caches"
echo 3 | ssh node2 "tee /proc/sys/vm/drop_caches"
echo 3 | ssh node3 "tee /proc/sys/vm/drop_caches"
echo 3 | ssh node4 "tee /proc/sys/vm/drop_caches"
echo 3 | ssh node5 "tee /proc/sys/vm/drop_caches"
sleep 5

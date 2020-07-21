## The scripts/code for the experiments with the baseline PVFS

Because the BORA code hasn't been disclosed yet, you can run this script for the experiment with the baseline PVFS at present.

## Environmental Requirements

1. Ubuntu 16.04/CentOS 6.10 or above
2. PVFS 2.9.5
3. ROS Kinetic Kame or above
4. Python 2.7 or above

## Contents

1. `pvfs-diff-topic/` contains the scripts for comparisons of query time by a single topic on a PVFS cluster. This script is used to reproduce the results in Fig. 15 (a) and (b) in our BORA paper.
2. `pvfs-multiple-topic/` contains the scripts for comparisons of query time by real-world applications on a PVFS cluster. This script is used to reproduce the results in Fig. 15 (c) and (d) in our BORA paper.
3. `pvfs-diff-end-time/` contains the scripts for comparisons of query time by one topic and start-end time of Handheld SLAM with a 42 GB bag on a PVFS cluster.  This script is used to reproduce the results in Fig. 16 in our BORA paper.

## Using the test scripts for PVFS

1. Create a directory for PVFS mount point, such as `/pvfsmnt_ssd`.

2. Mount PVFS under `/pvfsmnt_ssd`.

3. Copy bag files to the PVFS mount point. The default bags name in our scripts is `test-21g.bag` and `test-42g.bag`.

   (Due to the capacity limits, we uploaded two small bags (51MB and 100MB) for demonstration (You can download them from the following link: https://drive.google.com/drive/folders/174prLHkb_lyTNoDNkg9_jo4aiLtbU7GL?usp=sharing). The bag file names remain `test-21g.bag` and `test-42g.bag`, because our original script was using these two names.)

4. Get into one of script directories which you interested in and run `./run.sh`. You can observe the results in a file named `result.log` when the script is done.

   (`run.sh` will clear cache before running tests. Please make sure to change the `node#` alias in `clear-cache.sh` according to the number of nodes you have in your PVFS cluster. We provided a sample `clear-cache.sh` which represents a five-node PVFS cluster, just for your reference.)

We show a step-by-step instruction to test PVFS performance of querying differnt topics. (Fig. 15 (a)(b) in our BORA paper).

```shell
mkdir /pvfsmnt_ssd
mount -t pvfs2 tcp://node2:3334/pvfs2-fs /pvfsmnt_ssd # node2 refer to the PVFS server
cp test-21g.bag /pvfsmnt_ssd
cd pvfs-diff-topic
./run.sh
cat result.log # A file called result.log.sample is provided, which is used to check if it runs successfully.
```

## Reproduction Demo

We provided a short video to demonstrate the PVFS baseline experiment (`PVFS-TEST-DEMO.m4v`). Due to the capacity limit of GitHub, we can not upload a video that contains the entire test procedure. We only record the script of testing the file `test-21g.bag` for a short term, stop the script, and present the results in the result.log file.




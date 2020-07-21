## BORA

The source code of BORA is temporarily unavailable to the public because we are filing a PCT (Patent Cooperation Treaty, an international patent law treaty) patent (the patent number can be provided if it does not violate the anonymous role) for this project. The patent application already passed the International Search phase and is currently in the International Publication phase. Once it passes the International Publication phase, we will immediately disclose the BORA source code to the public.

## Environmental Requirements

1. Ubuntu 16.04/CentOS 6.10 or above
2. ROS Kinetic Kame or above
3. FUSE 2.9.4 or above
4. CMake 3.13 and gcc 7.4.0 or above

## Contents

1. `pvfs-scripts/`: All scripts for the baseline experiments with PVFS are stored under the `pvfs-scripts` sub-folder. Due to the storage capacity limit of GitHub, we only uploaded two small sample bag files (51MB and 100MB) instead of the 21 GB and 42 GB bag files that were used in the experiments shown in our BORA manuscript.

## Installation

1. First you must clone BORA code to the local machine

   ```shell
   git clone https://github.com/SC20-bora/bora
   ```

2. Get into BORA directory and compile it.

   ```shell
   cd BORA && mkdir build 
   cd build && cmake ..
   make -j4
   ```

## Using BORA

1. Mount BORA

   ```shell
   ./bin/bora /mnt/backend /mnt/bora
   ```

2. Then you can put bag file to the mount point and use ROS library to use it. The method of use is the same as the ROS official document.

3. Unmounting BORA

   ```shell
   fusermount -u /mnt/bora
   ```

## Reproduction Demo

We made a short video to demonstrate the reproduction procedure using a 3GB bag file. You can check the video with the name `BORADEMO.m4v`

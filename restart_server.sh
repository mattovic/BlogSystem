#! /bin/bash
for pid in $(ps aux|grep linaro |grep blogserver.py | awk '{print $2}')
do
kill $pid
done
nohup python blogserver.py &

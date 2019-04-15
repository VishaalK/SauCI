rm output.txt
python3 test2.py 2> output.txt
exit_code=$?
echo exit_code, $exit_code

if [ $exit_code -eq 1 ]
then
    echo "BUILD FAILED"
fi

# now we write a python shell to call my thingy
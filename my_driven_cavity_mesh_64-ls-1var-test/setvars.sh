export DAKOTA=/opt/dakota #DAKOTA should point to the basedirectory of wherever DAKOTA is installed!
export PATH=$PATH:$DAKOTA/bin:$DAKOTA/test
if [ "x$LD_LIBRARY_PATH" == "x" ]; then
    export LD_LIBRARY_PATH=$DAKOTA/bin:$DAKOTA/lib
else
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DAKOTA/bin:$DAKOTA/lib
fi

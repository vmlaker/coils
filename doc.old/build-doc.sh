#!/bin/bash

##########################################
#
#  Script to build Sphinx documentation.
#
##########################################

make -j8 clean html
VERSION=`cd ../build/lib; python -c 'import coils; print coils.__version__'`
find build -type f |\
   xargs grep -l "###version###" |\
   xargs sed -i s:'###version###':"$VERSION":g
find build -type f |\
   xargs grep -l "###date###" |\
   xargs sed -i s/'###date###'/"`date`"/g

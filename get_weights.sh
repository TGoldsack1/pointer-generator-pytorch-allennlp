#!/bin/bash
fileid="1356aa0FRZO2aIPBcnZ3Ttlh--kfm8hix"
filename="see_etal_weights_with_coverage.th"
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o ${filename}
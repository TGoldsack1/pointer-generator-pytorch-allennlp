#!/bin/bash
# Author: Tomas Goldsack

# allennlp predict pretrained_model_skeleton.tar.gz --weights-file see_etal_weights_without_coverage.th --include-package pointergen --cuda-device <gpu-id> --predictor beamsearch <test-file>
# allennlp predict my_post_coverage/model.tar.gz --include-package pointergen --cuda-device 0 --predictor beamsearch my_data/dataset_top3_test.jsonl --output-file outputs.json

# THIS NEEDS TO RUN PREDICT ON EVERY FILE IN my_data/longsumm/section_level



INPUT_FILES="$(pwd)/my_data/longsumm/section_level/*.jsonl"

for file in ${INPUT_FILES}; do
    echo "-------------------------------------------"
    filename=$(basename -- "$file")
    filename="${filename%.*}"
    echo "${filename}"
    echo "${file}"
    output_path="./predictions/sections/${filename}.jsonl"
    echo "$output_path"
    input_path="./my_data/longsumm/section_level/${filename}.jsonl"
    echo "$input_path"

    allennlp predict my_post_coverage/model.tar.gz --include-package pointergen --cuda-device 0 --predictor beamsearch $input_path --output-file $output_path
    #allennlp predict pretrained_model_skeleton.tar.gz --weights-file see_etal_weights_without_coverage.th --include-package pointergen --cuda-device 0 --predictor beamsearch $input_path --output-file $output_path
done


# ALSO NEED TO WRITE A SCRIPT TO CONCATENATE OUTPUTS BACK TOGETHER (before simplifying via access)

#python concat_section_preds.py
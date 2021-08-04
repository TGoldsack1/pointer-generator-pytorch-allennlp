'''
Concatenates the the model section output for each test instance. 
Author: Tomas Goldsack
'''

import os, json, ast

input_dir = "./predictions/sections/"

output_inst_level_preds = {}

# Iterate through prediction files for each test instance
for inst_preds_file in os.listdir(input_dir):

  inst_level_dict = {}

  inst_preds_content = open(inst_preds_content, "r")
  inst_section_preds = inst_preds_content.readlines() 
  inst_preds_content.close()

  # Convert str lines to dictionaries
  inst_sections_preds = [ast.literal_eval(x) for x in inst_section_preds]
  
  # Copy ground truth
  inst_level_dict['ground_truth'] = inst_sections_preds[0]['ground_truth']

  # Get section_level predictions and convert to a single summary
  inst_level_dict['prediction'] =  " ".join([x['prediction'] for x in inst_sections_preds])

  output_inst_level_preds[] = inst_level_dict # 

with open()
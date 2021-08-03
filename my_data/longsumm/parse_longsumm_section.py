'''
Parses longsummm dataset json file to make format input for the given model.
Reduces input size my using only the Abstract, Introduction and Conclusion.
Author: Tomas Goldsack
'''

import os, json, re
from nltk.tokenize import sent_tokenize

longsumm_file = open("./my_longsumm_test.json")
longsumm_dict = json.load(longsumm_file)
longsumm_file.close()


## pointer-generator-pytorch-allennlp
# Desired input format (json)
# { 
#   "article_lines": List[str],
#   "summary_lines": List[str]
# }

i = 0
for (paper_id, paper_dict) in longsumm_dict.items():
  paper_datafile = open(f'./section_level/my_longsumm_test_sections.{i}.jsonl', "w")

  summary_sents = paper_dict['Y']['summary']
  input_dict = paper_dict['X'] 
  # X format:
  # {
  #   "sections": [{ "heading": str, "text": str }], 
  #   "year": int,
  #   "references": [{...}],
  #   "id" : str,
  #   "authors" : [{ "name": str, "affiliations": str }]
  #   "abstractText": str,
  #   "title": str
  # }
  has_content = False

  section_data = {}
  article_lines = []

  if "abstractText" in input_dict.keys():
    article_lines = sent_tokenize(input_dict["abstractText"])

    section_data["summary_lines"] = summary_sents
    section_data["article_lines"] = article_lines

    paper_datafile.write(json.dumps(section_data))
    paper_datafile.write("\n")

    has_content = True


  if 'sections' in input_dict.keys() and len(input_dict['sections']) > 0:
    for section in input_dict['sections']:
      if 'text' in section.keys():
        section_data = {}
        article_lines = sent_tokenize(section["text"])

        if len(article_lines) > 0:
          section_data["summary_lines"] = summary_sents
          section_data["article_lines"] = article_lines

          paper_datafile.write(json.dumps(section_data))
          paper_datafile.write("\n")

          has_content = True

  if has_content:
    i += 1
  paper_datafile.close()







  










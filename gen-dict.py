#!/usr/bin/env python3
import sys
import os
from os import path
import subprocess

DICT_HEADER = """# Rime dict
# encoding: utf-8

---
name: xhup
version: "0.1"
sort: by_weight
use_preset_vocabulary: false
max_phrase_length: 14
encoder:
  exclude_patterns:
    - '^o.*$'
    - '^`.*$'
  rules:
    - length_equal: 2
      formula: "AaAbZaZb"
    - length_equal: 3
      formula: "AaBaZaZb"
    - length_in_range: [4, 14]
      formula: "AaBaCaZa"
...
"""

if __name__ == '__main__':
    argv = sys.argv
    orig_dict_file = argv[1]
    data_dir = argv[2]

    st_characters_file = path.join(data_dir, 'dictionary', 'STCharacters.txt')
    st_phrases_file = path.join(data_dir, 'dictionary', 'STPhrases.txt')
    hk_variants_file = path.join(data_dir, 'dictionary', 'HKVariants.txt')
    hk_variants_phrases_file = path.join(data_dir, 'dictionary', 'HKVariantsPhrases.txt')
    tw_variants_file = path.join(data_dir, 'dictionary', 'TWVariants.txt')
    jp_variants_file = path.join(data_dir, 'dictionary', 'JPVariants.txt')
    st_multi_file = path.join(data_dir, 'scheme', 'st_multi.txt')
    variant_file = path.join(data_dir, 'scheme', 'variant.txt')

    st_dict = dict()

    orig_dict_t_file = 'xhup-dict-t.txt'
    subprocess.check_call(['opencc', '-i', orig_dict_file,
                           '-o', orig_dict_t_file,
                           '-c', 's2t.json'])
    #  orig_dict_hk_file = 'xhup-dict-hk.txt'
    #  subprocess.check_call(['opencc', '-i', orig_dict_file,
                           #  '-o', orig_dict_hk_file,
                           #  '-c', 's2hk.json'])
    #  orig_dict_tw_file = 'xhup-dict-tw.txt'
    #  subprocess.check_call(['opencc', '-i', orig_dict_file,
                           #  '-o', orig_dict_tw_file,
                           #  '-c', 's2tw.json'])

    with open(orig_dict_file) as sf, open(orig_dict_t_file) as tf:
    #  with open(orig_dict_file) as sf, open(orig_dict_t_file) as tf, \
         #  open(orig_dict_hk_file) as hkf, open(orig_dict_tw_file) as twf:

        sline = sf.readline().rstrip('\n')
        tline = tf.readline().rstrip('\n')
        #  hkline = hkf.readline().rstrip('\n')
        #  twline = twf.readline().rstrip('\n')
        #  while sline and tline and hkline and twline:
        while sline and tline:
            (s, code) = sline.split('\t')
            (t, code) = tline.split('\t')
            #  (hk, code) = hkline.split('\t')
            #  (tw, code) = twline.split('\t')

            if s not in st_dict:
                #  st_dict[s] = [t, hk, tw]
                st_dict[s] = [t]
            else:
                if t not in st_dict[s]:
                    st_dict[s].append(t)
                #  if hk not in st_dict[s]:
                    #  st_dict[s].append(hk)
                #  if tw not in st_dict[s]:
                    #  st_dict[s].append(tw)

            sline = sf.readline().rstrip('\n')
            tline = tf.readline().rstrip('\n')
            #  hkline = hkf.readline().rstrip('\n')
            #  twline = twf.readline().rstrip('\n')

    with open(st_multi_file) as f:
        line = f.readline().rstrip('\n')
        while line:
            (schar, tchars) = line.split('\t')[:2]
            tchars = tchars.split(' ')

            if schar in st_dict:
                for tchar in tchars:
                    if tchar not in st_dict[schar]:
                        st_dict[schar].append(tchar)
            else:
                st_dict[schar] = tchars

            line = f.readline().rstrip('\n')

    #  hk_variants_dict = dict()
    #  with open(hk_variants_file) as f:
        #  line = f.readline().rstrip('\n')
        #  while line:
            #  (tchar, variants) = line.split('\t')
            #  variants = variants.split(' ')
            #  hk_variants_dict[tchar] = variants
            #  line = f.readline().rstrip('\n')

    #  hk_variants_phrases_dict = dict()
    #  with open(hk_variants_phrases_file) as f:
        #  line = f.readline().rstrip('\n')
        #  while line:
            #  (tphrase, variants) = line.split('\t')
            #  variants = variants.split(' ')
            #  hk_variants_phrases_dict[tphrase] = variants
            #  line = f.readline().rstrip('\n')

    #  tw_variants_dict = dict()
    #  with open(tw_variants_file) as f:
        #  line = f.readline().rstrip('\n')
        #  while line:
            #  (tchar, variants) = line.split('\t')
            #  variants = variants.split(' ')
            #  tw_variants_dict[tchar] = variants
            #  line = f.readline().rstrip('\n')

    #  jp_variants_dict = dict()
    #  with open(jp_variants_file) as f:
        #  line = f.readline().rstrip('\n')
        #  while line:
            #  (tchar, variants) = line.split('\t')
            #  variants = variants.split(' ')
            #  jp_variants_dict[tchar] = variants
            #  line = f.readline().rstrip('\n')

    variant_dict = dict()
    with open(variant_file) as f:
        line = f.readline().rstrip('\n')
        while line:
            (tchar, variants) = line.split('\t')
            variants = variants.split(' ')
            variant_dict[tchar] = variants
            line = f.readline().rstrip('\n')

    for (s, t_list) in st_dict.items():
        for t in t_list.copy():
            if t in variant_dict:
                for v in variant_dict[t]:
                    if v not in t_list:
                        t_list.append(v)

            #  if t in hk_variants_dict:
                #  for v in hk_variants_dict[t]:
                    #  if v not in t_list:
                        #  t_list.append(v)

            #  if t in hk_variants_phrases_dict:
                #  for v in hk_variants_phrases_dict[t]:
                    #  if v not in t_list:
                        #  t_list.append(v)

            #  if t in tw_variants_dict:
                #  for v in tw_variants_dict[t]:
                    #  if v not in t_list:
                        #  t_list.append(v)

            #  if t in jp_variants_dict:
                #  for v in jp_variants_dict[t]:
                    #  if v not in t_list:
                        #  t_list.append(v)

    with open(st_characters_file) as f:
        line = f.readline().rstrip('\n')
        while line:
            (schar, tchars) = line.split('\t')
            tchars = tchars.split(' ')
            if schar in st_dict:
                for tchar in tchars:
                    if tchar not in st_dict[schar]:
                        st_dict[schar].append(tchar)
            else:
                st_dict[schar] = tchars

            line = f.readline().rstrip('\n')

    with open(st_phrases_file) as f:
        line = f.readline().rstrip('\n')
        while line:
            (sphrase, tphrases) = line.split('\t')
            tphrases = tphrases.split(' ')

            if sphrase in st_dict:
                for tphrase in tphrases:
                    if tphrase not in st_dict[sphrase]:
                        st_dict[sphrase].append(tphrase)
            else:
                st_dict[sphrase] = tphrases

            line = f.readline().rstrip('\n')

    print(DICT_HEADER)

    new_lines = set()
    with open(orig_dict_file) as f:
        line = f.readline().rstrip('\n')
        while line:
            (s, code) = line.split('\t')
            if s in st_dict:
                for t in st_dict[s]:
                    new_line = t + '\t' + code
                    if new_line not in new_lines:
                        new_lines.add(new_line)
                        print(new_line)
            else:
                assert False

            line = f.readline().rstrip('\n')

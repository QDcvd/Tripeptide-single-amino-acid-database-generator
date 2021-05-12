# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 00:05:03 2020

@author: 郝蛤蛤
"""
import sys
from Bio import PDB
import os
from tqdm import tqdm


# filename = sys.argv[1]


def pdb2fasta(pdbfilename):  # 将一个pdb文件转换为fasta序列
    new_filename = pdbfilename.replace(".pdb", "")

    parser = PDB.PDBParser()
    structure = parser.get_structure(new_filename, pdbfilename)
    ppb = PDB.PPBuilder()

    for pp in ppb.build_peptides(structure):
        ppstring = pp.get_sequence()
    # print(new_filename, "转换序列为：", ppstring)
        return ppstring


def aliCreator(alifilename):  # 产生ali文件
    with open(alifilename + ".ali", "w+") as alifile:
        alifile.write(">P1;" + alifilename + "\n")
        alifile.write("sequence:" + alifilename + ":::::::0.00: 0.00\n")
        alifile.write(alifilename + "*")


def fileInPath(file, list):
    for Strfile in list:
        if Strfile == file:
            return True
        else:
            return False


if __name__ == "__main__":
    # print(pdb2fasta("./sorted_file/" + filename))
    new_num_string = []
    insert_num = 1
    # 批量相隔两字符分割
    for i in os.listdir("./data/"):
        for num_string in str(pdb2fasta("./data/" + str(i))):
            # print(num_string)
            new_num_string.append(num_string)
            if insert_num % 3 == 0:
                new_num_string.append("-")
            insert_num += 1

    # 暴力删除
    list3string = str(new_num_string).replace("'", "")
    list3string = str(list3string).replace("[", "")
    list3string = str(list3string).replace("]", "")
    list3string = str(list3string).replace(",", "")
    list3string = str(list3string).replace(" ", "")
    listFor3Amino = list3string.split("-")
    # print(len(listFor2Amino[:-1]))
    newListFor3Amino = list(set(listFor3Amino[:-1]))  # 降重
    print(newListFor3Amino)
    print(len(newListFor3Amino))
    # print(newListFor3Amino.index("PRN"))

    for aliseq in tqdm(newListFor3Amino):
        if fileInPath(str(aliseq)+'.ali', newListFor3Amino):
            continue
        else:
            try:
                aliCreator(str(aliseq))
                os.system("python single_model-optimize2.py " + str(aliseq) + " reset_20ns-A-protein_addh > run.log")
                os.system("python add_A_forali.py " + str(aliseq) + ".B99990001 > run.log")
            except FileNotFoundError:
                print("文件不存在:", aliseq)
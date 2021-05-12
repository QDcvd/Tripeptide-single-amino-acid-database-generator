# -*- coding: utf-8 -*-
"""
Created on *********

@author: 了不起的田所李
"""
import os
import sys
from Bio import PDB


def pdb2fasta(pdbfilename):  # 将一个pdb文件转换为fasta序列
    new_filename = pdbfilename.replace(".pdb", "")

    parser = PDB.PDBParser()
    structure = parser.get_structure(new_filename, pdbfilename)
    ppb = PDB.PPBuilder()

    for pp in ppb.build_peptides(structure):
        ppstring = pp.get_sequence()
    # print(new_filename, "转换序列为：", ppstring)
        return ppstring


if __name__ == '__main__':
    amino_list = ['A', 'F', 'C', 'D', 'N', 'E', 'Q', 'G', 'H', 'L', 'I', 'K', 'M', 'P', 'R', 'S', 'T', 'V', 'W', 'Y']
    allAnimo_list = []

    #  得出含有所有组合的氨基酸列
    for i in amino_list:
        for j in amino_list:
            for k in amino_list:
                allAnimo_list.append(i + j + k)
    # print(allAnimo_list)
    print(len(allAnimo_list))

    new_num_string = []
    # insert_num = 1
    # 获取文件夹内的文件
    for z in os.listdir("./3AminoDataBase/"):
        new_num_string.append(z.replace(".B99990001_addh.pdb", ""))

    # print(new_num_string)
    print(len(new_num_string))
    #
    # # 暴力删除
    # list3string = str(new_num_string).replace("'", "")
    # list3string = str(list3string).replace("[", "")
    # list3string = str(list3string).replace("]", "")
    # list3string = str(list3string).replace(",", "")
    # list3string = str(list3string).replace(" ", "")
    # listFor3Amino = list3string.split("-")
    # # print(len(listFor2Amino[:-1]))
    # newListFor3Amino = list(set(listFor3Amino[:-1]))  # 降重
    # # print(newListFor3Amino)
    # print(len(newListFor3Amino))


    # 判断数据库里缺少什么序列
    aminoNotInDataBase = []
    # 全部设置为大写
    num_string = []
    for upper in new_num_string:
        num_string.append(upper.upper())

    for amino in allAnimo_list:
        # amino = amino.upper()
        if amino not in num_string:
            aminoNotInDataBase.append(amino)

    print("查看缺少氨基酸的列：", aminoNotInDataBase)
    print("缺少氨基酸的个数:", len(aminoNotInDataBase))

    # print(list(set(allAnimo_list).difference(set(new_num_string))))
    # print(len(list(set(allAnimo_list).difference(set(new_num_string)))))





















# Tripeptide-single-amino-acid-database-generator
A script to generate a tripeptide database. At present, the amino acids of tripeptides produced are not complete
一个基于已有的PDB文件构建三肽数据库的脚本，生成的三肽均已经加氢。

# 安装

Anaconda安装modeller模块

conda config --add channels salilab

conda install modeller

Anaconda安装biopython模块

conda install biopython

# 使用方法

1. 在脚本目录内创建一个data文件，里面放入pdb文件，用于做数据库

![45b4a75d2466f35b9dd3a6ffe4ccb61](https://user-images.githubusercontent.com/54057111/117917458-bc535980-b31b-11eb-9987-39b1f0942d8f.png)
![e14427820e7994001df8eecedad9b5e](https://user-images.githubusercontent.com/54057111/117917863-911d3a00-b31c-11eb-9f2b-9b43fe4edec7.png)



2. 在命令行界面输入命令：

命令： python 3AminoCsvCreator.py

即可开始生成三肽数据库

所需要的文件示例：

![aaa024b94ba5503dfc058217ca2bbbc](https://user-images.githubusercontent.com/54057111/117917654-1f44f080-b31c-11eb-8c46-25e7aeab31a3.png)

在此过程中会生成巨量的文件，只需要这些就行了。

在pymol上显示生成的三肽：

![ce08e7fb069698e8d40a76f0f4b797b](https://user-images.githubusercontent.com/54057111/117917990-cfb2f480-b31c-11eb-8e78-e2ba7202aca6.png)

三肽已经加氢。

3. 检查有无遗漏的三肽文件：

在这里提供了checkLostAmino.py脚本用于检查有无遗漏的三肽，理论上来讲，生成的三肽总数是有8000个文件

新建一个3AminoDataBase文件夹，将生成的三肽文件放进去，然后在命令行界面运行checkLostAmino.py脚本即可

命令： python checkLostAmino.py

效果：

![e9af6d409197498fc4202266f6b1e98](https://user-images.githubusercontent.com/54057111/117918326-62ec2a00-b31d-11eb-9a3f-090ceed3ba6a.png)



# ppr_practice
This script can help you to easily use projection-pursuit regression.


## How to use
First you should download indipendence and the python version should python >= 3.6
### Indipendence 
```sh
$ pip install numpy, scipy, scikit-learn, matplotlib, projection-pursuit
```
Then, clone this directory to the local.
```sh
$ git clone https://github.com/GaoyangLuo/ppr_practice.git
$ cd  ppr_practice
```
Then you can use the script ppr_practice.py to generate your simulation projection values.
```sh
python ppr.py -i <input> -o <output> -l <left range> -r <right range> -t <iterate_times>
```
### Notion
```sh
Here, the each value refers to:
    -i <input> #First column should contain indexes, the second is x, the third is y, header should be included.
    -o <output> #the output path you want to store the projection values
    -l <left range> #set the start of your simulation x range
    -r <right range> #set the end of your simulation x range
    -t <iterate_times> #set how many iterations you want to run.
```

# Cite 
Please freely use this script but don't forget to cite this page, thank you!
Please cite :
> https://github.com/GaoyangLuo/ppr_practice


# ppr_practice
This script can help you to easily use projection-pursuit regression.


## How to use
First you should download indipendence and the python version should python >= 3.6, numpy, scipy, scikit-learn, matplotlib, projection-pursuit
### Requirements 
`pip install numpy, scipy, scikit-learn, matplotlib, projection-pursuit`

### Running Predicion

Then, clone this directory to the local.
```sh
git clone https://github.com/GaoyangLuo/ppr_practice.git
cd ppr_practice
```

Then you can use the script ppr_practice.py to generate your simulation projection values. Note that this script used simulated x that generated from the real values of your scripts. And if you want to use higer dimensions of Xi, simulation may not work. The output can only generate a set of validated y values by the input of the original X, and by using the validated y values, the projection values of x, you can draw a linear regression using true y with the projections of y.

Example usage:

```sh
python ppr_practice.py -i example.txt -o out.txt -l 0.1 -r 1.0 -t 100
```

### Notion
Here, each value refers to:
```sh
Options:
    -i, --input First column should contain indexes, the second is x, the third is y, header should be included.
    -o, --output the output path you want to store the projection values
    -l, --lrange set the start of your simulation x range
    -r, --rrange set the end of your simulation y range
    -t, --times set how many iterations you want to run.
```

# Cite 
Please freely use this script but don't forget to cite this page, thank you!
Please cite:
> https://github.com/GaoyangLuo/ppr_practice


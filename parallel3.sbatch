#!/bin/bash
#SBATCH --partition classpart
#SBATCH --account classroom
#SBATCH --cpus-per-task 40
#SBATCH --mem 40000
#SBATCH --time 0-00:01:00
#SBATCH --job-name hello
#SBATCH --output parallel-%j.out
#SBATCH --error parallel-%j.err
#SBATCH --mail-type ALL
module load Python/3.8.0
python $HOME/parallel.py

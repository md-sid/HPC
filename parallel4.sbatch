#!/bin/bash
#SBATCH --partition classpart
#SBATCH --account classroom
#SBATCH --cpus-per-task 40
#SBATCH --mem 40000
#SBATCH --time 0-00:01:00
#SBATCH --job-name hello
#SBATCH --output bubble-parallel-%j.out
#SBATCH --error bubble-parallel-%j.err
#SBATCH --mail-type ALL
module load Python/3.8.0
python ./bubblesortpar.py

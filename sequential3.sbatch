#!/bin/bash
#SBATCH --partition classpart
#SBATCH --account classroom
#SBATCH --cpus-per-task 1
#SBATCH --mem 1000
#SBATCH --time 0-00:40:00
#SBATCH --job-name hello
#SBATCH --output sequential-%j.out
#SBATCH --error sequential-%j.err
#SBATCH --mail-type ALL
module load Python/3.8.0
python $HOME/sequential.py


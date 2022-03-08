#!/bin/bash
#SBATCH --partition classpart
#SBATCH --account classroom
#SBATCH --cpus-per-task 1
#SBATCH --mem 1000
#SBATCH --time 0-00:40:00
#SBATCH --job-name primearray
#SBATCH --array=1-1000
#SBATCH --output prime-%j.out
#SBATCH --error prime-%j.err
module load Python/3.8.0
python $HOME/HW5/single_prime_check.py $SLURM_ARRAY_TASK_ID


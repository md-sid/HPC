#!/bin/bash
#SBATCH --partition classpart
#SBATCH --account classroom
#SBATCH --cpus-per-task 1
#SBATCH --mem 1000
#SBATCH --time 0-00:40:00
#SBATCH --job-name summary
#SBATCH --output summary-%j.out
#SBATCH --error summary-%j.err
#SBATCH --dependency=afterany:2257947
#SBATCH --mail-type END
mv prime-* ./output/
cat ./output/*.out


#!/bin/bash
#
#SBATCH --job-name=test
#SBATCH --output=res.txt
#
#SBATCH --ntasks=1
#SBATCH --time=10:00
#SBATCH --mem-per-cpu=100

srun python3 /EasyVVUQ/docs/epidemic/epidemic.py ./epidemic_in.json out.csv
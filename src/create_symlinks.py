import subprocess
import os

root_dir = "/home/brandon/data/pingyin/snmultiome/input"


def create_symlinks(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    # Prepare the command
    command = ["cp", "-rs", os.path.join(input_dir, "."), output_dir]

    try:
        subprocess.run(command, check=True)
        print(f"Symlinked contents of '{input_dir}' into '{output_dir}' using cp -rs")
    except subprocess.CalledProcessError as e:
        print(f"Error during symlinking: {e}")


# remove "{root_dir}" if it exists
if os.path.exists(f"{root_dir}"):
    os.system(f"rm -r {root_dir}")

# 1619LM
input_dir = "/mnt/c/Users/Brand/Northwestern University/Ping Yin - BulunDai_snRNA_ATAC_seq_LM/1619LM"
output_dir = f"{root_dir}/1619LM"
create_symlinks(input_dir, output_dir)

# 1619MM
input_dir = "/mnt/c/Users/Brand/Northwestern University/Ping Yin - BulunDai_snRNA_ATAC_seq_LM/Bulun80_3.28.2024/1619MM"
output_dir = f"{root_dir}/1619MM"
create_symlinks(input_dir, output_dir)

# 1633MM-repeat
input_dir = "/mnt/c/Users/Brand/Northwestern University/Ping Yin - BulunDai_snRNA_ATAC_seq_LM/Bulun80_1633MM-repeat/1633MM-repeat"
output_dir = f"{root_dir}/1633MM-repeat"
create_symlinks(input_dir, output_dir)

# 1633LM
input_dir = "/mnt/c/Users/Brand/Northwestern University/Takuma Suzuki - Fibroid snRNAseq Project shared/Bulun80_03.28.2024/1633LM"
output_dir = f"{root_dir}/1633LM"
create_symlinks(input_dir, output_dir)

import muon as mu
from snakemake.script import snakemake


def run_mofa(input_file, output_file, model_file):
    mdata = mu.read(input_file)
    mu.tl.mofa(
        mdata,
        groups_label="sample",
        outfile=model_file,
        gpu_mode=True,
        gpu_device=0,
    )
    mdata.write(output_file)


run_mofa(snakemake.input[0], snakemake.output[0], snakemake.output["model"])

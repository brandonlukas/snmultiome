import anndata as ad
import scanpy as sc
import snapatac2 as snap
from snakemake.script import snakemake


def make_unique_cell_ids(adata):
    unique_cell_ids = [
        sa + ":" + bc for sa, bc in zip(adata.obs["sample"], adata.obs_names)
    ]
    return unique_cell_ids


def merge_snap(input_files, sample_names, output_file):
    adatas: dict[str, sc.AnnData] = {}
    for sample_name, input_file in zip(sample_names, input_files):
        adata = sc.read(input_file)
        adatas[sample_name] = adata

    adata = ad.concat(adatas, label="sample")

    # Make barcode names unique
    unique_cell_ids = make_unique_cell_ids(adata)
    adata.obs_names = unique_cell_ids

    # Feature selection
    sc.pp.highly_variable_genes(adata, batch_key="sample")

    # Save log-normalized counts in a .raw slot
    adata.raw = adata

    # Scale the log-normalized counts to zero mean and unit variance
    sc.pp.scale(adata, max_value=10)

    # This object is ready for muon analysis
    adata.write(output_file)


merge_snap(
    input_files=snakemake.input,
    sample_names=snakemake.params.sample_names,
    output_file=snakemake.output[0],
)

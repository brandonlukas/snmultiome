import scanpy as sc
import snapatac2 as snap
import celltypist
from snakemake.script import snakemake


def cellxgene_snap(input_file, output_file, qc_thresholds: dict):
    adata = sc.read(input_file)
    gene_matrix = snap.pp.make_gene_matrix(adata, snap.genome.hg38)

    # Normalization (log1p normalised expression to 10,000 counts per cell)
    sc.pp.normalize_total(gene_matrix, target_sum=1e4)
    sc.pp.log1p(gene_matrix)

    sc.pp.filter_genes(gene_matrix, min_cells=qc_thresholds.get("min_cells"))
    gene_matrix.write_h5ad(output_file)


cellxgene_snap(
    input_file=snakemake.input[0],
    output_file=snakemake.output[0],
    qc_thresholds=snakemake.params["qc_thresholds"],
)

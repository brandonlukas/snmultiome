import scanpy as sc
import celltypist
from snakemake.script import snakemake


def filter_anndata(
    input_file, out_file, qc_thresholds: dict, celltypist_model: str | None
):
    adata = sc.read_h5ad(input_file)
    sc.pp.filter_cells(adata, min_genes=qc_thresholds.get("min_genes"))
    sc.pp.filter_cells(adata, min_counts=qc_thresholds.get("min_counts"))

    if threshold := qc_thresholds.get("pct_counts_mt"):
        adata = adata[adata.obs["pct_counts_mt"] < threshold, :]

    if threshold := qc_thresholds.get("pct_counts_ribo"):
        adata = adata[adata.obs["pct_counts_ribo"] < threshold, :]

    if threshold := qc_thresholds.get("doublet_score"):
        adata = adata[adata.obs["doublet_score"] < threshold, :]

    # Normalization (log1p normalised expression to 10,000 counts per cell)
    adata.layers["counts"] = adata.X.copy()
    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)

    # Celltypist model
    if celltypist_model:
        predictions = celltypist.annotate(
            adata, model=celltypist_model, majority_voting=True
        )
        adata.obs = adata.obs.merge(
            predictions.predicted_labels,
            left_index=True,
            right_index=True,
        )

    sc.pp.filter_genes(adata, min_cells=qc_thresholds.get("min_cells"))
    adata.write_h5ad(out_file)


filter_anndata(
    snakemake.input[0],
    snakemake.output[0],
    qc_thresholds=snakemake.params["qc_thresholds"],
    celltypist_model=snakemake.params["celltypist_model"],
)

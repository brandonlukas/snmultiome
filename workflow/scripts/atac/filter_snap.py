import snapatac2 as snap
from snakemake.script import snakemake


def filter_snap(input_file, output_file, qc_thresholds: dict, n_jobs=8):
    adata = snap.read(input_file, backed="r").copy(output_file)
    snap.pp.filter_cells(
        adata,
        min_counts=qc_thresholds.get("min_counts"),
        min_tsse=qc_thresholds.get("min_tsse"),
        n_jobs=n_jobs,
    )
    snap.pp.filter_doublets(adata, n_jobs=n_jobs)
    adata.close()


filter_snap(
    snakemake.input[0],
    snakemake.output[0],
    qc_thresholds=snakemake.params["qc_thresholds"],
    n_jobs=snakemake.threads,
)

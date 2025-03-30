import snapatac2 as snap
import pandas as pd
from snakemake.script import snakemake


def init_snap(fragment_file, barcodes_file, output_file, blacklist_file, n_jobs=8):
    whitelist = pd.read_csv(barcodes_file, sep="\t", header=None)[0].values
    adata = snap.pp.import_fragments(
        fragment_file,
        chrom_sizes=snap.genome.hg38,
        file=output_file,
        sorted_by_barcode=False,
        whitelist=whitelist,
        n_jobs=n_jobs,
    )
    snap.metrics.tsse(adata, snap.genome.hg38, n_jobs=n_jobs)
    snap.pp.add_tile_matrix(adata, n_jobs=n_jobs)
    snap.pp.select_features(adata, blacklist=blacklist_file, n_jobs=n_jobs)
    snap.pp.scrublet(adata, n_jobs=n_jobs)
    adata.close()


init_snap(
    snakemake.input["fragment"],
    snakemake.input["barcodes"],
    snakemake.output[0],
    snakemake.params["blacklist"],
    n_jobs=snakemake.threads,
)

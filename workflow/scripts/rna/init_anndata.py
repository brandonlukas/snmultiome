import scanpy as sc
from snakemake.script import snakemake


def init_anndata(input_dir, out_file):
    adata = sc.read_10x_mtx(input_dir)
    sc.pp.scrublet(adata)
    adata.var["mt"] = adata.var_names.str.startswith("MT-")
    adata.var["ribo"] = adata.var_names.str.startswith(("RPS", "RPL"))
    adata.var["hb"] = adata.var_names.str.contains("^HB[^(P)]")
    sc.pp.calculate_qc_metrics(
        adata,
        qc_vars=["mt", "ribo", "hb"],
        percent_top=None,
        log1p=False,
        inplace=True,
    )

    adata.write_h5ad(out_file)


init_anndata(snakemake.input[0], snakemake.output[0])

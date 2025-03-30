import muon as mu
import anndata as ad
from snakemake.script import snakemake


def init_muon(rna_file, atac_file, output_file):
    adata_rna = ad.read_h5ad(rna_file)
    adata_atac = ad.read_h5ad(atac_file)
    mdata = mu.MuData({"rna": adata_rna, "atac": adata_atac})
    mu.pp.intersect_obs(mdata)
    mdata.obs["sample"] = mdata.obs["rna:sample"].astype("category")
    mdata.write(output_file)


init_muon(snakemake.input["rna"], snakemake.input["atac"], snakemake.output[0])

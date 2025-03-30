rule rna_metrics:
    input:
        config["results_dir"] + "0_initialization/{sample}/{sample}.h5mu",
    output:
        config["results_dir"] + "1_qc_metrics/{sample}/{sample}.rna.h5ad",
    log:
        notebook="logs/notebooks/1_qc_metrics/{sample}/1-rna_metrics.ipynb",
    notebook:
        "../notebooks/1_qc_metrics/1-rna_metrics.py.ipynb"


rule atac_metrics:
    input:
        config["results_dir"] + "0_initialization/{sample}/{sample}.h5mu",
        fragments=config["data_dir"] + "{sample}/outs/atac_fragments.tsv.gz",
        barcodes=config["data_dir"]
        + "{sample}/outs/filtered_feature_bc_matrix/barcodes.tsv.gz",
    output:
        config["results_dir"] + "1_qc_metrics/{sample}/{sample}.atac.h5ad",
    params:
        blacklist=config["ATAC"]["blacklist"],
    threads: 12
    log:
        notebook="logs/notebooks/1_qc_metrics/{sample}/2-atac_metrics.ipynb",
    notebook:
        "../notebooks/1_qc_metrics/2-atac_metrics.py.ipynb"

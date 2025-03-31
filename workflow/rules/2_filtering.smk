rule rna_filtering:
    input:
        config["results_dir"] + "1_qc_metrics/{sample}/{sample}.rna.h5ad",
    output:
        config["results_dir"] + "2_filtering/{sample}/{sample}.rna.h5ad",
    params:
        qc_filters=config["RNA"]["qc_filters"],
    log:
        notebook="logs/notebooks/2_filtering/{sample}/1-rna_filtering.ipynb",
    notebook:
        "../notebooks/2_filtering/1-rna_filtering.py.ipynb"


rule atac_filtering:
    input:
        config["results_dir"] + "1_qc_metrics/{sample}/{sample}.atac.h5ad",
    output:
        config["results_dir"] + "2_filtering/{sample}/{sample}.atac.h5ad",
    params:
        qc_filters=config["ATAC"]["qc_filters"],
    log:
        notebook="logs/notebooks/2_filtering/{sample}/2-atac_filtering.ipynb",
    notebook:
        "../notebooks/2_filtering/2-atac_filtering.py.ipynb"

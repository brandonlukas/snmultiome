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


rule combine_metrics:
    input:
        rna=config["results_dir"] + "1_qc_metrics/{sample}/{sample}.rna.h5ad",
        atac=config["results_dir"] + "1_qc_metrics/{sample}/{sample}.atac.h5ad",
    output:
        config["results_dir"] + "1_qc_metrics/{sample}/{sample}.h5mu",
    log:
        notebook="logs/notebooks/1_qc_metrics/{sample}/3-combine_metrics.ipynb",
    notebook:
        "../notebooks/1_qc_metrics/3-combine_metrics.py.ipynb"


rule aggregate_metrics:
    input:
        expand(
            config["results_dir"] + "1_qc_metrics/{sample}/{sample}.h5mu",
            sample=config["samples"],
        ),
    output:
        config["results_dir"] + "1_qc_metrics/qc_metrics.parquet",
    params:
        samples=config["samples"],
    script:
        "../scripts/1_qc_metrics/aggregate_metrics.py"

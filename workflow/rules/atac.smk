rule init_snap:
    input:
        fragment=config["data_dir"] + "{sample}/outs/atac_fragments.tsv.gz",
        barcodes=config["data_dir"]
        + "{sample}/outs/filtered_feature_bc_matrix/barcodes.tsv.gz",
    output:
        config["results_dir"] + "ATAC/samples/unfiltered/{sample}.h5ad",
    params:
        blacklist=config["ATAC"]["blacklist"],
    threads: 12
    script:
        "../scripts/atac/init_snap.py"


rule filter_snap:
    input:
        config["results_dir"] + "ATAC/samples/unfiltered/{sample}.h5ad",
    output:
        config["results_dir"] + "ATAC/samples/filtered/{sample}.h5ad",
    params:
        qc_thresholds=config["ATAC"]["qc"],
    threads: 12
    script:
        "../scripts/atac/filter_snap.py"


rule cellxgene_snap:
    input:
        config["results_dir"] + "ATAC/samples/filtered/{sample}.h5ad",
    output:
        config["results_dir"] + "ATAC/samples/cellxgene/{sample}.h5ad",
    params:
        qc_thresholds=config["ATAC"]["qc"],
    script:
        "../scripts/atac/cellxgene_snap.py"


rule merge_snap:
    input:
        expand(
            config["results_dir"] + "ATAC/samples/cellxgene/{sample}.h5ad",
            sample=config["samples"],
        ),
    output:
        config["results_dir"] + "ATAC/merged.h5ad",
    params:
        sample_names=config["samples"],
    script:
        "../scripts/atac/merge_snap.py"

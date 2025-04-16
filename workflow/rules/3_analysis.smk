rule rna_analysis:
    input:
        config["results_dir"] + "2_filtering/{sample}/{sample}.rna.h5ad",
    output:
        config["results_dir"] + "3_analysis/{sample}/{sample}.rna.h5ad",
    params:
        celltypist_model=config["RNA"]["celltypist_model"],
    log:
        notebook="logs/notebooks/3_analysis/{sample}/1-rna_analysis.ipynb",
    notebook:
        "../notebooks/3_analysis/1-rna_analysis.py.ipynb"

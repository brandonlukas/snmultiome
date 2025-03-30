rule run_soupX:
    input:
        config["data_dir"] + "{sample}/outs",
    output:
        directory(config["results_dir"] + "0_initialization/{sample}/SoupX"),
    log:
        notebook="logs/notebooks/0_initialization/{sample}/1-run_soupX.ipynb",
    notebook:
        "../notebooks/0_initialization/1-run_soupX.r.ipynb"


rule init_muon:
    input:
        h5=config["data_dir"] + "{sample}/outs/filtered_feature_bc_matrix.h5",
        soupX=config["results_dir"] + "0_initialization/{sample}/SoupX",
    output:
        config["results_dir"] + "0_initialization/{sample}/{sample}.h5mu",
    log:
        notebook="logs/notebooks/0_initialization/{sample}/2-init_muon.ipynb",
    notebook:
        "../notebooks/0_initialization/2-init_muon.py.ipynb"

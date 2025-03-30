rule run_soupX:
    input:
        config["data_dir"] + "{sample}/outs",
    output:
        directory(config["results_dir"] + "{sample}/SoupX"),
    log:
        notebook="logs/notebooks/{sample}/run_soupX.ipynb",
    notebook:
        "../notebooks/run_soupX.r.ipynb"


rule init_muon:
    input:
        h5=config["data_dir"] + "{sample}/outs/filtered_feature_bc_matrix.h5",
        soupX=config["results_dir"] + "{sample}/SoupX",
    output:
        config["results_dir"] + "{sample}/init.h5mu",
    log:
        notebook="logs/notebooks/{sample}/init_muon.ipynb",
    notebook:
        "../notebooks/init_muon.py.ipynb"

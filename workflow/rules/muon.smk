rule init_muon:
    input:
        rna=config["results_dir"] + "RNA/merged.h5ad",
        atac=config["results_dir"] + "ATAC/merged.h5ad",
    output:
        config["results_dir"] + "muon/merged.h5mu",
    script:
        "../scripts/muon/init_muon.py"


rule run_mofa:
    input:
        config["results_dir"] + "muon/merged.h5mu",
    output:
        config["results_dir"] + "muon/integrated_mofa.h5mu",
        model=config["results_dir"] + "muon/models/mofa.hdf5",
    script:
        "../scripts/muon/run_mofa.py"

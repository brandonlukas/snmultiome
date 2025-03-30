import muon as mu
import pandas as pd
from tqdm import tqdm
from snakemake.script import snakemake


def extract_metrics(file_path, sample_name):
    mdata = mu.read(file_path, backed="r")
    df = mdata.obs
    df["sample"] = sample_name
    return df


def aggregate_metrics(input_files, output_file, sample_names):
    iterable = list(zip(input_files, sample_names))
    df_list = [extract_metrics(f, name) for f, name in tqdm(iterable)]
    df = pd.concat(df_list)
    df.to_parquet(output_file, index=False)


aggregate_metrics(snakemake.input, snakemake.output[0], snakemake.params["samples"])

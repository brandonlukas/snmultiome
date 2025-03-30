library(SoupX)
library(DropletUtils)

remove_ambient_rna <- function(data_dir, out_dir) {
  sc <- load10X(data_dir)
  sc <- autoEstCont(sc)
  out <- adjustCounts(sc, roundToInt = TRUE)
  DropletUtils:::write10xCounts(out_dir, out)
}

remove_ambient_rna(snakemake@input[[1]], snakemake@output[[1]])

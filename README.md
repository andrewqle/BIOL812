# Analysis [The Cryptic Impacts of Invasion: Functional Homogenization of Tropical Ant Communities by Invasive Fire Ants]
Hello everyone!\
The goal of this repository is: \
1)to understand some of the procedural analysis done \
2)to ultimately reproduce some of the data published in: https://doi.org/10.1111/oik.06870 .\
Data can be found here: http://dx.doi.org/10.5061/dryad.s7h44j13f .\
OR \
Within this repository: file [2] & [3] \
*DATA IS NOT MINE*\
 \
There are 4 files in this repository:\
[1] BIOL8121stASSIGNMENT.Rmd is a R-Markdown that goes through some of the background analysis that was done in the paper, but not shown.\
This R-markdown was written in R version 4.1.0 (2021-05-18)\
Within this RMD:
1) A Principal Component Analsysis (PCA) was conducted to observe the variation of 6 traits in 29 different fire ant species.
2) A Trait Probability Density (TPD) approach was conducted at the species level to observe trait similarities and differences between species.\
Page 165-188 of https://digital.csic.es/bitstream/10261/221270/3/R_Material_traits.pdf was used. \
TPD Analysis at the species level was supposed to turn into community level, then into Functional richness (FRic), Functional evenness (FEve), Functional divergence (FDiv). But invaded versus uninvaded community data was not available. 

[2] README.md is a synposis on purpose of the repository \
[3] matrix.freq 1.csv is comma-separated values file that was not used in this particular R-markdown analysis. But would have been needed for TPD community analysis. \
[4] traits.ind 1.csv is comma-separated values file that was used in order to do majority of the analysis.\
[5] PCA.py is a Spyder(Python 3.9) script coded from the Anaconda-navigator in order to try to replicate the PCA analysis done in R-Markdown

# Analysis: [The Cryptic Impacts of Invasion: Functional Homogenization of Tropical Ant Communities by Invasive Fire Ants]
Hello everyone!\
The goal of this repository is: \
1)to understand some of the procedural analysis done \
&\
2)to ultimately reproduce some of the data published in: https://doi.org/10.1111/oik.06870 .\
Data can be found here: http://dx.doi.org/10.5061/dryad.s7h44j13f .\
OR \
Within this repository: file [2] & [3] \
 \
Background Information:\
In this Dataset, there are 29 different species and 6 different traits:\
Head Width\
Pronotum Width\
Mandible Length\
Scape Length\
Eye Width\
Leg Length\
\
The goal of their paper was:\
Investigate how S. invicta invasion affects taxonomic and functional beta diversity (the dissimilarities in species and traits between communities) at the multi-community (landscape) scale.

# Proposed Pipeline:
<img width="947" alt="Pipeline4" src="https://user-images.githubusercontent.com/101582963/160485724-5969dc5c-bafc-4230-be65-e9431b1d2989.png">

Blocks of Blue indicated areas that I could complete with the coding knowledge I know. \
Blocks of Grey indicated files where the code can be found within this repository.\
Blocks of Red indicated areas where I could not complete due to not enough information and coding knowledge.\
The green block represented the results and figures obtained in the paper.

# Principal Component Analysis:
In the original paper, 29 unique species with a total of 319 species were analyzed to observe the 6 different traits at the species level and community level. \
A Principal Component Analysis (PCA) was done in order to see which traits controlled most of the variation within species. \
They concluded that: 
\
PC1 (55.1%): Negatively correlated with Head and Pronotum Width | Positively correlated with Leg Length\
PC2 (21.6%): Negatively correlated with Eye Width | Positively correlated with Body Size\
Majority of the variation being controlled by the traits facilitating the first principal component.\
\
*However*:\
The PCA that I conducted gave different results:\
\
The first time I ran the PCA, I removed rows (individual species) if trait data was missing.\
PC1 (52.84%): Negatively correlated with Leg and Scape length | Positively correlated with Mandible Length and Pronotum and Head Width.\
PC2 (23.34%): Negatively correlated with Eye Width.\
The correlations for PC1 were in reverse. \
\
The second time I ran the PCA, I removed individual values using missMDA package.\
PC1 (51.24%): Negatively correlated with Leg and Scape length | Positively correlated with Mandible Length and Pronotum and Head Width.\
PC2 (24.78%): Negatively correlated with Eye Width.\
Which still gave different results.\
\
I tried replicating this PCA in python in order to see if I can replicate the same results by omitting rows with N/A.\
PC1 (52.8%)\
PC2 (23.8%)\
PC2 differentiated by 0.5%.\
\
GAPS: I couldn't construct a biplot in Python, and include a PCA of all species as I couldn't incoperate one colour per species up to 3 species. So a PCA of 3 species was shown. 

# Trait Probaility Density Analysis:
Ideally, the traits that controlled most of the variation were going to be used in order to observe pairwise traits within species.\
\
Probability density functions can be used to reflect intraspecific variation, the multidimensional nature of traits, species abundances and probabilistic trait distributions\
\
During the Trait Probability Denisty (TPD) analysis, I used Head Width and Mandible Length as they were two traits that controlled most of the variation in PC1.\
\
But to get familiar with the TPD function. TPD was conducted for all 6 traits for all species.\
X-axis showing size in millimeters.\
Y-axis showing the frequency/density of species.\
\
Then a pairwise analysis on the trait of Head Width and Mandible Length was done at the species level to observe the density at which size for both traits would be most frequent for each species.\
This realationship was plotted:\
X-axis is head width in millimeters.\
Y-axis is mandible length in millimeters.\
Lighter tones of blue shows higher probability of trait combination.\
Darker tones of blue shows lower probaility of trait combination.\
\
GAPS: TPD Analysis at the species level was supposed to turn into community level, then into 5 indices of functional diversity:\
\
Functional richness (FRic)\
Functional evenness (FEve)\
Functional divergence (FDiv)\
Functional Redundancy (FRed)\
Functional space controlled by richness (Rao)\
\
Which would then lead into the data presented in the paper. But invaded versus uninvaded community data was not available.

# Repository:
There are 5 files in this repository:\
[1] BIOL8121stASSIGNMENT.Rmd is a R-Markdown that goes through some of the background analysis that was done in the paper, but not shown.\
This R-markdown was written in R version 4.1.0 (2021-05-18)\
Within this RMD:

*1)* A Principal Component Analsysis (PCA) was conducted to observe the variation of 6 traits in 29 different fire ant species.\
*2)* A Trait Probability Density (TPD) approach was conducted at the species level to observe trait similarities and differences between species. Page 165-188 of https://digital.csic.es/bitstream/10261/221270/3/R_Material_traits.pdf was used. \
\
[2] README.md is a synposis on purpose of the repository and why certain things were done. \
[3] matrix.freq 1.csv is comma-separated values file that was not used in this particular R-markdown analysis. But would have been needed for TPD community analysis. \
[4] traits.ind 1.csv is comma-separated values file that was used in order to do majority of the analysis.\
[5] PCA1.py is a Spyder(Python 3.9) script coded from the Anaconda-navigator in order to try to replicate the PCA analysis done in R-Markdown. 

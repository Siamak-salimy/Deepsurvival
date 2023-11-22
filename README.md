# Deepsurvival
Omics data integration using deep learning-based method for identification of survival associated subgroups in colon cancer . </br>
Precise prognostic classification of patients and identifying survival subgroups and their associated genes can be important clinical references when designing treatment strategies for cancer patients. </br> 
Multi-omics and data integration techniques are powerful tools to achieve this goal. </br> This study aimed to introduce a machine learning method to integrate three types of biological data, and investigate the performance of two other methods,
in identifying the survival dependency of patients. </br>
The data included TCGA RNA-seq gene expression, DNA methylation, and clinical data from 368 patients with colon cancer also we use an independent external validation data set, containing 232 samples.</br> Three methods including, Hyper-Parameter Optimized Autoencoders (HPOAE), Normal autoencoder, and penalized principal component analysis (PPCA) were used for simultaneous data integration and estimation under a COX hazards model. </br> The HPOAE was thought to outperform other methods.  </br>The HPOAE had the Log Rank Mantel-Cox value of 14.27 ± 2, and a Breslow-Generalized Wilcoxon value of 13.13 ± 1.</br> 10 miRNA, 11 methylated genes, and 25 mRNA all by (Importance of marginal cutoff > 0.95) were identified.</br> The study demonstrated that hsa-miR-485-5p targets both ZMYM1 and Tp53, the latter of which has been previously associated with cancer in numerous studies.</br> Furthermore, compared to other methods, the HPOAE exhibited a greater capacity for identifying survival subgroups and the genes associated with them in patients with colon cancer.</br> However, all of the results were obtained by computational methods, and clinical and experimental studies are needed to validate these results.</br>
DOI: 10.1016/j.heliyon.2023.e17653 </br>
https://doi.org/10.1146/annurev-statistics-032921-022127 : 
In the era of precision medicine, time-to-event outcomes such as time to death or progression are routinely collected, along with high-throughput covariates. 
These high-dimensional data defy classical survival regression
models, which are either infeasible to fit or likely to incur low predictability
due to overfitting.To overcome this, recent emphasis has been placed on de-
veloping novel approaches for feature selection and survival prognostication.
In this article, we review various cutting-edge methods that handle survival
outcome data with high-dimensional predictors, highlighting recent inno-
vations in machine learning approaches for survival prediction.We cover the
statistical intuitions and principles behind these methods and conclude with
extensions to more complex settings, where competing events are observed.
We exemplify these methods with applications to the Boston Lung Can-
cer Survival Cohort study, one of the largest cancer epidemiology cohorts
investigating the complex mechanisms of lung cancer.

🧬 Integrated Multi-Omics Analysis for AML Biomarker Discovery
📋 Executive Summary
This project demonstrates a multi-dimensional approach to leukemia research by integrating Clinical, Transcriptomic (RNA-Seq), and Genomic data from the TCGA-LAML cohort. The goal is to identify molecular signatures that differentiate leukemic cells and understand the genomic architecture of driver mutations.
🛠️ Tech Stack & Methodology
Programming: Python 3.12.

Bioinformatics Tools: Biopython for genomic data processing.

Data Science: Pandas for data wrangling, Seaborn and Matplotlib for high-impact biological visualizations.

Data Source: National Cancer Institute (GDC API) - Real-world patient data.
📊 Phase 1: Clinical Cohort Profiling
Analysis was performed on a cohort of 100 AML patients to establish demographic baselines.

*Key Finding: The average age at diagnosis was 56.52 years.

*Observation: Data visualization revealed a significant spike in disease prevalence for individuals above age 60, correlating with known clinical patterns of AML.
🧬 Phase 2: Transcriptomic Signature (RNA-Seq)
I processed transcriptomic read counts to identify the most active genes in leukemic blast samples.

*Top Gene Identified: MT-RNR2 (Mitochondrial Ribosomal RNA 2).

*Biological Insight: The massive expression of mitochondrial genes suggests an intense metabolic demand and oxidative phosphorylation activity within the leukemic microenvironment.
🧬 Phase 2: Transcriptomic Signature (RNA-Seq)
I processed transcriptomic read counts to identify the most active genes in leukemic blast samples.

Top Gene Identified: MT-RNR2 (Mitochondrial Ribosomal RNA 2).

Biological Insight: The massive expression of mitochondrial genes suggests an intense metabolic demand and oxidative phosphorylation activity within the leukemic microenvironment.
🚀 Installation & Reproducibility
1_Requirements: pip install -r requirements.txt.

2_Run Analysis: Execute data_acquisition.py to fetch fresh data and regenerate all plots.

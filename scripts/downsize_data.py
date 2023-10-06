import pandas as pd
import json
import numpy as np

# This script downsizes the data to only include VGICs

cpm = pd.read_csv("/nethome/kcni/nxu/gene-ephys-tutorial/data/20200513_Mouse_PatchSeq_Release_cpm.v2.csv")
cpm = cpm.rename(columns = {'Unnamed: 0': 'gene_id'})

metadata = pd.read_csv("/nethome/kcni/nxu/gene-ephys-tutorial/data/20200625_patchseq_metadata_mouse.csv")
transcriptomic_to_specimen_id = metadata.set_index("transcriptomics_sample_id")["cell_specimen_id"].to_dict()

# remove genees that are not expresed in any cells
cpm = cpm.loc[cpm.sum(axis = 1) != 0]

# load list of VGICs
with open('./data/IC_list.json', 'r') as f:
    IC_list = json.load(f)

# Subset for VGICs only
cpm = cpm.loc[cpm.gene_id.isin(IC_list["VGIC"])]
cpm = cpm.set_index("gene_id")

# change the column names from transcriptomic_sample_id to cell_specimen_id
cpm.columns = cpm.columns.map(transcriptomic_to_specimen_id)

cpm.to_csv("/nethome/kcni/nxu/gene-ephys-tutorial/data/VGIC_cpm.csv")
# First, we need to create an empty list to store the CPM for each cell
cpm = []

# Then, for each cell, we compute the CPM and append it to the list
for column in count_matrix.columns:
    cpm.append(count_matrix[column] / lib_size.loc[column, 'library_size'] * 10000)

# Finally, we concatenate the list of CPM into a dataframe
cpm = pd.concat(cpm, axis = 1)
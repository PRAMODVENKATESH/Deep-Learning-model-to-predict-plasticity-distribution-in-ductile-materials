import
def Total_reaction_force_data(inputPath1):
# initialize the list of column names in the CSV file and then
# load it using Pandas
    cols = ["Totalreactionforce"]
    df = pd.read_csv(inputPath1, sep=",", header=None, names=cols)
    print(df.shape)
    #print(df.head(3))
    print(df.describe)
	  #return the data frame
    return df

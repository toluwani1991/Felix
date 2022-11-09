def EDA_category(data, var_group, x_size=6, y_size=4, sort=True):
    # setting figure_size
    size = len(var_group)
   
    plt.figure(figsize = (x_size*size, y_size), dpi = 100)
 
    # for every variable
    for j,i in enumerate(var_group):
 
        norm_count = data[i].value_counts(normalize = True).sort_index()
        if(sort):
            norm_count = data[i].value_counts(normalize = True)
       
        norm_count = np.round(norm_count,2)
        n_uni = data[i].nunique()
       
        # Plotting the variable with every information
        plt.subplot(1,size,j+1)
        sns.barplot(x=norm_count.reset_index()['index'].to_list(), y=norm_count)
        plt.ylabel('fraction')
        plt.xlabel('{}'.format(i))
        plt.title('Number of unique categories = {} \n Distribution \n {};'.format(n_uni,np.round(data[i].value_counts(normalize = True), 2)))
        plt.xticks(rotation=90)
        plt.show
 
def EDA_countplot(data, features, x_size=6, y_size=4):
   
    size = len(features)
   
    plt.figure(figsize = (x_size*size, y_size), dpi = 100)
   
    for j,feature in enumerate(features):
   
        pd.DataFrame(data[feature].value_counts()).sort_values(feature, ascending=False)
 
        plt.subplot(1,size,j+1)
        sns.countplot(data[feature])
        n_uniques = data[feature].nunique()
        value_counts = data[feature].value_counts()
        plt.title('Number of unique values = {} \n Value counts \n {};'.format(n_uniques,value_counts))
        plt.xticks(rotation=90)
        plt.show
 
def EDA_continuous(data, features, kind='dist', x_size=6, y_size=4):
    size = len(features)
    plt.figure(figsize = (x_size*size, y_size), dpi = 100)
    for j,feature in enumerate(features):
        plt.subplot(1,size,j+1)
        if(kind=='dist'):
            sns.distplot(data[feature])
        elif(kind=='box'):
            sns.boxplot(data[feature])
        elif(kind=='boxen'):
            sns.boxenplot(data[feature])    
        plt.title('Summary Statistics \n {};'.format(data[feature].describe()[[1,4,5,6]]))
        plt.xticks(rotation=45)
        plt.show
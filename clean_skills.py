def clean_skills(df):
    skills = df.copy()
    #Dropping columns
    skills = skills.drop(['attacking', 'skill', 'movement', 'power', 'mentality', 'defending', 'goalkeeping'], axis = 1)

    #Dropping NaNs
    skills = skills.dropna()
    skills = skills.reset_index(drop = True)

    #Replacing NaNs for the mean
    skills = skills.fillna(skills.mean())
    skills['composure'] = skills['composure'].round(decimals = 1)
    
    return skills

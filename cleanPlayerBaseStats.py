def cleanPlayerBaseStats(df):
    # Meaning of the columns:
    # W/F - Weak Foot
    # SM - Skill Moves
    # A/W - Attacking Work Rate
    # D/W - Defending Work Rate
    # IR -  Interception rate?
    # PAC - Pace .. player speed
    # SHO - Shoot
    # DRI - Dribling
    # DEF - Defense
    # PHY - Physical
    # Hits - 
    player_base_stats = df.copy()
   
    player_base_stats = player_base_stats.dropna()
    player_base_stats.reset_index(drop=True)

    player_base_stats_clean = player_base_stats.copy()
    removeStars1 = lambda x: x[:-1]
    removeStars2 = lambda x: x[:-2]
    player_base_stats_clean['w/f'] = player_base_stats_clean['w/f'].map(removeStars2)
    player_base_stats_clean['sm'] = player_base_stats_clean['sm'].map(removeStars1)
    player_base_stats_clean['ir'] = player_base_stats_clean['ir'].map(removeStars2)

    # We change names by data for some features (the ones that can be ordered)
    player_base_stats_clean2 = player_base_stats_clean.copy()
    mapping = {'Low':0,'Medium':1,'High':2}
    player_base_stats_clean2 = player_base_stats_clean2.replace({'a/w': mapping})
    player_base_stats_clean2 = player_base_stats_clean2.replace({'d/w': mapping})

    # We convert them to numeric values
    player_base_stats_clean3= player_base_stats_clean2.copy()
    player_base_stats_clean3['w/f'] = player_base_stats_clean3['w/f'].astype(float)
    player_base_stats_clean3['sm'] = player_base_stats_clean3['sm'].astype(float)
    player_base_stats_clean3['ir'] = player_base_stats_clean3['ir'].astype(float)

    def typeConvert(x):
        if 'K' in x:
            x = 1000*float(x[:-1])
        else:
            float(x)
        return str(x) 

    player_base_stats_clean3['hits'] = player_base_stats_clean3['hits'].map(typeConvert)
    player_base_stats_clean3['hits'] = player_base_stats_clean3['hits'].astype(float)

    return player_base_stats_clean3

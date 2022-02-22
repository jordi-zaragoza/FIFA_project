def cleanHightWeightFoot(df):
    #Height
    player_info_part_clean = df.copy()
    def feet2cm (x):
        height = x.split("'")
        return float(height[0])*30.48 + float(height[1][:-1])*2.54  
    player_info_part_clean['height'] = player_info_part_clean['height'].map(feet2cm)

    #Weight
    player_info_part_clean2 = player_info_part_clean.copy()
    def libs2kg (x):
        return float(x[:-3]) * 0.45359237
    player_info_part_clean2['weight'] = player_info_part_clean2['weight'].map(libs2kg)

    # Left and right foot
    player_info_part_clean3 = player_info_part_clean2.copy()
    mapping = {'Right':0,'Left':1}
    player_info_part_clean3 = player_info_part_clean3.replace({'foot': mapping})
    player_info_part_clean3.head()
    
    return player_info_part_clean3

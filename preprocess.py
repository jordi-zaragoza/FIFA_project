import clean_positions
import cleanPlayerBasesStats
import clean_skills
import clean_player
def preprocess(df):
    df_clean = df.copy()
    
    df_clean = clean_player(df_clean)
    df_clean = clean_skills(df_clean)
    df_clean = cleanPlayerBaseStats(df_clean)
    df_clean = clean_positions(df_clean)
    
    return df_clean

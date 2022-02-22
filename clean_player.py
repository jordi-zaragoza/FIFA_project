import clean_money
import cleanHightWeightFoot
def clean_player(x):
    x = x.drop(['Loan Date End'],axis=1)
    cols = []
    for i in range(len(x.columns)):
        cols.append(x.columns[i].lower())
    x.columns = cols
        
    x.position.fillna(x.bp, inplace=True)
    x.club.fillna(x['team & contract'], inplace=True)
    x = x.drop(['joined','team & contract'],axis=1)
    
    x = cleanHightWeightFoot(x)
    x = clean_money(x)
    
    return x

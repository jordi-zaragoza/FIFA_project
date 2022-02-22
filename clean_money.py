def clean_money(df):
    
    data = df.copy()
    
    def typeConvert(x):
        x = x[1:]
        if 'K' in x:
            x = 1000*float(x[:-1])
        elif "M" in x:
            x = 1000000*float(x[:-1])
        else:
            float(x)
        return str(x)

    data['release clause'] = data['release clause'].map(typeConvert)
    data['release clause'] = data['release clause'].astype(float)

    data['wage'] = data['wage'].map(typeConvert)
    data['wage'] = data['wage'].astype(float)

    data['value'] = data['value'].map(typeConvert)
    data['value'] = data['value'].astype(float)
    
    return data

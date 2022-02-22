def clean_positions(df):
    
    df_remaining = df.drop(['ls',  'st',  'rs',  'lw',  'lf', 'cf', 'rf', 'rw', 'lam', 'cam', 'ram', 
              'lm', 'lcm', 'cm', 'rcm',  'rm', 'lwb', 'ldm', 'cdm', 'rdm', 'rwb', 'lb',
              'lcb', 'cb', 'rcb', 'rb', 'gk', 'ova'], axis=1)
    
    #Get the relevant data
    df_edit = df[['ls',  'st',  'rs',  'lw',  'lf', 'cf', 'rf', 'rw', 'lam', 'cam', 'ram', 
              'lm', 'lcm', 'cm', 'rcm',  'rm', 'lwb', 'ldm', 'cdm', 'rdm', 'rwb', 'lb',
              'lcb', 'cb', 'rcb', 'rb', 'gk', 'ova']]
    
    pos = df_edit.copy()
    #Create splits and add to the df
    pos[['ls','ls_add']] = pos.ls.str.split('+',1).tolist()
    pos[['st','st_add']] = pos.st.str.split('+',1).tolist()
    pos[['rs','rs_add']] = pos.rs.str.split('+',1).tolist()
    pos[['lw','lw_add']] = pos.lw.str.split('+',1).tolist()
    pos[['lf','lf_add']] = pos.lf.str.split('+',1).tolist()
    pos[['cf','cf_add']] = pos.cf.str.split('+',1).tolist()
    pos[['rf','rf_add']] = pos.rf.str.split('+',1).tolist()
    pos[['rw','rw_add']] = pos.rw.str.split('+',1).tolist()
    pos[['lam','lam_add']] = pos.lam.str.split('+',1).tolist()
    pos[['cam','cam_add']] = pos.cam.str.split('+',1).tolist()
    pos[['ram','ram_add']] = pos.ram.str.split('+',1).tolist()
    pos[['lm','lm_add']] = pos.lm.str.split('+',1).tolist()
    pos[['lcm','lcm_add']] = pos.lcm.str.split('+',1).tolist()
    pos[['cm','cm_add']] = pos.cm.str.split('+',1).tolist()
    pos[['rcm','rcm_add']] = pos.rcm.str.split('+',1).tolist()
    pos[['rm','rm_add']] = pos.rm.str.split('+',1).tolist()
    pos[['lwb','lwb_add']] = pos.lwb.str.split('+',1).tolist()
    pos[['ldm','ldm_add']] = pos.ldm.str.split('+',1).tolist()
    pos[['cdm','cdm_add']] = pos.cdm.str.split('+',1).tolist()
    pos[['rwb','rwb_add']] = pos.rwb.str.split('+',1).tolist()
    pos[['lb','lb_add']] = pos.lb.str.split('+',1).tolist()
    pos[['lcb','lcb_add']] = pos.lcb.str.split('+',1).tolist()
    pos[['rcb','rcb_add']] = pos.rcb.str.split('+',1).tolist()
    pos[['rb','rb_add']] = pos.rb.str.split('+',1).tolist()
    pos[['gk','gk_add']] = pos.gk.str.split('+',1).tolist()
    
    
    #Convert all columns to numeric
    for a in pos:
        pos[a] =  pd.to_numeric(pos[a], errors='coerce')
    
    #Select only columns that are relevant in respect to multicollinearity
    pos_spl_final = pos[['st',  'lw', 'cf', 'cam', 'lm','cm', 'lwb', 'cdm',  'lb', 'lcb', 'gk', 'st_add',
                             'lw_add', 'cf_add','cam_add', 'lm_add', 'cm_add', 'lwb_add', 'cdm_add', 'lb_add', 
                             'lcb_add','gk_add','ova']]
    
    df_new = pd.concat([df_remaining,pos_spl_final], axis=1)    
    
    return df_new

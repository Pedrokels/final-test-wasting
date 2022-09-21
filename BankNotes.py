from pydantic import BaseModel

class BankNote(BaseModel):
    age_child:float#1
    sex_child:float#2
    bw_grams:float#2700
    feeding:float#3
    ethnicity:float#0
    agegroup_mom:float#2
    csc_mom:float#2
    psc1:float#2
    educ_mom:float#3
    educ1_hh:float#3
    psoc_hh:float#99
    urbanity:float#1
    wcooking:float#13
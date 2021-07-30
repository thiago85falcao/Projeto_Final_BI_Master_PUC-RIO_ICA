"""
---------------------------------------------
# Unconfined Compressive Strength equations #
---------------------------------------------
"""

def UCS_Li_and_Albertin (lito="carb",phi=0.5):
    """[This algorithm calculates unconfined compressive strength from porosity. It is valid for all sedimentary rocks 
    although different coefficients are used for sandstone, carbonates and clay. It was published by Li and Aubertin (2003).]

    Args:
        lito (str, optional): [description]. Defaults to "carb".
        phi (float, optional): [description]. Defaults to 0.5.

    Returns:
        [type]: [UCS (MPa)]
    """

    import math
    if lito == "carb":
        UCS_0 = 155.58
        x1 = 1.21
        x2 = 13.2
        phi_0 = 0.5072

    elif lito == "sand":
        UCS_0 = 193.04
        x1 = 1.31
        x2 = 25.39
        phi_0 = 0.5194

    elif lito == "clay":
        UCS_0 = 20.12
        x1 = 1.001
        x2 = 47.645
        phi_0 = 0.8306

    phi_ration = phi / phi_0
    pi = math.pi / 2
    a = math.sin(math.radians(pi * phi_ration))**x1
    b = math.cos(math.radians(pi * phi_ration))**x2

    TS = UCS_0*(1 - a + b)

    return TS


def UCS_Plumb_A (phi=0.5):
    """
   
    """
    UCS = 357*(1-(2.8*phi))**2
    return UCS

def UCS_Chang_2006 (phi=0.5):
    """
    
    """
    UCS = 254*(1-(2.7*phi))**2
    return UCS

# %%
def UCS_Chang_2006_A (phi=0.5):
    import math
    """
   
    """
    UCS = 277*(math.exp((-10*phi)))
    return UCS
# %%
def UCS_Lashkaripour (phi=0.1):
    """
    
    """
    UCS = 1.001*phi**(-1.143)
    return UCS

def UCS_Horsrud_2001A (phi=0.5):
    """
    
    """
    UCS = 2.922*phi**(-0.96)
    return UCS

# %%
def UCS_Chang_2006B (phi=0.5):
    """
    
    """
    UCS = 0.286*phi**(-1.762)
    return UCS
# %%
def UCS_Lashkaripour_2002 (phi=0.5):
    """
  
    """
    UCS = 4.7915*phi**(-0.821)
    return UCS

def UCS_ChangEtAl_2006_I_Carbonato (phi):
    """[This algorithm calculates unconfined compressive strength from porosity. It was derived for limestones in the Middle East with low 
    to moderate porosity (between 0.05 and 0.2) and high UCS (between 30MPa and 150MPa). It was published by Chang et al. (2006).]

    Args:
        phi ([type]): [v/v]
    """
    from math import exp
    UCS = 143.8*exp(-6.95*phi)
    return UCS

def UCS_ChangEtAl_2006_J_Carbonato(phi):
    """[This algorithm calculates unconfined compressive strength from porosity. It was derived for limestones with low to moderate porosity 
    (less than 0.2) and high UCS (between 10MPa and 300MPa). It was published by Chang et al. (2006).]

    Args:
        phi ([type]): [v/v]

    Returns:
        [type]: [MPa]
    """
    from math import exp
    UCS = 135.9*exp(-4.8*phi)
    return UCS


def dt_to_V(DT):
    v = 304800/DT
    return v

def E_dyn_young_modulus(DTC,DTS,rhob):
    
    E = (rhob*((4*DTC**2) - (3*DTS**2))) / ((DTS**2)*((DTC**2)-(DTS**2)))
    return E

def E_Dynamic_MavkoEtAl2009(rhob,DTS,PR):
    """[ This algorithm calculates the dynamic Young's Modulus in GPa from a combination of dynamic Poisson's ratio, 
    S-wave sonic velocity and density. It is based on theoretical calculations and is valid for all lithologies. 
    Note that there is also an algorithm to calculate dynamic Poisson's ratio from P-wave and S-wave sonic velocity.]

    Args:
        rhob ([type]): [g/cm3]
        DTS ([type]): [us/ft]
        PR ([type]): [adimensional]

    Returns:
        [Young's Modulus E]: [MPa]
    """
    E = (2*(rhob*1000)*((304800/DTS)**2)*(1+PR))/1000000
    return E

def E_dyn_Youngs_Modulus_Vp(rhob,v,Vs):
    """[summary]

    Args:
        rhob ([type]): [g/cm3]
        v ([type]): [adimensional]
        Vs ([type]): [m/s]

    Returns:
        [type]: [GPa]
    """
    E = (2*rhob*(1+v)*(Vs**2))/1e6
    return E

def E_est_Lacy_Carbonato (Edyn):

    E = (2.61097E-9+0.422)*Edyn
    return E

def E_StaticFromDynamic_Eissa_Kazi1988(Edyn):
    """[This algorithm calculates the static Young's Modulus from the dynamic Young's Modulus.
    It is based on data from a wide range of lithologies, and was published by Eissa & Kazi (1988).]

    Args:
        Edyn ([type]): [GPa]

    Returns:
        [type]: [description]
    """

    E = (0.74*Edyn)-0.82
    return E


 
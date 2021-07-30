def v_Dynamic_MavkoEtAl2009(DTC,DTS):
    poisson = 0.5*(((DTS/DTC)**2)-2)/((((DTS/DTC)**2)-1))
    return poisson

def v_Dynamic_VpVs(Vp,Vs):
    poisson = 1-(1/(2-(2*(Vs/Vp)**2)))
    return poisson

def v_dyn(DTC,DTS):
    """[Calculate Dynamic Poisson Ratio from DT]

    Args:
        DTC ([type]): [us/ft]
        DTS ([type]): [us/ft]

    Returns:
        [Poisson's Ratio]: [adimensional]
    """
    poisson= ((2 * (DTC**2)) - (DTS**2))/(2*((DTC**2)-(DTS**2)))
    return poisson



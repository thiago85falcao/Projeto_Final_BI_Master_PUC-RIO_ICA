#!/usr/bin/python
# -*- coding: latin-1 -*-
"""
#################################################
                Rock_Mec_Facies   
-------------------------------------------------
Module to develop Structural Geology and 
Geomechanical studies based on Rock Mechanical
behavior utilizing borehole log data.
-------------------------------------------------
Developed initially as Final Project of BI-Master
course from ICA - PUC-RJ.
Author: Thiago Falcao
Supervisor: Prof. Leonardo Mendonza

### Parameters table

|             Parameter             |                     Abbeviation                    |    Units   |
|:---------------------------------:|:--------------------------------------------------:|:----------:|
|              Porosity             |                       $\phi$                       |  fraction  |
|               VClay               |                         VCl                        |  fraction  |
|               VGrain              |                 VGr = 1-VCl-$\phi$                 |  fraction  |
|          Sonic   Velocity         |          Vp = 3048x10$^{5}$ / $\Delta t$           |     m/s    |
|       Shear Wave   Velocity       |                         Vs                         |     m/s    |
|      Internal   Transit time      |         $\Delta t =   3048*10^5 / Vp $             | $/me s/ft$ |
|              Density              |                       $\rho$                       | kg/m$^{3}$ |
|    Effective   vertical stress    |                    $ \sigma v'$                    |     MPa    |
|         Tensile   Strength        |                         TS                         |     MPa    |
| Unconfined   Compressive Strength |                         UCS                        |     MPa    |
|       Friction   Coefficient      |              $\mu = 1 -   \tan\varphi$             |      -     |
|          Friction   Angle         | $\varphi = \tan^{-1}   \mu \mid \mu=2\theta - 90°$ |   degrees  |
|        Angle of   Failuire        |            $theta = 45 +   (\varphi/2)$            |   degrees  |
|              Cohesion             |                          C                         |     MPa    |
|       Crack Surface   Energy      |                         Gc                         |  J/m$^{2}$ |
|         Young's   Modulus         |                          E                         |     GPa    |
|         Poisson's   Ratio         |                        $\nu$                       |      -     |
|             Ductility             |                          D                         |      -     |
|     Overconsolidation   Ratio     |                         OCR                        |      -     |
|                                   |                                                    |            |

"""
__all__ = [
    "get_data",
    "calc_mec_prop",
    "rock_class"
    ]
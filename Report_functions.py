from utils.common.is800_2007 import *
from pylatex import Math
from pylatex.utils import NoEscape


def cl_3_7_2_section_classification(class_of_section=None):
    """
    Find class of the section
    Args:
         class_of_section:
    Returns:
    Note:
        Reference:
        [Ref: Table 2, cl. 3.7.2 and 3.7.4 IS 800:2007]

    """

    section_classification_eqn = Math(inline=True)
    if class_of_section == int(1):
        section_classification_eqn.append(NoEscape( r'\begin{aligned} &Plastic \\'))
        section_classification_eqn.append(NoEscape(r' &[Ref: Table ~2, Cl. 3.7.2~ and ~3.7.4 ~IS~ 800:2007]\end{aligned}'))
    elif class_of_section == int(2):
        section_classification_eqn.append(NoEscape( r'\begin{aligned} &Compact \\'))
        section_classification_eqn.append(NoEscape(r' &[Ref: Table ~2, Cl. 3.7.2 ~and ~3.7.4 ~IS ~800:2007]\end{aligned}'))
    else:
        section_classification_eqn.append(NoEscape( r'\begin{aligned} &Semi-Compact \\'))
        section_classification_eqn.append(NoEscape(r' &[Ref: Table ~2, Cl. 3.7.2 ~and~ 3.7.4 ~IS ~800:2007]\end{aligned}'))
    return section_classification_eqn


def cl_5_4_1_table_4_5_gamma_value(v, t):
    """
    Calculate gamma value

    Args:
        v:value of the gamma (float)
        t:subscript (str)
    Returns:
        gamma value
    """

    v = str(v)
    gamma = Math(inline=True)
    gamma.append(NoEscape(r'\begin{aligned}\gamma_{' + t + '}&=' + v + r'\end{aligned}'))

    return gamma


def cl_6_1_tension_capacity_member(T_dg, T_dn=0.0, T_db =0.0):
    """
    Calculate Design strength of member
    Args:
         T_dg:Yeiding capacity of member
         T_dn: Rupture capacity of member
         T_db: Block shear capacity of member
    Returns:
          Design strength of member min of( Yeiding ,Rupture  and Block shear capacity)
    Note:
            Reference:
            IS 800:2007,  cl 6.1

    """

    tension_capacity_eqn = Math(inline=True)
    if T_db != 0.0 and T_dn!=0.0:
        T_d = min(T_dg,T_dn,T_db)
        T_d = str(T_d)
        T_dg = str(T_dg)
        T_dn = str(T_dn)
        T_db = str(T_db)
        tension_capacity_eqn.append(NoEscape(r'\begin{aligned} T_d &= min(T_{dg},T_{dn},T_{db})\\'))
        tension_capacity_eqn.append(NoEscape(r'&= min(' + T_dg + ',' + T_dn + ',' + T_db + r')\\'))
    elif T_db == 0.0 and T_dn!=0.0:
        T_d = min(T_dg, T_dn)
        T_dg = str(T_dg)
        T_dn = str(T_dn)
        T_d = str(T_d)
        tension_capacity_eqn.append(NoEscape(r'\begin{aligned} T_d &= min(T_{dg},T_{dn})\\'))
        tension_capacity_eqn.append(NoEscape(r'&= min(' + T_dg + ',' + T_dn + r')\\'))
    elif T_db != 0.0 and T_dn == 0.0:
        T_d = min(T_dg, T_db)
        T_d = str(T_d)
        T_dg = str(T_dg)
        T_db = str(T_db)
        tension_capacity_eqn.append(NoEscape(r'\begin{aligned} T_d &= min(T_{dg},T_{db})\\'))
        tension_capacity_eqn.append(NoEscape(r'&= min(' + T_dg + ',' + T_db + r')\\'))
    else:
        T_d = T_dg
        # T_dg = str(T_dg)
        T_d = str(T_d)
        tension_capacity_eqn.append(NoEscape(r'\begin{aligned} T_d &= T_{dg}\\'))
        # tension_capacity_eqn.append(NoEscape(r'&= min(' + T_dg + ',' + T_dn + r')\\'))
    tension_capacity_eqn.append(NoEscape(r'&='+ T_d + r'\\'))
    tension_capacity_eqn.append(NoEscape(r'[Ref&.~IS~800:2007,~Cl.~6.1]\end{aligned}'))

    return tension_capacity_eqn


def cl_6_2_tension_yield_capacity_member(l, t, f_y, gamma, T_dg, multiple =None,area=None):
    """
    Calculate tension yielding capacity of provided plate under axial tension
    Args:
        l: Height of  provided plate in mm (float)
        t: Thickness of  provided plate in mm (float)
        f_y:Yield stress of material in N/mm square (float)
        gamma:Partial safety factor for failure in the tension by yielding (float)
        T_dg: Tension yieldung capacity of provided plate under axial tension in N (float)
        multiple:1  (int)
    Returns:
          Tension yieldung capacity of provided plate under axial tension

    Note:
            Reference:
            IS 800:2007,  cl 6.2


    """
    if l is not None and t is not None:
        area = str(round(l * t, 2))
        l = str(l)
        t = str(t)
    else:
        area = str(area)
    f_y = str(f_y)
    gamma = str(gamma)
    T_dg = str(T_dg)
    tension_yield_eqn = Math(inline=True)
    tension_yield_eqn.append(NoEscape(r'\begin{aligned} T_{dg} &= \frac{A_gf_y}{\gamma_{mo}}\\'))
    if l is not None and t is not None:
        if multiple is None or multiple == 1:
            tension_yield_eqn.append(NoEscape(r'A_{g} &= l \times t ='+l+r'\times'+t+r'\\'))
        else:
            multiple = str(multiple)
            tension_yield_eqn.append(NoEscape(r'A_{g} &='+multiple+r' l \times t =' +multiple+
                                              r'\times'+ l + r'\times' + t + r'\\'))

    tension_yield_eqn.append(NoEscape(r'&=\frac{'+area+r'\times'+f_y+'}{'+ gamma+r'\times 10^3}\\'))
    tension_yield_eqn.append(NoEscape(r'&=' + T_dg +r'\\'))
    tension_yield_eqn.append(NoEscape(r'[Ref.&~IS~800:2007,~Cl.~6.2]\end{aligned}'))
    return tension_yield_eqn


def cl_6_3_tension_rupture_capacity_member(w_p, t_p, n_c, d_o, fu, gamma_m1, T_dn, multiple=1):
    """
    Calculate design in tension as governed by rupture of net
         cross-sectional area in case of bolted connection
    Args:
         w_p: Width of given section in mm (float)
         t_p: Thikness of given section in mm (float)
         n_c: No. of bolt holes in critical section (int)
         d_o: Diameter of bolt hole in mm (int)
         fu: Ultimate stress of material in N/mm square (float)
         gamma_m1:Partial safety factor for failure at ultimate stress  (float)
         T_dn: Rupture strength of net cross-sectional area in N (float)
         multiple: 1
    Returns:
         design in tension as governed by rupture of net cross-sectional area
    Note:
            Reference:
            IS 800:2007,  cl 6.3

    """

    w_p = str(w_p)
    t_p = str(t_p)
    n_c = str(n_c)
    d_o = str(d_o)
    f_u = str(fu)
    T_dn = str(T_dn)
    gamma_m1 = str(gamma_m1)
    multiple = str(multiple)
    Tensile_rup_eqnb = Math(inline=True)

    Tensile_rup_eqnb.append(NoEscape(r'\begin{aligned} T_{dn} &= \frac{0.9 A_{n}f_u}{\gamma_{m1}}\\'))
    Tensile_rup_eqnb.append(NoEscape(r'&=\frac{'+multiple+r'\times ~0.9\times ('+ w_p + '-' + n_c +r'\times'+ d_o + r')\times' + t_p + r'\times' + f_u + r'}{' + gamma_m1 + r'}\\'))
    Tensile_rup_eqnb.append(NoEscape(r'&=' + T_dn + r'\\'))
    Tensile_rup_eqnb.append(NoEscape(r'[Ref&.~IS~800:2007,~Cl.~6.3]\end{aligned}'))


    return Tensile_rup_eqnb


#TODO:Darshan is it possible to follow same format (as above equation) for all tension rupture equations? Ans: No
def member_rupture_prov(A_nc, A_go, F_u, F_y, L_c, w, b_s, t,gamma_m0,gamma_m1,beta,member_rup,multiple = 1):
    """
    Calculate design strength due to rupture of critical section
    Args:
          A_nc:Net area of connected leg in mm square (float)
          A_go:Gross area of outstanding leg in mm square (float)
          F_u:Ultimate stress of the material in N/mm square (float)
          F_y:Yield stess of the material in mm N/square (float)
          L_c:Length of the end connection in mm  (float)
          w:Outstanding leg width in mm  (float)
          b_s:Shear lag width in mm  (float)
          t:thickness of the leg in mm  (float)
          gamma_m0:partial safety factor for failure in tension by yeilding (float)
          gamma_m1:partial safety factor for failure at ultimate stress (float)
          beta:as per section 6.3.3 (float)
          member_rup:design strength due to rupture of critical section (float)
          multiple:1
    Returns:
           design strength due to rupture of critical section
    Note:
              Reference:
              IS 800:2007,  cl 6.3


    """
    w = str(w)
    t = str(t)
    fy = str(F_y)
    fu = str(F_u)
    b_s = str(b_s)
    L_c = str(L_c)
    A_nc = str(A_nc)
    A_go = str(A_go)
    gamma_m0 = str(gamma_m0)
    gamma_m1 = str(gamma_m1)
    beta = str(round(beta,2))
    member_rup = str(member_rup)
    multiple = str(multiple)
    member_rup_eqn = Math(inline=True)
    member_rup_eqn.append(NoEscape(r'\begin{aligned}\beta &= 1.4 - 0.076 \times \frac{w}{t}\times \frac{f_{y}}{0.9 f_{u}}\times\frac{b_s}{L_c}\\'))
    member_rup_eqn.append(NoEscape(r'&\leq\frac{0.9~f_{u}~\gamma_{m0}}{f_{y}~\gamma_{m1}} \geq 0.7 \\'))
    member_rup_eqn.append(NoEscape(r'&= 1.4 - 0.076 \times \frac{'+ w +'}{'+ t + r'}\times \frac{'+ fy +r'}{0.9\times'+ fu + r'}\times\frac{'+ b_s +'}{' + L_c + r' }\\'))
    member_rup_eqn.append(NoEscape(r'&\leq\frac{0.9'+ fu +r'\times'+ gamma_m0 +'}{' +fy+r'\times'+gamma_m1 + r'} \geq 0.7 \\'))
    member_rup_eqn.append(NoEscape(r'&= '+ beta + r'\\'))
    member_rup_eqn.append(NoEscape(r'T_{dn} &= '+multiple+r'\times (\frac{0.9 A_{nc}f_{u}}{\gamma_{m1}} + \frac{\beta A_{go} f_{y}}{\gamma_{m0}})\\'))
    member_rup_eqn.append(NoEscape(r'&= '+multiple+ r'\times(\frac{0.9\times'+ A_nc +r'\times' + fu + '}{'+ gamma_m1 + r'} + \frac{' + beta +r'\times' + A_go +r'\times' + fy + '}{' + gamma_m0 + r'})\\'))
    member_rup_eqn.append(NoEscape(r'&= '+ member_rup + r'\\'))
    member_rup_eqn.append(NoEscape(r'[Ref.&~IS~800:2007,~Cl.~6.3]\end{aligned}'))
    return member_rup_eqn


def cl_6_4_blockshear_capacity_member(Tdb, A_vg = None, A_vn = None, A_tg = None, A_tn = None, f_u = None, f_y = None, gamma_m0 = None, gamma_m1 = None, stress=None):
    """
    Calculate block shear strength of the plate or member

    Args:

        Tdb:block shear strength of the plate or member in N (float)
        A_vg:gross area of plate attached to web in shear along bolt line parallel to y axis in mm square (float)
        A_vn:net area of web cover plate attached to web in shear along bolt line parallel to y axis in mm square (float)
        A_tg:minimum gross area in tension along bolt line parallel to x-axis in mm square (float)
        A_tn:minimum net area in tension along bolt line perpendicular to shear load in mm square (float)
        f_u:ultimate stress of material in N/mm square (float)
        f_y:yield stress of material in N/mm square (float)
        gamma_m0:partial safety factor for failure in tension by yielding (float)
        gamma_m1:partial safety factor for failure at ultimate stress (float)
    Returns:
        block shear strength of the plate or member
    Note:
              Reference:
              IS 800:2007,  cl 6.4

    """

    Tdb = str(Tdb)
    A_vg = str(A_vg)
    A_vn = str(A_vn)
    A_tg = str(A_tg)
    A_tn = str(A_tn)
    f_y = str(f_y)
    f_u = str(f_u)
    gamma_m1 = str(gamma_m1)
    gamma_m0 = str(gamma_m0)

    member_block_eqn = Math(inline=True)


    if stress == "shear":
        member_block_eqn.append(NoEscape(r'\begin{aligned}V_{dbl1} &= \frac{A_{vg} f_{y}}{\sqrt{3} \gamma_{m0}} + \frac{0.9 A_{tn} f_{u}}{\gamma_{m1}}\\'))
        member_block_eqn.append(NoEscape(r'V_{dbl2} &= \frac{0.9A_{vn} f_{u}}{\sqrt{3} \gamma_{m1}} + \frac{A_{tg} f_{y}}{\gamma_{m0}}\\'))
        member_block_eqn.append(NoEscape(r'V_{db} &= min(V_{db1}, V_{db2})= ' + Tdb +  r'\\'))
        member_block_eqn.append(NoEscape(r'[Ref&.~IS~800:2007,~Cl.~6.4]\end{aligned}'))
    else:
        member_block_eqn.append(NoEscape(r'\begin{aligned}T_{dbl1} &= \frac{A_{vg} f_{y}}{\sqrt{3} \gamma_{m0}} + \frac{0.9 A_{tn} f_{u}}{\gamma_{m1}}\\'))
        member_block_eqn.append(NoEscape(r'T_{dbl2} &= \frac{0.9A_{vn} f_{u}}{\sqrt{3} \gamma_{m1}} + \frac{A_{tg} f_{y}}{\gamma_{m0}}\\'))
        member_block_eqn.append(NoEscape(r'T_{db} &= min(T_{db1}, T_{db2})= ' + Tdb + r'\\'))
        member_block_eqn.append(NoEscape(r'[Ref&.~IS~800:2007,~Cl.~6.4]\end{aligned}'))

    return member_block_eqn


# TODO:DARSHAN I don't think this is required Ans: It's required
def slenderness_req():
    """
    :return:
    """

    slenderlimit_eqn = Math(inline=True)
    slenderlimit_eqn.append(NoEscape(r'\begin{aligned}\frac{K L}{r} &\leq 400\end{aligned}'))

    return slenderlimit_eqn

def cl_7_1_2_effective_slenderness_ratio(K, L, r, slender):
    """
    Calculate effective selenderness ratio

    Args:

         K:Constant according to the end condition (float)
         L:Actual length of the section in mm (float)
         r:Radius of gyration  in mm (float)
         slender:  effective selenderness ratio (float)
    Returns:
        effective selenderness ratio
    Note:
              Reference:
              IS 800:2007,  cl 7.1.2

    """
    K = str(K)
    L = str(L)
    r = str(r)
    slender = str(slender)

    slender_eqn = Math(inline=True)
    slender_eqn.append(NoEscape(r'\begin{aligned}\frac{K L}{r} &= \frac{'+K+ r'\times'+L+'}{'+r+ r'}\\'))
    slender_eqn.append(NoEscape(r'&= ' + slender + r'\\'))
    slender_eqn.append(NoEscape(r'[Ref.~IS~&800:2007,~Cl.~7.1.2]\end{aligned}'))
    return slender_eqn


def cl_8_2_moment_capacity_member (Pmc, Mdc, M_c):
    """
    Calculate moment capacity of the section
    Args:
         Pmc:Plastic moment capacity of the member in  N-mm (float)
         Mdc:Moment deformation capacity of the member in  N-mm (float)
         M_c: Moment capacity of the section in  N-mm (float)
    Returns:
         moment capacity of the section
    Note:
              Reference:
              IS 800:2007,  cl 8.2


    """
    Pmc = str(Pmc)
    Mdc =str(Mdc)
    M_c = str (M_c)
    M_c_eqn = Math(inline=True)
    M_c_eqn.append(NoEscape(r'\begin{aligned} M_c &= min(Pmc,Mdc)\\'))
    M_c_eqn.append(NoEscape(r'&=min('+Pmc+','+Mdc+ r')\\'))
    M_c_eqn.append(NoEscape(r'&=' + M_c + r'\\'))
    M_c_eqn.append(NoEscape(r'[Re&f.~IS~800:2007,~Cl.~8.2]\end{aligned}'))
    return M_c_eqn


def cl_8_2_1_2_plastic_moment_capacity_member(beta_b, Z_p, f_y, gamma_m0, Pmc):  # same as #todo anjali
    """
    Calculate member design moment capacity
    Args:

          beta_b:1 for plastic and compact sections & Ze/Zp for semi compact section (int)
          Z_p:Plastic section modulus of cross section mm^3 (float)
          f_y:Yield stress of the material in N/mm square  (float)
          gamma_m0:partial safety factor (float)
          Pmc:Plastic moment capacity in  N-mm (float)
    Returns:
        Plastic moment capacity in  N-mm (float)

    Note:
              Reference:
              IS 800:2007,  cl 8.2.1.2

    """

    beta_b = str(beta_b)
    Z_p = str(Z_p)
    f_y = str(f_y)
    gamma_m0 =str(gamma_m0 )
    Pmc = str(Pmc)
    Pmc_eqn = Math(inline=True)
    Pmc_eqn.append(NoEscape(r'\begin{aligned} Pmc &= \frac{\beta_b \times Z_p \times fy}{\gamma_{mo} \times 10^6}\\'))
    Pmc_eqn.append(NoEscape(r'&=\frac{' + beta_b + r'\times' +Z_p + r'\times' + f_y + r'}{' + gamma_m0 + r' \times 10^6}\\'))
    Pmc_eqn.append(NoEscape(r'&=' + Pmc + r'\\'))
    Pmc_eqn.append(NoEscape(r'[Ref&.~IS~800:2007,~Cl.~8.2.1.2]\end{aligned}'))


    return Pmc_eqn


def cl_8_2_1_2_deformation_moment_capacity_member(fy, Z_e, Mdc):
    """
    Calculate moment deformation capacity
    Args:
         fy:Yield stress of the material in  N/mm square (float)
         Z_e:Elastic section modulus of cross section in  mm^3 (float)
         Mdc:Moment deformation capacity in  N-mm (float)
    Note:
              Reference:
              IS 800:2007,  cl 8.2.1.2
    Returns:
         moment deformation capacity
    """
    fy = str(fy)
    Z_e = str(Z_e)
    Mdc =str(Mdc)
    Mdc_eqn= Math(inline=True)
    Mdc_eqn.append(NoEscape(r'\begin{aligned} Mdc &= \frac{1.5 \times Z_e \times fy}{1.1 \times 10^6}\\'))
    Mdc_eqn.append(NoEscape(r'&= \frac{1.5 \times'+Z_e +r'\times' +fy +r'}{1.1\times 10^6}\\'))
    Mdc_eqn.append(NoEscape(r'&= ' + Mdc+ r'\\'))
    Mdc_eqn.append(NoEscape(r'[Ref.&~IS~800:2007,~Cl.~8.2.1.2]\end{aligned}'))
    return  Mdc_eqn


def cl_8_4_shear_capacity_member(V_dy, V_dn, V_db = 0.0):
    """
    Calculate shear capacity of member

    Args:
        V_dy: yielding capacity of plate
        V_dn: rupture capacity of plate
        V_db: block shear capacity of plate
    Returns:
         shear capacity of member
    Note:
              Reference:
              IS 800:2007,  cl 6.1

    """
    shear_capacity_eqn = Math(inline=True)
    if V_db != 0.0 and V_dn !=0.0:
        V_d = min(V_dy,V_dn,V_db)
        V_d = str(V_d)
        V_dy = str(V_dy)
        V_dn = str(V_dn)
        V_db = str(V_db)

        shear_capacity_eqn.append(NoEscape(r'\begin{aligned} V_d &= min(S_c,V_{dn},V_{db})\\'))
        shear_capacity_eqn.append(NoEscape(r'&= min('+V_dy+','+V_dn+','+V_db+r')\\'))

    elif V_db == 0.0 and V_dn == 0.0:
        V_d = V_dy
        V_d = str(V_d)
        V_dy = str(V_dy)
        shear_capacity_eqn.append(NoEscape(r'\begin{aligned} V_d &= S_c\\'))
        # shear_capacity_eqn.append(NoEscape(r'&=' + V_dy + r'\\'))

    elif V_db == 0.0 and V_dn != 0.0:
        V_d = min(V_dy, V_dn)
        V_d = str(V_d)
        V_dy = str(V_dy)
        V_dn = str(V_dn)
        shear_capacity_eqn.append(NoEscape(r'\begin{aligned} V_d &= min(S_c,V_{dn})\\'))
        shear_capacity_eqn.append(NoEscape(r'&= min(' + V_dy + ',' + V_dn + r')\\'))
    elif V_db != 0.0 and V_dn == 0.0:
        V_d = min(V_dy, V_db)
        V_d = str(V_d)
        V_dy = str(V_dy)
        V_db = str(V_db)
        shear_capacity_eqn.append(NoEscape(r'\begin{aligned} V_d &= min(S_c,V_{db})\\'))
        shear_capacity_eqn.append(NoEscape(r'&= min(' + V_dy + ',' + V_db + r')\\'))

    shear_capacity_eqn.append(NoEscape(r'&='+V_d + r'\\'))
    shear_capacity_eqn.append(NoEscape(r'[Ref&.~IS~800:2007,~Cl.~6.1]\end{aligned}'))

    return shear_capacity_eqn


def cl_8_4_shear_yielding_capacity_member(h, t, f_y, gamma_m0, V_dg, multiple=1):
    """
    Calculate shear yielding capacity of  plate (provided)
    Args:
        h:  Plate ht in mm (float)
        t:  Plate thickness in mm (float)
        f_y:Yeild strength of  plate material in N/mm square (float)
        gamma: IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']  (float)
        V_dg: Shear yeilding capacity of  plate in N (float)
        multiple:2 (int)
    Returns:
         Shear yielding capacity of  plate
     Note:
            Reference:
            IS 800:2007,  cl 10.4.3
    """

    h = str(h)
    t = str(t)
    f_y = str(f_y)
    gamma_m0 = str(gamma_m0)

    V_dg = str(V_dg)


    shear_yield_eqn = Math(inline=True)
    shear_yield_eqn.append(NoEscape(r'\begin{aligned} V_{dy} &= \frac{A_v~f_y}{\sqrt{3}~\gamma_{mo}}\\'))
    if multiple == 1:
        shear_yield_eqn.append(NoEscape(r'&=\frac{'+h+r'\times'+t+r'\times'+f_y+r'}{\sqrt{3} \times'+gamma_m0+r'}\\'))
    else:
        multiple = str(multiple)
        shear_yield_eqn.append(
            NoEscape(r'&=\frac{' + multiple + r'\times' + h + r'\times' + t + r'\times' + f_y + r'}{\sqrt{3} \times' + gamma_m0 + r'}\\'))
    shear_yield_eqn.append(NoEscape(r'&=' + V_dg + r'\\'))
    shear_yield_eqn.append(NoEscape(r'[Ref.&IS ~800:2007,Cl. 10.4.3]\end{aligned}'))
    return shear_yield_eqn


def AISC_J4_shear_rupture_capacity_member(h, t, n_r, d_o, fu, v_dn, gamma_m1=1.25,multiple =1):
    """
     Calculate shear rupture capacity of  plate (provided)
     Args:
          h: Height of  plate in mm (float)
          t:Thickness of  plate in mm (float)
          n_r:No of bolts provided in one line (float)
          d_o:Nominal diameter of bolt provide in plate in mm (float)
          fu: Ultimate strength of  plate material in N/mm square (float)
          v_dn: Shear rupture of plate in KN (float)
          gamma_m1: material factor of safety at ultimate load
          multiple: 1 (int)
    Returns:
          shear rupture capacity of  plate
    Note:
        Reference:
                    AISC  Sect.J4
    """
    h = str(h)
    t = str(t)
    n_r = str(n_r)
    d_o = str(d_o)
    f_u = str(fu)
    v_dn = str(v_dn)
    gamma_m1 = str(gamma_m1)
    multiple = str(multiple)
    shear_rup_eqn = Math(inline=True)
    shear_rup_eqn.append(NoEscape(r'\begin{aligned} V_{dn} &= \frac{0.75~A_{vn}~f_u}{\sqrt{3}~\gamma_{m1}}\\'))
    if multiple == 1:
        shear_rup_eqn.append(NoEscape(
            r'&=' + r'\times \frac{(' + h + '-(' + n_r + r'\times' + d_o + r'))\times' + t + r'\times' + f_u + r'}{\sqrt{3}\times' + gamma_m1 + r'}\\'))
    else:
        shear_rup_eqn.append(NoEscape(r'&='+multiple+ r'\times \frac{('+h+'-('+n_r+r'\times'+d_o+r'))\times'+t+r'\times'+f_u+r'}{\sqrt{3}\times' +gamma_m1+ r'}\\'))
    shear_rup_eqn.append(NoEscape(r'&=' + v_dn + r'\\'))
    shear_rup_eqn.append(NoEscape(r' [Ref.& AISC~~Sect.J4] \end{aligned}'))

    return shear_rup_eqn


def cl_9_3_combined_moment_axial_IR_section(M, M_d, N, N_d, IR, type=None):

    """
    Calculate
    Args:
         M: Moment acting on section in KN-mm (float)
         M_d:Moment capacity of the section in KN-mm (float)
         N: Axial force acting on section in KN (float)
         N_d:Tension capacity of the plate in KN (float)
         IR: Interaction ratio for combined moment and axial load (no units)
    Returns:
        mom_axial_IR_eqn: Equation to calculate IR
    Note:
            Reference:
            IS 800:2007,  cl 9.3


    """
    M = str(M)
    M_d = str(M_d)
    N = str(N)
    N_d = str(N_d)
    IR = str(IR)
    mom_axial_IR_eqn = Math(inline=True)

    if type == None:
        mom_axial_IR_eqn.append(NoEscape(r'\begin{aligned} &\frac{'+M+'}{'+M_d+r'}+\frac{'+N+'}{'+N_d+'}='+IR+r'\\'))
        mom_axial_IR_eqn.append(NoEscape(r'&[Ref.~IS~800:2007,~Cl.~10.7]\end{aligned}'))
    elif type == 'squared':
        mom_axial_IR_eqn.append(NoEscape(r'\begin{aligned} &(\frac{' + M + '}{' + M_d + r'})^2+(\frac{' + N + '}{' + N_d + '})^2=' + IR +r'\\'))
        mom_axial_IR_eqn.append(NoEscape(r'&[Ref.~IS~800:2007,~Cl.~10.7]\end{aligned}'))
    return mom_axial_IR_eqn


def cl_10_2_2_min_spacing(d, parameter='pitch'):#Todo:write condition for pitch and gauge

    """
    Calculate the min pitch distance
    Args:
      d:Diameter of provided bolt in mm (float)
    Returns:
       Minimum pitch distance in mm (float)
    Note:
        Reference:
        IS 800:2007,  cl. 10.2.2

    """
    min_pitch = 2.5*d
    d = str(d)
    min_pitch = str(min_pitch)

    min_pitch_eqn = Math(inline=True)

    if parameter == 'pitch':
        min_pitch_eqn.append(NoEscape(r'\begin{aligned}p_{min}&= 2.5 ~ d\\'))
    elif parameter == 'gauge':
        min_pitch_eqn.append(NoEscape(r'\begin{aligned} g_{min}&= 2.5 ~ d\\'))
    else:
        min_pitch_eqn.append(NoEscape(r'\begin{aligned} p/g_{min}&= 2.5 ~ d\\'))
    min_pitch_eqn.append(NoEscape(r'&=2.5 \times' + d + r'\\&=' + min_pitch + r'\\'))
    min_pitch_eqn.append(NoEscape(r'[Ref~I&S~800:2007,~Cl.~10.2.2]\end{aligned}'))

    return min_pitch_eqn


def cl_10_2_3_1_max_spacing(t,parameter=None):#TODO:write condition for pitch and gauge
    """
     Calculate the maximum pitch distance
     Args:
         t: Thickness of thinner plate in mm (float)
     Returns:
           Max pitch in mm (float)
     Note:
            Reference:
            IS 800:2007,  cl. 10.2.3
    """
    t1 = str(t[0])
    t2 = str(t[1])
    max_pitch_1 = 32*min(t)
    max_pitch_2 = 300
    max_pitch = min(max_pitch_1,max_pitch_2)
    t = str(min(t))
    max_pitch = str(max_pitch)
    max_pitch_eqn = Math(inline=True)
    if parameter=='pitch':
        max_pitch_eqn.append(NoEscape(r'\begin{aligned}p_{max}&=\min(32~t,~300~mm)\\'))
    elif parameter == 'gauge':
        max_pitch_eqn.append(NoEscape(r'\begin{aligned}g_{max}&=\min(32~t,~300~mm)\\'))
    else:
        max_pitch_eqn.append(NoEscape(r'\begin{aligned}p/g_{max}&=\min(32~t,~300~mm)\\'))

    max_pitch_eqn.append(NoEscape(r'&=\min(32~' + t+ r',~ 300 ~mm)\\&='+max_pitch+r'\\'))
    max_pitch_eqn.append(NoEscape(r'Where,~t &= min('+t1+','+t2+r')\\'))
    max_pitch_eqn.append(NoEscape(r'[Ref.~IS~&800:2007,~Cl.~10.2.3]\end{aligned}'))

    return max_pitch_eqn


def cl_10_2_4_2_min_edge_end_dist(d_0,edge_type='Sheared or hand flame cut', parameter='end_dist'):
    """
    Calculate minimum end and edge distance
    Args:
         d - Nominal diameter of fastener in mm (float)
         bolt_hole_type - Either 'Standard', 'Over-sized', 'Short Slot' or 'Long Slot' (str)
         edge_type - Either 'hand_flame_cut' or 'machine_flame_cut' (str)
         parameter - edge or end distance required to return the specific equation (str)
    Returns:
            Equation for minimum end and edge distance from the centre of any hole to the nearest edge of a plate in mm (float)
    Note:
        Reference:
        IS 800:2007, cl. 10.2.4.2
    """
    if edge_type == 'Sheared or hand flame cut':
        end_edge_multiplier = 1.7
    else:
        # TODO : bolt_hole_type == 'machine_flame_cut' is given in else
        end_edge_multiplier = 1.5

    min_end_edge_dist = round(end_edge_multiplier * d_0,2)

    d_0 = str(d_0)
    end_edge_multiplier = str(end_edge_multiplier)
    min_end_edge_dist = str(min_end_edge_dist)

    end_edge_eqn = Math(inline=True)
    if parameter == 'end_dist':
        end_edge_eqn.append(NoEscape(r'\begin{aligned}e_{min} &= ' + end_edge_multiplier + r'~d_0 \\'))
    elif parameter == 'edge_dist':
        end_edge_eqn.append(NoEscape(r'\begin{aligned}e`_{min} &= ' + end_edge_multiplier + r'~d_0 \\'))
    else:
        end_edge_eqn.append(NoEscape(r'\begin{aligned}e/e`_{min} &= ' + end_edge_multiplier + r'~d_0 \\'))

    end_edge_eqn.append(NoEscape(r'&= ' + end_edge_multiplier + r'\times' + d_0 + r'\\'))
    end_edge_eqn.append(NoEscape(r'&=' + min_end_edge_dist + r'\\'))
    end_edge_eqn.append(NoEscape(r'[Ref.~IS~&800:2007,~Cl.~10.2.4.2]\end{aligned}'))
    return end_edge_eqn


def cl_10_2_4_3_max_edge_end_dist(t_fu_fy, corrosive_influences=False, parameter='end_dist'):
    """
    Calculate maximum end and edge distance(new)
     Args:

         t_fu_fy: Thickness of thinner plate in mm (float)
         corrosive_influences: Whether the members are exposed to corrosive influences or not (Boolean)

    Returns:
         Maximum edge distance to the nearest line of fasteners from an edge of any un-stiffened part in mm (float)

    Note:
            Reference:
            IS 800:2007, cl. 10.2.4.3
    """
    t_epsilon_considered = t_fu_fy[0][0] * math.sqrt(250 / float(t_fu_fy[0][2]))
    t_considered = t_fu_fy[0][0]
    t_min = t_considered
    for i in t_fu_fy:
        t = i[0]
        f_y = i[2]
        epsilon = math.sqrt(250 / f_y)
        if t * epsilon <= t_epsilon_considered:
            t_epsilon_considered = t * epsilon
            t_considered = t
        if t < t_min:
            t_min = t

    if corrosive_influences is True:
        max_edge_dist =  round(40.0 + 4 * t_min,2)
    else:
        max_edge_dist = round(12 * t_epsilon_considered,2)

    max_edge_dist = str(max_edge_dist)
    t1=str(t_fu_fy[0][0])
    t2=str(t_fu_fy[1][0])
    fy1 = str(t_fu_fy[0][2])
    fy2 = str(t_fu_fy[1][2])
    max_end_edge_eqn = Math(inline=True)
    if corrosive_influences is False:
        if parameter == 'end_dist':
            max_end_edge_eqn.append(NoEscape(r'\begin{aligned}e_{max} &= 12~ t~ \varepsilon&\\'))
        else: #'edge_dist'
            max_end_edge_eqn.append(NoEscape(r'\begin{aligned}e`_{max} &= 12~ t~ \varepsilon&\\'))
        max_end_edge_eqn.append(NoEscape(r'\varepsilon &= \sqrt{\frac{250}{f_y}}\\'))
        max_end_edge_eqn.append(NoEscape(r'e1 &= 12 \times ' + t1 + r'\times \sqrt{\frac{250}{' + fy1 + r'}}\\'))
        max_end_edge_eqn.append(NoEscape(r'e2 &= 12 \times' + t2 + r'\times\sqrt{\frac{250}{' + fy2 + r'}}\\'))
        if parameter == 'end_dist':
            max_end_edge_eqn.append(NoEscape(r'e_{max}&=min(e1,e2)\\'))
        else: #'edge_dist'
            max_end_edge_eqn.append(NoEscape(r'e`_{max}&=min(e1,e2)\\'))
        max_end_edge_eqn.append(NoEscape(r' &=' + max_edge_dist + r'\\'))
        max_end_edge_eqn.append(NoEscape(r'[Ref.~IS&~800:2007,~Cl.~10.2.4.3]\end{aligned}'))

    else:
        if parameter == 'end_dist':
            max_end_edge_eqn.append(NoEscape(r'\begin{aligned}e_{max}&=40 + 4t\\'))
        else: #'edge_dist'
            max_end_edge_eqn.append(NoEscape(r'\begin{aligned}e`_{max}&=40 + 4t\\'))
        max_end_edge_eqn.append(NoEscape(r'Where, t&= min(' + t1 +','+t2+r')\\'))
        if parameter == 'end_dist':
            max_end_edge_eqn.append(NoEscape(r'e_{max}&='+max_edge_dist+r'\\'))
        else: #'edge_dist'
            max_end_edge_eqn.append(NoEscape(r'e`_{max}&='+max_edge_dist+r'\\'))
        max_end_edge_eqn.append(NoEscape(r'[Ref.~IS&~800:2007,~Cl.~10.2.4.3]\end{aligned}'))


    return max_end_edge_eqn


def cl_10_3_2_bolt_capacity(bolt_shear_capacity, bolt_bearing_capacity, bolt_capacity):
    """
    Calculate bolt  capacity (min of bearing and shearing)

    Args:
         bolt_shear_capacity: Bolt shearing capacity in KN (float)

         bolt_bearing_capacity: Bolt bearing capacity in KN (float)

         bolt_capacity: Bolt  capacity (min of bearing and shearing) in KN (float)

    Returns:
            Capacity  of bolt (min of bearing and shearing) in KN (float)
    Note:
            Reference:
            IS 800:2007, cl. 10.3.2


    """
    bolt_shear_capacity = str(bolt_shear_capacity)
    bolt_bearing_capacity = str(bolt_bearing_capacity)
    bolt_capacity = str(bolt_capacity)
    bolt_capacity_eqn = Math(inline=True)
    bolt_capacity_eqn.append(NoEscape(r'\begin{aligned}V_{db} &= min~ (V_{dsb}, V_{dpb})\\'))
    bolt_capacity_eqn.append(NoEscape(r'&= min~ (' + bolt_shear_capacity + ',' + bolt_bearing_capacity + r')\\'))
    bolt_capacity_eqn.append(NoEscape(r'&=' + bolt_capacity + r'\\'))
    bolt_capacity_eqn.append(NoEscape(r'[Ref.~&IS~800:2007,~Cl.~10.3.2]\end{aligned}'))

    return bolt_capacity_eqn


def cl_10_3_3_bolt_shear_capacity(f_ub, n_n, a_nb, gamma_mb, bolt_shear_capacity):
    """
    Calculate bolt shearing capacity
    Args:
         f_ub: Ultimate tensile strength of the bolt in MPa (float)
         n_n: Number of shear planes with threads intercepting the shear plane (int)

         a_nb: Net Shear area of the bolt at threads in sq. mm  (float)

         gamma_mb: Partial safety factor =1.25 [Ref: Table 5, cl.5.4.1,IS 800:2007]
         bolt_shear_capacity: Bolt shear capacity in KN  (float)
    Returns:
            Shear capacity of bolt(provided ) in KN  (float)
    Note:
            Reference:
            IS 800:2007, cl. 10.3.3

    """
    f_ub = str(f_ub)
    n_n = str(n_n)
    a_nb = str(a_nb)
    gamma_mb = str(gamma_mb)
    bolt_shear_capacity = str(bolt_shear_capacity)
    bolt_shear_eqn = Math(inline=True)
    bolt_shear_eqn.append(NoEscape(r'\begin{aligned}V_{dsb} &= \frac{f_{ub} ~n_n~ A_{nb}}{1000\times \sqrt{3} ~\gamma_{mb}}\\'))
    bolt_shear_eqn.append(NoEscape(r'&= \frac{'+f_ub+r'\times'+n_n+r'\times'+a_nb+r'}{1000\times \sqrt{3}~\times ~'+ gamma_mb+r'}\\'))
    bolt_shear_eqn.append(NoEscape(r'&= '+bolt_shear_capacity+r'\\'))
    bolt_shear_eqn.append(NoEscape(r'[Ref.&~IS~800:2007,~Cl.~10.3.3]\end{aligned}'))

    return bolt_shear_eqn

# #TODO:DARSHAN I don't think this is required Ans: User will not require to see code and gives better understanding.
# def cl_10_3_3_2_large_grip_req():
#     """
#      Returns:
#         Reduced bolt capacity  in KN (float)
#     Note:
#               Reference:
#               IS 800:2007,  cl 10.3.3.2
#     """
#     large_grip_eqn = Math(inline=True)
#     large_grip_eqn.append(NoEscape(r'\begin{aligned} &if~l_g \geq 5 * d~then~\beta_{lg} = 8/(3+l_g/d)\\'))
#     large_grip_eqn.append(NoEscape(r' &if~l_g \leq 5 * d~then~\beta_{lg} = 1\\'))
#     large_grip_eqn.append(NoEscape(r'& where,\\'))
#     large_grip_eqn.append(NoEscape(r'&  l_g ~=~plate.thk~+~member.thk \\'))
#     large_grip_eqn.append(NoEscape(r'& if~\beta_{lg} \geq \beta_{lj}~then~\beta_{lg} = \beta_{lj} \\'))
#     large_grip_eqn.append(NoEscape(r'& V_{rd} = \beta_{lg} * V_{db} \\'))
#     large_grip_eqn.append(NoEscape(r'&[Ref.~IS~800:2007,~Cl.~10.3.3.2]\end{aligned}'))
#     return large_grip_eqn
#
#
# def cl_10_3_3_2_large_grip_check(d, pt, mt, blj, blg):
#
#     l_g = pt + mt
#     l_g1 = str(l_g)
#     pt1 = str(pt)
#     mt1 = str(mt)
#     blj1 = str(blj)
#     blg1 = str(blg)
#     d1= str(d)
#     d2 = str((5*d))
#
#
#     large_grip_eqn = Math(inline=True)
#     # long_joint_bolted_eqn.append(NoEscape(r'\begin{aligned} &if~l\leq 15 * d~then~V_{rd} = \beta_{lj} * V_{db} \\'))
#     # long_joint_bolted_eqn.append(NoEscape(r'& where,\\'))
#
#     if l_g > 5 * d :
#         large_grip_eqn.append(NoEscape(r'\begin{aligned} l_g & = ~plate.thk~+~member.thk \\'))
#         large_grip_eqn.append(NoEscape(r' &= '+pt1+'+'+mt1+ '='+l_g1+ r'\\'))
#         large_grip_eqn.append(NoEscape(r'&5~*~d= 5 \times'+d1+r' ='+d2+r' \\'))
#         large_grip_eqn.append(NoEscape(r'&since,~l_g \geq 5 * d~then~\beta_{lg} = 8/(3+l_g/d)\\'))
#         large_grip_eqn.append(NoEscape(r'&\beta_{lg}= 8/(3+ '+l_g1+'/'+d1+r') = '+blg1+r'\\'))
#         if blg>blj:
#             large_grip_eqn.append(NoEscape(r'&since,~\beta_{lg} \geq \beta_{lj},\beta_{lg} = '+blj1+r' \\'))
#         else:
#             large_grip_eqn.append(NoEscape(r'&since,~\beta_{lg} \leq \beta_{lj},\beta_{lg} = ' + blg1 + r' \\'))
#
#     else:
#         large_grip_eqn.append(NoEscape(r'\begin{aligned} l_g & = ~plate.thk~+~member.thk \\'))
#         large_grip_eqn.append(NoEscape(r' &= ' + pt1 + '+' + mt1 + '=' + l_g1 + r'\\'))
#         large_grip_eqn.append(NoEscape(r'&5~*~d~= 5 \times' + d1 + r' \\'))
#         large_grip_eqn.append(NoEscape(r'&since,~l_g \leq 5 * d~then~\beta_{lg} = 1.0\\'))
#     large_grip_eqn.append(NoEscape(r'&[Ref.~IS~800:2007,~Cl.~10.3.3.2]\end{aligned}'))
#
#     return large_grip_eqn


def cl_10_3_4_calculate_kb(e, p, d, fub, fu):
    """
    Calculate kb provided to find bearing capacity of bolt
    Args:
        e:End distance of the fastener along bearing direction in mm (float)
        p:Pitch distance of the fastener along bearing direction in mm (float)
        d: diameter of the bolt in mm (float)
        fub: Ultimate tensile strength of the bolt in MPa (float)
        fu:Ultimate tensile strength of the plate in MPa (float)

    Returns:
         kb  to find bearing capacity of bolt
    Note:
            Reference:
            IS 800:2007,  cl 10.3.4

    """


    kb1 = round((e / (3.0 * d)),2)
    kb2 = round((p / (3.0 * d)-0.25),2)
    kb3 = round(( fub / fu),2)
    kb4 = 1.0
    kb_1 = min(kb1,kb2,kb3,kb4)
    kb_2 = min(kb1,kb3,kb4)
    pitch = p
    e = str(e)
    p = str(p)
    d = str(d)
    fub = str(fub)
    fu = str(fu)
    kb1 = str(kb1)
    kb2 = str(kb2)
    kb3 = str(kb3)
    kb4 = str(kb4)
    kb_1 = str(kb_1)
    kb_2 = str(kb_2)
    kb_eqn = Math(inline=True)
    if pitch != 0:
        kb_eqn.append(NoEscape(r'\begin{aligned} k_b & = min(\frac{e}{3d_0},\frac{p}{3d_0}-0.25,\frac{f_{ub}}{f_u},1.0)\\' ))
        kb_eqn.append(NoEscape(r'& = min(\frac{'+e+r'}{3\times'+d+r'},\frac{'+p+r'}{3\times'+d+r'}-0.25,\frac{'+fub+'}{'+fu+r'},1.0)\\'))
        kb_eqn.append(NoEscape(r'& = min('+kb1+','+kb2+','+kb3+','+kb4+r')\\'))
        kb_eqn.append(NoEscape(r'& = '+kb_1+r'\\'))
        kb_eqn.append(NoEscape(r'[Ref&.~IS~800:2007,~Cl.~10.3.4]\end{aligned}'))

    else:
        kb_eqn.append(NoEscape(r'\begin{aligned} k_b & = min(\frac{e}{3d_0},\frac{f_{ub}}{f_u},1.0)\\'))
        kb_eqn.append(NoEscape(r'& = min(\frac{' + e + r'}{3\times' + d + r'},\frac{' + fub + '}{' + fu + r'},1.0)\\'))
        kb_eqn.append(NoEscape(r'& = min(' + kb1 + ',' + kb3 + ',' + kb4 + r')\\'))
        kb_eqn.append(NoEscape(r'& = ' + kb_2 + r'\\'))
        kb_eqn.append(NoEscape(r'[Ref&~IS~800:2007,~Cl.~10.3.4]\end{aligned}'))

    return kb_eqn


def cl_10_3_4_bolt_bearing_capacity(k_b, d, conn_plates_t_fu_fy, gamma_mb, bolt_bearing_capacity):
    """
    Calculate bolt bearing capacity of bolt

    Args:
        k_b:  min(e/(3.0*d_0), p/(3.0*d_0)-0.25, f_ub/f_u, 1.0)

        d: Diameter of bolt in mm (float)
        conn_plates_t_fu_fy: Ultimate tensile strength of the plate in MPa (float)
        gamma_mb:Partial safety factor =1.25 [Ref: Table 5, cl.5.4.1,IS 800:2007]
        bolt_bearing_capacity: Bolt bearing capacity in KN (float)
    Returns:
            Bearing capacity of bolt(provided ) in KN  (float)
    Note:
            Reference:
            IS 800:2007, cl. 10.3.4


    """
    t_fu_prev = conn_plates_t_fu_fy[0][0] * conn_plates_t_fu_fy[0][1]
    t = conn_plates_t_fu_fy[0][0]
    f_u = conn_plates_t_fu_fy[0][1]
    for i in conn_plates_t_fu_fy:
        t_fu = i[0] * i[1]
        if t_fu <= t_fu_prev:
            t = i[0]
            f_u = i[1]
    k_b = str(round(k_b, 2))
    d = str(d)
    t = str(t)
    f_u = str(f_u)
    gamma_mb = str(gamma_mb)
    bolt_bearing_capacity = str(bolt_bearing_capacity)
    bolt_bearing_eqn = Math(inline=True)
    bolt_bearing_eqn.append(NoEscape(r'\begin{aligned}V_{dpb} &= \frac{2.5~ k_b~ d~ t~ f_u}{1000\times \gamma_{mb}}\\'))
    bolt_bearing_eqn.append(NoEscape(
        r'&= \frac{2.5 \times ' + k_b + r'\times' + d + r'\times' + t + r'\times' + f_u + r'}{1000\times' + gamma_mb + r'}\\'))
    bolt_bearing_eqn.append(NoEscape(r'&=' + bolt_bearing_capacity + r'\\'))
    bolt_bearing_eqn.append(NoEscape(r'[Ref.~&IS~800:2007,~Cl.~10.3.4]\end{aligned}'))

    return bolt_bearing_eqn


def cl_10_3_5_bearing_bolt_tension_resistance(f_ub, f_yb, A_sb, A_n, tension_capacity):
    """
    Calculate design tensile strength of bearing bolt
    Args:
        f_ub - Ultimate tensile strength of the bolt in MPa (float)
        f_yb - Yield strength of the bolt in MPa (float)
        A_sb - Shank area of bolt in sq. mm  (float)
        A_n - Net tensile stress area of the bolts as per IS 1367 in sq. mm  (float)
        tension_capacity - Tension resistance/capacity of a bolt in KN (float)
    return:
        T_db - Design tensile strength of bearing bolt in N (float)
    Note:
        Reference:
        IS 800:2007,  cl 10.3.5
    """
    f_ub = str(f_ub)
    f_yb = str(f_yb)
    A_sb = str(A_sb)
    A_n = str(A_n)
    gamma_mb = str(1.5)
    gamma_m0 = IS800_2007.cl_5_4_1_Table_5['gamma_m0']['yielding']
    gamma_m0 = str(gamma_m0)
    tension_capacity = str(tension_capacity)
    tension_resistance = Math(inline=True)
    tension_resistance.append(NoEscape(r'\begin{aligned} T_{db} &= 0.90~f_{ub}~A_n < f_{yb}~A_{sb}~(\gamma_{mb}~/~\gamma_{m0}) \\'))
    tension_resistance.append(NoEscape(r'\begin &= 0.90~' + f_ub + '~ ' + A_n + '< ' + f_yb + '~ ' + A_sb + '~(' + gamma_mb + '~/~' + gamma_m0 + ''))
    tension_resistance.append(NoEscape(r'\begin &= 0.90~' + f_ub + '~ ' + A_n + ''))
    tension_resistance.append(NoEscape(r'&= '+ tension_capacity + r'\\'))
    tension_resistance.append(NoEscape(r'&[Ref.~IS~&800:2007,~Cl.~10.3.5]\end{aligned}'))

    return tension_resistance


def cl_10_3_6_bearing_bolt_combined_shear_and_tension(V_sb, V_db, T_b, T_db, value):#Todo:not done
    """
    Check for bolt subjected to combined shear and tension
    Args:
        V_sb - factored shear force acting on the bolt,
        V_db - design shear capacity,
        T_b - factored tensile force acting on the bolt,
        T_db - design tension capacity.
    Returns:
        combined shear and friction value
    Note:
        Reference:
        IS 800:2007,  cl 10.3.6
    """
    V_sb = str(V_sb)
    V_db = str(V_db)
    T_b = str(T_b)
    T_db = str(T_db)
    value = str(value)

    combined_capacity_eqn = Math(inline=True)
    combined_capacity_eqn.append(NoEscape(r'\begin{aligned}\bigg(\frac{V_{sb}}{V_{db}}\bigg)^2 + \bigg(\frac{T_{b}}{T_{db}}\bigg)^2  \leq 1.0\\'))
    combined_capacity_eqn.append(NoEscape(r'\bigg(\frac{' + V_sb + '}{' + V_db + r'}\bigg)^2 + \bigg(\frac{' + T_b + '}{' + T_db + r'}\bigg)^2 = '
                                          + value + ''))
    combined_capacity_eqn.append(NoEscape(r'&[Ref.~IS~800:2007,~Cl.~10.3.6]&\end{aligned}'))

    return combined_capacity_eqn


def cl_10_4_3_HSFG_bolt_capacity(mu_f, n_e, K_h, fub, Anb, gamma_mf, capacity):
    """
    Calculate design shear strength of friction grip bolt as governed by slip
 
    Args:
         mu_f:Coefficient of friction (slip factor) as specified in Table 20 , IS 800:2007
           
         n_e:Number of  effective interfaces offering  frictional resistance to slip (int)
         K_h:1 for bolts in clearence holes and 0.85 for bolts in oversized holes
         fub: Ultimate tensile strength of the bolt in KN (float)
           
         Anb: Net area of bolt in mm square
         gamma_mf:Partial safety factor  [Ref: Table 5, cl.5.4.1,IS 800:2007]
         capacity: Design shear strength of friction grip bolt as governed by slip in N (float)

    Returns:
           Design shear strength of friction grip bolt as governed by slip in N (float)

    Note:
            Reference:
            IS 800:2007,  cl 10.4.3

    """
    mu_f = str(mu_f)
    n_e = str(n_e)
    K_h = str(K_h)
    fub = str(fub)
    Anb = str(Anb)
    gamma_mf = str(gamma_mf)
    capacity = str(capacity)

    HSFG_bolt_capacity_eqn = Math(inline=True)
    HSFG_bolt_capacity_eqn.append(NoEscape(r'\begin{aligned}V_{dsf} & = \frac{\mu_f~ n_e~  K_h~ F_o}{\gamma_{mf}}\\'))
    HSFG_bolt_capacity_eqn.append(NoEscape(r' Where&, F_o = 0.7f_{ub} A_{nb}\\'))
    HSFG_bolt_capacity_eqn.append(NoEscape(r'V_{dsf} & = \frac{'+ mu_f +r'\times' + n_e +r'\times' + K_h +r'\times 0.7 \times' +fub+r'\times'+Anb +r'}{'+gamma_mf+r'}\\'))
    HSFG_bolt_capacity_eqn.append(NoEscape(r'& ='+capacity+r'\\'))
    HSFG_bolt_capacity_eqn.append(NoEscape(r'[Ref.~IS~&800:2007,~Cl.~10.4.3]\end{aligned}'))

    return HSFG_bolt_capacity_eqn


def cl_10_4_7_tension_in_bolt_due_to_prying(T_e, l_v, f_o, b_e, t, f_y, end_dist, pre_tensioned, beta, Q, l_e, eta=1.5):
    """Calculate prying force of friction grip bolt
                   Args:
                      2 * T_e - Tension Force in 2 bolts on either sides of the web/plate
                      l_v - distance from the bolt centre line to the toe of the fillet weld or to half
                            the root radius for a rolled section,
                      b_e - effective width of flange per pair of bolts
                      f_o - proof stress in consistent units
                      t - thickness of the end plate
                      f_y - yield strength of end plate
                      end_dist - end distance of bolt
                      pre_tensioned: 'Pretensioned' if bolt is pretension None if it is not
                      beta - 2 for non pre-tensioned bolt and 1 for pre-tensioned bolt
                      Q - Prying force
                      l_e - min(e, 1.1~t~\sqrt{\frac{\beta~f_o}{f_y}})
                      eta - 1.5
                   return:
                       equation for Prying force of friction grip bolt
                   Note:
                       Reference:
                       IS 800:2007,  cl 10.4.7
    """
    T_e = str(T_e)
    l_v = str(l_v)
    f_o = str(f_o)
    b_e = str(b_e)
    t= str(t)
    f_y = str(f_y)
    l_e = str(l_e)
    end_dist = str(end_dist)
    pre_tensioned = str(pre_tensioned)
    beta = str(beta)
    eta = str(eta)
    tension_in_bolt_due_to_prying = Math(inline=True)
    tension_in_bolt_due_to_prying.append(NoEscape(r'\begin{aligned} Q &= \frac{l_v}{2\times l_e} \times [T_e - \frac{\beta \times  \eta \times f_o \times b_e \times t^4}{27 \times l_e \times l_v^2}]\\'))
    tension_in_bolt_due_to_prying.append(NoEscape(r'Q &\geq 0\\'))
    if pre_tensioned == 'Pretensioned':
        tension_in_bolt_due_to_prying.append(NoEscape(r'\beta &= 1 (pre-tensioned) \\'))
    else:
        tension_in_bolt_due_to_prying.append(NoEscape(r'\beta &= 2 (Not pre-tensioned) \\'))
    tension_in_bolt_due_to_prying.append(NoEscape(r'l_e &= min(e, 1.1~t~\sqrt{\frac{\beta~f_o}{f_y}}) \\'))
    tension_in_bolt_due_to_prying.append(NoEscape(r' &= min('+end_dist+r', 1.1\times'+t+r'\times \sqrt{\frac{'+beta+r'\times'+f_o+r'}{'+f_y+r'}}) \\'))
    tension_in_bolt_due_to_prying.append(NoEscape(r' &= ' + l_e + r' \\'))
    tension_in_bolt_due_to_prying.append(NoEscape(r'l_v &= ' + l_v + r' \\'))
    tension_in_bolt_due_to_prying.append(NoEscape(r'b_e &= ' + b_e + r' \\'))
    tension_in_bolt_due_to_prying.append(
        NoEscape(r'Q &=\frac{'+l_v+r'}{2\times'+l_e+r'}\times\\'))
    tension_in_bolt_due_to_prying.append(NoEscape(r'&[' + T_e + r'- \frac{'+beta+r' \times' + eta +r'\times' + f_o +r'\times' + b_e +r'\times'+ t+r'^4}{27 \times'+ l_e+r'\times'+ l_v+r'^2}]\\'))
    if Q <= 0.0:
        tension_in_bolt_due_to_prying.append(NoEscape(r'Q &= 0.0 \end{aligned}'))
    else:
        Q = str(Q)
        tension_in_bolt_due_to_prying.append(NoEscape(r'Q &= ' + Q + r'\end{aligned}'))
    tension_in_bolt_due_to_prying.append(NoEscape(r'[Ref.~IS~&800:2007,~Cl.~10.4.7]\end{aligned}'))
    return tension_in_bolt_due_to_prying


#TODO: DARSHAN, Keep only one of the following Ans: Use the one with weld thickness reduction
def cl_10_5_2_3_min_fillet_weld_size_required(conn_plates_weld, min_weld_size,red=0.0):
    """
    Calculate minimum size of fillet weld,to avoid the
        risk of cracking in the absence of preheating
    Args:
        conn_plates_weld:Thickness of either plate element being welded in mm (float
        Thickness of other plate element being welded in mm (float)

        red:reduce the thickness of thicker part according to given size range
        min_weld_size:minimum size of the weld
    Returns:
        minimum size of the weld
    Note:
            Reference:
            IS 800, Table 21 (Cl 10.5.2.3) : Minimum Size of First Run or of a Single Run Fillet Weld


    """
    # t1 = str(conn_plates_weld[0])
    # t2 = str(conn_plates_weld[0])
    tmax = min(conn_plates_weld)
    tmin = int (tmax - red)
    tmin = str(tmin)
    tmax= str(int(tmax))
    weld_min = str(min_weld_size)

    min_weld_size_eqn = Math(inline=True)
    min_weld_size_eqn.append(NoEscape(r'\begin{aligned} & t_{w_{min}}~based~on~thinner~part\\'))
    min_weld_size_eqn.append(NoEscape(r'& ='+tmax+ '~or~' +tmin+ r'\\'))
    min_weld_size_eqn.append(NoEscape(r'& IS800:2007~cl.10.5.2.3~Table 21\\' ))
    min_weld_size_eqn.append(NoEscape(r'& s_{min}~based~on~thicker~part=' + weld_min + r'\\'))
    min_weld_size_eqn.append(NoEscape(r'& [Ref~IS~800:2007,Table ~21 ~(Cl 10.5.2.3)]\end{aligned}'))
    return min_weld_size_eqn


# def cl_10_5_2_3_min_fillet_weld_size_required(conn_plates_weld, min_weld_size):
#     """
#     Calculate minimum size of fillet weld as per Table 21 of IS 800:2007
#     Args:
#
#         conn_plates_weld:Thickness of either plate element being welded in mm (float)
#                              Thickness of other plate element being welded in mm (float)
#
#          min_weld_size: Minimum size of first run or of a single run fillet weld in mm (float)
#
#     Returns:
#           minimum size of fillet weld
#     Note:
#             Reference:
#             IS 800, Table 21 (Cl 10.5.2.3) : Minimum Size of First Run or of a Single Run Fillet Weld
#
#     """
#
#     t1 = str(conn_plates_weld[0])
#     t2 = str(conn_plates_weld[1])
#     tmax = str(max(conn_plates_weld))
#     weld_min = str(min_weld_size)
#
#     min_weld_size_eqn = Math(inline=True)
#     min_weld_size_eqn.append(NoEscape(r'\begin{aligned} &Thickness~of~Thicker~part\\'))
#     min_weld_size_eqn.append(NoEscape(r'\noindent &=max('+t1+','+t2+r')\\'))
#     min_weld_size_eqn.append(NoEscape(r'&='+tmax+r'\\'))
#     min_weld_size_eqn.append(NoEscape(r'&[Ref.IS~800:2007~Cl.10.5.2.3~Table ~21],\\'))
#     min_weld_size_eqn.append(NoEscape(r' &s_{min}=' + weld_min + r'\\'))
#     min_weld_size_eqn.append(NoEscape(r'& [Ref.~IS~800:2007,~Table ~21~ (Cl. 10.5.2.3)]\end{aligned}'))
#
#
#     return min_weld_size_eqn


def cl_10_5_3_1_max_weld_size(conn_plates_weld, max_weld_size):
    """
    Calculate maximum weld size of fillet weld
    Args:

        conn_plates_weld: Thickness of either plate element being welded in mm (float)
                            Thickness of other plate element being welded in mm (float)

         max_weld_size: Maximum weld size of fillet weld
    Returns:
          Maximum weld size of fillet weld
    Note:
            Reference:
            IS 800:2007,  cl 10.5.3.1


    """
    t1 = str(conn_plates_weld[0])
    t2 = str(conn_plates_weld[1])
    t_min = str(min(conn_plates_weld))
    weld_max = str(max_weld_size)

    max_weld_size_eqn = Math(inline=True)
    max_weld_size_eqn.append(NoEscape(r'\begin{aligned} & Thickness~of~Thinner~part\\'))
    max_weld_size_eqn.append(NoEscape(r'&=min('+t1+','+t2+r')='+t_min+r'\\'))
    max_weld_size_eqn.append(NoEscape(r'&s_{max} =' + weld_max + r'\\'))
    max_weld_size_eqn.append(NoEscape(r'&[Ref.~IS~800:2007,~Cl.~10.5.3.1]\end{aligned}'))

    return max_weld_size_eqn


# TODO: DARSHAN,ANJALI I don't think this is required Ans: It's required.
def cl_10_5_3_1_throat_thickness_req():
    """
    Note:
              Reference:
              IS 800:2007,  cl 10.5.3.1
    """
    throat_eqn = Math(inline=True)
    throat_eqn.append(NoEscape(r'\begin{aligned} t_t &\geq 3 \\'))
    throat_eqn.append(NoEscape(r'&[Ref.~IS~800:2007,~Cl.~10.5.3.1]&\end{aligned}'))

    return throat_eqn


def cl_10_5_3_1_throat_thickness_weld(tw, f):
    """
    Calculate effective throat thickness of fillet weld for stress calculation

    Args:
         tw:Fillet weld size in mm (float)
         f:Constant depending upon the angle between  fusion faces  (float)
    Returns:
        Throat thickness in mm (float)
    Note:
              Reference:
              IS 800:2007,  cl 10.5.3.1

    """
    tt = tw * f
    t_t= max(tt,3)
    tw = str(round(tw,2))
    f= str(round(f,2))
    tt = str(round(tt,2))
    t_t = str(round(t_t,2))

    throat_eqn = Math(inline=True)
    throat_eqn.append(NoEscape(r'\begin{aligned} t_t & = '+ f+r't_w 'r'\\'))
    throat_eqn.append(NoEscape(r'& = ' + f +r'\times'+ tw +r'\\'))
    throat_eqn.append(NoEscape(r't_t & = ' + t_t + r'\\'))
    throat_eqn.append(NoEscape(r'[Ref.&~IS~800:2007,~Cl.~10.5.3.1]\end{aligned}'))
    return throat_eqn


def cl_10_5_7_1_1_weld_strength(conn_plates_weld_fu, gamma_mw, t_t, f_w):
    """
    Calculate the design strength of fillet weld
    Args:
         conn_plates_weld_fu:Ultimate stresses of weld and parent metal in MPa (list or tuple) in N/mm square(float)
         gamma_mw: 1.25(for shop weld);1.5(site weld)  (float)
         t_t:Throat thickness in mm (float)
         f_w:Design strength of fillet weld in N/mm (float)
    Returns:
        Design strength of fillet weld
    Note:
            Reference:
            IS 800:2007,  cl 10.5.7.1.1

    """

    f_u = str(min(conn_plates_weld_fu))
    t_t = str(t_t)
    gamma_mw = str(gamma_mw)
    f_w = str(f_w)
    weld_strength_eqn = Math(inline=True)
    weld_strength_eqn.append(NoEscape(r'\begin{aligned} f_w &=\frac{t_t~f_u}{\sqrt{3}~\gamma_{mw}}\\'))
    weld_strength_eqn.append(NoEscape(r'&=\frac{'+t_t+r'\times'+f_u+r'}{\sqrt{3}\times'+ gamma_mw+r'}\\'))
    weld_strength_eqn.append(NoEscape(r'&='+f_w+r'\\'))
    weld_strength_eqn.append(NoEscape(r'[Ref.&~IS~800:2007,~Cl.~10.5.7.1.1]\end{aligned}'))
    return weld_strength_eqn


def cl_10_5_7_3_weld_strength_post_long_joint(h, l, t_t, ws, wsr, direction=None):
    """
    Calculate Reduced flange weld strength  in case of long joint (welded connection)

    Args:

         h: plate height in mm (float)
         l: plate length in mm (float)
         t_t: weld throat thickness  in mm (float)
         ws: weld strength  in KN (float)
         wsr:reduced weld strength  in KN (float)
    Returns:
        reduced weld strength
    Note:
              Reference:
              IS 800:2007,  cl 10.5.7.3

    """
    lj = max(h,l)
    lt = 150 * t_t
    B = 1.2 - ((0.2 * lj) / (150 * t_t))
    if B <= 0.6:
        B = 0.6
    elif B >= 1:
        B = 1
    else:
        B = B
    Bi = str(round(B, 2))
    t_t= str(t_t)
    lt_str = str(lt)
    h = str(h)
    l = str(l)
    ws = str(ws)
    wsr = str(wsr)
    ljs= str(lj)

    long_joint_welded_prov = Math(inline=True)
    # if conn =="web":

    if direction=='height':
        long_joint_welded_prov.append(NoEscape(r'\begin{aligned} l_w ~&= h\\'))
        long_joint_welded_prov.append(NoEscape(r' &='+ h+r'\\'))
    else:
        long_joint_welded_prov.append(NoEscape(r'\begin{aligned} l ~&= pt.length ~ or ~ pt.height \\'))
        long_joint_welded_prov.append(NoEscape(r' l_l &= max(' + h + ',' + l + r') \\'))
        long_joint_welded_prov.append(NoEscape(r' &=' + ljs + r' \\'))
    long_joint_welded_prov.append(NoEscape(r'& 150 t_t =150 \times' + t_t + ' = ' + lt_str + r' \\'))
    if lj < lt:
        long_joint_welded_prov.append(NoEscape(r'& since,~l < 150 t_t~\\&then~f_{wrd} = f_{w} \\'))
        long_joint_welded_prov.append(NoEscape(r' f_{wrd} &= ' + ws + r' \\'))
        long_joint_welded_prov.append(NoEscape(r'[Ref.~&IS~800:2007,~Cl.~10.5.7.3]\end{aligned}'))
    else:
        long_joint_welded_prov.append(NoEscape(r'&since,~l \geq 150 t_t~ \\&then~V_{rd} = \beta_{lw} V_{db} \\'))
        long_joint_welded_prov.append(NoEscape(r'\beta_{l_w}& = 1.2 - (0.2 \times' + lj + r')/(150 \times' + t_t+ r')\\& =' + Bi + r'\\'))
        long_joint_welded_prov.append(NoEscape(r' f_{wrd}& = ' + Bi + r' \times' + ws + '=' + wsr + r' \\'))
        long_joint_welded_prov.append(NoEscape(r'[Ref.~&IS~800:2007,~Cl.~10.5.7.3]\end{aligned}'))

    return long_joint_welded_prov


##################
# TODO: DARSHAN arrange all reduction factors of bolted and welded (I dont think req functions are required.
# TODO Ans: User will not require to see the code and gives better understanding.
# TODO: DARSHAN Refactor functions as per clause no
#################

def cl_10_3_3_1_long_joint_bolted_req():
    """
     Returns:
        Long joint reduction factor
    Note:
              Reference:
              IS 800:2007,  cl 10.3.3.1
    """
    long_joint_bolted_eqn = Math(inline=True)
    long_joint_bolted_eqn.append(NoEscape(r'\begin{aligned} &if~l_j\geq 15 d~then~V_{rd} = \beta_{lj} V_{db} \\'))
    long_joint_bolted_eqn.append(NoEscape(r'& if~l_j < 15 d~then~V_{rd} = V_{db} \\'))
    long_joint_bolted_eqn.append(NoEscape(r'& where,\\'))
    long_joint_bolted_eqn.append(NoEscape(r'& l_j = ((nc~or~nr) - 1) \times (p~or~g) \\'))

    long_joint_bolted_eqn.append(NoEscape(r'& \beta_{lj} = 1.075 - l/(200 d) \\'))
    long_joint_bolted_eqn.append(NoEscape(r'& but~0.75\leq\beta_{lj}\leq1.0 \\'))
    long_joint_bolted_eqn.append(NoEscape(r'&[Ref.~IS~800:2007,~Cl.~10.3.3.1]\end{aligned}'))
    return long_joint_bolted_eqn

#
def cl_10_3_3_1_long_joint_bolted_prov(nc, nr, p, g, d, Tc, Tr, direction=None):
    """
    Calculate reduced bolt capacity in case of long joint

    Args:
         nc:No. of row of bolts in one line (int)
         nr:No. of  bolts in one line (int)
         p:Pitch distance of the plate in mm (float)
         g:Gauge distance of the plate in mm (float)
         d:Diameter of the bolt in mm (float)
         Tc:Bolt capacity  in KN (float)
         Tr: Reduced bolt capacity  in KN (float)
         direction: n_r or None(string)
    Returns:
        Long joint reduction factor
    Note:
              Reference:
              IS 800:2007,  cl 10.3.3.1
              If direction is n_r it will calculate long joint for no. of rows
              else max of rows and column length will be considered

    """
    lc = (nc - 1) * p
    lr = (nr - 1) * g
    l = max(lc,lr)
    lt = 15 * d
    B = 1.075 - (l / (200 * d))
    Bi = round(B,2)
    nc= str(nc)
    nr= str(nr)
    g= str(g)
    p = str(p)
    d = str(d)
    Tc = str(Tc)
    Tr = str(Tr)
    if B<=0.75:
        B =0.75
    elif B>=1:
        B =1
    else:
        B=B
    B = str(round(B,2))
    Bi = str(Bi)
    lc_str = str(lc)
    lr_str = str(lr)
    l_str = str(l)
    lt_str = str(lt)
    long_joint_bolted_eqn = Math(inline=True)
    # long_joint_bolted_eqn.append(NoEscape(r'\begin{aligned} &if~l\leq 15 * d~then~V_{rd} = \beta_{lj} * V_{db} \\'))
    # long_joint_bolted_eqn.append(NoEscape(r'& where,\\'))

    if direction == 'n_r':
        long_joint_bolted_eqn.append(NoEscape(r'\begin{aligned} l_j &= (n_r - 1) \times  p \\'))
        long_joint_bolted_eqn.append(NoEscape(r' &= (' + nr + r' - 1) \times ' + g + '=' + lr_str + r'\\'))
    else:
        long_joint_bolted_eqn.append(NoEscape(r'\begin{aligned} l_j &= ((n_c~or~n_r) - 1) \times  (p~or~g) \\'))
        long_joint_bolted_eqn.append(NoEscape(r' &= (' + nc + r' - 1) \times  ' + p + '=' + lc_str + r'\\'))
        long_joint_bolted_eqn.append(NoEscape(r' &= (' + nr + r' - 1) \times  ' + g + '=' + lr_str + r'\\'))
    long_joint_bolted_eqn.append(NoEscape(r' l&= ' + l_str + r'\\'))
    long_joint_bolted_eqn.append(NoEscape(r'& 15 \times d = 15 \times ' + d + ' = ' + lt_str + r' \\'))
    if l < (lt):
        long_joint_bolted_eqn.append(NoEscape(r'& since,~l_j < 15 \times d~then~V_{rd} = V_{db} \\'))
        # long_joint_bolted_eqn.append(NoEscape(r'& V_{rd} = '+Tc+r' \\'))
        long_joint_bolted_eqn.append(NoEscape(r'&[Ref.~IS~800:2007,~Cl.~10.3.3.1]\end{aligned}'))
    else:
        long_joint_bolted_eqn.append(NoEscape(r'& since,~l_j \geq 15~d~then~V_{rd} = \beta_{lj}~V_{db} \\'))
        long_joint_bolted_eqn.append(NoEscape(r'& \beta_{lj} = 1.075 - '+ l_str + r'/(200~\times'+d+') ='+Bi+r'\\'))
        # long_joint_bolted_eqn.append(NoEscape(r'& V_{rd} = '+B+' * '+Tc+'='+Tr+ r' \\'))
        long_joint_bolted_eqn.append(NoEscape(r'&[Ref.~IS~800:2007,~Cl.~10.3.3.1]\end{aligned}'))

    return long_joint_bolted_eqn

def cl_10_3_3_2_large_grip_bolted_req():
    """
     Returns:
        Large grip reduction factor
    Note:
              Reference:
              IS 800:2007,  cl 10.3.3.2
    """
    large_grip_bolted_eqn = Math(inline=True)
    large_grip_bolted_eqn.append(NoEscape(r'\begin{aligned} &if~l_g\geq 5~d~then~V_{rd} = \beta_{lg}~V_{db} \\'))
    large_grip_bolted_eqn.append(NoEscape(r'& if~l_g < 5d~then~V_{rd} = V_{db} \\'))
    large_grip_bolted_eqn.append(NoEscape(r'& l_g \leq 8d \\'))
    large_grip_bolted_eqn.append(NoEscape(r'& where,\\'))
    large_grip_bolted_eqn.append(NoEscape(r'& l_g = \Sigma (t_{ep}+t_{member}) \\'))
    large_grip_bolted_eqn.append(NoEscape(r'& \beta_{lg} = 8d/(3d + l_g) \\'))
    large_grip_bolted_eqn.append(NoEscape(r'& but~\beta_{lg}\leq \beta_{lj} \\'))
    large_grip_bolted_eqn.append(NoEscape(r'&[Ref.~IS~800:2007,~Cl.~10.3.3.2]\end{aligned}'))
    return large_grip_bolted_eqn

def cl_10_3_3_2_large_grip_bolted_prov(t_sum, d, beta_lj=1.0):
    """
    Calculate reduced bolt capacity in case of large grip

    Args:
         t_sum : Sum of thickness of the connected plates
         d:Diameter of the bolt in mm (float)
    Returns:
        Large grip reduction factor
    Note:
              Reference:
              IS 800:2007,  cl 10.3.3.2

    """
    lg = t_sum
    B = 8*d/(3*d+lg)
    Bi = round(B,2)
    #
    # Tc = str(Tc)
    # Tr = str(Tr)
    if lg <= 5*d:
        B = 1.0
    # elif B>=beta_lj:
    #     B = beta_lj
    else:
        B=B
    d5_str = str(5*d)
    d_str = str(d)
    # B = str(round(B,3))
    Bi = str(Bi)
    lg_str = str(lg)
    t_sum_str = str(t_sum)
    beta_lj_str = str(round(beta_lj,2))
    large_grip_bolted_eqn = Math(inline=True)
    # large_grip_bolted_eqn.append(NoEscape(r'\begin{aligned} &if~l\leq 15 * d~then~V_{rd} = \beta_{ij} * V_{db} \\'))
    # large_grip_bolted_eqn.append(NoEscape(r'& where,\\'))

    large_grip_bolted_eqn.append(NoEscape(r'\begin{aligned} l_g &= \Sigma (t_{ep}+t_{member}) \\'))
    # large_grip_bolted_eqn.append(NoEscape(r' &= ' + t_sum_str + r'\\'))
    large_grip_bolted_eqn.append(NoEscape(r' &= ' + t_sum_str + r'\\'))
    large_grip_bolted_eqn.append(NoEscape(r' 5d &= ' + d5_str + r'\\'))
    if lg <= 5*d:
        large_grip_bolted_eqn.append(NoEscape(r'& since,~l_g < 5d~then~\beta_{lg} = 1.0 \\'))
        # large_grip_bolted_eqn.append(NoEscape(r'& V_{rd} = V_{db} \\'))
        large_grip_bolted_eqn.append(NoEscape(r'&[Ref.~IS~800:2007,~Cl.~10.3.3.2]\end{aligned}'))
    else:
        large_grip_bolted_eqn.append(NoEscape(r'& since,~l_g \geq 5d~then~V_{rd} = \beta_{lg}~V_{db} \\'))
        large_grip_bolted_eqn.append(NoEscape(r'& \beta_{lg} = 8\times'+ d_str +r'/(3\times'+ d_str +' + '+ lg_str +') ='+Bi+r'\\'))
        if B > beta_lj:
            large_grip_bolted_eqn.append(NoEscape(r'& since,~\beta_{lg} \geq \beta_{lj}~then~\beta_{lg} = \beta_{lj} \\'))
            large_grip_bolted_eqn.append(NoEscape(r'& \beta_{lg} = ' + beta_lj_str + r'\\'))
        # large_grip_bolted_eqn.append(NoEscape(r'& V_{rd} = '+B+' * '+Tc+'='+Tr+ r' \\'))
        large_grip_bolted_eqn.append(NoEscape(r'&[Ref.~IS~800:2007,~Cl.~10.3.3.2]\end{aligned}'))

    return large_grip_bolted_eqn


def packing_plate_bolted_req():
    """
     Returns:
        Packing plate reduction factor
    Note:
              Reference:
              IS 800:2007,  cl 10.3.3.3
    """
    packing_plate_bolted_eqn = Math(inline=True)
    packing_plate_bolted_eqn.append(NoEscape(r'\begin{aligned} &if~t_{pk}\geq 6 mm~then~V_{rd} = \beta_{pk}V_{db} \\'))
    packing_plate_bolted_eqn.append(NoEscape(r'& if~t_{pk} < 6 mm~then~V_{rd} = V_{db} \\'))
    packing_plate_bolted_eqn.append(NoEscape(r'& where,\\'))
    packing_plate_bolted_eqn.append(NoEscape(r'& t_{pk} = packing~plate~thickness \\'))
    packing_plate_bolted_eqn.append(NoEscape(r'& \beta_{pk} = 1.0 - 0.0125~t_{pk} \\'))
    packing_plate_bolted_eqn.append(NoEscape(r'&[Ref.~IS~800:2007,~Cl.~10.3.3.3]\end{aligned}'))
    return packing_plate_bolted_eqn


def packing_plate_bolted_prov(gap):
    """
    Calculate reduced bolt capacity in case of large grip

    Args:
         gap: Gap between connector plate and the supporting element
    Returns:
        Packing plate reduction factor
    Note:
              Reference:
              IS 800:2007,  cl 10.3.3.3

    """
    tpk = gap
    B = 1 - 0.0125*tpk
    Bi = round(B,3)

    if tpk<=6:
        B =1.0
    # elif B>=beta_lj:
    #     B = beta_lj
    else:
        B=B
    tpk_str = str(tpk)
    # B = str(round(B,3))
    Bi = str(Bi)
    packing_plate_bolted_eqn = Math(inline=True)
    # packing_plate_bolted_eqn.append(NoEscape(r'\begin{aligned} &if~l\leq 15 * d~then~V_{rd} = \beta_{ij} * V_{db} \\'))
    # packing_plate_bolted_eqn.append(NoEscape(r'& where,\\'))

    packing_plate_bolted_eqn.append(NoEscape(r'\begin{aligned} t_{pk}&= gap \\'))
    packing_plate_bolted_eqn.append(NoEscape(r' &= ' + tpk_str + ' mm 'r'\\'))
    if tpk <= 6:
        packing_plate_bolted_eqn.append(NoEscape(r'& since,~t_{pk} ~\leq~ 6 mm ~then~V_{rd} = V_{db}\\'))
        # packing_plate_bolted_eqn.append(NoEscape(r'& V_{rd} = '+Tc+r' \\'))
        packing_plate_bolted_eqn.append(NoEscape(r'&[Ref.~IS~800:2007,~Cl.~10.3.3.3]\end{aligned}'))
    else:
        packing_plate_bolted_eqn.append(NoEscape(r'& since,~t_{pk} \geq 6 mm~then~V_{rd} = \beta_{pk}~V_{db} \\'))
        packing_plate_bolted_eqn.append(NoEscape(r'& \beta_{pk} = 1.0 - 0.0125 \times '+tpk_str+' ='+Bi+r'\\'))

        # packing_plate_bolted_eqn.append(NoEscape(r'& V_{rd} = '+B+' \times '+Tc+'='+Tr+ r' \\'))
        packing_plate_bolted_eqn.append(NoEscape(r'&[Ref.~IS~800:2007,~Cl.~10.3.3.3]\end{aligned}'))

    return packing_plate_bolted_eqn


def bolt_capacity_reduced_req():
    """
     Returns:
        Bolt capacity post reduction factors
    Note:
              Reference:
              IS 800:2007,  cl 10.3.3
    """
    bolt_capacity_reduced_eqn = Math(inline=True)
    bolt_capacity_reduced_eqn.append(NoEscape(r'\begin{aligned} V_{rd} &= \beta_{lj}~\beta_{lg}~\beta_{pk}~V_{db} \\'))

    return bolt_capacity_reduced_eqn


def bolt_capacity_reduced_prov(beta_lj, beta_lg, beta_pk, Vdb):
    """
    Calculate reduced bolt capacity

    Args:
         beta_lj : Long joint reduction factor
         beta_lg : Large grip reduction factor
         beta_pk : Packing plate reduction factor
         V_{db} : Original Bolt Capacity
    Returns:
        Reduced bolt capacity
    Note:
              Reference:
              IS 800:2007,  cl 10.3.3

    """
    Blj = beta_lj
    Blg = beta_lg
    Bpk = beta_pk
    Vred = Blj * Blg * Bpk * Vdb
    Vdb = round(Vdb, 2)
    Vred = round(Vred, 2)
    Blj_str = str(round(Blj, 3))
    Blg_str = str(round(Blg, 3))
    Bpk_str = str(round(Bpk, 3))
    Vdb_str = str(round(Vdb,2))
    Vred_str = str(Vred)

    bolt_capacity_reduced_eqn = Math(inline=True)
    # packing_plate_bolted_eqn.append(NoEscape(r'\begin{aligned} &if~l\leq 15 * d~then~V_{rd} = \beta_{ij} * V_{db} \\'))
    # packing_plate_bolted_eqn.append(NoEscape(r'& where,\\'))
    bolt_capacity_reduced_eqn.append(
        NoEscape(r'\begin{aligned} V_{rd} &= \beta_{lj}~\beta_{lg} \beta_{pk} \times V_{db} \\'))
    bolt_capacity_reduced_eqn.append(
        NoEscape(r' &= ' + Blj_str + r' \times ' + Blg_str + r' \times ' + Bpk_str + r' \times ' + Vdb_str + r'\\'))

    bolt_capacity_reduced_eqn.append(NoEscape(r' &= ' + Vred_str + r'\\'))

    bolt_capacity_reduced_eqn.append(NoEscape(r'&[Ref.~IS~800:2007,~Cl.~10.3.3]\end{aligned}'))

    return bolt_capacity_reduced_eqn


def long_joint_bolted_beam(nc,nr,p,g,d,Tc,Tr,joint,end_dist,gap,edge_dist,web_thickness,root_radius,conn=None):
    """
    Calculate reduced bolt capacity in case of long joint

    Args:

        nc:No. of row of bolts in one line (int)
        nr:No. of  bolts in one line (int)
        p:Pitch distance of the plate in mm (float)
        g:Gauge distance of the plate in mm (float)
        d:Diameter of the bolt in mm (float)
        Tc:Bolt capacity  in KN (float)
        Tr: Reduced bolt capacity  in KN (float)
        joint:Flange or web (str)
        end_dist: flange plate end distance in mm (float)
        gap:gap between flange plate in mm (float)
        edge_dist: flane plate edge distance in mm (float)
        web_thickness: web thickness in mm (float)
        root_radius: root radius of the section in mm (float)
    Returns:
        reduced bolt capacity in case of long joint
    Note:
              Reference:
              IS 800:2007,  cl 10.3.3.1

    """

    if joint == 'web':
        lc = round(2*((nc/2 - 1) * p + end_dist) + gap ,2)
        lr = round((nr - 1) * g,2)
    else:
        lc = round(2*((nc/2 - 1) * p + end_dist) +gap ,2)
        lr = round(2*((nr/2 - 1) * g + edge_dist +root_radius ) + web_thickness ,2)

    l = round(max(lc,lr) ,2)

    lt = 15 * d
    B = 1.075 - (l / (200 * d))
    # Bi = round(B,2)
    nc= str(nc)
    nr= str(nr)
    g= str(g)
    p = str(p)
    d = str(d)
    Tc = str(Tc)
    Tr = str(Tr)
    if B<=0.75:
        B =0.75
    elif B>=1:
        B =1
    else:
        B=B
    B = round(B,2)
    Bi = str(B)
    lc_str = str(lc)
    lr_str = str(lr)
    l_str = str(l)
    lt_str = str(lt)
    end_dist =str(end_dist)

    edge_dist = str(edge_dist)
    web_thickness = str(web_thickness)
    gap =str(gap)
    root_radius =str(root_radius)
    long_joint_bolted_eqn = Math(inline=True)
    # long_joint_bolted_eqn.append(NoEscape(r'\begin{aligned} &if~l\leq 15 * d~then~V_{rd} = \beta_{lj} * V_{db} \\'))
    # long_joint_bolted_eqn.append(NoEscape(r'& where,\\'))
    if l < (lt):

        if joint == 'web':
            long_joint_bolted_eqn.append(NoEscape(r'\begin{aligned} l&= ((nc~or~nr) - 1) \times (p~or~g) \\'))
            if conn =="beam_beam":
                long_joint_bolted_eqn.append(NoEscape( r' lr &= 2\times((\frac{' + nc + r'}{2} - 1) \times ' + p + '+' + end_dist + ')+ ' + gap + r'\\&=' + lc_str + r'\\'))
                long_joint_bolted_eqn.append(NoEscape(r' lc &= (' + nr + r' - 1) \times ' + g + '=' + lr_str + r'\\'))
            elif conn =="col_col":
                long_joint_bolted_eqn.append(NoEscape(r' lc &= 2 \times ((\frac{' + nc + r'}{2} - 1) \times ' + p + '+' + end_dist + ')+ ' + gap + r'\\&=' + lc_str + r'\\'))
                long_joint_bolted_eqn.append(NoEscape(r' lr &= (' + nr + r' - 1) \times ' + g + '=' + lr_str + r'\\'))
            else:
                long_joint_bolted_eqn.append(NoEscape(r' lc &= 2\times((\frac{' + nc + r'}{2} - 1) \times ' + p + '+' + end_dist + ')+ ' + gap + r'\\&=' + lc_str + r'\\'))
                long_joint_bolted_eqn.append(NoEscape(r' lr &= (' + nr + r' - 1) \times ' + g + '=' + lr_str + r'\\'))

            long_joint_bolted_eqn.append(NoEscape(r' l&= ' + l_str + r'\\'))
            long_joint_bolted_eqn.append(NoEscape(r'& 15d = 15 \times '+d+' = '+lt_str +r' \\'))
            long_joint_bolted_eqn.append(NoEscape(r'& since,~l < 15d~\\&then~V_{rd} = V_{db} \\'))
            long_joint_bolted_eqn.append(NoEscape(r'& V_{rd} = '+Tc+r' \\'))
            long_joint_bolted_eqn.append(NoEscape(r'&[Ref.~IS~800:2007,~Cl.~10.3.3.1]\end{aligned}'))
        else:
            long_joint_bolted_eqn.append(NoEscape(r'\begin{aligned} l~&= ((nc~or~nr) - 1) \times (p~or~g) \\'))
            if conn == "beam_beam":
                long_joint_bolted_eqn.append(NoEscape(r' lr&= 2\times((\frac{' + nc + r'}{2} - 1) \times ' + p + '+' + end_dist + ')+ ' + gap + r'\\&=' + lc_str + r'\\'))
                long_joint_bolted_eqn.append(NoEscape(r' lc&= 2\times((\frac{' + nr + r'}{2} - 1) \times ' + g + '+' + edge_dist + r'\\& +' + root_radius + ')+ ' + web_thickness + '=' + lr_str + r'\\'))
            elif conn == "col_col":
                long_joint_bolted_eqn.append(NoEscape(r' lc&= 2\times((\frac{' + nc + r'}{2} - 1) \times ' + p + '+' + end_dist + ')+ ' + gap + r'\\&=' + lc_str + r'\\'))
                long_joint_bolted_eqn.append(NoEscape(r' lr&= 2\times((\frac{' + nr + r'}{2} - 1) \times ' + g + '+' + edge_dist + r'\\& +' + root_radius + ')+ ' + web_thickness + '=' + lr_str + r'\\'))
            else:
                long_joint_bolted_eqn.append(NoEscape( r' lc&= 2\times((\frac{' + nc + r'}{2} - 1) \times ' + p + '+' + end_dist + ')+ ' + gap + r'\\&=' + lc_str + r'\\'))
                long_joint_bolted_eqn.append(NoEscape(r' lr&= 2\times((\frac{' + nr + r'}{2} - 1) \times ' + g + '+' + edge_dist + r'\\& +' + root_radius + ')+ ' + web_thickness + '=' + lr_str + r'\\'))

            long_joint_bolted_eqn.append(NoEscape(r' l~&= ' + l_str + r'\\'))
            long_joint_bolted_eqn.append(NoEscape(r'& 15d = 15 \times ' + d + ' = ' + lt_str + r' \\'))
            long_joint_bolted_eqn.append(NoEscape(r'& since,~l < 15d~ \\& then~V_{rd} = V_{db} \\'))
            long_joint_bolted_eqn.append(NoEscape(r'& V_{rd} = ' + Tc + r' \\'))
            long_joint_bolted_eqn.append(NoEscape(r'&[Ref.~IS~800:2007,~Cl.~10.3.3.1]\end{aligned}'))
    else:
        if joint == 'web':
            long_joint_bolted_eqn.append(NoEscape(r'\begin{aligned} l&= ((nc~or~nr) - 1) \times (p~or~g) \\'))
            if conn == "beam_beam":
                long_joint_bolted_eqn.append(NoEscape(r' lr&= 2\times((\frac{' + nc + r'}{2} - 1) \times' + p + '+' + end_dist + ')+ ' + gap + r'\\&=' + lc_str + r'\\'))
                long_joint_bolted_eqn.append(NoEscape(r' lc&= (' + nr + r' - 1) \times' + g + '=' + lr_str + r'\\'))
            elif conn == "col_col":
                long_joint_bolted_eqn.append(NoEscape(r' lc&= 2\times((\frac{' + nc + r'}{2} - 1) \times ' + p + '+' + end_dist + ')+ ' + gap + r'\\&=' + lc_str + r'\\'))
                long_joint_bolted_eqn.append(NoEscape(r' lr&= (' + nr + r' - 1) \times ' + g + '=' + lr_str + r'\\'))
            else:
                long_joint_bolted_eqn.append(NoEscape(r' lc&= 2\times((\frac{' + nc + r'}{2} - 1) \times ' + p + '+' + end_dist + ')+ ' + gap + r'\\&=' + lc_str + r'\\'))
                long_joint_bolted_eqn.append(NoEscape(r' lr&= (' + nr + r' - 1) \times ' + g + '=' + lr_str + r'\\'))

            long_joint_bolted_eqn.append(NoEscape(r' l&= ' + l_str + r'\\'))
            long_joint_bolted_eqn.append(NoEscape(r'& 15d = 15 \times' + d + ' = ' + lt_str + r' \\'))
            long_joint_bolted_eqn.append(NoEscape(r'&since,~l \geq 15d~ \\&then~V_{rd} = \beta_{lj} \times V_{db} \\'))
            long_joint_bolted_eqn.append(NoEscape(r'\beta_{lj} &= 1.075 - '+ l_str +r'/(200 \times'+d+r') \\&='+Bi+r'\\'))
            long_joint_bolted_eqn.append(NoEscape(r'V_{rd} &= '+Bi+r' \times'+Tc+'='+Tr+ r' \\'))
            long_joint_bolted_eqn.append(NoEscape(r'[Ref.&~IS~800:2007,~Cl.~10.3.3.1]&\end{aligned}'))
        else:
            long_joint_bolted_eqn.append(NoEscape(r'\begin{aligned} l~&= ((nc~or~nr) - 1) \times (p~or~g) \\'))
            if conn == "beam_beam":
                long_joint_bolted_eqn.append(NoEscape(r' lr&= 2\times((\frac{' + nc + r'}{2} - 1) \times ' + p + '+' + end_dist + ')+ ' + gap + r'\\&=' + lc_str + r'\\'))
                long_joint_bolted_eqn.append(NoEscape(r' lc&= 2\times((\frac{' + nr + r'}{2} - 1) \times ' + g + '+' + edge_dist +r'\\& +'+root_radius+')+ ' + web_thickness + '=' + lr_str + r'\\'))
            elif conn == "col_col":
                long_joint_bolted_eqn.append(NoEscape(r' lc&= 2\times((\frac{' + nc + r'}{2} - 1) \times ' + p + '+' + end_dist + ')+ ' + gap + r'\\&=' + lc_str + r'\\'))
                long_joint_bolted_eqn.append(NoEscape(r' lr&= 2\times((\frac{' + nr + r'}{2} - 1) \times ' + g + '+' + edge_dist + r'\\& +' + root_radius + ')+ ' + web_thickness + '=' + lr_str + r'\\'))
            else:
                long_joint_bolted_eqn.append(NoEscape(r' lc&= 2\times((\frac{' + nc + r'}{2} - 1) \times ' + p + '+' + end_dist + ')+ ' + gap + r'\\&=' + lc_str + r'\\'))
                long_joint_bolted_eqn.append(NoEscape( r' lr&= 2\times((\frac{' + nr + r'}{2} - 1) \times ' + g + '+' + edge_dist + r'\\& +' + root_radius + ')+ ' + web_thickness + '=' + lr_str + r'\\'))

            long_joint_bolted_eqn.append(NoEscape(r' l~&= ' + l_str + r'\\'))
            long_joint_bolted_eqn.append(NoEscape(r'&15d = 15 \times' + d + ' = ' + lt_str + r' \\'))
            long_joint_bolted_eqn.append(NoEscape(r'&since,~l \geq 15d~\\ &then~V_{rd} = \beta_{lj} \times V_{db} \\'))
            long_joint_bolted_eqn.append(NoEscape(r'\beta_{lj} &= 1.075 - '+ l_str +r'/(200\times'+d+ r')\\& ='+Bi+r'\\'))
            long_joint_bolted_eqn.append(NoEscape(r' V_{rd}& = '+Bi+ r' \times '+Tc+'='+Tr+ r' \\'))
            long_joint_bolted_eqn.append(NoEscape(r'[Ref.&~IS~800:2007,~Cl.~10.3.3.1]&\end{aligned}'))
    return long_joint_bolted_eqn


def long_joint_welded_req():

    long_joint_bolted_eqn = Math(inline=True)
    long_joint_bolted_eqn.append(NoEscape(r'\begin{aligned} &if~l\geq 150 t_t~then~V_{rd} = \beta_{l_w} V_{db} \\'))
    long_joint_bolted_eqn.append(NoEscape(r'& if~l < 150 t_t~then~V_{rd} = V_{db} \\'))
    long_joint_bolted_eqn.append(NoEscape(r'& where,\\'))
    long_joint_bolted_eqn.append(NoEscape(r'&  l ~= pt.length ~ or ~ pt.height \\'))
    long_joint_bolted_eqn.append(NoEscape(r'& \beta_{l_w} = 1.2 - \frac{(0.2 l )}{(150 t_t)}  \\'))
    long_joint_bolted_eqn.append(NoEscape(r'& but~0.6\leq\beta_{l_w}\leq1.0 \\'))
    long_joint_bolted_eqn.append(NoEscape(r'&[Ref.~IS~800:2007,~Cl.~10.5.7.3]&\end{aligned}'))
    return long_joint_bolted_eqn


def long_joint_welded_beam_prov(plate_height,l_w,t_w,gap,t_t,Tc,Tr):
    """
    Calculate Reduced flange weld strength  in case of long joint

    Args:
         plate_height:flange plate height in mm (float)
         l_w:available long flane length in mm (float)
         t_w:flange weld size in mm (float)
         gap:flange plate gap  in mm (float)
         t_t:flange weld throat thickness in mm (float)
         Tc:flange weld strength in KN (float)
         Tr:reduced flange weld strength in KN/mm (float)
    Returns:
        reduced flange weld strength in KN/mm (float)
    Note:
              Reference:
              IS 800:2007,  cl 10.5.7.3

    """
    ll = round(2*(l_w +(2*t_w)) +gap,2)
    lh = plate_height
    l = round(max(ll,lh) ,2)
    lt = 150 * t_t
    B = 1.2 - ((0.2 * l) / (150 * t_t))
    if B <= 0.6:
        B = 0.6
    elif B >= 1:
        B = 1
    else:
        B = B
    Bi = str(round(B, 2))
    t_t= str(t_t)
    # l =str(l)
    l_str= str(l)
    # lt = str(lt)
    lt_str = str(lt)

    # B = str(round(B, 2))
    # Bi = str(Bi)
    t_t= str(t_t)
    ll_str =str(ll)
    lh_str= str(lh)
    plate_height =str(plate_height)
    Tc = str(Tc)
    Tr = str(Tr)
    l_w  = str(l_w )

    t_w = str(t_w)
    l_w = str(l_w)
    gap = str(gap)
    long_joint_welded_beam_prov = Math(inline=True)
    # if conn =="web":
    if l < lt:
        long_joint_welded_beam_prov.append(NoEscape(r'\begin{aligned} l ~&= pt.length ~ or ~ pt.height \\'))
        long_joint_welded_beam_prov.append(NoEscape(r' l_l &= 2('+l_w +r'+(2 \times'+t_w+'))+'+gap+r' \\'))
        long_joint_welded_beam_prov.append(NoEscape(r' &='+ ll_str+ r' \\'))
        long_joint_welded_beam_prov.append(NoEscape(r'l_h& =' +lh_str+r' \\'))
        long_joint_welded_beam_prov.append(NoEscape(r' l~&= ' + l_str + r'\\'))
        long_joint_welded_beam_prov.append(NoEscape(r'& 150 \times t_t =150 \times'+t_t+' = '+lt_str +r' \\'))
        long_joint_welded_beam_prov.append(NoEscape(r'& since,~l < 150 \times t_t~\\&then~V_{rd} = V_{db} \\'))
        long_joint_welded_beam_prov.append(NoEscape(r' V_{rd} &= ' + Tc +r' \\'))
        long_joint_welded_beam_prov.append(NoEscape(r'[Ref.~&IS~800:2007,~Cl.~10.5.7.3]&\end{aligned}'))
    else:
        long_joint_welded_beam_prov.append(NoEscape(r'\begin{aligned} l~&= pt.length ~or ~pt.height \\'))
        long_joint_welded_beam_prov.append(NoEscape(r' l_l &= 2(' + l_w + r'+(2 \times' + t_w + '))+' + gap + r' \\'))
        long_joint_welded_beam_prov.append(NoEscape(r' &=' + ll_str + r' \\'))
        long_joint_welded_beam_prov.append(NoEscape(r' l_h& =' + lh_str + r' \\'))
        long_joint_welded_beam_prov.append(NoEscape(r' l~&= ' + l_str + r'\\'))
        long_joint_welded_beam_prov.append(NoEscape(r'& 150 \times t_t =150 \times' + t_t + ' = ' + lt_str + r' \\'))
        long_joint_welded_beam_prov.append(NoEscape(r'&since,~l \geq 150 \times t_t~ \\&then~V_{rd} = \beta_{lw} \times V_{db} \\'))
        long_joint_welded_beam_prov.append(NoEscape(r'\beta_{l_w}& = 1.2 - (0.2 \times' + l_str + r')/(150 \times' + t_t+ r')\\& =' + Bi + r'\\'))
        long_joint_welded_beam_prov.append(NoEscape(r' V_{rd}& = ' + Bi + r' \times' + Tc + '=' + Tr + r' \\'))
        long_joint_welded_beam_prov.append(NoEscape(r'[Ref.&~IS~800:2007,~Cl.~10.5.7.3]\end{aligned}'))

    return long_joint_welded_beam_prov


def bolt_red_capacity_prov(blj,blg,V,Vrd,type):
    blj = str(blj)
    blg = str(blg)
    V = str(V)
    Vrd = str(Vrd)
    bolt_capacity_eqn = Math(inline=True)
    if type == "b":
        bolt_capacity_eqn.append(NoEscape(r'\begin{aligned}V_{rd} &= \beta_{lj} \beta_{lg} V_{db} \\'))
        bolt_capacity_eqn.append(NoEscape(r' &= ' + blj + r'\times' + blg + r'\times' + V + r'\\'))
        bolt_capacity_eqn.append(NoEscape(r'& = ' + Vrd + r'\end{aligned}'))
    else:
        bolt_capacity_eqn.append(NoEscape(r'\begin{aligned}V_{rd} &= \beta_{lj} V_{db} \\'))
        bolt_capacity_eqn.append(NoEscape(r' &= ' + blj + r'\times' + V + r'\\'))
        bolt_capacity_eqn.append(NoEscape(r'& = ' + Vrd + r'\end{aligned}'))

    return bolt_capacity_eqn


########################################
# End of IS Code functions
##########################################
#Minimum loads functions
##########################################


def ir_sum_bb_cc(Al, M , A_c ,M_c,IR_axial ,IR_moment ,sum_IR):
    """

    :param Al:
    :param M:
    :param A_c:
    :param M_c:
    :param IR_axial:
    :param IR_moment:
    :param sum_IR:
    :return:
    """
    IR_axial = str(IR_axial)
    IR_moment = str(IR_moment)
    Al = str(Al)
    M = str(M)
    A_c = str(A_c)
    M_c = str(M_c)
    sum_IR =str(sum_IR)
    ir_sum_bb_cc_eqn = Math(inline=True)
    ir_sum_bb_cc_eqn.append(NoEscape(r'\begin{aligned} IR ~axial~~~~&= A_l / A_c \\'))
    ir_sum_bb_cc_eqn.append(NoEscape(r'& ='+ Al +'/'+ A_c+r' \\'))
    ir_sum_bb_cc_eqn.append(NoEscape(r'& ='+ IR_axial +r' \\'))

    ir_sum_bb_cc_eqn.append(NoEscape(r'IR ~moment &= M / M_c \\'))
    ir_sum_bb_cc_eqn.append(NoEscape(r'& =' + M + '/' + M_c + r' \\'))
    ir_sum_bb_cc_eqn.append(NoEscape(r'& =' + IR_moment + r' \\'))

    ir_sum_bb_cc_eqn.append(NoEscape(r'IR ~sum~~~~~ &= IR ~axial + IR ~moment  \\'))
    ir_sum_bb_cc_eqn.append(NoEscape(r'&= '+ IR_axial +'+ '+IR_moment + r' \\'))
    ir_sum_bb_cc_eqn.append(NoEscape(r'& =' + sum_IR + r'\end{aligned}'))
    return ir_sum_bb_cc_eqn


def min_loads_required(conn):
    """

    :param conn:
    :return:
    """
    min_loads_required_eqn= Math(inline=True)
    min_loads_required_eqn.append(NoEscape(r'\begin{aligned}  &if~~ IR ~axial < 0.3 ~and~ IR ~moment < 0.5 \\'))
    min_loads_required_eqn.append(NoEscape(r' &~~~Ac_{min} = 0.3 \times A_c\\'))
    min_loads_required_eqn.append(NoEscape(r' &~~~Mc_{min}= 0.5 \times M_c\\'))
    if conn =="beam_beam":
        min_loads_required_eqn.append(NoEscape(r' &elif~~ sum ~IR <= 1.0 ~and~ IR ~moment < 0.5\\'))
        min_loads_required_eqn.append(NoEscape(r'&~~~if~~ (0.5 - IR ~moment) < (1 - sum ~IR)\\'))
        min_loads_required_eqn.append(NoEscape(r'&~~~~~~Mc_{min} = 0.5 \times M_c\\'))
        min_loads_required_eqn.append(NoEscape(r'& ~~~else\\'))
        min_loads_required_eqn.append(NoEscape(r'&~~~~~~Mc_{min} = M + ((1 - sum ~IR) \times M_c)\\'))
        min_loads_required_eqn.append(NoEscape(r'&~~~Ac_{min} = AL \\'))

        min_loads_required_eqn.append(NoEscape(r'&elif~~ sum ~IR <= 1.0~ and~ IR ~axial < 0.3\\'))
        min_loads_required_eqn.append(NoEscape(r'&~~~if~~ (0.3 - IR ~axial) < (1 -  sum ~IR)\\'))
        min_loads_required_eqn.append(NoEscape(r'&~~~~~~Ac_{min} = 0.3 \times A_c\\'))
        min_loads_required_eqn.append(NoEscape(r'&~~~else~~\\'))
        min_loads_required_eqn.append(NoEscape(r'&~~~~~~Ac_{min} = AL + ((1 - sum ~IR) \times A_c)\\'))
        min_loads_required_eqn.append(NoEscape(r'&~~~Mc_{min} = M \\'))
    else:
        min_loads_required_eqn.append(NoEscape(r'&elif~~ sum ~IR <= 1.0~ and~ IR ~axial < 0.3\\'))
        min_loads_required_eqn.append(NoEscape(r'&~~~if~~ (0.3 - IR ~axial) < (1 -  sum ~IR)\\'))
        min_loads_required_eqn.append(NoEscape(r'&~~~~~~Ac_{min} = 0.3 \times A_c\\'))
        min_loads_required_eqn.append(NoEscape(r'&~~~else~~\\'))
        min_loads_required_eqn.append(NoEscape(r'&~~~~~~Ac_{min} = AL + ((1 - sum ~IR) \times A_c)\\'))
        min_loads_required_eqn.append(NoEscape(r'&~~~Mc_{min} = M \\'))

        min_loads_required_eqn.append(NoEscape(r' &elif~~ sum ~IR <= 1.0 ~and~ IR ~moment < 0.5\\'))
        min_loads_required_eqn.append(NoEscape(r'&~~~if~~ (0.5 - IR ~moment) < (1 - sum ~IR)\\'))
        min_loads_required_eqn.append(NoEscape(r'&~~~~~~Mc_{min} = 0.5 \times M_c\\'))
        min_loads_required_eqn.append(NoEscape(r'& ~~~else\\'))
        min_loads_required_eqn.append(NoEscape(r'&~~~~~~Mc_{min} = M + ((1 - sum ~IR) \times M_c)\\'))
        min_loads_required_eqn.append(NoEscape(r'&~~~Ac_{min} = AL \\'))

    min_loads_required_eqn.append(NoEscape(r'&else~~\\'))
    min_loads_required_eqn.append(NoEscape(r'&~~~Ac_{min} = AL\\'))
    min_loads_required_eqn.append(NoEscape(r'&~~~Mc_{min} = M \\'))
    min_loads_required_eqn.append(NoEscape(r'&~Note:~AL=~User~Applied~Load\end{aligned}'))
    return min_loads_required_eqn


def min_loads_provided(min_ac,min_mc,conn):
    """

    :param min_ac:
    :param min_mc:
    :param conn:
    :return: minimum moment (kNm) and axial(kN)
     Note:
            Reference:
            IS 800:2007,  cl 10.7
    """
    min_ac = str(min_ac)
    min_mc = str(min_mc)

    if conn == "beam_beam":
        min_loads_provided_eqn = Math(inline=True)
        min_loads_provided_eqn.append(NoEscape(r'\begin{aligned} & Mc_{min} =' + min_mc + r'\\'))
        min_loads_provided_eqn.append(NoEscape(r'& Ac_{min} =' + min_ac + r'\\'))
        min_loads_provided_eqn.append(NoEscape(r'&[Ref.~IS~800:2007,~Cl.~10.7]\end{aligned}'))
    else:
        min_loads_provided_eqn = Math(inline=True)
        min_loads_provided_eqn.append(NoEscape(r'\begin{aligned} & Ac_{min} =' + min_ac + r'\\'))
        min_loads_provided_eqn.append(NoEscape(r'& Mc_{min} =' + min_mc +  r'\\'))
        min_loads_provided_eqn.append(NoEscape(r'& [Ref.~IS~800:2007,~Cl.~10.7]\end{aligned}'))
    return min_loads_provided_eqn


def axial_capacity_req(axial_capacity,min_ac):
    """
    Calculate minimum  required axial capacity of member
    Args:
         axial_capacity:Axial capacity of member in KN
         min_ac: Minimum axial capacity of member in KN
    Returns:
         Minimum axial capacity of member in KN

    Note:
              Reference:
              IS 800:2007,  cl 10.7

    """

    min_ac = str(min_ac)
    axial_capacity = str(axial_capacity)
    ac_req_eqn = Math(inline=True)
    ac_req_eqn.append(NoEscape(r'\begin{aligned} Ac_{min} &= 0.3A_c\\'))
    ac_req_eqn.append(NoEscape(r'&= 0.3 \times' + axial_capacity + r'\\'))
    ac_req_eqn.append(NoEscape(r'&=' + min_ac + r'\\'))
    ac_req_eqn.append(NoEscape(r'Ac_{max} &=' +axial_capacity +r'\\'))
    ac_req_eqn.append(NoEscape(r'[Ref.~IS~&800:2007,~Cl.~10.7]&\end{aligned}'))


    return ac_req_eqn


def prov_axial_load(axial_input,min_ac,app_axial_load,axial_capacity):
    """
    Calculate load axial force for column end plate
    Args:
         axial_input:Axial load in KN (float)
         min_ac:Minimum axial load in KN (float)
         app_axial_load:Factored axial load in KN (float)
    Returns:
        Factored axial load
    Note:
              Reference:
              IS 800:2007,  cl 10.7

    """
    min_ac = str(min_ac)
    axial_input = str(axial_input)
    app_axial_load = str(app_axial_load)

    prov_axial_load_eqn = Math(inline=True)
    prov_axial_load_eqn.append(NoEscape(r'\begin{aligned} Au~~ &= max(A,Ac_{min} )\\'))
    prov_axial_load_eqn.append(NoEscape(r'&= max( ' + axial_input + ',' + min_ac + r')\\'))
    prov_axial_load_eqn.append(NoEscape(r'&=' + app_axial_load + r'\end{aligned}'))

    return prov_axial_load_eqn


def prov_shear_load(shear_input,min_sc,app_shear_load,shear_capacity_1):
    """
    Calculate maximum shear force
    Args:

        shear_input factored input shear force
        min_sc:Minimum shear force
        app_shear_load:Maximum of factored input shear force and minimum shear force
    Returns:
        maximum shear force
    Note:
              Reference:
              IS 800:2007,  cl 10.7


    """

    min_sc = str(min_sc)
    shear_input = str(shear_input)
    app_shear_load = str(app_shear_load)
    shear_capacity_1 = str(shear_capacity_1)
    app_shear_load_eqn = Math(inline=True)
    app_shear_load_eqn.append(NoEscape(r'\begin{aligned} Vc_{min} &=  min(0.15 \times V_{dy}, 40.0)\\'))
    app_shear_load_eqn.append(NoEscape(r'& =  min(0.15 \times'+ shear_capacity_1 +r', 40.0)\\'))
    app_shear_load_eqn.append(NoEscape(r'&=' + min_sc + r'\\'))
    app_shear_load_eqn.append(NoEscape(r'[Ref&.~IS~800:2007,~Cl.~10.7]\\'))
    app_shear_load_eqn.append(NoEscape(r' Vu~~ &= max(V,Vc_{min})\\'))
    app_shear_load_eqn.append(NoEscape(r'&=  max(' + shear_input + ',' + min_sc + r')\\'))
    app_shear_load_eqn.append(NoEscape(r'&=' + app_shear_load + r'\end{aligned}'))
    # app_shear_load_eqn.append(NoEscape(r'&[Ref.~IS~800:2007,~Cl.~8.4]&\end{aligned}'))


    return app_shear_load_eqn


def allow_shear_capacity(V_d, S_c):
    V_d = str(V_d)
    S_c = str(S_c)
    allow_shear_capacity_eqn = Math(inline=True)
    allow_shear_capacity_eqn.append(NoEscape(r'\begin{aligned} S_{c} &= 0.6~V_{dy}\\'))
    allow_shear_capacity_eqn.append(NoEscape(r'&=0.6 \times'+V_d+r'\\'))
    allow_shear_capacity_eqn.append(NoEscape(r'&=' + S_c + r'\\'))
    allow_shear_capacity_eqn.append(NoEscape(r'[Limited~&to~low~shear~capacity]\end{aligned}'))
    return allow_shear_capacity_eqn


def prov_moment_load(moment_input,min_mc,app_moment_load,moment_capacity):
    """
    Calculate max moment load of input moment and min moment of the section
    Args:

         moment_input:Factored input moment in KN (float)
         min_mc:Min moment of the section in KN (float)
         app_moment_load:Factored moment max of input moment and min moment of the section in KN (float)
    Returns:
         max moment load of input moment and min moment of the section
    Note:
              Reference:
              IS 800:2007,  cl 8.2.1.2

    """

    min_mc = str(min_mc)
    moment_input = str(moment_input)
    app_moment_load = str(app_moment_load)
    moment_capacity = str(moment_capacity)
    app_moment_load_eqn = Math(inline=True)
    # app_moment_load_eqn.append(NoEscape(r'\begin{aligned} Mc_{min} &= 0.5 * M_c\\'))
    # app_moment_load_eqn.append(NoEscape(r'&= 0.5 \times' + moment_capacity + r'\\'))
    # app_moment_load_eqn.append(NoEscape(r'&=' + min_mc + r'\\'))
    app_moment_load_eqn.append(NoEscape(r' \begin{aligned} Mu &= max(M,Mc_{min} )\\'))
    app_moment_load_eqn.append(NoEscape(r'&= max(' + moment_input + r',' + min_mc + r')\\'))
    app_moment_load_eqn.append(NoEscape(r'&=' + app_moment_load + r'\\'))
    app_moment_load_eqn.append(NoEscape(r'[Re&f.~IS~800:2007,~Cl.~8.2.1.2]\end{aligned}'))
    return  app_moment_load_eqn


##################################
# End of Min load functions
###################################
#Other bolt functions
###################################

def force_in_bolt_due_to_load(P,n,T_ba,load='tension'):
    P= str(P)
    n = str(n)
    T_ba = str (T_ba)
    tension_in_bolt_due_to_axial_load_n_moment  = Math(inline=True)
    if load == 'tension':
        tension_in_bolt_due_to_axial_load_n_moment.append(NoEscape(r'\begin{aligned} T_{ba} &= \frac{P}{\ n}\\'))
        tension_in_bolt_due_to_axial_load_n_moment.append(NoEscape(r'&=\frac{' +P + '}{' + n + r'}\\'))
    else:
        tension_in_bolt_due_to_axial_load_n_moment.append(NoEscape(r'\begin{aligned} V_{bv} &= \frac{V}{\ n}\\'))
        tension_in_bolt_due_to_axial_load_n_moment.append(NoEscape(r'&=\frac{' + P + '}{' + n + r'}\\'))
    tension_in_bolt_due_to_axial_load_n_moment.append(NoEscape(r'&= ' + T_ba + r'\end{aligned}'))
    return tension_in_bolt_due_to_axial_load_n_moment


def total_bolt_tension_force(T_ba,Q,T_b):
    T_ba = str(T_ba)
    Q = str(Q)
    T_b = str(T_b)
    total_tension_in_bolt = Math(inline = True)
    total_tension_in_bolt.append(NoEscape(r'\begin{aligned} T_b &= T_{ba} + Q\\'))
    total_tension_in_bolt.append(NoEscape(r'&=' + T_ba +'+'+ Q + r'\\'))
    total_tension_in_bolt.append(NoEscape(r'&='+ T_b + r'\end{aligned}'))
    return total_tension_in_bolt


def tension_in_bolt_due_to_axial_load_n_moment(P,n,M,y_max,y_sqr,T_b):
    """
    Calculate tension in bolt due to axial load n moment

    Args:
          P: external axial load in KN (float)
          n: no. of bolts (int)
          M:external moment in KN-mm (float)
          y_max:vertical distance of farthest bolt from center of flange in mm (float)
          y_sqr: distance of each bolt from center of flange in mm square (float)
          T_b: tension in bolt due to axial load n moment in KN (float)
    Returns:
          tension in bolt due to axial load n moment
    """
    P= str(P)
    n = str(n)
    M = str(M)
    y_max =str(y_max)
    y_sqr = str(y_sqr)
    T_b = str (T_b)
    tension_in_bolt_due_to_axial_load_n_moment  = Math(inline=True)
    tension_in_bolt_due_to_axial_load_n_moment.append(NoEscape(r'\begin{aligned} T_b &= \frac{P}{\ n} + \frac{M \times y_{max}}{\ y_{sqr}}\\'))
    tension_in_bolt_due_to_axial_load_n_moment.append(NoEscape(r'&=\frac{' +P +r'\times 10^3}{' + n + r'} + \frac{' +M +r'\times 10^6 \times' +  y_max+ r'}{' + y_sqr + r'}\\'))
    tension_in_bolt_due_to_axial_load_n_moment.append(NoEscape(r'&= ' + T_b + r'\end{aligned}'))
    return tension_in_bolt_due_to_axial_load_n_moment


def design_capacity_of_end_plate(M_dp,b_eff,f_y,gamma_m0,t_p):
    """
    Calculate design capacity of end plate
    Args:
         M_dp:Design capacity of end plate in N-mm (float)
         b_eff:Effective width for load dispersion
         f_y:Yeild strength of  plate material in N/mm square (float)
         gamma_m0: IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']  (float)
         t_p:Thickness of end plate
    Returns:
        design capacity of end plate

    """

    M_dp= str(M_dp)
    t_p = str(t_p)
    b_eff= str(b_eff)
    f_y= str(f_y)
    gamma_m0= str(gamma_m0)

    design_capacity_of_end_plate= Math(inline=True)

    design_capacity_of_end_plate.append(NoEscape(r'\begin{aligned}  M_{dp} & = { \frac{ b_{eff}~t_p^2~f_y}{ 4~\gamma_{m0}}}\\'))

    design_capacity_of_end_plate.append(NoEscape(r'&={\frac{' + b_eff +r'\times'+t_p+r'^2'+r' \times'+f_y + r'}{4 \times'+gamma_m0 + r'}}\\'))
    design_capacity_of_end_plate.append(NoEscape(r'&=' +M_dp  + r'\end{aligned}'))

    return design_capacity_of_end_plate


#####################################
# End of other bolt functions
#####################################
#common utility functions
#####################################

def required_IR_or_utilisation_ratio(IR):
    """
    :param IR:
    :return:
    """
    IR = str(IR)
    IR_req_eqn = Math(inline=True)
    IR_req_eqn.append(NoEscape(r'\begin{aligned} \leq'+IR+'\end{aligned}'))
    return IR_req_eqn


def display_prov(v, t, ref=None):
    """
    Args:
          v: value of t (float or int)
          t: typically a notation (string) (float)
          ref: unit of the value (ex: mm, kN)
                (can be none if it has no units)
    Returns:
          equation in form of t = v

    """

    v = str(v)
    display_eqn = Math(inline=True)
    if ref is not None:
        display_eqn.append(NoEscape(r'\begin{aligned} ' + t + ' &=' + v + '~(' + ref + r')\end{aligned}'))
    else:
        display_eqn.append(NoEscape(r'\begin{aligned} ' + t + ' &=' + v + r'\end{aligned}'))
    return display_eqn



def get_pass_fail(required, provided,relation='greater'):

    if provided == 0 or required == 'N/A' or provided == 'N/A' or required == 0:
        return ''
    else:
        if relation == 'greater':
            if required > provided:
                return 'Pass'
            else:
                return 'Fail'
        elif relation == 'geq':
            if required >= provided:
                return 'Pass'
            else:
                return 'Fail'
        elif relation == 'leq':
            if required <= provided:
                return 'Pass'
            else:
                return 'Fail'
        else:
            if required < provided:
                return 'Pass'
            else:
                return 'Fail'


def min_prov_max(min, provided,max):
    """
    Calculate min and maximum axial capacity (provided)
    Args:
        min:0.3*tension yeilding caapcity of the section
        provided:resisting force
        max:tension yeilding caapcity of the section
    Returns:
        min and maximum axial capacity (provided)
    """
    min = float(min)
    provided = float(provided)
    max = float(max)
    if provided==0:
        return 'N/A'
    else:
        if (max >= provided and min<=provided) or (min >= provided and max<=provided):
            return 'Pass'
        else:
            return 'Fail'

#####################################
#End of common utility functions
#####################################

def end_plate_gauge(connection,e_min,s,t_w,T_w,R_r,module='None'):
    g1 = round(2*(e_min+s)+t_w,2)
    g2 = round(2*(e_min+R_r)+T_w,2)
    g_min = round(max(g1,g2),2)
    g1 = str(g1)
    g2 =str(g2)
    g_min=str(g_min)
    e_min=str(e_min)
    s=str(s)
    t_w=str(t_w)
    T_w = str(T_w)
    R_r = str(R_r)
    end_plate_gauge = Math(inline=True)
    if connection == VALUES_CONN_1[0]:
        end_plate_gauge.append(NoEscape(r'\begin{aligned}g_1 &= 2(e`_{min}+s)+t_w\\'))
        end_plate_gauge.append(NoEscape(r'&= 2(' + e_min + '+' + s + ')+' + t_w + r'\\'))
        end_plate_gauge.append(NoEscape(r'&=' + g1 + r'\\'))
        end_plate_gauge.append(NoEscape(r'g_2 &= 2(e`_{min}+R_r)+T_w\\'))
        end_plate_gauge.append(NoEscape(r'&= 2(' + e_min + '+' + R_r + ')+' + T_w + r'\\'))
        end_plate_gauge.append(NoEscape(r'&='+g2+r'\\'))
        end_plate_gauge.append(NoEscape(r'g_{min}&= max(g_1,g_2)\\'))
        end_plate_gauge.append(NoEscape(r'&='+g_min+r' \end{aligned}'))
    else:
        end_plate_gauge.append(NoEscape(r'\begin{aligned}g_{min} &= 2(e`_{min}+s)+t_w\\'))
        end_plate_gauge.append(NoEscape(r'&= 2(' + e_min + '+' + s + ')+' + t_w + r'\\'))
        end_plate_gauge.append(NoEscape(r'&=' + g1 + r' \end{aligned}'))

    return end_plate_gauge


def row_col_limit(min=1,max=None,parameter ="rows"):
    min = str(min)
    max = str(max)
    row_col_limit_eqn = Math(inline=True)
    if max != None and parameter == "rows":
        row_col_limit_eqn.append(NoEscape(r'\begin{aligned}'+min+r' \leq n_r \leq'+ max+r' \end{aligned}'))
    elif max == None and parameter == "rows":
        row_col_limit_eqn.append(NoEscape(r'\begin{aligned} n_r \geq'+ min + r' \end{aligned}'))
    elif max != None and parameter == "cols":
        row_col_limit_eqn.append(NoEscape(r'\begin{aligned}' + min + r' \leq n_c \leq' + max + r' \end{aligned}'))
    elif max == None and parameter == "cols":
        row_col_limit_eqn.append(NoEscape(r'\begin{aligned} n_c \geq' + min + r' \end{aligned}'))
    else:
        return None

    return row_col_limit_eqn


def get_trial_bolts(V_u, A_u,bolt_capacity,multiple=1,conn=None):

    """
    Calculate Total no. of bolts required for both side of web/ flange splices

    Args:
        V_u:Actual  shear force acting on the bolt(direct shear+ force due to eccentricity) in KN
        A_u: Axial force acting on the bolt in KN
        bolt_capacity: Capacity of  web/flange bolt  in KN
        multiple: 2 for web ,4 for flange  (int)
    Returns:
          Total no. of bolts required for both side of web/ flange splices
    """

    res_force = math.sqrt(V_u**2+ A_u**2)
    trial_bolts = multiple * math.ceil(res_force/bolt_capacity)
    V_u=str(V_u)
    A_u=str(A_u)
    bolt_capacity=str(bolt_capacity)
    trial_bolts=str(trial_bolts)
    trial_bolts_eqn = Math(inline=True)
    trial_bolts_eqn.append(NoEscape(r'\begin{aligned}R_{u} &= \sqrt{V_u^2+A_u^2}\\'))
    trial_bolts_eqn.append(NoEscape(r'n_{trial} &= R_u/ V_{bolt}\\'))
    if conn == "flange_web":
        trial_bolts_eqn.append(NoEscape(r'R_{u} &= \frac{2 \times \sqrt{' + V_u + r'^2+' + A_u + r'^2}}{' + bolt_capacity + r'}\\'))
    else:
        trial_bolts_eqn.append(NoEscape(r'R_{u} &= \frac{\sqrt{'+V_u+r'^2+'+A_u+r'^2}}{'+bolt_capacity+ r'}\\'))
    trial_bolts_eqn.append(NoEscape(r'&='+trial_bolts+ r'\end{aligned}'))
    return trial_bolts_eqn


def parameter_req_bolt_force(bolts_one_line,gauge,ymax,xmax,bolt_line,pitch,length_avail, conn=None):
    """
    Calculate xmax and ymax
    Args:
        bolts_one_line: No. of bolts in one row (float)
        gauge: Gauge distance in mm (float)
        ymax: Vertical distance of farthest bolt from center of rotation of bolt group in mm (float)
        xmax: :Horizontal distance of farthest bolt from center of rotation of bolt group in mm (float)
        bolt_line: No. of row of bolts (float)
        pitch: Pitch distance in mm (float)
        length_avail: Length available in mm  (float)
        conn:Connection type (str)
    Returns:
         xmax and ymax

    """

    bolts_one_line = str(bolts_one_line)
    ymax = str(ymax)
    xmax = str(xmax)
    gauge = str(gauge)
    pitch = str(pitch)
    bolt_line = str(bolt_line)
    length_avail = str(length_avail)

    parameter_req_bolt_force_eqn = Math(inline=True)
    parameter_req_bolt_force_eqn.append(NoEscape(r'\begin{aligned} l_n~~~ &= length~available \\'))
    if conn == 'fin':
        parameter_req_bolt_force_eqn.append(NoEscape(r' l_n~~~ &= p~(n_r - 1)\\'))
    elif conn == 'beam_beam':
        parameter_req_bolt_force_eqn.append(NoEscape(r' l_n~~~ &= g~(n_r - 1)\\'))
    elif conn== 'col_col':
        parameter_req_bolt_force_eqn.append(NoEscape(r' l_n~~~ &= g~(n_c - 1)\\'))
    parameter_req_bolt_force_eqn.append(NoEscape(r' &= '+gauge+r' \times (' + bolts_one_line + r' - 1)\\'))
    parameter_req_bolt_force_eqn.append(NoEscape(r' & ='+length_avail+ r'\\'))

    parameter_req_bolt_force_eqn.append(NoEscape(r' y_{max} &= l_n / 2\\'))
    parameter_req_bolt_force_eqn.append(NoEscape(r' &= '+length_avail+ r' / 2 \\'))
    parameter_req_bolt_force_eqn.append(NoEscape(r' & =' + ymax + r'\\'))


    if conn == 'fin':
        parameter_req_bolt_force_eqn.append(NoEscape(r'x_{max} &= g(n_c - 1)/2 \\'))
        parameter_req_bolt_force_eqn.append(NoEscape(r' &= '+pitch+r' \times (\frac{'+bolt_line+ r'}{2} - 1) / 2 \\'))
    elif conn == 'col_col':
        parameter_req_bolt_force_eqn.append(NoEscape(r'x_{max} &= p(\frac{n_r}{2} - 1) / 2 \\'))
        parameter_req_bolt_force_eqn.append(NoEscape(r' &= ' + pitch + r' \times (\frac{' + bolt_line + r'}{2} - 1) / 2 \\'))
    else:
        parameter_req_bolt_force_eqn.append(NoEscape(r'x_{max} &= p(\frac{n_c}{2} - 1) / 2 \\'))
        parameter_req_bolt_force_eqn.append(NoEscape(r' &= ' + pitch + r' \times (\frac{' + bolt_line + r'}{2} - 1) / 2 \\'))


    parameter_req_bolt_force_eqn.append(NoEscape(r' & =' + xmax + r'\end{aligned}'))

    return parameter_req_bolt_force_eqn


def moment_demand_req_bolt_force(shear_load, web_moment,moment_demand,ecc):
    """
     Calculate moment demand on web section
     Args:
          shear_load: Factored shear force acting on member in KN (float)
          web_moment: Moment in web in KN-m (float)
          moment_demand: Moment demand by section in N-mm (float)
          ecc:Distance between bolt center line toface of connected supporting section in mm (float)
    Returns:
          Moment demand on  web section in N-mm (float)

    """

    ecc = str(ecc)
    web_moment = str(web_moment)
    moment_demand = str(moment_demand)
    shear_load = str(shear_load)
    loads_req_bolt_force_eqn = Math(inline=True)


    loads_req_bolt_force_eqn.append(NoEscape(r'\begin{aligned}  M_d &= (V_u \times ecc + M_w)\\'))
    loads_req_bolt_force_eqn.append(NoEscape(r'ecc &= eccentricity\\'))
    loads_req_bolt_force_eqn.append(NoEscape(r' &= \frac{('+shear_load+r' \times 10^3 \times'+ecc+' + '+web_moment+r'\times 10^6)}{10^6}\\'))
    loads_req_bolt_force_eqn.append(NoEscape(r' & =' + moment_demand + r'\end{aligned}'))
    return loads_req_bolt_force_eqn


def Vres_bolts(bolts_one_line,ymax,xmax,bolt_line,axial_load ,moment_demand,r,vbv,tmv,tmh,abh,vres,shear_load,conn=None):
    """
    Calculte resultant shear load on each bolt
    Args:
         bolts_one_line: No. of bolts provided in one row (int)
         ymax: Vertical distance of farthest bolt from center of rotation of bolt group in mm (float)
         xmax:Horizontal   distance of farthest bolt from center of rotation of bolt group in mm (float)
         bolt_line: NO. of row of bolts (int)
         axial_load: Axial compressive force due to factored loads in KN (float)
         moment_demand:Moment demand on  web section in KN-mm (float)
         r: Distance of each bolt from center of rotation of each group in mm (float)
         vbv: Horizontal force acting on each bolt in KN (float)
         tmv:Vertical shear force acting on each bolt due to moment devloped by ecentricity in KN (float)
         tmh: Horizontal shear force acting on each bolt due to moment devloped by ecentricity in KN (float)
         abh: Vertical force acting on each bolt in KN (float)
         vres: Resultant sher load on  each bolt in KN (float)
         shear_load: Factored shear force acting on member in KN (float)
    Returns:
          Resultant shear load on bolt in KN (float)

    """


    bolts_one_line =str(bolts_one_line)
    ymax =str(ymax)
    xmax =str(xmax)
    bolt_line = str(bolt_line)

    r = str(r)
    moment_demand = str(moment_demand)
    axial_load =str(axial_load)
    shear_load = str(shear_load)
    vbv =str(vbv)
    tmv =str(tmv)
    tmh =str(tmh)
    abh =str(abh)
    vres = str(vres)
    Vres_bolts_eqn = Math(inline=True)
    if conn == "beam_beam":
        Vres_bolts_eqn.append(NoEscape(r'\begin{aligned} vbv~~ &= V_u / (n_r \times (n_c/2))\\'))
        Vres_bolts_eqn.append(NoEscape(r' &= \frac{'+shear_load+ '}{ ('+bolts_one_line +r'\times ('+ bolt_line+r'/2))}\\'))
    elif conn == "col_col":
        Vres_bolts_eqn.append(NoEscape(r'\begin{aligned} vbv~~ &= V_u / ((n_r/2) \times n_c)\\'))
        Vres_bolts_eqn.append(NoEscape(r' &= \frac{' + shear_load + '}{ (' + bolts_one_line +r'\times (' + bolt_line + r'/2))}\\'))
    else:
        Vres_bolts_eqn.append(NoEscape(r'\begin{aligned} vbv~~ &= V_u / (n_r \times n_c)\\'))
        Vres_bolts_eqn.append(NoEscape(r' &= \frac{' + shear_load + '}{ (' + bolts_one_line +r'\times' + bolt_line + r')}\\'))

    Vres_bolts_eqn.append(NoEscape(r' & =' + vbv + r'\\'))
    Vres_bolts_eqn.append(NoEscape(r'tmh~ &= \frac{M_d \times y_{max} }{ \Sigma r_i^2} \\'))
    Vres_bolts_eqn.append(NoEscape(r' &= \frac{'+moment_demand+r'\times'+ ymax+'}{'+r+r'}\\'))
    Vres_bolts_eqn.append(NoEscape(r' & =' + tmh + r'\\'))

    Vres_bolts_eqn.append(NoEscape(r' tmv ~&= \frac{M_d \times x_{max}}{\Sigma r_i^2}\\'))
    Vres_bolts_eqn.append(NoEscape(r'&= \frac{' +moment_demand+r'\times '+xmax+'}{'+r+ r'}\\'))
    Vres_bolts_eqn.append(NoEscape(r' & =' + tmv + r'\\'))
    if conn == "beam_beam":
        Vres_bolts_eqn.append(NoEscape(r' abh~ & = \frac{A_u }{(n_r \times n_c/2)}\\'))
        Vres_bolts_eqn.append(NoEscape(r'  & =\frac{' + axial_load + '}{ (' + bolts_one_line + r' \times (' + bolt_line + r'/2))}\\'))
    elif conn == "col_col":
        Vres_bolts_eqn.append(NoEscape(r' abh~ & = \frac{A_u }{((n_r/2) \times n_c)}\\'))
        Vres_bolts_eqn.append(NoEscape(r'  & =\frac{' + axial_load + '}{ (' + bolts_one_line + r' \times (' + bolt_line + r'/2))}\\'))
    else:
        Vres_bolts_eqn.append(NoEscape(r' abh~ & = \frac{A_u }{(n_r \times n_c)}\\'))
        Vres_bolts_eqn.append(NoEscape(r'  & =\frac{' + axial_load + '}{ (' + bolts_one_line + r' \times' + bolt_line + r')}\\'))

    Vres_bolts_eqn.append(NoEscape(r' & =' + abh + r'\\'))
    Vres_bolts_eqn.append(NoEscape(r' vres &=\sqrt{(vbv +tmv) ^ 2 + (tmh+abh) ^ 2}\\'))
    # Vres_bolts_eqn.append(NoEscape(r' vres &= \sqrt((vbv + tmv) ^ 2 + (tmh + abh) ^ 2)\\'))
    Vres_bolts_eqn.append(NoEscape(r'  &= \sqrt{('+vbv+' +'+ tmv+') ^2 + ('+tmh +'+'+ abh+r') ^ 2}\\'))
    Vres_bolts_eqn.append(NoEscape(r' & =' + vres +  r'\end{aligned}'))

    return Vres_bolts_eqn


def forces_in_web(Au,T,A,t,D,Zw,Mu,Z,Mw,Aw):
    """
    Calculate axial force in web and moment in web
    Args:
         Au: Gross area of web cover plate in mm^2 (float)
         T: Thickness of flaNGE in mm (float)
         A: Total area of smaller column in mm square (float)
         t: Thickness of web in mm (float)
         D: Depth of the column in mm (float)
         Zw: Section modules of web in mm^4 (float)
         Mu: Factored bending moment in N-mm (float)
         Z: Section modules of section in mm^4 (float)
         Mw:Moment in web in N-mm (float)
         Aw: Vertical compression force carried by web of the section
    Returns:
          Web axial force and moment in web
    """
    Au = str(Au)
    T = str(T)
    A = str(A)
    t = str(t)
    D = str(D)
    Zw = str(Zw)
    Mu = str(Mu)
    Z = str(Z)
    Mw = str(Mw)
    Aw = str(Aw)
    forcesinweb_eqn = Math(inline=True)

    forcesinweb_eqn.append(NoEscape(r'\begin{aligned}A_w &= Axial~ force~ in~ web  \\'))
    forcesinweb_eqn.append(NoEscape(r'  &= \frac{(D- 2T)~t~Au }{A} \\'))
    forcesinweb_eqn.append(NoEscape(r'&= \frac{(' + D + r'- 2 \times' + T + r') \times' + t +r'\times' + Au + ' }{' + A + r'} \\'))
    forcesinweb_eqn.append(NoEscape(r'&=' + Aw + r'~ kN\\'))
    forcesinweb_eqn.append(NoEscape( r'M_w &= Moment ~in ~web  \\'))
    forcesinweb_eqn.append(NoEscape(r' &= \frac{Z_w \times Mu}{Z} \\'))
    forcesinweb_eqn.append(NoEscape(r'&= \frac{' + Zw + r' \times ' + Mu + '}{' + Z + r'} \\'))
    forcesinweb_eqn.append(NoEscape(r'&=' + Mw + r'~{kNm}\end{aligned}'))
    return forcesinweb_eqn


def forces_in_flange(Au, B,T,A,D,Mu,Mw,Mf,Af,ff):
    """
    Calculate forces in flange and flange moment
    Args:
         Au: Factored axial force in KN (float)
         B: Width of flange in mm (float)
         T: Thikness of flange in mm (float)
         A: Total area of smaller column in mm square (float)
         D: Depth of column in mm (float)
         Mu: Factored bending moment in KN-mm (float)
         Mw: Moment in web in KN-mm (float)
         Mf: Moment in flange in KN-mm (float)
         Af: Axial force in flange in KN (float)
         ff: Force in each cover plate due to moment in KN (float)
    Returns:
          Flange moment,force in each cover plate due to moment,Axial and flange force

    """
    Au =str(Au)
    B=str(B)
    T=str(T)
    A=str(A)
    D=str(D)
    Mu=str(Mu)
    Mw=str(Mw)
    Mf=str(Mf)
    Af=str(Af)
    ff = str(ff)
    forcesinflange_eqn= Math(inline=True)
    forcesinflange_eqn.append(NoEscape(r'\begin{aligned} A_f&= Axial~force~ in ~flange  \\'))
    forcesinflange_eqn.append(NoEscape(r'&= \frac{Au~B~T}{A} \\'))
    forcesinflange_eqn.append(NoEscape(r'&= \frac{' + Au + r' \times ' + B +r'\times' + T + '}{' + A + r'} \\'))
    forcesinflange_eqn.append(NoEscape(r'&=' + Af + r'~ kN\\'))
    forcesinflange_eqn.append(NoEscape(r'M_f& =Moment~ in~ flange \\'))
    forcesinflange_eqn.append(NoEscape(r' & = Mu-M_w\\'))
    forcesinflange_eqn.append(NoEscape(r'&= ' + Mu + '-' + Mw + r'\\'))
    forcesinflange_eqn.append(NoEscape(r'&=' + Mf + r'~{kNm}\\'))
    forcesinflange_eqn.append(NoEscape(r' F_f& =flange~force  \\'))
    forcesinflange_eqn.append(NoEscape(r'& = \frac{M_f \times 10^3}{D-T} + A_f \\'))
    forcesinflange_eqn.append(NoEscape(r'&= \frac{' + Mf +r'\times 10^3}{' + D + '-' + T + '} +' + Af + r' \\'))
    forcesinflange_eqn.append(NoEscape(r'&=' + ff + r'~kN \end{aligned}'))

    return forcesinflange_eqn


def min_plate_ht_req(beam_depth,min_plate_ht):
    """
    Calculate min plate height required
    Args:
        beam_depth: Depth of section in mm (float)
        min_plate_ht:Min plate height required in mm (float)
    Returns:
          Min plate height required
    Note:
            Reference:
            INSDAG - Chapter 5, Section 5.2.3

    """
    beam_depth = str(beam_depth)
    min_plate_ht = str(round(min_plate_ht,2))
    min_plate_ht_eqn = Math(inline=True)
    min_plate_ht_eqn.append(NoEscape(r'\begin{aligned}&0.6~d_b= 0.6 \times '+ beam_depth + r'='+min_plate_ht+r'\\'))
    min_plate_ht_eqn.append(NoEscape(r'&[Ref.~ INSDAG-Chpt.5,~Sect. 5.2.3]\end{aligned}'))


    return min_plate_ht_eqn


def min_flange_plate_ht_req(beam_width,min_flange_plate_ht):## when only outside plate is considered
    """
    Calculate  Min flane plate height
    Args:
           beam_width: Width of section in mm (float)
           min_flange_plate_ht:Min flange plate height in mm (float)
    Returns:
           Required min flange plate height in mm (float)
    """
    beam_width = str(beam_width)
    min_flange_plate_ht = str(min_flange_plate_ht)
    min_flange_plate_ht_eqn = Math(inline=True)
    min_flange_plate_ht_eqn.append(NoEscape(r'\begin{aligned}min~flange~plate~ht &= beam~width\\'))
    min_flange_plate_ht_eqn.append(NoEscape(r'&='+min_flange_plate_ht+r'\end{aligned}'))

    return min_flange_plate_ht_eqn


def min_inner_flange_plate_ht_req(beam_width, web_thickness,root_radius,min_inner_flange_plate_ht): ## when inside and outside plate is considered #todo
    """
    Calculate minimum inner flange plate height
    Args:
        beam_width: Width of section in mm (float)
        web_thickness: Web thickness in mm (float)
        root_radius: Root radius in mm (float)
        min_inner_flange_plate_ht: Min inner flange plate height  in mm (float)
    Returns:
         Minimum inner flange plate height
    """
    beam_width = str(beam_width) ### same function used for max height
    min_inner_flange_plate_ht = str(min_inner_flange_plate_ht)
    web_thickness=str(web_thickness)
    root_radius=str(root_radius)
    min_inner_flange_plate_ht_eqn = Math(inline=True)
    min_inner_flange_plate_ht_eqn.append(NoEscape(r'\begin{aligned}&= \frac{B -t- (2R1)}{2}\\'))
    min_inner_flange_plate_ht_eqn.append(NoEscape(r'&=\frac{'+beam_width+ r' -' +web_thickness+ r' - 2 \times'+ root_radius+r'}{2}\\'))
    min_inner_flange_plate_ht_eqn.append(NoEscape(r'&='+min_inner_flange_plate_ht+r'\end{aligned}'))

    return min_inner_flange_plate_ht_eqn


def max_plate_ht_req(connectivity,beam_depth, beam_f_t, beam_r_r, notch, max_plate_h):
    """
    Calculate maximum height for fin plate
    Args:
          connectivity:
          beam_depth:Section depth in mm (float)
          beam_f_t: Flange thickness in mm  (float)
          beam_r_r:Root radius in mm  (float)
          notch: Supported section notch height in mm  (float)
          max_plate_h: Fin plate of max height in mm  (float)
    Returns:
          Maximum height for Fin plate
    """
    beam_depth = str(beam_depth)
    beam_f_t = str(beam_f_t)
    beam_r_r = str(beam_r_r)
    max_plate_h = str(max_plate_h)
    notch = str(notch)
    max_plate_ht_eqn = Math(inline=True)
    if connectivity in VALUES_CONN_1:
        max_plate_ht_eqn.append(NoEscape(r'\begin{aligned} &d_b - 2 (t_{bf} + r_{b1} + gap)\\'))
        max_plate_ht_eqn.append(NoEscape(r'&='+beam_depth+ r'- 2 \times (' + beam_f_t + '+' + beam_r_r +r'+ 10)\\'))
    else:
        max_plate_ht_eqn.append(NoEscape(r'\begin{aligned} &d_b - t_{bf} + r_{b1} - notch_h\\'))
        max_plate_ht_eqn.append(NoEscape(r'&=' + beam_depth + '-' + beam_f_t + '+' + beam_r_r + '-'+ notch+ r'\\'))
    max_plate_ht_eqn.append(NoEscape(r'&=' + max_plate_h + '\end{aligned}'))
    return max_plate_ht_eqn


def ep_min_plate_width_req(g,e_min,wp_min):

    g= str(g)
    e_min = str(e_min)
    wp_min = str(wp_min)
    ep_min_plate_w_eqn = Math(inline=True)
    ep_min_plate_w_eqn.append(NoEscape(r'\begin{aligned} w_{p_{min}} &= g` + e`_{min}~2 \\'))
    ep_min_plate_w_eqn.append(NoEscape(r'&='+ g +'+'+ e_min +r'\times 2\\'))
    ep_min_plate_w_eqn.append(NoEscape(r'&='+wp_min +r'\end{aligned}'))
    return ep_min_plate_w_eqn


def ep_max_plate_width_avail(conn,D,T_w,R_r,T_f,wp_max):
    conn = str(conn)
    D = str(D)
    T_w = str(T_w)
    R_r = str(R_r)
    T_f = str(T_f)
    wp_max = str(wp_max)
    ep_max_plate_w_eqn = Math(inline=True)
    if conn == VALUES_CONN_1[0]:
        ep_max_plate_w_eqn.append(NoEscape(r'\begin{aligned} w_{p_{max}} &= T_f \\'))
        ep_max_plate_w_eqn.append(NoEscape(r'&=' + wp_max + '\end{aligned}'))
    elif conn == VALUES_CONN_1[1]:
        ep_max_plate_w_eqn.append(NoEscape(r'\begin{aligned} w_{p_{max}} &= D - 2T_f - 2R_r \\'))
        ep_max_plate_w_eqn.append(NoEscape(r'&=' + D + r'-2 \times' + T_f + r'-2 \times' + R_r +  r'\\'))
        ep_max_plate_w_eqn.append(NoEscape(r'&=' + wp_max + '\end{aligned}'))
    else:
        ep_max_plate_w_eqn.append(NoEscape(r'\begin{aligned} N/A \end{aligned}'))
    return ep_max_plate_w_eqn


#TODO: YASH --- Try using ep_min_plate_width_req
def end_plate_ht_req(D,e,h_p):
    """Calculate end plate height foe column end plate connection
    Args:
         D:section depth in mm (float)
         e: End distance in mm (float)
         h_p:End plate height in mm (float)
    Returns:
         End plate height
    """

    D = str(D)
    h_p = str(h_p)
    e = str(e)
    end_plate_ht_eqn = Math(inline=True)

    end_plate_ht_eqn.append(NoEscape(r'\begin{aligned} &D + 4e \\'))
    end_plate_ht_eqn.append(NoEscape(r'&=' + D + '+' + r' 4 \times' + e + r'\\'))
    end_plate_ht_eqn.append(NoEscape(r'&=' + h_p + '\end{aligned}'))
    return end_plate_ht_eqn


def end_plate_thk_req(M_ep,b_eff,f_y,gamma_m0,t_p):
    """
    Calculate end plate thickness
     Args:
         M_ep:Moment acting on the end plate in N-mm (float)
         b_eff:Effective width for load dispersion
         f_y:Yeild strength of  plate material in N/mm square (float)
         gamma_m0: IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']  (float)
         t_p:Thickness of end plate
    Returns:
        end plate thickness
    """

    M_ep= str(M_ep)
    t_p = str(t_p)
    b_eff= str(b_eff)
    f_y= str(f_y)
    gamma_m0= str(gamma_m0)

    end_plate_thk_eqn = Math(inline=True)

    end_plate_thk_eqn.append(NoEscape(r'\begin{aligned} t_p &= {\sqrt{\frac{ M_{ep} \times 4\gamma_{m0}}{ b_{eff}f_y}}}\\'))

    end_plate_thk_eqn.append(NoEscape(r'&={\sqrt{\frac{' + M_ep + r'\times 4'+r'\times' +gamma_m0 + r'}{'+b_eff+ r'\times' + f_y + r' }}}\\'))
    end_plate_thk_eqn.append(NoEscape(r'&=' + t_p + '\end{aligned}'))
    return end_plate_thk_eqn


def moment_acting_on_end_plate(M_ep,t_b,e):
    """  Calculate moment acting on the  end plate
    Args:
         M_ep:  moment acting on the  end plate in N-mm (float)
         b_eff:Effective width for load dispersion
         f_y:Yeild strength of  plate material in N/mm square (float)
         gamma_m0: IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']  (float)
         t_p:Thickness of end plate
    Returns:
         moment acting on the end plate

    """

    M_ep= str(M_ep)
    t_b = str(t_b)
    e = str(e)

    # gamma_m0= str(gamma_m0)

    moment_acting_on_end_plate= Math(inline=True)

    moment_acting_on_end_plate.append(NoEscape(r'\begin{aligned}  M_{ep}&= Tension~ in~ Bolt \times End~ dist\\'))
    moment_acting_on_end_plate.append(NoEscape(r'&= T_b \times e\\'))

    moment_acting_on_end_plate.append(NoEscape(r'&=' + t_b + r'\times'+  e + r'\\'))
    moment_acting_on_end_plate.append(NoEscape(r'&=' +M_ep + '\end{aligned}'))
    return moment_acting_on_end_plate


def moment_acting_on_end_plate_flush(M_ep,t_b,e,tb_2):
    """  Calculate moment acting on the  end plate
    Args:
         M_ep:  moment acting on the  end plate in N-mm (float)
         b_eff:Effective width for load dispersion
         f_y:Yeild strength of  plate material in N/mm square (float)
         gamma_m0: IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']  (float)
         t_p:Thickness of end plate
    Returns:
         moment acting on the end plate

    """

    M_ep= str(M_ep)
    t_b = str(t_b)
    tb_2 = str(tb_2)
    e = str(e)

    # gamma_m0= str(gamma_m0)

    moment_acting_on_end_plate= Math(inline=True)

    moment_acting_on_end_plate.append(NoEscape(r'\begin{aligned}  M_{ep}&= max (0.5 \times Tension~ in~ First~ Bolt \times End~ \\'))
    moment_acting_on_end_plate.append(NoEscape(r'& dist, Tension~ in~ Second~ Bolt \times End~ dist)\\'))
    moment_acting_on_end_plate.append(NoEscape(r'&= max(0.5 \times  T_b1  \times  e, T_b2  \times  e)\\'))

    moment_acting_on_end_plate.append(NoEscape(r'&= max(0.5  \times  ' + t_b +r'\times'+  e + ','+tb_2+r'\times'+e+r'\\'))
    moment_acting_on_end_plate.append(NoEscape(r'&=' +M_ep + '\end{aligned}'))
    return moment_acting_on_end_plate


def ht_of_stiff(t_s):
    t_s = str(t_s)
    stiff_ht = Math(inline=True)
    stiff_ht.append(NoEscape(r'\begin{aligned}  h_{s}&= 14~ts \\'))
    stiff_ht.append(NoEscape(r'&=' + t_s + '\end{aligned}'))
    return stiff_ht


def ht_of_stiff1(t_s):
    t_s = str(t_s)
    stiff_ht = Math(inline=True)
    stiff_ht.append(NoEscape(r'\begin{aligned}  h_{s}&= 14~ts \\'))
    stiff_ht.append(NoEscape(r'& if~<~100~mm\\'))
    stiff_ht.append(NoEscape(r'&=' + t_s + '\end{aligned}'))
    return stiff_ht


def wt_of_stiff(w_s,e):
    w_s = str(w_s)
    e = str(e)
    stiff_wt = Math(inline=True)
    stiff_wt.append(NoEscape(r'\begin{aligned}  w_{s}&= 2~e \\'))
    stiff_wt.append(NoEscape(r'&= 2 \times' +e+ r'\\'))
    stiff_wt.append(NoEscape(r'&=' + w_s + '\end{aligned}'))
    return stiff_wt


def min_plate_length_req(min_pitch, min_end_dist,bolt_line,min_length):
    """
    Calculate minimum length of fin plate
     Args:

        min_pitch: minimum pitch distance in mm (float)
        min_end_dist: minimum end distance in mm (float)
        bolt_line: no. of rows of bolts in fin plate (int)
        min_length: minimum length of fin plate in  mm (float)
    Returns:
           minimum length of fin plate
    """

    min_pitch = str(min_pitch)
    min_end_dist = str(min_end_dist)
    bolt_line = str(bolt_line)
    min_length = str(min_length)
    min_plate_length_eqn = Math(inline=True)
    min_plate_length_eqn.append(NoEscape(r'\begin{aligned} &2e_{min} + (n_c-1) p_{min})\\'))
    min_plate_length_eqn.append(NoEscape(r'&=2 \times' + min_end_dist + '+(' + bolt_line + r'-1)  \times  ' + min_pitch + r'\\'))
    min_plate_length_eqn.append(NoEscape(r'&=' + min_length + '\end{aligned}'))
    return min_plate_length_eqn


def min_flange_plate_length_req(min_pitch, min_end_dist,bolt_line,min_length,gap,sec =None):

    """
    Calculate minimum flange plate length required
    Args:

        min_pitch:Min pitch distance of flange bolt in mm (float)
        min_end_dist: Min end distance of flange bolt in mm (float)
        bolt_line: No. of bolts provided in one line in mm (int)
        min_length: Flange plate of minimum lenght in mm (float)
        gap: Gap between flange plate in mm (float)
        sec: Beam or Column (str)
    Returns:
        minimum flange plate length required
    """

    min_pitch = str(min_pitch)
    min_end_dist = str(min_end_dist)
    bolt_line = str(bolt_line)
    min_length = str(min_length)
    gap = str(gap)
    min_flange_plate_length_eqn = Math(inline=True)
    if sec =="column":
        min_flange_plate_length_eqn.append(NoEscape(r'\begin{aligned} & 2 \times [2e_{min} + ({\frac{n_r}{2}}-1)p_{min})]\\'))
        min_flange_plate_length_eqn.append(NoEscape(r'& +\frac{gap}{2}]\\'))
        min_flange_plate_length_eqn.append(NoEscape(r'&=2 \times [(2 \times' + min_end_dist +r' + (\frac{'+bolt_line+r'}{2}' + r'-1)  \times  ' + min_pitch + r'\\'))
        min_flange_plate_length_eqn.append(NoEscape(r'&= + \frac{'+gap+r'}{2}]\\'))
        min_flange_plate_length_eqn.append(NoEscape(r'&=' + min_length + '\end{aligned}'))
    else:
        min_flange_plate_length_eqn.append(NoEscape(r'\begin{aligned} & 2 \times [2e_{min} + ({\frac{n_c}{2}}-1)  \times  p_{min})]\\'))
        min_flange_plate_length_eqn.append(NoEscape(r'& +\frac{gap}{2}]\\'))
        min_flange_plate_length_eqn.append(NoEscape(r'&=2 \times [(2 \times' + min_end_dist + r' + (\frac{' + bolt_line + r'}{2}' + r'-1)  \times  ' + min_pitch + r'\\'))
        min_flange_plate_length_eqn.append(NoEscape(r'&= + \frac{' + gap + r'}{2}]\\'))
        min_flange_plate_length_eqn.append(NoEscape(r'&=' + min_length + '\end{aligned}'))
    return min_flange_plate_length_eqn


def min_plate_thk_req(t_w):
    """
    Calculate min thickness of the fin plate
    Args:
        t_w:Web thickness in mm (float)
    Returns:
        min thickness of the fin plate
    """
    t_w = str(t_w)
    min_plate_thk_eqn = Math(inline=True)
    min_plate_thk_eqn.append(NoEscape(r'\begin{aligned} t_w='+t_w+'\end{aligned}'))
    return min_plate_thk_eqn


def vres_cap_bolt_check(V_u, A_u,bolt_capacity,bolt_req,multiple=1,conn=None):
    """
    Calculate no. of bolts required for flange and web
    Args:

         V_u:Shear force  in KN (float)
         A_u:Axial force  in KN (float)
         bolt_capacity:Bolt capacity  in KN (float)
         bolt_req:no. of bolts required (int)
         multiple:1
         conn:
    Returns:
         no. of bolts required (int)
    """

    res_force = math.sqrt(V_u**2+ A_u**2)
    trial_bolts = multiple * math.ceil(res_force/bolt_req)
    V_u=str(V_u)
    A_u=str(A_u)
    bolt_req =str(bolt_req)
    bolt_capacity=str(bolt_capacity)
    trial_bolts=str(trial_bolts)
    trial_bolts_eqn = Math(inline=True)

    if conn == "flange_web":
        trial_bolts_eqn.append(NoEscape(r' \begin{aligned} V_{res} &= \frac{2~\sqrt{V_u^2+A_u^2}} {bolt_{req}}\\'))
        trial_bolts_eqn.append(NoEscape(r' &= \frac{2 \times \sqrt{' + V_u + r'^2+' + A_u + r'^2}}{' + bolt_req + r'}\\'))
    else:
        trial_bolts_eqn.append(NoEscape(r' \begin{aligned} V_{res} &= \frac{\sqrt{V_u^2+A_u^2}} {bolt_{req}}\\'))
        trial_bolts_eqn.append(NoEscape(r' &= \frac{\sqrt{'+V_u+r'^2+'+A_u+r'^2}}{'+bolt_req+ r'}\\'))
    trial_bolts_eqn.append(NoEscape(r'&='+bolt_capacity+ r'\end{aligned}'))
    return trial_bolts_eqn

def height_of_flange_cover_plate(B,sp,b_fp): #weld
    """
    Calculate height of falnge cover plate
    Args:
        B:Width of  flange section in mm (float)
        sp: Spacing between flange plate in mm (float)
        b_fp: Height of flange cover plate in mm (float)
    Returns:
          Height of flange cover plate in mm (float)
    """
    B = str(B)
    sp = str(sp)
    b_fp = str (b_fp)
    height_for_flange_cover_plate_eqn =Math(inline=True)

    height_for_flange_cover_plate_eqn.append(NoEscape(r'\begin{aligned} B_{fp} &= {B - 2sp} \\'))
    height_for_flange_cover_plate_eqn.append(NoEscape(r'&= {' + B + r' - 2  \times  ' + sp + r'} \\'))

    height_for_flange_cover_plate_eqn.append(NoEscape(r'&=' + b_fp + r'\end{aligned}'))
    return height_for_flange_cover_plate_eqn


def height_of_web_cover_plate(D,sp,b_wp,T,R_1): #weld
    """
    Calculate height of web cover plate
    Args:
        D: Depth of the section in mm (float)
        sp: Space between web plate in mm (float)
        b_wp: Height of web cover plate in mm (float)
        T: Thickness of flange in mm (float)
        R_1: Root radius in mm (float)
    Returns:
         Height of web cover plate in mm (float)
    """
    D = str(D)
    sp = str(sp)
    b_wp = str (b_wp)
    R_1 = str(R_1)
    T= str(T)
    height_for_web_cover_plate_eqn =Math(inline=True)

    height_for_web_cover_plate_eqn.append(NoEscape(r'\begin{aligned} W_{wp} &= {D-2T -2R1- 2sp} \\'))
    height_for_web_cover_plate_eqn.append(NoEscape(r'&= {' + D + r' - 2  \times  ' +T+r'- (2 \times'+ R_1+r')- 2 \times'+ sp + r'} \\'))

    height_for_web_cover_plate_eqn.append(NoEscape(r'&=' + b_wp + '\end{aligned}'))
    return height_for_web_cover_plate_eqn


def inner_plate_height_weld(B,sp,t,r_1, b_ifp):#weld
    """
    Calculate inner flange plate height for beam welded
    Args:

        B:Width of flange in mm (float)
        sp: Spacing between flange plate in mm (float)
        t: Web thickness in mm (float)
        r_1: Root radius in mm (float)
        b_ifp: Height of inner flange plate in mm (float)
    Returns:
         Height of inner flange plate in mm (float)
    """
    B = str(B)
    sp = str(sp)
    t = str (t)
    r_1 = str(r_1)
    b_ifp = str(b_ifp)
    inner_plate_height_weld_eqn =Math(inline=True)
    inner_plate_height_weld_eqn.append(NoEscape(r'\begin{aligned} B_{ifp} &= \frac{B - 4sp - t- 2R1}{2} \\'))
    inner_plate_height_weld_eqn.append(NoEscape(r'&= \frac{'+B +r'- 4 \times'+sp+'-' +t+ r'- 2 \times'+r_1+r'} {2} \\'))
    inner_plate_height_weld_eqn.append(NoEscape(r'&=' + b_ifp + '\end{aligned}'))
    return inner_plate_height_weld_eqn


def plate_Length_req(l_w,t_w,g,l_fp,conn =None): #weld
    """
    Calculate minimum flange plate length
    Args:
       l_w: Weld length of flange in mm (float)
       t_w:Flange weld size in mm (float)
       g: Gap between flange plate in mm (float)
       l_fp: Minimum flange plate length in mm (float)
       conn: Flange or web (str)
    Returns:
          Minimum flange plate length  in mm (float)
    """
    l_w = str(l_w)
    t_w = str (t_w)
    g = str (g)
    l_fp = str(l_fp)
    min_plate_Length_eqn = Math(inline=True)
    if conn =="Flange":
        min_plate_Length_eqn.append(NoEscape(r'\begin{aligned} L_{fp} & = [2 \times (l_{w} + 2 \times t_w) + g]\\'))
        min_plate_Length_eqn.append(NoEscape(r'&= [2 \times ('+ l_w + r'+2 \times'+t_w+') +' + g+ r']\\'))
        min_plate_Length_eqn.append(NoEscape(r'&=' + l_fp + '\end{aligned}'))
    else:
        min_plate_Length_eqn.append(NoEscape(r'\begin{aligned} L_{wp} & = [2 \times (l_{w} + 2 \times t_w) + g]\\'))
        min_plate_Length_eqn.append(NoEscape(r'&= [2 \times (' + l_w + r'+2 \times' + t_w + ') +' + g + r']\\'))
        min_plate_Length_eqn.append(NoEscape(r'&=' + l_fp + '\end{aligned}'))

    return min_plate_Length_eqn


#TODO: DARSHAN, ANJALI (Tension rupture for welded is not required)
# def tension_rupture_welded_prov(w_p, t_p, fu,gamma_m1,T_dn,multiple =1):
#     """
#     Calculate design in tension as governed by rupture of net
#          cross-sectional area in case of welded connection
#     Args:
#          w_p: Width of given section in mm (float)
#          t_p: Thikness of given section in mm (float)
#          fu: Ultimate stress of material in N/mm square (float)
#          gamma_m1:Partial safety factor for failure at ultimate stress  (float)
#          T_dn: rupture strength of net cross-sectional area in N (float)
#          multiple: 1 (int)
#     Returns:
#           design in tension as governed by rupture of net cross-sectional area
#     Note:
#             Reference:
#             IS 800:2007,  cl 6.3
#
#
#     """
#     w_p = str(w_p)
#     t_p = str(t_p)
#     f_u = str(fu)
#     T_dn = str(T_dn)
#     gamma_m1 = str(gamma_m1)
#     multiple = str(multiple)
#     T_dn = str(T_dn)
#     gamma_m1 = str(gamma_m1)
#     Tensile_rup_eqnw = Math(inline=True)
#     Tensile_rup_eqnw.append(NoEscape(r'\begin{aligned} T_{dn} &= \frac{0.9 A_{n}~f_u}{\gamma_{m1}}\\'))
#     # Tensile_rup_eqnw.append(NoEscape(r'&=\frac{0.9\times'+w_p+'\times'+t_p+'\times'+f_u+'}{'+gamma_m1+r'}\\'))
#     Tensile_rup_eqnw.append(NoEscape(r'&=\frac{' + multiple + r'\times 0.9 \times' + w_p + r'\times' + t_p + r'\times' + f_u + '}{' + gamma_m1 + r'}\\'))
#     Tensile_rup_eqnw.append(NoEscape(r'&=' + T_dn +r'\\'))
#     Tensile_rup_eqnw.append(NoEscape(r'[Ref&.~IS~800:2007,~Cl.~6.3]\end{aligned}'))
#
#     return Tensile_rup_eqnw


def spacing (sp,t_w):

    """
    Calculate spacing
    Args:
        sp:Spacing required in mm (float)
        t_w:Size of weld in mm (float)
    Returns:
        Required spacing (float)
    """

    # sp = max(15,s+5)
    sp = str(sp)
    t_w = str(t_w)
    space_provided_eqn = Math(inline=True)
    space_provided_eqn.append(NoEscape(r'\begin{aligned} sp &= max(15,(t_w+5))\\'))
    space_provided_eqn.append(NoEscape(r'&= max(15,('+t_w+ r'+5))\\'))
    space_provided_eqn.append(NoEscape(r'&=' + sp + r'\end{aligned}'))
    return space_provided_eqn


# TODO: ANJALI, Keep only one of the following if possible
def weld_strength_req(V,A,M,Ip_w,y_max,x_max,l_w,R_w):
    # def weld_strength_stress(V_u, A_w, M_d, Ip_w, y_max, x_max, l_eff, R_w):

    """
    Calculate resultant stress on weld
    Args:
        V:Factored shear force acting on the member in KN (float)
        A:Vertical compression force carried by web of the section in KN (float)

        M:Moment devloped by ecentricity in KN/mm(float)
        Ip_w:Polar moment inertia of the web group in mm^4 (float)
        y_max:Vertical distance of farthest point in weld group from shear center of the weld group in mm (float)
        x_max:Horizontal distance of farthest point in weld group from shear center of the weld group in mm (float)

        l_w:Required effective web weld length in mm (float)
        R_w:Resultant stress on the weld in KN/mm (float)
    Returns:
         Resultant stress on the weld
    Note:
            Reference:
            Subramanyan (TODO: add page number)


    """

    V_wv = str(round(V / l_w, 2))
    A_wh = str(round(A / l_w, 2))

    V = str(V)
    A = str(A)
    l_w = str(l_w)
    R_w = str(R_w)

    if M > 0.0:
        T_wh = str(round(M * y_max/Ip_w,2))
        T_wv = str(round(M * x_max/Ip_w,2))
        y_max = str(y_max)
        x_max = str(x_max)
        Ip_w = str(Ip_w)
        M = str(M)

        weld_stress_eqn = Math(inline=True)
        weld_stress_eqn.append(NoEscape(r'\begin{aligned} R_w&=\sqrt{(T_{wh}+A_{wh})^2 + (T_{wv}+V_{wv})^2}\\'))
        weld_stress_eqn.append(NoEscape(r'T_{wh}&=\frac{M \times y_{max}}{I{pw}}=\frac{'+M+r'\times'+y_max+'}{'+Ip_w+r'}\\'))
        weld_stress_eqn.append(NoEscape(r'T_{wv}&=\frac{M \times x_{max}}{I{pw}}=\frac{'+M+r'\times'+x_max+'}{'+Ip_w+r'}\\'))
        weld_stress_eqn.append(NoEscape(r'V_{wv}&=\frac{V}{l_w}=\frac{'+V+'}{'+l_w+r'}\\'))
        weld_stress_eqn.append(NoEscape(r'A_{wh}&=\frac{A}{l_w}=\frac{'+A+'}{'+l_w+r'}\\'))
        weld_stress_eqn.append(NoEscape(r'R_w&=\sqrt{('+T_wh+'+'+A_wh+r')^2 + ('+T_wv+'+'+V_wv+r')^2}\\'))
        weld_stress_eqn.append(NoEscape(r'&='+R_w+r'\end{aligned}'))
    else:
        weld_stress_eqn = Math(inline=True)
        weld_stress_eqn.append(NoEscape(r'\begin{aligned} R_w&=\sqrt{(A_{wh})^2 + (V_{wv})^2}\\'))
        weld_stress_eqn.append(NoEscape(r'V_{wv}&=\frac{V}{l_w}=\frac{' + V + '}{' + l_w + r'}\\'))
        weld_stress_eqn.append(NoEscape(r'A_{wh}&=\frac{A}{l_w}=\frac{' + A + '}{' + l_w + r'}\\'))
        weld_stress_eqn.append(NoEscape(r'R_w&=\sqrt{('+A_wh + r')^2 + (' + V_wv + r')^2}\\'))
        weld_stress_eqn.append(NoEscape(r'&=' + R_w + r'\end{aligned}'))

    return weld_stress_eqn


def weld_strength_stress(V_u,A_w,M_d,Ip_w,y_max,x_max,l_eff,R_w):
    """
    Calculate resultant stress on weld
    Args:
          V_u:factored shear force acting on the member in KN (float)
          A_w:vertical compression force carried by web of the section in KN (float)
          M_d:moment devloped by ecentricity in KN/mm(float)
          Ip_w:moment devloped by ecentricity in KN/mm(float)
          y_max:moment devloped by ecentricity in KN/mm(float)
          x_max:horizontal distance of farthest point in weld group from shear center of the weld group in mm (float)
          l_eff:required effective web weld length in mm (float)
          R_w:resultant stress on the weld in KN/mm (float)
    Returns:
          resultant stress on the weld
    Note:
            Reference:
            Subramanyan (TODO: add page number)



    """
    T_wh = str(round(M_d * y_max/Ip_w,2))
    T_wv = str(round(M_d * x_max/Ip_w,2))
    V_wv = str(round(V_u  /l_eff,2))
    A_wh = str(round(A_w/l_eff,2))

    V_u= str(V_u)
    A_w = str(A_w)
    M_d= str(M_d)
    Ip_w = str(Ip_w)
    y_max = str(y_max)
    x_max = str(x_max)
    l_eff = str(l_eff)
    R_w = str(R_w)
    weld_stress_eqn = Math(inline=True)
    weld_stress_eqn.append(NoEscape(r'\begin{aligned} R_w&=\sqrt{(T_{wh}+A_{wh})^2 + (T_{wv}+V_{wv})^2}\\'))
    weld_stress_eqn.append(NoEscape(r'T_{wh}&=\frac{M_d \times y_{max}}{I{pw}}\\'))
    weld_stress_eqn.append(NoEscape(r'&=\frac{'+M_d+r'\times'+y_max+'}{'+Ip_w+r'}\\'))
    weld_stress_eqn.append(NoEscape(r'T_{wv}&=\frac{M_d \times x_{max}}{I{pw}}\\'))
    weld_stress_eqn.append(NoEscape(r'&=\frac{'+M_d+r'\times'+x_max+'}{'+Ip_w+r'}\\'))
    weld_stress_eqn.append(NoEscape(r'V_{wv}&=\frac{V_u}{l_{eff}}\\ '))
    weld_stress_eqn.append(NoEscape(r'&=\frac{'+V_u+'}{'+l_eff+r'}\\'))
    weld_stress_eqn.append(NoEscape(r'A_{wh}&=\frac{A_u}{l_{eff}}\\'))
    weld_stress_eqn.append(NoEscape(r'&=\frac{'+A_w+'}{'+l_eff+r'}\\'))
    weld_stress_eqn.append(NoEscape(r'R_w&=\sqrt{('+T_wh+'+'+A_wh+r')^2 + ('+T_wv+'+'+V_wv+r')^2}\\'))
    weld_stress_eqn.append(NoEscape(r'&='+R_w+r'\end{aligned}'))

    return weld_stress_eqn


#TODO: ANJALI Shear rupture check is not required for weld
def shear_Rupture_prov_weld(h, t,fu,v_dn,gamma_m1,multiple =1):  #weld

    """
      Calculate design strength in tension due to rupture of critical section in case of welded connection
      Args:
           h:Height of the flange in mm (float)
           t:Thickness of the flange in mm (float)
           fu:Ultimate stress of the material N/ mm square (float)
           v_dn:Design strength due to ruoture in N (float)
           gamma_m1:Partial safety factor for failure at ultimate stress (float)
           multiple:1
      Returns:
          design strength in tension due to rupture of critical section in case of welded connection

      Note:
                Reference:
                IS 800:2007,  cl 6.3

      """

    h = str(h)
    t = str(t)
    gamma_m1 =  str(gamma_m1)
    f_u = str(fu)
    v_dn = str(v_dn)
    multiple = str(multiple)

    shear_rup_eqn = Math(inline=True)
    shear_rup_eqn.append(NoEscape(r'\begin{aligned} V_{dn} &= \frac{0.75 \times A_{vn}~f_u}{\sqrt{3}~\gamma_{m1}}\\'))
    shear_rup_eqn.append(NoEscape(r'&=\frac{'+ multiple+r'\times 0.75 \times'+h+r'\times'+t+r'\times'+f_u+r'}{\sqrt{3} \times' +gamma_m1+ r'}\\'))
    shear_rup_eqn.append(NoEscape(r'&=' + v_dn + r'\\'))
    shear_rup_eqn.append(NoEscape(r'[Ref.&~IS~800:2007,~Cl.~6.3]\end{aligned}'))
    return shear_rup_eqn


def flange_weld_stress(F_f,l_eff,F_ws):
    """
    Calculate flange weld stress

    Args:

        F_f:flange force in KN (float)
        l_eff:available effective length in mm (float)
        F_ws:flange weld stress in N/mm (float)
    Returns:
        flange weld stress
    """
    F_f = str(F_f)
    l_eff = str(l_eff)
    F_ws = str(F_ws)
    flange_weld_stress_eqn = Math(inline=True)
    flange_weld_stress_eqn.append(NoEscape(r'\begin{aligned} Stress &= \frac{F_f \times 10^3}{l_{eff}}\\'))
    flange_weld_stress_eqn.append(NoEscape(r' &= \frac{'+F_f+r'\times 10^3}{'+l_eff+ r'}\\'))
    flange_weld_stress_eqn.append(NoEscape(r'&= ' + F_ws+ r'\end{aligned}'))

    return flange_weld_stress_eqn


def no_of_bolts_along_web(D,T_f,e,p,n_bw):
    """
    Calculate no. of bolts along web

    Args:
        D: section depth in mm  (float)
        T_f:flange thickness in mm  (float)
        e: end distance in mm  (float)
        p:pitch distance in mm  (float)
        n_bw: no. of bolts along web (int)
    Returns:
         no. of bolts along web
    """

    D = str(D)
    e= str(e)
    p = str(p)
    T_f = str(T_f)
    n_bw = str(n_bw)
    no_of_bolts_along_web = Math(inline=True)
    no_of_bolts_along_web.append(NoEscape(r'\begin{aligned} n_{bw} &= 2 \times ( \frac{D -(2 \times T_f) -(2 \times e)}{\ p}  + 1 )\\'))
    no_of_bolts_along_web.append(NoEscape(r'&= 2 \times (\frac{' + D + r' -(2 \times'+T_f +r')-(2 \times'+e + r')}{' + p + r'} +1 ) \\'))
    no_of_bolts_along_web.append(NoEscape(r'&= ' + n_bw + r'\end{aligned}'))
    return no_of_bolts_along_web


def no_of_bolts_along_flange(b,T_w,e,p,n_bf):
    """
    Calculate no of bolts along flange

    Args:
          b:flange width in mm  (float)
          T_w:web thickness in mm  (float)
          e: end distance in mm  (float)
          p: pitch distance in mm  (float)
          n_bf: no. of bolts along flange (int)
    Returns:
          no. of bolts along flange
    """
    b = str(b)
    e= str(e)
    p = str(p)
    T_w = str(T_w)
    n_bf = str(n_bf)
    no_of_bolts_along_flange = Math(inline=True)
    no_of_bolts_along_flange.append(NoEscape(r'\begin{aligned} n_{bf} &= 2 \times ( \frac{b/2 -(T_w / 2) -(2 \times e)}{\ p}  + 1 )\\'))
    no_of_bolts_along_flange.append(NoEscape(r'&= 2 \times (\frac{' + b + r'/2 -(0.5 \times'+T_w +r')-(2 \times'+e + r')}{' + p + r'} +1 )\\'))
    no_of_bolts_along_flange.append(NoEscape(r'&= ' + n_bf + r'\end{aligned}'))
    return no_of_bolts_along_flange


def shear_force_in_bolts_near_web(V,n_wb,V_sb):
    """
    Calculate shear force in each bolts near web

    Args:
           V: factored shear load in KN (float)
           n_wb: no. of bolts in web (int)
           V_sb:shear force in each bolts near web in KN (float)
    Returns:
        shear force in bolts near web
    """
    V = str(V)
    n_wb = str(n_wb)
    V_sb = str(V_sb)
    shear_force_in_bolts_near_web = Math(inline=True)
    shear_force_in_bolts_near_web.append(NoEscape(r'\begin{aligned} V_{sb} &= \frac{V}{\ n_{wb}} \\'))
    shear_force_in_bolts_near_web.append(NoEscape(r'&=\frac{' + V + '}{' + n_wb + r'} \\'))
    shear_force_in_bolts_near_web.append(NoEscape(r'&= ' + V_sb + r'\end{aligned}'))
    return shear_force_in_bolts_near_web


def depth_req(e, g, row, sec =None):
    """
    Calculate depth required for web spacing check

    Args:
        e:edge distance for web plate in mm (float)
        g:gauge distance for web plate in mm (float)
        row: row (float)
        sec:coulmn or beam (str)
    Returns:
        depth required for web spacing check
    """

    d = 2*e + (row-1)*g
    depth = d
    depth = str(depth)
    e = str(e)
    g = str(g)
    row = str(row)

    depth_eqn = Math(inline=True)
    if sec == "C":
        depth_eqn.append(NoEscape(r'\begin{aligned} depth & = 2~e + (rl -1)~g \\'))
        depth_eqn.append(NoEscape(r'& = 2\times '+e+'+('+row+r'-1) \times'+g+r' \\'))
        depth_eqn.append(NoEscape(r'& = ' + depth + r'\end{aligned}'))
    elif sec == "column":
        depth_eqn.append(NoEscape(r'\begin{aligned} depth & = 2~e + (c_l -1)~g\\'))
        depth_eqn.append(NoEscape(r'& = 2 \times ' + e + '+(' + row + r'-1)\times' + g +  r'\\'))
        depth_eqn.append(NoEscape(r'& = ' + depth + r'\end{aligned}'))
    elif sec =="beam":
        depth_eqn.append(NoEscape(r'\begin{aligned} depth & = 2~e + (r_l -1)~g\\'))
        depth_eqn.append(NoEscape(r'& = 2 \times ' + e + '+(' + row + r'-1)\times' + g + r'\\'))
        depth_eqn.append(NoEscape(r'& = ' + depth + r'\end{aligned}'))
    else:
        depth_eqn.append(NoEscape(r'\begin{aligned} depth & = 2~e + (r_l -1)~g\\'))
        depth_eqn.append(NoEscape(r'& = 2 \times ' + e + '+(' + row + r'-1)\times' + g + r'\\'))
        depth_eqn.append(NoEscape(r'& = ' + depth + r'\end{aligned}'))

    return depth_eqn


def end_plate_moment_demand(connectivity,g,T_w,R_r,t_w,s,T_e,M):
    ecc1 = round(g/2-t_w/2-s,2)
    ecc2 = round(g/2-T_w/2-R_r,2)
    ecc = max(ecc1,ecc2)
    T_e = str(T_e)
    M = str(M)
    ecc1 = str(ecc1)
    ecc2 = str(ecc2)
    ecc = str(ecc)


    EP_Mom = Math(inline=True)
    EP_Mom.append(NoEscape(r'\begin{aligned}M &= T_e \times ecc \\'))
    if connectivity == VALUES_CONN_1[0]:
        EP_Mom.append(NoEscape(r'ecc_1 &=\frac{g}{2}-\frac{t_w}{2}-s &='+ecc1+r'\\'))
        EP_Mom.append(NoEscape(r'ecc_2 &=\frac{g}{2}-\frac{T_w}{2}-R_r &=' + ecc2 + r'\\'))
        EP_Mom.append(NoEscape(r'&max(ecc_1,ecc_2) &='+ecc+r'\\'))
    else:
        EP_Mom.append(NoEscape(r'ecc &=\frac{g}{2}-\frac{t_w}{2}-s &=' + ecc1 + r'\\'))
    EP_Mom.append(NoEscape(r'M&='+T_e+r'\times'+ecc+r'\times 10^{-3} &='+M+r'\end{aligned}'))
    return EP_Mom


def gusset_ht_prov(beam_depth, clearance, height, mul = 1):
    """
    Calculate gusset plate height
    Args:
         beam_depth:Section depth in mm (float)
         clearance:clearence between gusset plates in mm (float)
         height:Height of the gusset plate in mm (float)
         mul:
    Returns:
         gusset plate height
    """
    beam_depth = str(beam_depth)
    clearance = str(clearance)
    height = str(height)
    mul = str(mul)
    plate_ht_eqn = Math(inline=True)
    plate_ht_eqn.append(
        NoEscape(r'\begin{aligned} H &= '+mul+r'\times Depth + clearance 'r'\\'))
    plate_ht_eqn.append(
        NoEscape(r'&=('+mul+r'\times' + beam_depth + ')+' + clearance + r'\\'))
    plate_ht_eqn.append(NoEscape(r'&= '  + height + r'\end{aligned}'))
    return plate_ht_eqn


def gusset_lt_b_prov(nc,p,e,length):
    """
    Calculate length of the gusset plate in case of bolted connection

    Args:

        nc:No. of row of bolts (int)
        p: pitch distance of the gusset plate in mm (float)
        e:Edge distance of the gusset plate in mm (float)
        length:length of the gusset plate in mm (float)
    Returns:
        length of the gusset plate in case of bolted connection
    """
    nc = str(nc)
    p = str(p)
    e = str(e)
    length = str(length)
    length_htb_eqn = Math(inline=True)
    length_htb_eqn.append(
        NoEscape(r'\begin{aligned} L &= (nc -1) p + 2  e\\'))
    length_htb_eqn.append(
        NoEscape(r'&= ('+nc+r'-1) \times'+ p + r'+ (2 \times'+ e + r')\\'))
    length_htb_eqn.append(NoEscape(r'&= ' + length + r'\end{aligned}'))
    return length_htb_eqn


def gusset_lt_w_prov(weld,cls,length):
    """
    Calculate length of the gusset plate in case of welded connection

    Args:
          weld:weld length in mm (float)
          cls:clearance in mm (float)
          length:plate length in mm (float)
    Returns:
        length of the gusset plate in case of welded connection

    """
    weld = str(weld)
    cls = str(cls)
    length = str(length)
    length_htw_eqn = Math(inline=True)
    length_htw_eqn.append(
        NoEscape(r'\begin{aligned} L &= Flange weld + clearance 'r'\\'))
    length_htw_eqn.append(
        NoEscape(r'&= '+ weld + '+' + cls + r'\\'))
    length_htw_eqn.append(NoEscape(r'&= ' + length + r'\end{aligned}'))
    return length_htw_eqn


def bearing_length(V,t_w,t_f,r_r,f_y,gamma_m0,t,r_ra,gap):

    bearing_length = round((float(V) * 1000) * gamma_m0 / t_w / f_y, 3)
    b1_req = round(bearing_length - (t_f + r_r),2)
    k = round(t_f + r_r,2)
    b1 = round(max(b1_req, k),2)
    b2 = round(max(b1 + gap - t - r_ra, 0.0),2)

    b1_req = str(b1_req)
    k = str(k)
    b1 = str(b1)
    V = str(V)
    t_w=str(t_w)
    t_f =str(t_f)
    gamma_m0 = str(gamma_m0)
    r_r = str(r_r)
    b2 = str(b2)
    f_y = str(f_y)
    gap = str(gap)
    t= str(t)
    r_ra = str(r_ra)

    bearing_length = Math(inline=True)
    bearing_length.append(NoEscape(r'\begin{aligned} b_{lreq} &= \frac{V\times \gamma_m0}{t_w \times f_y} - t_f - r_r \\'))
    bearing_length.append(NoEscape(r'&= \frac{'+V+r'\times'+ gamma_m0+'}{'+t_w+r'\times'+ f_y+'} - '+t_f+'-'+ r_r+r' \\'))
    bearing_length.append(NoEscape(r'&=' +b1_req+r' \\'))
    bearing_length.append(NoEscape(r'k &= t_f +r_r \\'))
    bearing_length.append(NoEscape(r'k &='+ t_f +'+'+ r_r +'='+k+r'\\'))
    bearing_length.append(NoEscape(r'b_1&= max(b_{1req},k)='+b1+r'\\'))
    bearing_length.append(NoEscape(r'b_2 &= b_1+gap-t-r_{ra}\\'))
    bearing_length.append(NoEscape(r'b_2 &='+ b1+'+'+gap+'-'+t+'-'+r_ra+r'\\'))
    bearing_length.append(NoEscape(r'b_2&= max(b_2,0)=' + b2 + r'\end{aligned}'))
    return bearing_length


def moment_demand_SA(b_1,b_2,V,M):
    if b_2 == 0.0:
        ecc = 0.0
    elif b_2 <= b_1:
        ecc = round((b_2 /b_1) * (b_2 / 2),2)
    else:
        ecc = round((b_2 - b_1 / 2),2)

    V = str(V)
    b_1 = str(b_1)
    b_2 = str(b_2)
    M = str(M)
    ecc = str(ecc)

    moment_demand_eqn = Math(inline=True)
    moment_demand_eqn.append(NoEscape(r'\begin{aligned} M &= V \times ecc \\'))
    if float(b_2) == 0.0:
        moment_demand_eqn.append(NoEscape(r'if ~b_2 = 0, &ecc = 0 \\'))
        moment_demand_eqn.append(NoEscape(r'M = 0 \\'))
    elif float(b_2) <= float(b_1):
        moment_demand_eqn.append(NoEscape(r'if~b_2 \leq b_1, ecc &= \frac{b_2}{b_1}\times \frac{b_2}{2} \\'))
        moment_demand_eqn.append(NoEscape(r'ecc &=\frac{'+b_2+'}{'+b_1+r'}\times \frac{'+b_2+r'}{2}\\'))
        moment_demand_eqn.append(NoEscape(r'&='+ecc+r'\\'))
    else:
        moment_demand_eqn.append(NoEscape(r'if ~b_2 > b_1, ecc &= \frac{b_2-b_1}{2} \\'))
        moment_demand_eqn.append(NoEscape(r'ecc &=\frac{' + b_2 + '-' + b_1 + r'}{2}\\'))
        moment_demand_eqn.append(NoEscape(r'&=' + ecc + r'\\'))
    moment_demand_eqn.append(NoEscape(r'M &=' + V +r'\times' + ecc + r'\times 10^{-3}\\'))
    moment_demand_eqn.append(NoEscape(r' &=' + M + r'\end{aligned}'))
    return moment_demand_eqn


def efficiency_prov(F, Td, eff):
    """
    Calculate efficiency of the tension member(provided)

    Args:
         F:axial force on the member in KN (float)
         Td:tension capacity of the section in KN (float)
         eff:efficiency of the tension member  (float)
    Returns:
        efficiency of the tension member
    """
    F = str(F)
    Td = str(round(Td/1000,2))
    eff = str(eff)
    eff_eqn = Math(inline=True)
    eff_eqn.append(NoEscape(r'\begin{aligned} Utilization~Ratio &= \frac{F}{T_d}&=\frac{'+F+'}{'+Td+r'}\\'))
    eff_eqn.append(NoEscape(r'&= ' + eff + r'\end{aligned}'))

    return eff_eqn


def moment_cap(beta,m_d,f_y,gamma_m0,m_fd,mom_cap):
    """
     Calculate  moment capacity of the column when (class_of_section == 1 or self.class_of_section == 2)

     Args:
             beta: value according to the class of section
             m_d: bending moment acting on the column
             f_y: yield strength of material
             gamma_m0: partial safety factor
             m_fd:factored bending moment acting on the column
             mom_cap: moment capacity of the column
    Returns:
             moment capacity of the column
    """
    #todo reference
    beta= str(beta)
    m_d= str(m_d)
    f_y= str(f_y)
    gamma_m0 = str(gamma_m0)
    m_fd = str(m_fd)
    mom_cap = str(mom_cap)
    moment_cap =Math(inline=True)

    moment_cap.append(NoEscape(r'\begin{aligned} M_{c} &=  m_d - \beta(m_d -m_{fd})  \\'))
    moment_cap.append(NoEscape(r'&= ' + m_d + r'-' + beta + r'('+m_d+r'-'+m_fd+r') \\'))
    moment_cap.append(NoEscape(r'&= ' + mom_cap + r'\end{aligned}'))
    return moment_cap


def eff_len_prov(l_eff, b_fp, t_w, l_w,con= None):
    """
    Calculate required flange length

    Args:
        l_eff:required flange length in mm (float)
        b_fp:flange plate height in mm (float)
        t_w:flange weld size in mm (float)
        l_w:flange weld length in mm (float)
        con:flange or web (str)
    Returns:
         required flange length
    """
    l_eff = str(l_eff)
    l_w = str(l_w)
    b_fp = str(b_fp)
    t_w = str(t_w)
    eff_len_eqn = Math(inline=True)
    if con == "Flange":
        eff_len_eqn.append(NoEscape(r'\begin{aligned} l_{eff} &= (2\times l_w) + B_{fp} - 2\times t_w\\'))
        eff_len_eqn.append(NoEscape(r'&= (2 \times' + l_w + ') +' + b_fp + r' - 2\times' + t_w + r'\\'))
        eff_len_eqn.append(NoEscape(r'& = ' + l_eff + r'\end{aligned}'))
    else:
        eff_len_eqn.append(NoEscape(r'\begin{aligned} l_{eff} &= (2\times l_w) + W_{wp} - 2\times t_w\\'))
        eff_len_eqn.append(NoEscape(r'&= (2 \times' + l_w + ') +' + b_fp + r' - 2\times' + t_w + r'\\'))
        eff_len_eqn.append(NoEscape(r'& = ' + l_eff + r'\end{aligned}'))

    return eff_len_eqn


def eff_len_prov_out_in(l_eff, b_fp,b_ifp, t_w, l_w):
    """
    Calculate effective length provided on outside

    Args:
           l_eff:required length of flange in mm (float)
           b_fp:flange plate height in mm (float)
           b_ifp:flange plate inner height in mm (float)
           t_w:flange weld size in mm (float)
           l_w:flange weld length in mm (float)
    Returns:
          effective length provided on outside
    """
    l_eff = str(l_eff)
    l_w = str(l_w)
    b_fp = str(b_fp)
    b_ifp = str(b_ifp)
    t_w = str(t_w)
    eff_len_prov_out_in_eqn = Math(inline=True)
    eff_len_prov_out_in_eqn.append(NoEscape(r'\begin{aligned} l_{eff} &= (6 \times l_w) + B_{fp} + (2 \times B_{ifp})- 6 \times t_w\\'))
    eff_len_prov_out_in_eqn.append(NoEscape(r'&= (6 \times' + l_w + ') +' + b_fp + r'+ 2 \times' +b_ifp + r'- 6 \times' + t_w + r'\\'))
    eff_len_prov_out_in_eqn.append(NoEscape(r'& = ' + l_eff + r'\end{aligned}'))

    return eff_len_prov_out_in_eqn


def plate_area_req(crs_area, flange_web_area):
    """
    Calculate plate area required

    Args:
         crs_area:cross sectional area of plate in mm square (float)
         flange_web_area:combined area of flange and web in mm square (float)
    Returns:
         plate area required
     Note:
         [Ref: cl.8.6.3.2 IS 800:2007]
    """

    crs_area = str(crs_area)
    flange_web_area = str(flange_web_area)

    plate_crs_sec_area_eqn =Math(inline=True)
    plate_crs_sec_area_eqn.append(NoEscape(r'\begin{aligned} &pt.area >= \\& connected~member~area \times 1.05\\'))
    # plate_crs_sec_area_eqn.append(NoEscape(r'& = '+crs_area+ r' * 1.05 \\'))
    plate_crs_sec_area_eqn.append(NoEscape(r' &= ' + flange_web_area  +  r'\\'))
    plate_crs_sec_area_eqn.append(NoEscape(r' &[Ref: Cl.8.6.3.2 ~IS ~800:2007]\end{aligned}'))
    return plate_crs_sec_area_eqn


def width_pt_chk(B,t,r_1,pref):
    """
    Check the plate width

    Args:
          B:flange width in mm (float)
          t:web thickness in mm  (float)
          r_1:root radius in mm  (float)
          pref:"Outside" or "Outside +Inside" (str)
    Returns:
         the plate width
    """
    if pref == "Outside":
        outerwidth = round(B  - (2 * 21) ,2)
        outerwidth = str(outerwidth)
    else:
        innerwidth = round((B -t - (2*r_1)-(4*21))/2 ,2)
        innerwidth = str(innerwidth)

    B = str(B)
    t = str(t)
    r_1 = str(r_1)
    Innerwidth_pt_chk_eqn = Math(inline=True)
    if pref == "Outside":
        Innerwidth_pt_chk_eqn.append(NoEscape(r'\begin{aligned} B_{fp} &= B-(2 \times 21)\\'))
        Innerwidth_pt_chk_eqn.append(NoEscape(r'&=' + B + r'-(2 \times 21)\\'))
        Innerwidth_pt_chk_eqn.append(NoEscape(r'&= ' + outerwidth +r'\end{aligned}'))
    else:
        Innerwidth_pt_chk_eqn.append(NoEscape(r'\begin{aligned} B_{ifp} &= \frac{B-t-(2 \times R1)-(4 \times 21)}{2}\\'))
        Innerwidth_pt_chk_eqn.append(NoEscape(r'&=\frac{'+B+'-'+t+r'-(2 \times'+r_1+r')-(4 \times 21)}{2}\\'))
        Innerwidth_pt_chk_eqn.append(NoEscape(r'&= ' + innerwidth + r'\end{aligned}'))
    return Innerwidth_pt_chk_eqn


def width_pt_chk_bolted(B,t,r_1):
    """
    Check the width of plate (bolted connection)

    Args:
           B:flange width
           t:web thickness
           r_1:root radius
    Returns:
          width of plate
    """
    innerwidth =round((B -t - (2*r_1))/2 ,2)
    B = str(B)
    t = str(t)
    r_1 = str(r_1)
    innerwidth = str(innerwidth)
    width_pt_chk_bolted_eqn = Math(inline=True)

    width_pt_chk_bolted_eqn.append(NoEscape(r'\begin{aligned} B_{fp} &= \frac{B-t-(2 \times R1)}{2}\\'))
    width_pt_chk_bolted_eqn.append(NoEscape(r'&=\frac{' + B + '-' + t + r'-(2 \times' + r_1 + r')}{2}\\'))
    width_pt_chk_bolted_eqn.append(NoEscape(r'&= ' + innerwidth + r'\end{aligned}'))
    return width_pt_chk_bolted_eqn


def web_width_chk_bolt (pref,D,tk,T,R_1,webplatewidth,webclearance = None):
    """
    Calculate web plate width

    Args:
          pref:prefference (outside or outside+inside) (str)
          D:Section depth in mm (float)
          tk:flange plate thickness (provided) in mm (float)
          T:flange thickness in mm (float)
          R_1: root radius in mm (float)
          webplatewidth: web width in mm (float)
          webclearance: web clearance in mm (float)
    Returns:
          web plate width
    """
    T = str(T)
    tk = str(tk)
    R_1 = str(R_1)
    webplatewidth= str(webplatewidth)
    webclearance =str(webclearance)
    web_width_chk_bolt_eqn = Math(inline=True)
    if pref =="Outside":
        D = str(D)
        web_width_chk_bolt_eqn.append(NoEscape(r'\begin{aligned} W_{wp} &= D - (2 \times T) - (2 \times R1)\\'))
        web_width_chk_bolt_eqn.append(NoEscape(r' &= '+D+ r' - (2 \times'+T+r') - (2 \times'+ R_1+r')\\'))
        web_width_chk_bolt_eqn.append(NoEscape(r' &=' + webplatewidth +  r'\end{aligned}'))
    else :

        if D > 600.00:
            web_width_chk_bolt_eqn.append(NoEscape(r'\begin{aligned} C~~ &= max((R1, t_{ifp}) + 25) \\'))
            web_width_chk_bolt_eqn.append(NoEscape(r'&= max(('+R_1+',' +tk+r') + 25) \\'))
            web_width_chk_bolt_eqn.append(NoEscape(r'&= ' + webclearance + r' \\'))

        else:
            web_width_chk_bolt_eqn.append(NoEscape(r'\begin{aligned} C~~ &= max((R1, t_{ifp}) + 10) \\'))
            web_width_chk_bolt_eqn.append(NoEscape(r'&= max((' + R_1 + ',' +tk + r') +10) \\'))
            web_width_chk_bolt_eqn.append(NoEscape(r'&= ' + webclearance + r' \\'))
        D = str(D)
        web_width_chk_bolt_eqn.append(NoEscape(r' W_{wp} &= D - (2 \times T) - (2 \times C)\\'))
        web_width_chk_bolt_eqn.append(NoEscape(r' &= ' + D + r' - (2 \times ' + T + r') - (2 \times' + webclearance + r')\\'))
        web_width_chk_bolt_eqn.append(NoEscape(r' &='+webplatewidth + r'\end{aligned}'))

    return web_width_chk_bolt_eqn


def web_width_chk_weld (D,tk,R_1,webplatewidth):
    """
    Calculate web plate height in case of beam_beam welded connection

     Args:
         D:Section depth in mm (float)
         tk:flange thickness in mm (float)
         R_1:root radius of the section in mm (float)
         webplatewidth:web plate height in mm (float)
    Returns:
         web plate height
    """
    tk = str(tk)
    R_1 = str(R_1)
    D = str(D)
    webplatewidth = str(webplatewidth)
    web_width_chk_weld_eqn = Math(inline=True)
    web_width_chk_weld_eqn.append(NoEscape(r'\begin{aligned} W_{wp} &= D - (2 \times T) - (2 \times R1)- (2\times 21)\\'))
    web_width_chk_weld_eqn.append(NoEscape(r' &= ' + D + r' - (2 \times ' + tk + r') - (2 \times' + R_1 + r')- (2\times 21)\\'))
    web_width_chk_weld_eqn.append(NoEscape(r' &=' + webplatewidth + r'\end{aligned}'))
    return web_width_chk_weld_eqn


def web_width_min (D,min_req_width):
    """
    Calculate minimum web plate height

    Args:
         D:Section depth in mm (float)
         min_req_width:minimum web plate height in mm (float)
    Returns:
         minimum web plate height
     Note:
           [Ref: INSDAG - Chapter 5, Sect. 5.2.3]
    """
    D = str(D)
    min_req_width = str(min_req_width)
    web_width_min_eqn = Math(inline=True)
    web_width_min_eqn.append(NoEscape(r'\begin{aligned}  &= 0.6 \times D\\'))
    web_width_min_eqn.append(NoEscape(r' &= 0.6 \times'+D+r'\\'))
    web_width_min_eqn.append(NoEscape(r' &= ' + min_req_width+ r'\\'))
    web_width_min_eqn.append(NoEscape(r' &[Ref:INSDAG-Chp~ 5,\\&Sect.5.2.3]\end{aligned}'))
    return web_width_min_eqn


def flange_plate_area_prov(B,pref,y,outerwidth,fp_area,t,r_1,innerwidth =None):
    """
    Calculate flange plate area

    Args:
         B:Width of the section in mm (float)
         pref:Outside or OUtside +inside (str)
         y:flange thickness in mm (float)
         outerwidth:over width in mm (float)
         fp_area:flange plate area in mm square (float)
         t:web thickness in mm (float)
         r_1:root radius in mm (float)
         innerwidth:Innerwidth in mm (float)
    Returns:
         flange plate area
    """

    outerwidth = str(outerwidth)
    B = str(B)
    fp_area = str(fp_area)
    t = str(t)
    r_1 = str(r_1)
    innerwidth = str(innerwidth)
    y = str(y)
    flangeplate_crs_sec_area_eqn = Math(inline=True)

    if pref == "Outside":
        flangeplate_crs_sec_area_eqn.append(NoEscape(r'\begin{aligned} B_{fp} &= B - (2 \times 21)\\'))
        flangeplate_crs_sec_area_eqn.append(NoEscape(r'&= '+B+r' - (2 \times 21)\\'))
        flangeplate_crs_sec_area_eqn.append(NoEscape(r'&= ' + outerwidth + r' \\'))
        flangeplate_crs_sec_area_eqn.append(NoEscape(r' pt.area &= '+y+ r' \times' +outerwidth+r'\\'))
        flangeplate_crs_sec_area_eqn.append(NoEscape(r'&= '+fp_area+r'\end{aligned}'))
    else:
        flangeplate_crs_sec_area_eqn.append(NoEscape(r'\begin{aligned} B_{fp} &= B-(2 \times 21)\\'))
        flangeplate_crs_sec_area_eqn.append(NoEscape(r'&='+B+ r'-(2 \times 21)\\'))
        flangeplate_crs_sec_area_eqn.append(NoEscape(r'&= ' + outerwidth + r' \\'))
        flangeplate_crs_sec_area_eqn.append(NoEscape(r'B_{ifp}&= \frac{B-t-(2 \times R1)-(4 \times 21)}{2}\\'))
        flangeplate_crs_sec_area_eqn.append(NoEscape(r'&=\frac{'+B+'-'+t+r'-(2 \times '+r_1+r')-(4 \times 21)}{2}\\'))
        flangeplate_crs_sec_area_eqn.append(NoEscape(r'&= ' + innerwidth + r' \\'))
        flangeplate_crs_sec_area_eqn.append(NoEscape(r' pt.area &=('+outerwidth+r'+(2 \times' +innerwidth+r')) \times' +y+r'\\'))
        flangeplate_crs_sec_area_eqn.append(NoEscape(r'&= ' + fp_area + r'\end{aligned}'))


    return flangeplate_crs_sec_area_eqn


def plate_recheck_area_weld(outerwidth,innerwidth=None,f_tp=None,t_wp=None,conn=None,pref=None):
    """
    Re-check plate area

    Args:
          flange_plate_area: area of the flange plate in mm square (float)
          web_plate_area:area of the web plate in mm square (float)
          outerwidth: flange plate height in mm  (float)
          innerwidth: flange plate Innerheight  in mm  (float)
          f_tp: flange plate thickness provided  in mm  (float)
          t_wp:None
          conn:"flange" or "web" (str)
          pref: "Outside+Inside" or "outside" (str)
    Returns:
          plate area
    """

    if conn == "flange":
        if pref =="Outside":
            flange_plate_area = (outerwidth * f_tp)

        else:
            flange_plate_area = (outerwidth + (2 * innerwidth)) * f_tp
            # flange_plate_area = str(flange_plate_area)
    else :
        web_plate_area = (2 * outerwidth * t_wp)
        # web_plate_area = str(web_plate_area)
    outerwidth = str(outerwidth)
    innerwidth = str(innerwidth)
    f_tp= str(f_tp)
    t_wp = str(t_wp)
    # flange_plate_area  = str(flange_plate_area)
    # web_plate_area  = str(web_plate_area)
    plate_recheck_area_weld_eqn = Math(inline=True)
    if conn == "flange":
        if pref =="Outside":
            flange_plate_area = str(flange_plate_area)
            plate_recheck_area_weld_eqn.append(NoEscape(r'\begin{aligned}  pt.area &=B_{fp} \times t_{ifp}\\'))
            plate_recheck_area_weld_eqn.append(NoEscape(r' &='+outerwidth+r'\times'+f_tp+r'\\'))
            plate_recheck_area_weld_eqn.append(NoEscape(r'&= ' + flange_plate_area + r'\end{aligned}'))
        else:
            flange_plate_area = str(flange_plate_area)
            plate_recheck_area_weld_eqn.append(NoEscape(r'\begin{aligned}  pt.area &=(B_{fp} +(2\times B_{ifp}))\times  t_{ifp}  \\'))
            plate_recheck_area_weld_eqn.append(NoEscape(r' &=(' + outerwidth + r'+(2\times' + innerwidth + r'))\times' + f_tp + r'\\'))
            plate_recheck_area_weld_eqn.append(NoEscape(r'&= ' + flange_plate_area +r'\end{aligned}'))
    else:
        web_plate_area  = str(web_plate_area)
        plate_recheck_area_weld_eqn.append(NoEscape(r'\begin{aligned}  pt.area &=2\times W_{wp} \times t_{wp}  \\'))
        plate_recheck_area_weld_eqn.append(NoEscape(r' &=2\times' + outerwidth +r' \times' + t_wp + r'\\'))
        plate_recheck_area_weld_eqn.append(NoEscape(r'&= ' + web_plate_area + r'\end{aligned}'))
    return plate_recheck_area_weld_eqn


def flange_plate_area_prov_bolt(B,pref,y,outerwidth,fp_area,t,r_1,innerwidth =None):
    """
     Calculate the flange plate area for column-column bolted connection

     Args:

          B:flange width of the section in mm (float)
          pref:outside or (outside +inside) (string)
          y: web thickness in mm (float)
          outerwidth: outerwidth of flange width in mm (float)
          fp_area:area of flange plate in mm square (float)
          t: flange thickness in mm (float)
          r_1:root radius of the section in mm (float)
          innerwidth:innerwidth of flange plate in mm (float)
     Returns:
          flange plate area
    """
    outerwidth = str(outerwidth)
    B = str(B)
    fp_area = str(fp_area)
    t = str(t)
    r_1 = str(r_1)
    innerwidth = str(innerwidth)
    y = str(y)
    flangeplate_crs_sec_area_bolt_eqn = Math(inline=True)
    if pref == "Outside":

        flangeplate_crs_sec_area_bolt_eqn.append(NoEscape(r'\begin{aligned} B_{fp} &= B\\'))
        flangeplate_crs_sec_area_bolt_eqn.append(NoEscape(r'&= ' + outerwidth +r'\\'))

        flangeplate_crs_sec_area_bolt_eqn.append(NoEscape(r' pt.area &= ' + y + r' \times ' + outerwidth + r'\\'))
        flangeplate_crs_sec_area_bolt_eqn.append(NoEscape(r'&= ' + fp_area + r'\end{aligned}'))
    else:

        flangeplate_crs_sec_area_bolt_eqn.append(NoEscape(r'\begin{aligned} B_{fp} &= B\\'))
        flangeplate_crs_sec_area_bolt_eqn.append(NoEscape(r'&= ' + outerwidth + r' \\'))
        flangeplate_crs_sec_area_bolt_eqn.append(NoEscape(r'B_{ifp} &= \frac{B-t-(2 \times R1)}{2}\\'))
        flangeplate_crs_sec_area_bolt_eqn.append(NoEscape(r'&=\frac{' + B + '-' + t + r'-(2 \times' + r_1 + r')}{2}\\'))
        flangeplate_crs_sec_area_bolt_eqn.append(NoEscape(r'&= ' + innerwidth + r' \\'))
        flangeplate_crs_sec_area_bolt_eqn.append(NoEscape(r' pt.area &=(' + outerwidth + r'+(2 \times' + innerwidth + r')) \times' + y + r'\\'))
        flangeplate_crs_sec_area_bolt_eqn.append(NoEscape(r'&= ' + fp_area + r'\end{aligned}'))

    return flangeplate_crs_sec_area_bolt_eqn


def web_plate_area_prov(D, y, webwidth, wp_area, T, r_1):
    """
    Calculate   area of provided plate for web in case of welded connection

    Args:
           D:section depth in mm (float)
           y:thickness of web in mm (float)
           webwidth:width of web section  in mm (float)
           wp_area:  area of provided plate for web in mm square (float)
           T: flange thickness  in mm (float)
           r_1:  section root radius in mm (float)

    Returns:
          area of provided plate for web
    """
    D = str(D)
    T = str(T)
    r_1 = str(r_1)
    webwidth = str(webwidth)
    wp_area =str(wp_area)
    y =str(y)

    web_plate_area_prov = Math(inline=True)
    # web_plate_area_prov.append(NoEscape(r'\begin{aligned} W_{wp}&= D-(2*T)-(2*R1)-(2*21)\\'))
    # web_plate_area_prov.append(NoEscape(r'&='+D+'-(2\times'+T+')-(2\times'+r_1+r')-(2*21)\\'))
    # web_plate_area_prov.append(NoEscape(r'&= ' + webwidth + r' \\'))
    web_plate_area_prov.append(NoEscape(r'\begin{aligned} pt.area &= t_{wp} \times 2 \times W_{wp}\\'))
    web_plate_area_prov.append(NoEscape(r'  &= ' + y +r'\times 2 \times ' + webwidth + r'\\'))
    web_plate_area_prov.append(NoEscape(r'&= ' + wp_area + r'\end{aligned}'))
    return web_plate_area_prov


def web_plate_area_prov_bolt(D, y, webwidth, wp_area, T, r_1):
    """
    Calculate   area of provided plate for web

    Args:
          D:section depth in mm (float)
          y:thickness of web in mm (float)
          webwidth:width of web section  in mm (float)
          wp_area:  area of provided plate for web in mm square (float)
          T: flange thickness  in mm (float)
          r_1: root radius in mm (float)
    Returns:
         area of provided plate for web
    """
    D = str(D)
    T = str(T)
    r_1 = str(r_1)
    webwidth = str(webwidth)
    wp_area = str(wp_area)
    y = str(y)

    web_plate_area_prov = Math(inline=True)
    # web_plate_area_prov.append(NoEscape( W_{wp}&= D-(2*T)-(2*R1)\\'))
    # web_plate_area_prov.append(NoEscape(r'&=' + D + '-(2\times' + T + ')-(2\times' + r_1 + r')\\'))
    # web_plate_area_prov.append(NoEscape(r'&= ' + webwidth + r' \\'))
    web_plate_area_prov.append(NoEscape(r'\begin{aligned}pt.area &= t_{wp} \times 2 \times  W_{wp} \\'))
    web_plate_area_prov.append(NoEscape(r'&= ' + y +r'\times 2 \times' + webwidth + r'\\'))
    web_plate_area_prov.append(NoEscape(r'&= ' + wp_area + r'\end{aligned}'))
    return web_plate_area_prov

# functions for base plate


def square_washer_size(side):
    """ equation for the size of square plate washer """
    side = str(side)

    washer_dim = Math(inline=True)
    washer_dim.append(NoEscape(r'\begin{aligned} Square - ' + side + r' X ' + side + r' \\'))
    washer_dim.append(NoEscape(r'&[Ref.~IS~6649:1985,~(Table~2)]\end{aligned}'))

    return washer_dim


def square_washer_thk(thickness):
    """ equation for the thickness of square plate washer """
    thickness = str(thickness)

    washer_thk = Math(inline=True)
    washer_thk.append(NoEscape(r'\begin{aligned} t_{w} = ' + thickness + r' \\'))
    washer_thk.append(NoEscape(r'&[Ref.~IS~6649:1985,~(Table~2)]\end{aligned}'))

    return washer_thk


def square_washer_in_dia(dia):
    """ equation for the hole diameter of square plate washer """
    dia = str(dia)

    washer_in_dia = Math(inline=True)
    washer_in_dia.append(NoEscape(r'\begin{aligned} ' + dia + r' \\'))
    washer_in_dia.append(NoEscape(r'&[Ref.~IS~6649:1985,~(Table~2)]\end{aligned}'))

    return washer_in_dia


def hexagon_nut_thickness(nut_thick):
    """ equation for the thickness of the hexagon nut """
    nut_thick = str(nut_thick)

    nut_thickness = Math(inline=True)
    nut_thickness.append(NoEscape(r'\begin{aligned} t_{n} = ' + nut_thick + r' \\'))
    nut_thickness.append(NoEscape(r'&[Ref.~IS~1364-3:2002,~(Table~1)]\end{aligned}'))

    return nut_thickness


def anchor_len_above_footing(length):
    """ equation for the length of the anchor bolt above footing """
    length = str(length)

    anchor_len = Math(inline=True)
    anchor_len.append(NoEscape(r'\begin{aligned} grout thickness + thickness of base plate + thickness of plate washer +nut thickness + 20 \\'))
    anchor_len.append(NoEscape(r'\begin{aligned} = ' + length + r' \\'))

    return anchor_len


def bp_length(col_depth, end_distance, length):
    """ equation for the min length of the base plate"""
    col_depth = str(col_depth)
    end_distance = str(end_distance)
    length = str(length)

    bp_length_min = Math(inline=True)
    bp_length_min.append(NoEscape(r'\begin{aligned} L = column~depth ~+~2~(e~+~e) \\'))
    bp_length_min.append(NoEscape(r'\begin{aligned}   = ' + col_depth + r' ~+~2~(' + end_distance + r'~+~' + end_distance + r') \\'))
    bp_length_min.append(NoEscape(r'\begin{aligned}   = ' + length + r' \\'))
    bp_length_min.append(NoEscape(r'&[Ref.~based~on~detailing~requirement]\end{aligned}'))

    return bp_length_min


def bp_length_sb(col_depth, end_distance, length, projection):
    """ equation for the min length of the welded slab base/base plate for hollow/tubular sections"""
    col_depth = str(col_depth)
    end_distance = str(end_distance)
    length = str(length)
    projection = str(projection)

    bp_length_min = Math(inline=True)
    bp_length_min.append(NoEscape(r'\begin{aligned} L = column~depth ~+~2~(c~+~e) \\'))
    bp_length_min.append(NoEscape(r'\begin{aligned}   = ' + col_depth + r' ~+~2~(' + projection + r'~+~' + end_distance + r') \\'))
    bp_length_min.append(NoEscape(r'\begin{aligned}   = ' + length + r' \\'))
    bp_length_min.append(NoEscape(r'&[Ref.~based~on~detailing~requirement]\end{aligned}'))

    return bp_length_min


def bp_width(flange_width, edge_distance, width):
    """ equation for the min length of the base plate"""
    flange_width = str(flange_width)
    edge_distance = str(edge_distance)
    width = str(width)

    bp_width_min = Math(inline=True)
    bp_width_min.append(NoEscape(r'\begin{aligned} W = flange~width ~+~2~(1.5 \times e~+~1.5 \times e) \\'))  # TODO add e' instead of e
    bp_width_min.append(NoEscape(r'\begin{aligned}   = ' + flange_width + r' ~+~2~(1.5 \times ' + edge_distance + r'~+~1.5 \times ' + edge_distance +
                                 r') \\'))
    bp_width_min.append(NoEscape(r'\begin{aligned}   = ' + width + r') \\'))
    bp_width_min.append(NoEscape(r'&[Ref.~based~on~detailing~requirement]\end{aligned}'))

    return bp_width_min


def bearing_strength_concrete(concrete_grade, bearing_strength_value):
    """ equation for the bearing strength of concrete"""
    concrete_grade = str(concrete_grade)
    bearing_strength_value = str(bearing_strength_value)

    bearing_strength = Math(inline=True)
    bearing_strength.append(NoEscape(r'\begin{aligned} \sigma_{br} = 0.45f_{ck} \\'))
    bearing_strength.append(NoEscape(r'\begin{aligned}             = 0.45 ' + concrete_grade + r' \\'))
    bearing_strength.append(NoEscape(r'\begin{aligned}             = ' + bearing_strength_value + r' \\'))
    bearing_strength.append(NoEscape(r'&[Ref.~IS~800:2007,~(Cl.7.4.1)]\end{aligned}'))

    return bearing_strength


def actual_bearing_pressure(axial_load, bp_area_provided, bearing_pressure):
    """ """
    axial_load = str(axial_load)
    bp_area_provided = str(bp_area_provided)
    bearing_pressure = str(bearing_pressure)

    bp_bearing_pressure = Math(inline=True)
    bp_bearing_pressure.append(NoEscape(r'\begin{aligned} {\sigma_{br}}_{actual} = \frac{P}{A_{provided}} \\'))
    bp_bearing_pressure.append(NoEscape(r'\begin{aligned}                        = \frac{' + axial_load + r'}{' + bp_area_provided + r'} \\'))
    bp_bearing_pressure.append(NoEscape(r'\begin{aligned}                        = ' + bearing_pressure + r' \\'))

    return bp_bearing_pressure


def bp_thk_1(plate_thk, projection, actual_bearing_stress, gamma_m0, fy_plate):
    """ """
    plate_thk = str(plate_thk)
    projection = str(projection)
    actual_bearing_stress = str(actual_bearing_stress)
    gamma_m0 = str(gamma_m0)
    fy_plate = str(fy_plate)

    thk = Math(inline=True)
    thk.append(NoEscape(r'\begin{aligned} t_p = c~\Bigg[\frac{2.5~{\sigma_{br}}_{actual}~\gamma_{m0}}{{f_{y}}_{plate}}\Bigg]^{0.5} \\'))
    thk.append(NoEscape(r'\begin{aligned}     = ' + projection + r'~\Bigg[\frac{2.5~' + actual_bearing_stress + r'~' + gamma_m0 + r'}{'
                        + fy_plate + r'}\Bigg]^{0.5} \\'))
    thk.append(NoEscape(r'\begin{aligned}     = ' + plate_thk + r' \\'))

    return thk


def eccentricity(moment, axial_load, eccentricity_zz):
    """ calculate eccentricity along the major axis"""
    moment = str(moment)
    axial_load = str(axial_load)
    eccentricity_zz = str(eccentricity_zz)

    ecc_zz = Math(inline=True)
    ecc_zz.append(NoEscape(r'\begin{aligned} e_{zz} = \frac{M_{zz}}{P} \\'))
    ecc_zz.append(NoEscape(r'\begin{aligned}        = \frac{' + moment + r'}{' + axial_load + r'} \\'))
    ecc_zz.append(NoEscape(r'\begin{aligned}        = ' + eccentricity_zz + r' \\'))

    return ecc_zz


def k1(ecc_zz, bp_length, k1_value):
    """ calculate k1

    Args:
        ecc_zz (e) - end distance in mm (float)
        bp_length (L) - length of the base plate in mm (float)
        k1_value - value of k1 (float)

    Returns:
        k1 [k1 = 3 * (e - L/2)] (float)
    """
    ecc_zz = str(ecc_zz)
    bp_length = str(bp_length)
    k1_value = str(k1_value)

    k1 = Math(inline=True)
    k1.append(NoEscape(r'\begin{aligned} k_{1} = 3~\Big(e_{zz} ~-~\frac{L}{2}\Big) \\'))
    k1.append(NoEscape(r'\begin{aligned}       = 3~\Big(' + ecc_zz + r'~-~\frac{' + bp_length + r'}{2}\Big) \\'))
    k1.append(NoEscape(r'\begin{aligned}       = ' + k1_value + r' \\'))
    k1.append(NoEscape(r'&[Ref.~Design~of~Welded~Structures~-~Omer~W~Blodgett~(section~3.3)]\end{aligned}'))

    return k1


def modular_ratio(E_s, f_ck, modular_ratio):
    """ calculate modular ratio

    """
    E_s = str(E_s)
    E_c = round((5000 * math.sqrt(f_ck)), 3)
    E_c = str(E_c)
    f_ck = str(f_ck)

    n = Math(inline=True)
    n.append(NoEscape(r'\begin{aligned} n = \frac{E_{s}}{E_{c}} \\'))
    n.append(NoEscape(r'\begin{aligned} E_s = 2 \times 10 ^ {5}~(N/mm^{2}) \\'))
    n.append(NoEscape(r'\begin{aligned} E_c = 5000~\sqrt{f_{ck}}~(N/mm^{2}) \\'))
    n.append(NoEscape(r'\begin{aligned}     = 5000~\sqrt{' + f_ck + r'}~=~' + E_c + r' \\'))
    n.append(NoEscape(r'\begin{aligned} n = \frac{' + E_s + r'}{' + E_c + r'} \\'))
    n.append(NoEscape(r'\begin{aligned}   =  ' + modular_ratio + r'\\'))
    n.append(NoEscape(r'&[Ref.~Design~of~Welded~Structures~-~Omer~W~Blodgett~(section~3.3)] \end{aligned}'))

    return n


def epsilon(yield_stress, epsilon_value):
    """ """
    yield_stress = str(yield_stress)
    epsilon_value = str(epsilon_value)

    value = Math(inline=True)
    value.append(NoEscape(r'\begin{aligned} \epsilon_{st} = \sqrt{\frac{250}{f_{y}}} \\'))
    value.append(NoEscape(r'\begin{aligned}               = \sqrt{\frac{250}{' + yield_stress + r'}} \\'))
    value.append(NoEscape(r'\begin{aligned}               = ' + epsilon_value + r' \end{aligned}'))

    return value


def total_anchor_area_tension(anchor_dia, anchor_nos_tension, anchor_area_tension):
    """

    """
    anchor_dia = str(anchor_dia)
    anchor_nos_tension = str(anchor_nos_tension)
    anchor_area_tension = str(anchor_area_tension)

    total_anchor_area = Math(inline=True)
    total_anchor_area.append(NoEscape(r'\begin{aligned} A_{s} = n \times ~\Big(\frac{\pi}{4}\Big)~d^{2} \\'))
    total_anchor_area.append(NoEscape(r'\begin{aligned}       = ' + anchor_nos_tension + r' \times ~\Big(\frac{\pi}{4}\Big)~ '
                                      + anchor_dia + r'^{2} \\'))
    total_anchor_area.append(NoEscape(r'\begin{aligned} = ' + anchor_area_tension + r' \\'))

    return total_anchor_area


def calc_f(end_distance, bp_length, f):
    """

    """
    end_distance = str(end_distance)
    bp_length = str(bp_length)

    dist_f = Math(inline=True)
    dist_f.append(NoEscape(r'\begin{aligned} f = \Big(\frac{L}{2} - e\Big) \\'))
    dist_f.append(NoEscape(r'\begin{aligned}   = \Big(\frac{' + bp_length + r'}{2} - ' + end_distance + r'\Big) \\'))
    dist_f.append(NoEscape(r'\begin{aligned}   = ' + f + r' \\'))
    dist_f.append(NoEscape(r'&[Ref.~Design~of~Welded~Structures~-~Omer~W~Blodgett~(section~3.3)]\end{aligned}'))

    return dist_f


def k2(n, anchor_area_tension, bp_width, f, e, k2_value):
    """ calculate k2

    Args:
        n - modular ratio (float)
        anchor_area_tension (A_s) - total area of the anchor hold down bolts under tension (float)
        bp_width (B) - width of the base plate in mm (float)
        f = distance between the centre of the base plate and the centre of the anchor bolt(s) under tension (float)
        e = eccentricity (float)
        k2_value (float)

    Returns:
        k2 [k2 = (6*n*A_s / W) * (f + e) ] (float)
    """
    n = str(n)
    anchor_area_tension = str(anchor_area_tension)
    bp_width = str(bp_width)
    f = str(f)
    e = str(e)
    k2_value = str(k2_value)

    k2 = Math(inline=True)
    k2.append(NoEscape(r'\begin{aligned} k_2 = \frac{6~n~A_s}{W}~\Big(f~+~e_{zz}\Big) \\'))
    k2.append(
        NoEscape(r'\begin{aligned}     = \frac{6~' + n + r'~' + anchor_area_tension + r'}{' + bp_width + r'}~\Big(' + f + r'~+~' + e + r'\Big) \\'))
    k2.append(NoEscape(r'\begin{aligned}     = ' + k2_value + r' \\'))
    k2.append(NoEscape(r'&[Ref.~Design~of~Welded~Structures~-~Omer~W~Blodgett~(section~3.3)]\end{aligned}'))

    return k2


def k3(k2_value, bp_length, f, k3_value):
    """ calculate k3 """
    k2_value = str(k2_value)
    bp_length = str(bp_length)
    f = str(f)
    k3_value = str(k3_value)

    k3 = Math(inline=True)
    k3.append(NoEscape(r'\begin{aligned} k_3 = - ~k_2~\Big(\frac{L}{2}~+~f\Big) \\'))
    k3.append(NoEscape(r'\begin{aligned}     = - ~' + k2_value + r'~\Big(\frac{' + bp_length + r'}{2}~+~' + f + r'\Big) \\'))
    k3.append(NoEscape(r'\begin{aligned}     = ' + k3_value + r' \\'))
    k3.append(NoEscape(r'&[Ref.~Design~of~Welded~Structures~-~Omer~W~Blodgett~(section~3.3)]\end{aligned}'))

    return k3


def y(k1_value, k2_value, k3_value, y_value):
    """ calculate the distance (y) of the base plate under compression"""
    k1_value = str(k1_value)
    k2_value = str(k2_value)
    k3_value = str(k3_value)
    y_value = str(y_value)

    y = Math(inline=True)
    y.append(NoEscape(r'\begin{aligned} y^{3}~+~k_{1}~y^{2}~+~k_{2}~y~+~k_{3} = 0 \\'))
    y.append(NoEscape(r'\begin{aligned} y^{3}~+~' + k1_value + r'~y^{2}~+~' + k2_value + r'~y~+~' + k3_value + r' = 0 \\'))
    y.append(NoEscape(r'\begin{aligned} y = ' + y_value + r' \\'))
    y.append(NoEscape(r'&[Ref.~Design~of~Welded~Structures~-~Omer~W~Blodgett~(section~3.3)]\end{aligned}'))

    return y


def tension_demand_anchor(axial_load, bp_length, dist_y, ecc_zz, f, anchor_tension):
    """ calculate total tension demand on the hold down bolt(s)"""
    axial_load = str(axial_load)
    bp_length = str(bp_length)
    dist_y = str(dist_y)
    ecc_zz = str(ecc_zz)
    f = str(f)
    anchor_tension = str(anchor_tension)

    tension_total = Math(inline=True)
    tension_total.append(NoEscape(r'\begin{aligned} P_t = -~P_c~\Bigg[\frac{\frac{L}{2}-\frac{y}{3}-e_{zz}}{\frac{L}{2}-\frac{y}{3}+f}\Bigg] \\'))
    tension_total.append(NoEscape(r'\begin{aligned}     = -~P_c~\Bigg[\frac{\frac{' + bp_length + r'}{2}-\frac{' + dist_y + r'}{3}-' + ecc_zz + r'}'
                                                                                                                                                r'{\frac{' + bp_length + r'}{2}-\frac{' + dist_y + r'}{3}+' + f + r'}\Bigg] \\'))
    tension_total.append(NoEscape(r'\begin{aligned}     = ' + anchor_tension + r' \\'))
    tension_total.append(NoEscape(r'&[Ref.~Design~of~Welded~Structures~-~Omer~W~Blodgett~(section~3.3)]\end{aligned}'))

    return tension_total


def tension_demand_each_anchor(total_tension_demand, anchor_nos, tension_each_anchor):
    """ """
    total_tension_demand = str(total_tension_demand)
    anchor_nos = str(anchor_nos)
    tension_each_anchor = str(tension_each_anchor)

    tension_total = Math(inline=True)
    tension_total.append(NoEscape(r'\begin{aligned} T_{d} = \frac{P_{t}}{n} \\'))
    tension_total.append(NoEscape(r'\begin{aligned}       = \frac{' + total_tension_demand + r'}{' + anchor_nos + r'} \\'))
    tension_total.append(NoEscape(r'\begin{aligned}       = ' + tension_each_anchor + r'\end{aligned}'))

    return tension_total


def eff_bearing_area(col_depth, col_flange_width, col_flange_thk, col_web_thk):
    """ calculate min area req for base plate (only for axial loads)"""
    col_depth = str(col_depth)
    col_flange_width = str(col_flange_width)
    col_flange_thk = str(col_flange_thk)
    col_web_thk = str(col_web_thk)

    area = Math(inline=True)
    area.append(NoEscape(r'\begin{aligned} {A_{br}}_{eff} = (D~+~2 c) (B~+~2 c) - \Big[ \big(D - 2(T~+~c)\big) \big(B - t\big) \Big] \\'))
    area.append(NoEscape(r'\begin{aligned}                = (' + col_depth + r' ~+~2 c) (' + col_flange_width + r' ~+~2 c) - \Big[ \big('
                         + col_depth + r' - 2(' + col_flange_thk + r'~+~c)\big) \big(' + col_flange_width + r' - ' + col_web_thk + r'\big) \Big] \\'))
    area.append(NoEscape(r'\begin{aligned} Note: c is the projection beyond the face of the column \\'))
    area.append(NoEscape(r'&[Ref.~Design~of~Steel~Structures~-~N.~Subramanian~(Limit~State~Method~-~edition~2019)]\end{aligned}'))

    return area


def eff_projection(col_depth, col_flange_width, col_flange_thk, col_web_thk, min_area, projection, end_distance):
    """ calculate min area req for base plate (only for axial loads)"""
    col_depth = str(col_depth)
    col_flange_width = str(col_flange_width)
    col_flange_thk = str(col_flange_thk)
    col_web_thk = str(col_web_thk)
    min_area = str(min_area)
    projection = str(projection)
    end_distance = str(end_distance)

    c = Math(inline=True)
    c.append(NoEscape(r'\begin{aligned} {A_{br}}_{eff} = {A_{req}}_{min} \\'))
    c.append(NoEscape(r'\begin{aligned}                = ' + min_area + r' \\'))
    c.append(NoEscape(r'\begin{aligned} Therefore,~ ' + min_area + r' = (' + col_depth + r' ~+~2 c) (' + col_flange_width + r' ~+~2 c) - \Big[ \big('
                      + col_depth + r' - 2(' + col_flange_thk + r'~+~c)\big) \big(' + col_flange_width + r' - ' + col_web_thk + r'\big) \Big] \\'))
    c.append(NoEscape(r'\begin{aligned}              c  = ' + projection + r' \\'))
    c.append(NoEscape(r'\begin{aligned} projection = max(' + projection + r',~' + end_distance + r') \\'))
    c.append(NoEscape(r'\begin{aligned}            = ' + projection + r' \\'))
    c.append(NoEscape(r'&[Ref.~Design~of~Steel~Structures~-~N.~Subramanian~(Limit~State~Method~-~edition~2019)]\end{aligned}'))

    return c


def min_area_req(axial_load, bearing_strength, bp_min_area):
    """ calculate min area req for base plate (only for axial loads)"""
    axial_load = str(axial_load)
    bearing_strength = str(bearing_strength)
    bp_min_area = str(bp_min_area)

    area = Math(inline=True)
    area.append(NoEscape(r'\begin{aligned} {A_{req}}_{min} = \frac{P_c}{\sigma_{br}} \\'))
    area.append(NoEscape(r'\begin{aligned}                 = \frac{' + axial_load + r'}{' + bearing_strength + r'} \\'))
    area.append(NoEscape(r'\begin{aligned}        = ' + bp_min_area + r' \end{aligned}'))

    return area


def mom_bp_case(case, eccentricity, bp_length):
    """ """
    case = str(case)
    eccentricity = str(eccentricity)
    bp_length = str(bp_length)

    bp_case = Math(inline=True)
    if case == 'Case1':
        bp_length = int(bp_length)
        value = bp_length / 6
        value = str(value)
        bp_length = str(bp_length)

        bp_case.append(NoEscape(r'\begin{aligned} e_{zz} \leq \frac{L_{min}}{6} \\'))
        bp_case.append(NoEscape(r'\begin{aligned} ' + eccentricity + r' \leq \frac{' + bp_length + r'}{6} \\'))
        bp_case.append(NoEscape(r'\begin{aligned} ' + eccentricity + r' \leq ' + value + r' \end{aligned}'))
    elif case == 'Case2':
        bp_length = int(bp_length)
        value1 = bp_length / 6
        value2 = bp_length / 3
        value1 = str(value1)
        value2 = str(value2)
        bp_length = str(bp_length)

        bp_case.append(NoEscape(r'\begin{aligned} \frac{L_{min}}{6} < e_{zz} < \frac{L_{min}}{3} \\'))
        bp_case.append(NoEscape(r'\begin{aligned} \frac{' + bp_length + r'}{6} < ' + eccentricity + r' < \frac{' + bp_length + r'}{3} \\'))
        bp_case.append(NoEscape(r'\begin{aligned} ' + value1 + r' < ' + eccentricity + r' < ' + value2 + r'\end{aligned}'))
    elif case == 'Case3':
        bp_length = int(bp_length)
        value = bp_length / 3
        value = str(value)
        bp_length = str(bp_length)

        bp_case.append(NoEscape(r'\begin{aligned} e_{zz} \geq \frac{L_{min}}{3} \\'))
        bp_case.append(NoEscape(r'\begin{aligned} ' + eccentricity + r' \geq \frac{' + bp_length + r'}{3} \\'))
        bp_case.append(NoEscape(r'\begin{aligned} ' + eccentricity + r' \leq ' + value + r'\end{aligned}'))

    return bp_case


def bp_section_modulus(bp_length, bp_width, section_modulus):
    """ """
    bp_length = str(bp_length)
    bp_width = str(bp_width)
    section_modulus = str(section_modulus)

    ze_zz = Math(inline=True)
    ze_zz.append(NoEscape(r'\begin{aligned} {z_{e}}_{plate} = \frac{W L^{2}}{6} \\'))
    ze_zz.append(NoEscape(r'\begin{aligned}                 = \frac{' + bp_width + r' ' + bp_length + r'^{2}}{6} \\'))
    ze_zz.append(NoEscape(r'\begin{aligned}                 = ' + section_modulus + r'\end{aligned}'))

    return ze_zz


def bending_stress(axial_load, moment_major, bp_area, section_modulus, sigma_max, sigma_min):
    """ """
    axial_load = str(axial_load)
    moment_major = str(moment_major)
    bp_area = str(bp_area)
    section_modulus = str(section_modulus)
    sigma_max = str(sigma_max)
    sigma_min = str(sigma_min)

    sigma = Math(inline=True)
    sigma.append(NoEscape(r'\begin{aligned} {\sigma_{b}}_{max} = \frac{P_{c}}{A}~+~\frac{M_{zz}}{{z_{e}}_{plate}} \\'))
    sigma.append(NoEscape(r'\begin{aligned}                    = \frac{' + axial_load + r'}{' + bp_area + r'}~+~\frac{' + moment_major + r'}{' +
                          section_modulus + r'} \\'))
    sigma.append(NoEscape(r'\begin{aligned}                 = ' + sigma_max + r' \\'))

    sigma.append(NoEscape(r'\begin{aligned} {\sigma_{b}}_{min} = \frac{P_{c}}{A}~-~\frac{M_{zz}}{{z_{e}}_{plate}} \\'))
    sigma.append(NoEscape(r'\begin{aligned}                    = \frac{' + axial_load + r'}{' + bp_area + r'}~-~\frac{' + moment_major + r'}{' +
                          section_modulus + r'} \\'))
    sigma.append(NoEscape(r'\begin{aligned}                 = ' + sigma_min + r'\end{aligned}'))

    return sigma


def critical_section(bp_length, col_depth, critical_len):
    """ """
    bp_length = str(bp_length)
    col_depth = str(col_depth)
    critical_len = str(critical_len)

    length = Math(inline=True)
    length.append(NoEscape(r'\begin{aligned} y_{critical} = \frac{L ~- ~(0.95D)}{2} \\'))
    length.append(NoEscape(r'\begin{aligned}              = \frac{' + bp_length + r' ~- ~(0.95' + col_depth + r')}{2} \\'))
    length.append(NoEscape(r'\begin{aligned}              = ' + critical_len + r'\end{aligned}'))

    return length


def critical_section_case_2_3(critical_xx, y):
    """ """
    critical_len = Math(inline=True)

    if y > critical_xx:
        critical_xx = str(critical_xx)
        y = str(y)
        critical_len.append(NoEscape(r'\begin{aligned} y~ > ~y_{critical}~~~ (' + y + r'~ > ~' + critical_xx + r') \\'))
        critical_len.append(NoEscape(r'\begin{aligned} \therefore y_{critical} = ' + critical_xx + r' \\'))
    else:
        critical_xx = str(critical_xx)
        y = str(y)
        critical_len.append(NoEscape(r'\begin{aligned} y~ < ~y_{critical}~~~ (' + y + r'~ < ~' + critical_xx + r') \\'))
        critical_len.append(NoEscape(r'\begin{aligned} \therefore y_{critical} = ' + y + r' \\'))

    return critical_len


def bending_stress_critical_sec(bending_stress_critical):
    """ """
    bending_stress_critical = str(bending_stress_critical)

    stress = Math(inline=True)
    stress.append(NoEscape(r'\begin{aligned} {\sigma_{b}}_{critical} = ' + bending_stress_critical + r'\\'))

    return stress


def moment_critical_section(sigma_x, sigma_max, critical_len, moment, concrete_bearing_stress, bp_width, case='Case1'):
    """ """
    sigma_x = str(sigma_x)
    sigma_max = str(sigma_max)
    critical_len = str(critical_len)
    moment = str(moment)
    concrete_bearing_stress = str(concrete_bearing_stress)
    bp_width = str(bp_width)

    critical_moment = Math(inline=True)

    if case == 'Case1':
        critical_moment.append(NoEscape(r'\begin{aligned} M_{critical} =  \bigg({\sigma_{b}}_{critical} \times y_{critical}\times '
                                        r'\frac{y_{critical}}{2}\bigg)~ + \bigg(\frac{1}{2}\times y_{critical}\times '
                                        r'\big({{\sigma_{b}}_{max} - \sigma_{b}}_{critical}\big)\times \frac{2}{3}\times y_{critical}\bigg) \\'))

        critical_moment.append(NoEscape(r'\begin{aligned}              =  \bigg(' + sigma_x + r' \times ' + critical_len + r'\times '
                                                                                                                           r'\frac{' + critical_len + r'}{2}\bigg)~ + \bigg(\frac{1}{2}\times ' + critical_len + r'\times '
                                                                                                                                                                                                                 r'\big({' + sigma_max + r' - ' + sigma_x + r'\big)\times \frac{2}{3}\times ' + critical_len + r'\bigg) \\'))

        critical_moment.append(NoEscape(r'\begin{aligned}              = ' + moment + r' \end{aligned}'))
    else:
        critical_moment.append(NoEscape(r'\begin{aligned} {M_{critical}}_{1} = 0.45f_{ck}~W~y_{critical}\times \bigg(\frac{y_{critical}}{2}\bigg) \\'))
        critical_moment.append(NoEscape(r'\begin{aligned} {M_{critical}}_{1} = 0.45' + concrete_bearing_stress + r'~' + bp_width + r'~'
                                        + critical_len + r'\times \bigg(\frac{' + critical_len + r'}{2}\bigg) \\'))
        critical_moment.append(NoEscape(r'\begin{aligned}                    = ' + moment + r' \end{aligned}'))

    return critical_moment


def lever_arm_tension(bp_len, column_D, column_T, end_distance, lever_arm):
    """ """
    bp_len = str(bp_len)
    column_D = str(column_D)
    column_T = str(column_T)
    end_distance = str(end_distance)
    lever_arm = str(lever_arm)

    dist = Math(inline=True)
    dist.append(NoEscape(r'\begin{aligned} l = \frac{L}{2}-\frac{D}{2}+\frac{T}{2}-e \\'))
    dist.append(NoEscape(r'\begin{aligned}   = \frac{' + bp_len + r'}{2}-\frac{' + column_D + r'}{2}+\frac{' + column_T + r'}{2}-'
                         + end_distance + r' \\'))
    dist.append(NoEscape(r'\begin{aligned}  = ' + lever_arm + r'\end{aligned}'))

    return dist


def lever_arm_moment(tension_demand, lever_arm, moment):
    """ """
    tension_demand = str(tension_demand)
    lever_arm = str(lever_arm)
    moment = str(moment)

    moment_critical = Math(inline=True)
    moment_critical.append(NoEscape(r'\begin{aligned} {M_{critical}}_{2} = T_{d}~l\times1000 \\'))
    moment_critical.append(NoEscape(r'\begin{aligned}   = ' + tension_demand + r'~ ' + lever_arm + r'\times1000 \\'))
    moment_critical.append(NoEscape(r'\begin{aligned}  = ' + moment + r'\end{aligned}'))

    return moment_critical


def max_moment(critical_mom_1, critical_mom_2):
    """ """
    moment = max(critical_mom_1, critical_mom_2)
    moment = str(moment)
    critical_mom_1 = str(critical_mom_1)
    critical_mom_2 = str(critical_mom_2)

    moment_critical = Math(inline=True)
    moment_critical.append(NoEscape(r'\begin{aligned} M_{critical} = max~\big({M_{critical}}_{1}, ~{M_{critical}}_{2}\big) \\'))
    moment_critical.append(NoEscape(r'\begin{aligned}              = max~\big(' + critical_mom_1 + r', ~' + critical_mom_2 + r'\big) \\'))
    moment_critical.append(NoEscape(r'\begin{aligned}              = ' + moment + r'\end{aligned}'))

    return moment_critical


def md_plate():
    """ """
    moment_demand = Math(inline=True)
    moment_demand.append(NoEscape(r'\begin{aligned} {z_{e}}_{plate} = \frac{b{t_{p}}^{2}}{6} ,~where~(b = 1) \\'))
    moment_demand.append(NoEscape(r'\begin{aligned} {M_{d}}_{plate} = \frac{1.5~{f_{y}}_{p}~{z_{e}}_{plate}}{\gamma_{m0}} \\'))
    moment_demand.append(NoEscape(r'\begin{aligned}                 = \frac{1.5~{f_{y}}_{p}~\bigg(\frac{b \times t_p^{2}}{6}\bigg)}{\gamma_{m0}} \\'))
    moment_demand.append(NoEscape(r'&[Ref.~IS~800:2007,~(Cl.8.2.1.2)]\end{aligned}'))

    return moment_demand


def plate_thk1(critical_mom, plate_thk, gamma_m0, f_y_plate, bp_width):
    """ """
    critical_mom = str(critical_mom)
    plate_thk = str(plate_thk)
    gamma_m0 = str(gamma_m0)
    f_y_plate = str(f_y_plate)
    bp_width = str(bp_width)

    thk = Math(inline=True)
    thk.append(NoEscape(r'\begin{aligned} {M_{d}}_{plate} = M_{critical} \\'))
    thk.append(NoEscape(r'\begin{aligned} t_{p} = \bigg[\frac{4~M_{critical}~ \gamma_{m0}} { {f_{y}}_{p}~W }\bigg]^{0.5}  \\'))
    thk.append(NoEscape(r'\begin{aligned}       = \bigg[\frac{4~' + critical_mom + r'~' + gamma_m0 + r'}{' + f_y_plate + r'~'
                        + bp_width + r'}\bigg]^{0.5}  \\'))
    thk.append(NoEscape(r'\begin{aligned}       = ' + plate_thk + r' \\'))

    return thk


def max_bearing_stress(tension_demand, y, area_anchor_tension, n, bp_length, f, sigma_c):
    """ """
    tension_demand = str(tension_demand)
    y = str(y)
    area_anchor_tension = str(area_anchor_tension)
    n = str(n)
    bp_length = str(bp_length)
    f = str(f)
    y = str(y)
    sigma_c = str(sigma_c)

    sigma_max = Math(inline=True)
    sigma_max.append(NoEscape(r'\begin{aligned} {\sigma_{c}}_{_{{max}}} = \frac{P_{t}~y}{A_{s}~n~\big(\frac{L}{2} - y + f\big)}  \\'))
    sigma_max.append(NoEscape(r'\begin{aligned}                         = \frac{' + tension_demand + r'~' + y + r'}{' + area_anchor_tension + r'~'
                              + n + r'~\big(\frac{' + bp_length + r'}{2} - ' + y + r' + ' + f + r'\big)} \\'))
    sigma_max.append(NoEscape(r'\begin{aligned}       = ' + sigma_c + r' \\'))

    return sigma_max


def anchor_len_above(grout_thk, plate_thk, plate_washer_thk, nut_thk, len):
    """ """
    grout_thk = str(grout_thk)
    plate_thk = str(plate_thk)
    plate_washer_thk = str(plate_washer_thk)
    nut_thk = str(nut_thk)
    len = str(len)

    length = Math(inline=True)
    length.append(NoEscape(r'\begin{aligned} l_{1} = t_{g}~+~t_{p}~+~t_{w}~+~t_{n}~+~20 \\'))
    length.append(NoEscape(r'\begin{aligned}       = ' + grout_thk + r'~+~' + plate_thk + r'~+~' + plate_washer_thk + r'~+~' + nut_thk + r'~+~20 \\'))
    length.append(NoEscape(r'\begin{aligned}       = ' + len + r' \end{aligned}'))

    return length


def anchor_len_below(bolt_tension, bearing_strength, len):
    """ """
    bolt_tension = str(bolt_tension)
    bearing_strength = str(bearing_strength)
    len = str(len)

    length = Math(inline=True)
    length.append(NoEscape(r'\begin{aligned} l_{2} = \Bigg[\frac{T_{b}}{15.5\sqrt{f_{ck}}}\Bigg]^{0.67} \\'))
    length.append(NoEscape(r'\begin{aligned}       = \Bigg[\frac{' + bolt_tension + r'}{15.5\sqrt{' + bearing_strength + r'}}\Bigg]^{0.67} \\'))
    length.append(NoEscape(r'\begin{aligned}       = ' + len + r' \end{aligned}'))

    return length


def anchor_range(anchor_len_min, anchor_len_max):
    """ """
    anchor_len_min = str(anchor_len_min)
    anchor_len_max = str(anchor_len_max)

    len_range = Math(inline=True)
    len_range.append(NoEscape(r'\begin{aligned} ' + anchor_len_min + r' \leq ~l_{a}~\leq ' + anchor_len_max + r'\end{aligned}'))

    return len_range


def anchor_length(anchor_len_above, anchor_len_below, anchor_len_total):
    """ """
    anchor_len_above = str(anchor_len_above)
    anchor_len_below = str(anchor_len_below)
    anchor_len_total = str(anchor_len_total)

    length = Math(inline=True)
    length.append(NoEscape(r'\begin{aligned} l_{a} = l_{1}~+~l_{2} \\'))
    length.append(NoEscape(r'\begin{aligned}            = ' + anchor_len_above + r' ~+~' + anchor_len_below + r' \\'))
    length.append(NoEscape(r'\begin{aligned}            = ' + anchor_len_total + r' \end{aligned}'))

    return length


def uplift_demand(uplift_tension):
    """ """
    uplift_tension = str(uplift_tension)

    tension = Math(inline=True)
    tension.append(NoEscape(r'\begin{aligned} P_{up} = ' + uplift_tension + r' \end{aligned}'))

    return tension


def no_bolts_uplift(uplift_force, tension_capa):
    """ """
    bolts = uplift_force / tension_capa
    bolts = str(bolts)
    uplift_force = str(uplift_force)
    tension_capa = str(tension_capa)

    n = Math(inline=True)
    n.append(NoEscape(r'\begin{aligned} n_{up} = \frac{P_{up}}{T_{db}} \\'))
    n.append(NoEscape(r'\begin{aligned}        = \frac{' + uplift_force + r'}{' + tension_capa + r'} \\'))
    n.append(NoEscape(r'\begin{aligned}        = ' + bolts + r' \end{aligned}'))

    return n


def stiff_len_flange(bp_width, col_flange_width, stiff_length):
    """ """
    bp_width = str(bp_width)
    col_flange_width = str(col_flange_width)
    stiff_length = str(stiff_length)

    len = Math(inline=True)
    len.append(NoEscape(r'\begin{aligned} {L_{st}}_{f} = \frac{W - B}{2} \\'))
    len.append(NoEscape(r'\begin{aligned}              = \frac{' + bp_width + r' - ' + col_flange_width + r'}{2} \\'))
    len.append(NoEscape(r'\begin{aligned}              = ' + stiff_length + r' \\'))
    len.append(NoEscape(r'&[Ref.~based~on~detailing~requirement \end{aligned}'))

    return len


def stiff_height_flange(stiff_length_flange, stiff_height):
    """ """
    stiff_height = str(stiff_height)
    stiff_length_flange = str(stiff_length_flange)

    height = Math(inline=True)
    height.append(NoEscape(r'\begin{aligned} {H_{st}}_{f} = {L_{st}}_{f}~+~50 \\'))
    height.append(NoEscape(r'\begin{aligned}              = ' + stiff_length_flange + r'~+~50 \\'))
    height.append(NoEscape(r'\begin{aligned}              = ' + stiff_height + r' \\'))
    height.append(NoEscape(r'&[Ref.~stiffener~drawing~attached~below \end{aligned}'))

    return height


def stiff_thk_flange(stiff_length_flange, epsilon, col_flange_thk):
    """ """
    stiff_thk = stiff_length_flange / (8.4 * epsilon)
    stiff_thk = str(stiff_thk)
    stiff_length_flange = str(stiff_length_flange)
    epsilon = str(epsilon)
    col_flange_thk = str(col_flange_thk)

    thickness = Math(inline=True)
    thickness.append(NoEscape(r'\begin{aligned} {t_{st}}_{f} = \bigg(\frac{{L_{st}}_{f}}{8.4\times \epsilon_{st}}\bigg) \geq T \\'))
    thickness.append(NoEscape(r'\begin{aligned}        = \bigg(\frac{' + stiff_length_flange + r'}{8.4\times ' + epsilon + r'}\bigg) \geq '
                              + col_flange_thk + r' \\'))
    thickness.append(NoEscape(r'\begin{aligned}        = ' + stiff_thk + r' \geq ' + col_flange_thk + r' \\'))
    thickness.append(NoEscape(r'&[Ref.~IS~800:2007~(Table~2) \end{aligned}'))

    return thickness


def stiff_len_web(bp_length, col_depth, stiff_length):
    """ """
    bp_length = str(bp_length)
    col_depth = str(col_depth)
    stiff_length = str(stiff_length)

    len = Math(inline=True)
    len.append(NoEscape(r'\begin{aligned} {L_{st}}_{w} = \frac{L - D}{2} \\'))
    len.append(NoEscape(r'\begin{aligned}              = \frac{' + bp_length + r' - ' + col_depth + r'}{2} \\'))
    len.append(NoEscape(r'\begin{aligned}              = ' + stiff_length + r' \\'))
    len.append(NoEscape(r'&[Ref.~based~on~detailing~requirement \end{aligned}'))

    return len


def stiff_height_web(stiff_length_web, stiff_height):
    """ """
    stiff_height = str(stiff_height)
    stiff_length_web = str(stiff_length_web)

    height = Math(inline=True)
    height.append(NoEscape(r'\begin{aligned} {H_{st}}_{w} = {L_{st}}_{w}~+~50 \\'))
    height.append(NoEscape(r'\begin{aligned}              = ' + stiff_length_web + r'~+~50 \\'))
    height.append(NoEscape(r'\begin{aligned}              = ' + stiff_height + r' \\'))
    height.append(NoEscape(r'&[Ref.~stiffener~drawing~attached~below \end{aligned}'))

    return height


def stiff_thk_web(stiff_length_web, epsilon, col_web_thk):
    """ """
    stiff_thk = stiff_length_web / (8.4 * epsilon)
    stiff_thk = str(stiff_thk)
    stiff_length_web = str(stiff_length_web)
    epsilon = str(epsilon)
    col_web_thk = str(col_web_thk)

    thickness = Math(inline=True)
    thickness.append(NoEscape(r'\begin{aligned} {t_{st}}_{w} = \bigg(\frac{{L_{st}}_{w}}{8.4\times \epsilon_{st}}\bigg) \geq t \\'))
    thickness.append(NoEscape(r'\begin{aligned}        = \bigg(\frac{' + stiff_length_web + r'}{8.4\times ' + epsilon + r'}\bigg) \geq '
                              + col_web_thk + r' \\'))
    thickness.append(NoEscape(r'\begin{aligned}        = ' + stiff_thk + r' \geq ' + col_web_thk + r' \\'))
    thickness.append(NoEscape(r'&[Ref.~IS~800:2007~(Table~2) \end{aligned}'))

    return thickness


def stiff_len_across_web(stiff_length_flange, stiff_length_web, stiff_length):
    """ """
    stiff_length_flange = str(stiff_length_flange)
    stiff_length_web = str(stiff_length_web)
    stiff_length = str(stiff_length)

    len = Math(inline=True)
    # len.append(NoEscape(r'\begin{aligned} {L_{st}}_{w} = \frac{L - D}{2} '))
    len.append(NoEscape(r'\begin{aligned} {L_{st}}_{aw} = max~(a, ~b) \\'))
    len.append(NoEscape(r'\begin{aligned}               = max~(' + stiff_length_flange + r', ~' + stiff_length_web + r') \\'))
    len.append(NoEscape(r'\begin{aligned}               = ' + stiff_length + r' \\'))
    len.append(NoEscape(r'&[Ref.~based~on~detailing~requirement \end{aligned}'))

    return len


def stiff_height_across_web(stiff_length_across_web, stiff_height):
    """ """
    stiff_height = str(stiff_height)
    stiff_length_across_web = str(stiff_length_across_web)

    height = Math(inline=True)
    height.append(NoEscape(r'\begin{aligned} {H_{st}}_{aw} = {L_{st}}_{aw}~+~50 \\'))
    height.append(NoEscape(r'\begin{aligned}              = ' + stiff_length_across_web + r'~+~50 \\'))
    height.append(NoEscape(r'\begin{aligned}              = ' + stiff_height + r' \\'))
    height.append(NoEscape(r'&[Ref.~stiffener~drawing~attached~below \end{aligned}'))

    return height


def stiff_thk_across_web(stiff_length_across_web, epsilon, col_web_thk):
    """ """
    stiff_thk = stiff_length_across_web / (8.4 * epsilon)
    stiff_thk = str(stiff_thk)
    stiff_length_across_web = str(stiff_length_across_web)
    epsilon = str(epsilon)
    col_web_thk = str(col_web_thk)

    thickness = Math(inline=True)
    thickness.append(NoEscape(r'\begin{aligned} {t_{st}}_{aw} = \bigg(\frac{{L_{st}}_{aw}}{8.4\times \epsilon_{st}}\bigg) \geq t \\'))
    thickness.append(NoEscape(r'\begin{aligned}        = \bigg(\frac{' + stiff_length_across_web + r'}{8.4\times ' + epsilon + r'}\bigg) \geq '
                              + col_web_thk + r' \\'))
    thickness.append(NoEscape(r'\begin{aligned}        = ' + stiff_thk + r' \geq ' + col_web_thk + r' \\'))
    thickness.append(NoEscape(r'&[Ref.~IS~800:2007~(Table~2) \end{aligned}'))

    return thickness


def stiffener_stress_flange(sigma_crit):
    """ """
    sigma_crit = str(sigma_crit)

    stress_along_flange = Math(inline=True)
    stress_along_flange.append(NoEscape(r'\begin{aligned} {\sigma_{st}}_{f} = {\sigma_{br}}_{critical} \\'))
    stress_along_flange.append(NoEscape(r'\begin{aligned}                   = ' + sigma_crit + r' \end{aligned}'))

    return stress_along_flange


def stiffener_stress_web(sigma_max, sigma_crit, sigma_val, f_ck, type='welded_hollow_bp', case='None'):
    """ """
    sigma_val = str(sigma_val)

    stress_along_web = Math(inline=True)

    if (type == 'welded_hollow_bp') and (case == 'None'):
        stress_along_web.append(NoEscape(r'\begin{aligned} {\sigma_{st}}_{w} = {\sigma_{br}}_{actual} \\'))
        stress_along_web.append(NoEscape(r'\begin{aligned}                   = ' + sigma_val + r' \end{aligned}'))

    elif (type == 'moment_bp') and (case == 'Case2&3'):
        f_ck = str(f_ck)
        stress_along_web.append(NoEscape(r'\begin{aligned} {\sigma_{st}}_{w} = 0.45f_{ck} \\'))
        stress_along_web.append(NoEscape(r'\begin{aligned}                   = 0.45' + f_ck + r' \\'))
        stress_along_web.append(NoEscape(r'\begin{aligned}                   = ' + sigma_val + r'\end{aligned}'))

    else:
        sigma_val = (sigma_max + sigma_crit) / 2
        sigma_val = str(sigma_val)
        sigma_max = str(sigma_max)
        sigma_crit = str(sigma_crit)

        stress_along_web.append(NoEscape(r'\begin{aligned} {\sigma_{st}}_{w} = \frac{{\sigma_{b}}_{max} + {\sigma_{b}}_{critical}}{2} \\'))
        stress_along_web.append(NoEscape(r'\begin{aligned}                   = \frac{' + sigma_max + r' + ' + sigma_crit + r'}{2} \\'))
        stress_along_web.append(NoEscape(r'\begin{aligned}                   = ' + sigma_val + r' \end{aligned}'))

    return stress_along_web


def stiffener_stress_across_web(sigma, sigma_max, sigma_min, type='welded_hollow_bp', case='None'):
    """ """
    sigma = str(sigma)

    stress_across_web = Math(inline=True)

    if (type == 'welded_hollow_bp') and (case == 'None'):
        stress_across_web.append(NoEscape(r'\begin{aligned} {\sigma_{st}}_{aw} = {\sigma_{br}}_{actual} \\'))
    elif (type == 'moment_bp') and (case == 'Case2&3'):
        stress_across_web.append(NoEscape(r'\begin{aligned} {\sigma_{st}}_{aw} = {\sigma_{br}}_{actual} \\'))
    else:
        sigma_max = str(sigma_max)
        sigma_min = str(sigma_min)

        stress_across_web.append(NoEscape(r'\begin{aligned} {\sigma_{st}}_{aw} = \frac{{\sigma_{b}}_{max}~ - ~{\sigma_{b}}_{min}}{2} \\'))
        stress_across_web.append(NoEscape(r'\begin{aligned}                    = \frac{' + sigma_max + r'~ - ~' + sigma_min + r'}{2} \\'))

    stress_across_web.append(NoEscape(r'\begin{aligned}                    = ' + sigma + r' \end{aligned}'))

    return stress_across_web


def shear_demand_stiffener(sigma, stiff_length, stiff_height, shear, location='flange'):
    """ """
    sigma = str(sigma)
    stiff_length = str(stiff_length)
    stiff_height = str(stiff_height)
    shear = str(shear)

    shear_demand = Math(inline=True)

    if location == 'flange':
        shear_demand.append(NoEscape(r'\begin{aligned} {V_{st}}_{f} =  {\sigma_{st}}_{f} \times {L_{st}}_{f}~{H_{st}}_{f} \\'))
    elif location == 'web':
        shear_demand.append(NoEscape(r'\begin{aligned} {V_{st}}_{w} =  {\sigma_{st}}_{w} \times {L_{st}}_{w}~{H_{st}}_{w} \\'))
    else:
        shear_demand.append(NoEscape(r'\begin{aligned} {V_{st}}_{aw} =  {\sigma_{st}}_{aw} \times {L_{st}}_{aw}~{H_{st}}_{aw} \\'))

    shear_demand.append(NoEscape(r'\begin{aligned}              =  ' + sigma + r' \times ' + stiff_length + r'~' + stiff_height + r' \\'))
    shear_demand.append(NoEscape(r'\begin{aligned}              =  ' + shear + r' \end{aligned}'))

    return shear_demand


def shear_capacity_stiffener(stiff_thk, stiff_height, stiff_fy, shear_capa, gamma_m0, location='flange'):
    """ """
    stiff_thk = str(stiff_thk)
    stiff_height = str(stiff_height)
    stiff_fy = str(stiff_fy)
    shear_capa = str(shear_capa)
    gamma_m0 = str(gamma_m0)

    shear_capacity = Math(inline=True)

    if location == 'flange':
        shear_capacity.append(NoEscape(r'\begin{aligned} {V_{d}}_{f} =  \frac{A_{vg}~f_{y}}{\sqrt{3}~\gamma_{m0}} \\'))
        shear_capacity.append(NoEscape(r'\begin{aligned}             =  \frac{{(H_{st}}_{f}\times {t_{st}}_{f})f_{y}}{\sqrt{3}~\gamma_{m0}} \\'))
    elif location == 'web':
        shear_capacity.append(NoEscape(r'\begin{aligned} {V_{d}}_{w} =  \frac{A_{vg}~f_{y}}{\sqrt{3}~\gamma_{m0}} \\'))
        shear_capacity.append(NoEscape(r'\begin{aligned}             =  \frac{{(H_{st}}_{w}\times {t_{st}}_{w})f_{y}}{\sqrt{3}~\gamma_{m0}} \\'))
    else:
        shear_capacity.append(NoEscape(r'\begin{aligned} {V_{d}}_{aw} =  \frac{A_{vg}~f_{y}}{\sqrt{3}~\gamma_{m0}} \\'))
        shear_capacity.append(NoEscape(r'\begin{aligned}             =  \frac{{(H_{st}}_{aw}\times {t_{st}}_{aw})f_{y}}{\sqrt{3}~\gamma_{m0}} \\'))

    shear_capacity.append(NoEscape(r'\begin{aligned}             =  \frac{' + stiff_height + r' \times ' + stiff_thk + r')' + stiff_fy + r'}'
                                                                                                                                         r'{\sqrt{3}~' + gamma_m0 + r'} \\'))

    shear_capacity.append(NoEscape(r'\begin{aligned}              =  ' + shear_capa + r' \\'))
    shear_capacity.append(NoEscape(r'&[Ref.~IS~800:2007~(Cl.~8.4.1) \end{aligned}'))

    return shear_capacity


def moment_demand_stiffener(sigma, stiff_thk, stiff_length, moment, location='flange'):
    """ """
    sigma = str(sigma)
    stiff_length = str(stiff_length)
    stiff_thk = str(stiff_thk)
    moment = str(moment)

    moment_demand = Math(inline=True)

    if location == 'flange':
        moment_demand.append(NoEscape(r'\begin{aligned} {M_{st}}_{f} =  {\sigma_{st}}_{f} \times {t_{st}}_{f}~\frac{{{L_{st}}_{f}}^{2}}{2} \\'))
    elif location == 'web':
        moment_demand.append(NoEscape(r'\begin{aligned} {M_{st}}_{w} =  {\sigma_{st}}_{w} \times {t_{st}}_{f}~\frac{{{L_{st}}_{f}}^{2}}{2} \\'))
    else:
        moment_demand.append(NoEscape(r'\begin{aligned} {M_{st}}_{aw} =  {\sigma_{st}}_{aw} \times {t_{st}}_{f}~\frac{{{L_{st}}_{f}}^{2}}{2} \\'))

    moment_demand.append(NoEscape(r'\begin{aligned}              =  ' + sigma + r' \times ' + stiff_thk + r'~\frac{' + stiff_length + r'^{2}}{2} \\'))
    moment_demand.append(NoEscape(r'\begin{aligned}              =  ' + moment + r' \end{aligned}'))

    return moment_demand


def zp_stiffener(zp_val):
    """ """
    zp_val = str(zp_val)

    zp = Math(inline=True)
    zp.append(NoEscape(r'\begin{aligned} {z_{p}}_{st} = ' + zp_val + r' \end{aligned}'))

    return zp


def moment_capacity_stiffener(zp, stiff_fy, gamma_m0, moment_capa, location='flange'):
    """ """
    zp = str(zp)
    stiff_fy = str(stiff_fy)
    moment_capa = str(moment_capa)
    gamma_m0 = str(gamma_m0)

    moment_capacity = Math(inline=True)

    if location == 'flange':
        moment_capacity.append(NoEscape(r'\begin{aligned} {M_{d}}_{f} =  \frac{\beta_{b}~ {z_{p}}_{st}~f_{y}}{\gamma_{m0}} \\'))
    elif location == 'web':
        moment_capacity.append(NoEscape(r'\begin{aligned} {M_{d}}_{w} =  \frac{\beta_{b}~ {z_{p}}_{st}~f_{y}}{\gamma_{m0}} \\'))
    else:
        moment_capacity.append(NoEscape(r'\begin{aligned} {M_{d}}_{aw} =  \frac{\beta_{b}~ {z_{p}}_{st}~f_{y}}{\gamma_{m0}} \\'))

    moment_capacity.append(NoEscape(r'\begin{aligned}             =  \frac{1\times ~ {z_{p}}_{st}~f_{y}}{\gamma_{m0}}~~~~(\beta_{b} = 1) \\'))
    moment_capacity.append(NoEscape(r'\begin{aligned}             =  \frac{1\times ~' + zp + r'~' + stiff_fy + r'}{' + gamma_m0 + r'} \\'))
    moment_capacity.append(NoEscape(r'\begin{aligned}              =  ' + moment_capa + r' \\'))
    moment_capacity.append(NoEscape(r'&[Ref.~IS~800:2007~(Cl.~8.2.1.2) \end{aligned}'))

    return moment_capacity



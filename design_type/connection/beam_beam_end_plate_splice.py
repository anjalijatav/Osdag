"""
@Author:    Danish Ansari - Osdag Team, IIT Bombay [(P) danishdyp@gmail.com / danishansari@iitb.ac.in]

@Module - Beam-Beam End Plate Splice Connection
           - Flushed End Plate
           - Extended One Way End Plate
           - Extended Both Way End Plate


@Reference(s): 1) IS 800: 2007, General construction in steel - Code of practice (Third revision)
               2) IS 808: 1989, Dimensions for hot rolled steel beam, column, channel, and angle sections and
                                it's subsequent revision(s)
               3) IS 2062: 2011, Hot rolled medium and high tensile structural steel - specification
               4) Design of Steel Structures by N. Subramanian (Fifth impression, 2019, Chapter 15)
               5) Limit State Design of Steel Structures by S K Duggal (second edition, Chapter 11)

     other     6)
  references   7)

 Note: This file works with the helper file named 'end_plate_splice_helper.py' at ../Osdag/design_type/connection
"""

# Importing modules from the project directory

from design_type.connection.moment_connection import MomentConnection
from design_type.connection.end_plate_splice_helper import EndPlateSpliceHelper
from design_type.connection import end_plate_splice_helper
from design_type.connection.shear_connection import ShearConnection
from utils.common.is800_2007 import IS800_2007
from utils.common.other_standards import IS_5624_1993
from utils.common.component import *
from utils.common.material import *
from utils.common.common_calculation import *
from Common import *
from utils.common.load import Load
from utils.common.other_standards import *
from design_report.reportGenerator import save_html
from Report_functions import *
from design_report.reportGenerator_latex import CreateLatex

import logging
import math
import numpy as np


class BeamBeamEndPlateSplice(MomentConnection):

    def __init__(self):
        super(BeamBeamEndPlateSplice, self).__init__()

        self.load_moment = 0.0
        self.load_moment_effective = 0.0
        self.load_shear = 0.0
        self.load_axial = 0.0

        # self.supported_section = Beam
        self.bolt_diameter = []
        self.bolt_list = []
        self.bolt_diameter_provided = 0
        self.bolt_grade = []
        self.bolt_grade_provided = 0.0
        self.bolt_type = ""
        self.plate_thickness = []

        self.beam_plastic_mom_capa_zz = 0.0
        self.tension_due_to_moment = 0.0
        self.tension_due_to_axial_force = 0.0
        self.load_tension_flange = 0.0
        self.bolt_tension = 0.0
        self.bolt_fu = 0.0
        self.dp_bolt_fy = 0.0
        self.proof_load = 0.0

        self.pitch_distance_provided = 0.0
        self.gauge_distance_provided = self.pitch_distance_provided
        self.end_distance_provided = 0.0
        self.edge_distance_provided = self.end_distance_provided
        self.gauge_cs_distance_provided = 0.0
        self.space_available_inside_D = 0.0
        self.rows_inside_D_max = 0
        self.rows_outside_D_max = 0
        self.rows_total_max = 0
        self.rows_minimum_req = 0
        self.rows_outside_D_provided = 0
        self.rows_inside_D_provided = 0
        self.rows_near_tension_flange = (self.rows_outside_D_provided / 2) + (self.rows_inside_D_provided / 2)
        self.rows_near_web = 0
        self.rows_near_tension_flange_max = 0
        self.rows_near_web_max = 0
        self.bolt_numbers_tension_flange = 0
        self.bolt_numbers_web = 0

        self.bolt_column = 0
        self.bolt_row = 0
        self.bolt_numbers = self.bolt_column * self.bolt_row

        self.ep_width_provided = 0.0
        self.ep_height_max = 0.0

        self.minimum_load_status_moment = False
        self.plate_design_status = False
        self.bolt_design_status = False
        self.deep_beam_status = False

        self.beam_properties = {}
        self.safety_factors = {}

    # Set logger
    def set_osdaglogger(key):
        """ Function to set Logger for the module """
        global logger
        logger = logging.getLogger('osdag')

        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')

        handler.setFormatter(formatter)
        logger.addHandler(handler)
        handler = logging.FileHandler('logging_text.log')

        formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        if key is not None:
            handler = OurLog(key)
            formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')
            handler.setFormatter(formatter)
            logger.addHandler(handler)

    # set module name
    def module_name(self):
        """ display module name """
        return KEY_DISP_BB_EP_SPLICE

    # create UI for Input Dock
    def input_values(self):
        """ create a list of tuples to be displayed as the UI in Input Dock """
        self.module = KEY_DISP_BB_EP_SPLICE

        options_list = []

        t16 = (KEY_MODULE, KEY_DISP_BB_EP_SPLICE, TYPE_MODULE, None, True, 'No Validator')
        options_list.append(t16)

        t1 = (None, DISP_TITLE_CM, TYPE_TITLE, None, True, 'No Validator')
        options_list.append(t1)

        t2 = (KEY_CONN, KEY_DISP_CONN, TYPE_COMBOBOX, VALUES_CONN_SPLICE, True, 'No Validator', [1, 2])
        options_list.append(t2)

        t2 = (KEY_ENDPLATE_TYPE, KEY_DISP_ENDPLATE_TYPE, TYPE_COMBOBOX, VALUES_ENDPLATE_TYPE, True, 'No Validator')
        options_list.append(t2)

        t15 = (KEY_IMAGE, None, TYPE_IMAGE, "./ResourceFiles/images/extended.png", True, 'No Validator')
        options_list.append(t15)

        t4 = (KEY_SUPTDSEC, KEY_DISP_BEAMSEC, TYPE_COMBOBOX, connectdb("Beams"), True, 'No Validator')
        options_list.append(t4)

        t5 = (KEY_MATERIAL, KEY_DISP_MATERIAL, TYPE_COMBOBOX, VALUES_MATERIAL, True, 'No Validator')
        options_list.append(t5)

        t6 = (None, DISP_TITLE_FSL, TYPE_TITLE, None, True, 'No Validator')
        options_list.append(t6)

        t17 = (KEY_MOMENT, KEY_DISP_MOMENT, TYPE_TEXTBOX, None, True, 'Int Validator')
        options_list.append(t17)

        t7 = (KEY_SHEAR, KEY_DISP_SHEAR, TYPE_TEXTBOX, None, True, 'Int Validator')
        options_list.append(t7)

        t8 = (KEY_AXIAL, KEY_DISP_AXIAL, TYPE_TEXTBOX, None,True, 'Int Validator')
        options_list.append(t8)

        t9 = (None, DISP_TITLE_BOLT, TYPE_TITLE, None, True, 'No Validator')
        options_list.append(t9)

        t10 = (KEY_D, KEY_DISP_D, TYPE_COMBOBOX_CUSTOMIZED, VALUES_D, True, 'No Validator')
        options_list.append(t10)

        t11 = (KEY_TYP, KEY_DISP_TYP, TYPE_COMBOBOX, VALUES_TYP, True, 'No Validator')
        options_list.append(t11)

        t12 = (KEY_GRD, KEY_DISP_GRD, TYPE_COMBOBOX_CUSTOMIZED, VALUES_GRD, True, 'No Validator')
        options_list.append(t12)

        t21 = (None, DISP_TITLE_ENDPLATE, TYPE_TITLE, None, True, 'No Validator')
        options_list.append(t21)

        t22 = (KEY_PLATETHK, KEY_DISP_ENDPLATE_THICKNESS, TYPE_COMBOBOX_CUSTOMIZED, VALUES_ENDPLATE_THICKNESS, True, 'No Validator')
        options_list.append(t22)

        t23 = (None, DISP_TITLE_WELD, TYPE_TITLE, None, True, 'No Validator')
        options_list.append(t23)

        t24 = (KEY_WELD_TYPE, KEY_DISP_WELD_TYPE, TYPE_COMBOBOX, VALUES_WELD_TYPE_BB_FLUSH, True, 'No Validator')
        options_list.append(t24)

        return options_list

    # add representative images in UI
    def input_value_changed(self):
        """ """
        lst = []

        t1 = ([KEY_CONN, KEY_ENDPLATE_TYPE], KEY_IMAGE, TYPE_IMAGE, self.fn_conn_image)
        lst.append(t1)

        t2 = ([KEY_MATERIAL], KEY_MATERIAL, TYPE_CUSTOM_MATERIAL, self.new_material)
        lst.append(t2)

        return lst

    def fn_conn_image(self):
        """ display representative images of end plate type """
        conn = self[0]
        ep_type = self[1]
        if ep_type == 'Flushed - Reversible Moment':
            return './ResourceFiles/images/flush_ep.png'
        elif ep_type == 'Extended One Way - Irreversible Moment':
            return './ResourceFiles/images/owe_ep.png'
        elif ep_type == 'Extended Both Ways - Reversible Moment':
            return './ResourceFiles/images/extended.png'
        else:
            return ''

    # create customized input for UI
    def customized_input(self):
        """ list of values available with customize option"""

        list1 = []
        t1 = (KEY_GRD, self.grdval_customized)
        list1.append(t1)

        t3 = (KEY_D, self.diam_bolt_customized)
        list1.append(t3)

        t6 = (KEY_PLATETHK, self.endplate_thick_customized)
        list1.append(t6)
        return list1

    # create UI for Output Dock
    def output_values(self, flag):
        """ create a list of tuples to be displayed as the UI in the Output Dock """
        out_list = []
        return []

    # create UI for DP
    def tab_list(self):
        tabs = []

        t1 = (KEY_DISP_BEAMSEC, TYPE_TAB_1, self.tab_supported_section)
        tabs.append(t1)

        t6 = ("Connector", TYPE_TAB_2, self.plate_connector_values)
        tabs.append(t6)

        t2 = ("Bolt", TYPE_TAB_2, self.bolt_values)
        tabs.append(t2)

        t2 = ("Weld", TYPE_TAB_2, self.weld_values)
        tabs.append(t2)

        t4 = ("Detailing", TYPE_TAB_2, self.detailing_values)
        tabs.append(t4)

        t5 = ("Design", TYPE_TAB_2, self.design_values)
        tabs.append(t5)

        return tabs

    def edit_tabs(self):
        return []

    def tab_value_changed(self):

        change_tab = []

        # t1 = (KEY_DISP_COLSEC, [KEY_SUPTNGSEC_MATERIAL], [KEY_SUPTNGSEC_FU, KEY_SUPTNGSEC_FY], TYPE_TEXTBOX,
        # self.get_fu_fy_I_section_suptng)
        # change_tab.append(t1)

        t2 = (KEY_DISP_BEAMSEC, [KEY_SUPTDSEC_MATERIAL], [KEY_SUPTDSEC_FU, KEY_SUPTDSEC_FY], TYPE_TEXTBOX,
        self.get_fu_fy_I_section_suptd)
        change_tab.append(t2)

        t3 = ("Connector", [KEY_CONNECTOR_MATERIAL], [KEY_CONNECTOR_FU, KEY_CONNECTOR_FY_20, KEY_CONNECTOR_FY_20_40,
                                                      KEY_CONNECTOR_FY_40], TYPE_TEXTBOX, self.get_fu_fy)

        change_tab.append(t3)

        # t4 = (KEY_DISP_COLSEC, ['Label_1', 'Label_2', 'Label_3', 'Label_4', 'Label_5'],
        #       ['Label_11', 'Label_12', 'Label_13', 'Label_14', 'Label_15', 'Label_16', 'Label_17', 'Label_18',
        #        'Label_19', 'Label_20', 'Label_21', 'Label_22', KEY_IMAGE], TYPE_TEXTBOX, self.get_I_sec_properties)
        # change_tab.append(t4)

        t5 = (KEY_DISP_BEAMSEC, ['Label_1', 'Label_2', 'Label_3', 'Label_4', 'Label_5'],
              ['Label_11', 'Label_12', 'Label_13', 'Label_14', 'Label_15', 'Label_16', 'Label_17', 'Label_18',
               'Label_19', 'Label_20', 'Label_21', 'Label_22', KEY_IMAGE], TYPE_TEXTBOX, self.get_I_sec_properties)
        change_tab.append(t5)

        # t6 = (KEY_DISP_COLSEC, [KEY_SUPTNGSEC], [KEY_SOURCE], TYPE_TEXTBOX, self.change_source)
        # change_tab.append(t6)

        t7 = (KEY_DISP_BEAMSEC, [KEY_SUPTDSEC], [KEY_SOURCE], TYPE_TEXTBOX, self.change_source)
        change_tab.append(t7)

        return change_tab

    def refresh_input_dock(self):

        add_buttons = []

        # t1 = (KEY_DISP_COLSEC, KEY_SUPTNGSEC, TYPE_COMBOBOX, KEY_SUPTNGSEC, None, None, "Columns")
        # add_buttons.append(t1)

        t2 = (KEY_DISP_BEAMSEC, KEY_SUPTDSEC, TYPE_COMBOBOX, KEY_SUPTDSEC, None, None, "Beams")
        add_buttons.append(t2)

        return add_buttons

    def input_dictionary_design_pref(self):
        design_input = []

        t2 = (KEY_DISP_BEAMSEC, TYPE_COMBOBOX, [KEY_SUPTDSEC_MATERIAL])
        design_input.append(t2)

        t3 = ("Bolt", TYPE_COMBOBOX, [KEY_DP_BOLT_TYPE, KEY_DP_BOLT_HOLE_TYPE, KEY_DP_BOLT_SLIP_FACTOR])
        design_input.append(t3)

        t4 = ("Weld", TYPE_COMBOBOX, [KEY_DP_WELD_FAB])
        design_input.append(t4)

        t4 = ("Weld", TYPE_TEXTBOX, [KEY_DP_WELD_MATERIAL_G_O])
        design_input.append(t4)

        t5 = ("Detailing", TYPE_COMBOBOX, [KEY_DP_DETAILING_EDGE_TYPE, KEY_DP_DETAILING_CORROSIVE_INFLUENCES])
        design_input.append(t5)

        t5 = ("Detailing", TYPE_TEXTBOX, [KEY_DP_DETAILING_GAP])
        design_input.append(t5)

        t6 = ("Design", TYPE_COMBOBOX, [KEY_DP_DESIGN_METHOD])
        design_input.append(t6)

        t7 = ("Connector", TYPE_COMBOBOX, [KEY_CONNECTOR_MATERIAL])
        design_input.append(t7)

        return design_input

    def input_dictionary_without_design_pref(self):
        design_input = []

        t1 = (KEY_MATERIAL, [KEY_SUPTDSEC_MATERIAL], 'Input Dock')
        design_input.append(t1)

        t2 = (None, [KEY_DP_BOLT_TYPE, KEY_DP_BOLT_HOLE_TYPE, KEY_DP_BOLT_SLIP_FACTOR,
                     KEY_DP_WELD_FAB, KEY_DP_WELD_MATERIAL_G_O, KEY_DP_DETAILING_EDGE_TYPE, KEY_DP_DETAILING_GAP,
                     KEY_DP_DETAILING_CORROSIVE_INFLUENCES, KEY_DP_DESIGN_METHOD, KEY_CONNECTOR_MATERIAL], '')
        design_input.append(t2)

        return design_input

    def get_values_for_design_pref(self, key, design_dictionary):

        if design_dictionary[KEY_MATERIAL] != 'Select Material':
            fu = Material(design_dictionary[KEY_MATERIAL], 41).fu
        else:
            fu = ''

        val = {KEY_DP_BOLT_TYPE: "Pre-tensioned",
               KEY_DP_BOLT_HOLE_TYPE: "Standard",
               KEY_DP_BOLT_SLIP_FACTOR: str(0.3),
               KEY_DP_WELD_FAB: KEY_DP_FAB_SHOP,
               KEY_DP_WELD_MATERIAL_G_O: str(fu),
               KEY_DP_DETAILING_EDGE_TYPE: "Sheared or hand flame cut",
               KEY_DP_DETAILING_GAP: '0',
               KEY_DP_DETAILING_CORROSIVE_INFLUENCES: 'No',
               KEY_DP_DESIGN_METHOD: "Limit State Design",
               KEY_CONNECTOR_MATERIAL: str(design_dictionary[KEY_MATERIAL])
               }[key]

        return val

    # call individual 3D model in UI
    def get_3d_components(self):
        """ call individual 3D model in UI """
        components = []

        t1 = ('Model', self.call_3DModel)
        components.append(t1)

        t2 = ('Beam', self.call_3DBeam)
        components.append(t2)

        t3 = ('Column', self.call_3DColumn)
        components.append(t3)

        # t4 = ('End Plate', self.call_3DPlate)
        # components.append(t4)

        return components

    # get the input values from UI
    def set_input_values(self, design_dictionary):
        """ get the input values from UI (input dock and DP) for performing the design etc. """
        super(BeamBeamEndPlateSplice, self).set_input_values(self, design_dictionary)

        # section details
        self.mainmodule = "Moment Connection"
        self.connectivity = design_dictionary[KEY_CONN]
        self.endplate_type = design_dictionary[KEY_ENDPLATE_TYPE]
        self.material = Material(material_grade=design_dictionary[KEY_MATERIAL])

        # self.supporting_section = Column(designation=design_dictionary[KEY_SUPTNGSEC],
        #                                      material_grade=design_dictionary[KEY_SUPTNGSEC_MATERIAL])
        self.supported_section = Beam(designation=design_dictionary[KEY_SUPTDSEC],
                                      material_grade=design_dictionary[KEY_SUPTDSEC_MATERIAL])

        # bolt details
        self.bolt = Bolt(grade=design_dictionary[KEY_GRD], diameter=design_dictionary[KEY_D],
                         bolt_type=design_dictionary[KEY_TYP],
                         bolt_hole_type=design_dictionary[KEY_DP_BOLT_HOLE_TYPE],
                         edge_type=design_dictionary[KEY_DP_DETAILING_EDGE_TYPE],
                         mu_f=design_dictionary.get(KEY_DP_BOLT_SLIP_FACTOR, None),
                         corrosive_influences=design_dictionary[KEY_DP_DETAILING_CORROSIVE_INFLUENCES],
                         bolt_tensioning=design_dictionary[KEY_DP_BOLT_TYPE])

        # force details
        self.load = Load(shear_force=float(design_dictionary[KEY_SHEAR]),
                         axial_force=float(design_dictionary[KEY_AXIAL]),
                         moment=float(design_dictionary[KEY_MOMENT]), unit_kNm=True)

        # plate details
        self.plate = Plate(thickness=design_dictionary.get(KEY_PLATETHK, None),
                           material_grade=design_dictionary[KEY_CONNECTOR_MATERIAL],
                           gap=design_dictionary[KEY_DP_DETAILING_GAP])
        self.plate.design_status_capacity = False

        # weld details
        self.top_flange_weld = Weld(material_g_o=design_dictionary[KEY_DP_WELD_MATERIAL_G_O],
                                    type=design_dictionary[KEY_DP_WELD_TYPE],
                                    fabrication=design_dictionary[KEY_DP_WELD_FAB])
        self.bottom_flange_weld = Weld(material_g_o=design_dictionary[KEY_DP_WELD_MATERIAL_G_O],
                                       type=design_dictionary[KEY_DP_WELD_TYPE],
                                       fabrication=design_dictionary[KEY_DP_WELD_FAB])
        self.web_weld = Weld(material_g_o=design_dictionary[KEY_DP_WELD_MATERIAL_G_O],
                             type=design_dictionary[KEY_DP_WELD_TYPE], fabrication=design_dictionary[KEY_DP_WELD_FAB])

        # properties fro design preferences

        # beam properties
        self.beam_properties = {
            "beam_D": self.supported_section.depth,
            "beam_B": self.supported_section.flange_width,
            "beam_T": self.supported_section.flange_thickness,
            "beam_t": self.supported_section.web_thickness,
            "beam_r1": self.supported_section.root_radius,
            "beam_r2": self.supported_section.toe_radius,
            "beam_zp_zz": self.supported_section.plast_sec_mod_z,
            "beam_fu": self.supported_section.fu,
            "beam_fy": self.supported_section.fy
        }

        self.beam_D = self.supported_section.depth
        self.beam_bf = self.supported_section.flange_width
        self.beam_tf = self.supported_section.flange_thickness
        self.beam_tw = self.supported_section.web_thickness
        self.beam_r1 = self.supported_section.root_radius
        self.beam_r2 = self.supported_section.toe_radius
        self.beam_zp_zz = self.supported_section.plast_sec_mod_z

        self.dp_beam_fu = float(self.supported_section.fu)
        self.dp_beam_fy = float(self.supported_section.fy)

        # bolt
        # TODO: check if required
        # if self.bolt.bolt_tensioning == 'Pretensioned':
        #     self.beta = 1
        # else:
        #     self.beta = 2

        # end plate

        # weld
        self.dp_weld_fab = str(design_dictionary[KEY_DP_WELD_FAB])
        self.dp_weld_fu_overwrite = float(design_dictionary[KEY_DP_WELD_MATERIAL_G_O])

        # safety factors (Table 5, IS 800:2007)
        self.safety_factors = {
            "gamma_m0": self.cl_5_4_1_Table_5["gamma_m0"]["yielding"],
            "gamma_m1": self.cl_5_4_1_Table_5["gamma_m1"]["ultimate_stress"],
            "gamma_mb": self.cl_5_4_1_Table_5["gamma_mb"][self.dp_weld_fab],
            "gamma_mw": self.cl_5_4_1_Table_5["gamma_mw"]["Field weld"]
        }
        self.gamma_m0 = self.cl_5_4_1_Table_5["gamma_m0"]["yielding"]  # gamma_mo = 1.10
        self.gamma_m1 = self.cl_5_4_1_Table_5["gamma_m1"]["ultimate_stress"]  # gamma_m1 = 1.25
        self.gamma_mb = self.cl_5_4_1_Table_5["gamma_mb"][self.dp_weld_fab]  # gamma_mb = 1.25
        self.gamma_mw = self.cl_5_4_1_Table_5["gamma_mw"]["Field weld"]  # gamma_mw = 1.25 for 'Shop Weld' and 1.50 for 'Field Weld'

        # warn if a beam of older version of IS 808 is selected
        # self.warn_text(self)

    # def warn_text(self):
    #     """ give logger warning when a beam from the older version of IS 808 is selected """
    #     global logger
    #     red_list = red_list_function()
    #     if self.supported_section.designation in red_list:
    #         logger.warning(
    #             " : You are using a section (in red color) that is not available in latest version of IS 808")
    #         logger.info(
    #             " : You are using a section (in red color) that is not available in latest version of IS 808")

        # helper function
        self.call_helper = EndPlateSpliceHelper(self.load, self.bolt, ep_type=self.endplate_type, bolt_design_status=self.bolt_design_status)

    # start of design simulation

    def set_parameters(self):
        """ set/initialize parameters for performing the analyses and design """

        # set minimum load (Annex F, F-4.3.1)

        # moment capacity of beam (cl 8.2.1.2, IS 800:2007)
        self.beam_plastic_mom_capa_zz = (1 * self.supported_section.plast_sec_mod_z * self.supported_section.fy) / self.gamma_m0

        if self.load.moment < (0.5 * self.beam_plastic_mom_capa_zz):
            self.minimum_load_status_moment = True
            # update moment value
            self.load_moment = round(0.5 * self.beam_plastic_mom_capa_zz, 2)  # kN

            logger.warning("[Minimum Factored Load] The external factored bending moment ({} kN-m) is less than 0.5 times the plastic moment "
                           "capacity of the beam ({} kN-m)".format(self.load.moment, self.load_moment))
            logger.info("The minimum factored bending moment should be at least 0.5 times the plastic moment capacity of the beam to qualify the "
                        "connection as rigid and transfer full moment from the spliced beam (Cl. 10.7, IS 800:2007)")
            logger.info("Designing the connection for a load of {} kN-m".format(self.load_moment))
        else:
            self.minimum_load_status_moment = False
            self.load_moment = self.load.moment  # kN

        # TODO: check min loads for shear and axial
        self.load_shear = self.load.shear_force  # kN
        self.load_axial = self.load.axial_force  # kN

        # effective moment is the moment due to external factored moment plus moment due to axial force
        self.load_moment_effective = self.load_moment + (self.load_axial * ((self.beam_D / 2) - (self.beam_tf / 2)))  # kN-m

        # setting bolt ist
        self.bolt_diameter = self.bolt.bolt_diameter
        self.bolt_grade = self.bolt.bolt_grade
        self.bolt_type = self.bolt.bolt_type

        # set plate thickness list [minimum to maximum]
        # Note: minimum plate thk is at-least equal to the thk of thicker connecting element (flange thk or web thk)
        self.plate_thickness = []
        for i in self.plate.thickness:
            if i > max(self.beam_tf, self.beam_tw):
                self.plate_thickness.append(i)

        self.plate_thickness = self.plate_thickness  # final list of plate thicknesses considered for simulation

        # set bolt diameter, grade combination
        self.bolt_list = []  # this list will be used to run the iteration

        # combine each diameter with each grade
        for i in self.bolt.bolt_diameter:
            for j in self.bolt.bolt_grade:
                self.bolt_list.append(i)
                self.bolt_list.append(j)

        self.bolt_list = self.bolt_list

        # create a list of tuple with a combination of each bolt diameter with each grade for iteration
        # list is created using the approach --- minimum diameter, small grade to maximum diameter, high grade
        self.bolt_list = [i for i in zip(*[iter(self.bolt_list)]*2)]
        logger.info("Checking the design with the following bolt diameter-grade combination {}".format(self.bolt_list))

    def design_connection(self):
        """ perform analysis and design of bolt and end plate """

        # Check 1: calculate tension due to external factored moment and axial force in the tension flange
        # Assumption: the NA is assumed at the centre of the bottom flange

        self.tension_due_to_moment = round((self.load_moment / (self.beam_D - self.beam_tf)), 2)  # kN
        self.tension_due_to_axial_force = round((self.load_axial / ((self.beam_D / 2) - (self.beam_tf / 2))), 2)  # kN
        self.load_tension_flange = self.tension_due_to_moment + self.tension_due_to_axial_force  # kN

        # performing the check with minimum plate thickness and a suitable bolt dia-grade combination (thin plate - large dia approach)
        logger.info("[Optimisation] Performing the design by optimising the plate thickness, using the thin plate and large (suitable) bolt diameter "
                    "approach")
        logger.info("If you wish to optimise the bolt diameter-grade combination, pass a higher value of plate thickness using the Input Dock")

        # loop starts
        self.plate_design_status = False  # initialise plate status to False to activate the loop for first (and subsequent, if required) iteration(s)

        for i in self.plate_thickness:
            self.plate_thickness = i  # assigns plate thickness from the list

            if not self.plate_design_status:

                self.bolt_design_status = False  # initialize bolt status as False to activate the bolt design loop

                # selecting a single dia-grade combination (from the list of a tuple) each time for performing all the checks
                for j in self.bolt_list:

                    if not self.bolt_design_status:

                        test_list = j  # choose a tuple from the list of bolt dia and grade - (dia, grade)
                        self.bolt_diameter_provided = test_list[0]  # select trial diameter
                        self.bolt_grade_provided = test_list[1]  # select trial grade

                        # assign bolt mechanical properties
                        self.bolt_fu = self.bolt.bolt_fu
                        self.dp_bolt_fy = self.bolt.bolt_fy
                        self.proof_load = self.bolt.proof_load

                        # Check 2: detailing checks

                        # pitch/gauge
                        self.pitch_distance_provided = self.cl_10_2_2_min_spacing(self.bolt_diameter_provided)  # mm
                        # add nut size (half on each side)
                        self.pitch_distance_provided = self.pitch_distance_provided + ((1 / 2) * IS1364Part3.nut_size(self.bolt_diameter_provided))
                        self.gauge_distance_provided = self.pitch_distance_provided

                        # end/edge
                        end_distance = self.cl_10_2_4_2_min_edge_end_dist(self.bolt_diameter_provided, self.bolt.bolt_hole_type, self.bolt.edge_type)
                        end_distance = end_distance + ((1 / 2) * IS1364Part3.nut_size(self.bolt_diameter_provided))  # add nut size (half on each side)

                        self.end_distance_provided = round_up(end_distance, 2)  # mm
                        self.edge_distance_provided = self.end_distance_provided

                        # cross-centre gauge
                        self.gauge_cs_distance_provided = self.beam_tw + (2 * self.beam_r1) + (2 * self.end_distance_provided)
                        self.gauge_cs_distance_provided = round_up(self.gauge_cs_distance_provided, 2)  # mm

                        # Check 3: end plate dimensions (designed for groove weld at flange only)

                        # plate width (provided and maximum are same)
                        self.ep_width_provided = self.beam_bf + 25  # mm, 12.5 mm on each side

                        # plate height (maximum) - fixing maximum two rows above and below flange for ep extending beyond the flange
                        if self.endplate_type == 'Flushed - Reversible Moment':
                            self.ep_height_max = self.beam_D + 25  # mm, 12.5 mm beyond either flanges
                        else:  # assuming two rows
                            space_available_above_flange = (2 * self.end_distance_provided) + self.pitch_distance_provided  # mm, extension on each side

                            if self.endplate_type == 'Extended One Way - Irreversible Moment':
                                self.ep_height_max = self.beam_D + space_available_above_flange  # mm
                            else:
                                self.ep_height_max = self.beam_D + (2 * space_available_above_flange)  # mm

                        # Check 4: number of rows of bolt - above and below beam depth
                        # Note: space_available_inside_D is calculated assuming minimum space available after providing minimum rows inside (i.e. 2)
                        self.space_available_inside_D = self.beam_D - (2 * self.beam_tf) - (2 * self.beam_r1) - (2 * self.end_distance_provided)
                        self.rows_inside_D_max = 2 + round_down(self.space_available_inside_D, self.pitch_distance_provided, 1)

                        if self.endplate_type == 'Extended One Way - Irreversible Moment':
                            self.rows_outside_D_max = 2
                            self.rows_total_max = self.rows_outside_D_max + self.rows_inside_D_max

                            self.rows_minimum_req = 3  # 2 near tension flange and 1 near the bottom flange
                        else:
                            if self.endplate_type == 'Flushed - Reversible Moment':
                                self.rows_outside_D_max = 0
                                self.rows_minimum_req = 2  # 2 at each flanges (inside flanges)

                            else:  # extended both way
                                self.rows_outside_D_max = 2 * 2  # 2 on outside of both the flanges
                                self.rows_minimum_req = 2 * 2  # 2 at each flanges (above and below)

                            self.rows_total_max = self.rows_outside_D_max + self.rows_inside_D_max

                        if self.rows_inside_D_max <= 0:
                            logger.error("[Detailing] The selected beam cannot accommodate at-least a single row of bolt inside it's depth")
                            logger.info("Select/Provide a beam of suitable depth")

                        # # checking if the beam is deep enough (based on detailing thumb rule)
                        # # Allowing max of 3 rows (each inside top and bottom flange)
                        # # If the space available after providing a total of 6 rows inside flange is greater than or equal to max pitch, then the beam
                        # # is considered as deep enough from detailing perspective ONLY.
                        # # This check will help in assessing how many rows of bolts can be provided near the web to carry shear and axial force
                        #
                        # if (self.space_available_inside_flange - (4 * self.pitch_distance_provided)) >= min(32 * self.plate_thickness, 300):
                        #     self.deep_beam_status = True
                        # else:
                        #     self.deep_beam_status = False
                        #
                        # # initialising with minimum number of rows to start the iteration
                        # if self.connectivity == 'Flushed - Reversible Moment':
                        #     self.rows_outside_D_max = 0
                        #     self.rows_outside_D_provided = 0
                        #
                        #     self.rows_inside_D_provided = 2  # initialize with minimum 2 rows (1 at top and bottom flange each)
                        # else:
                        #     self.rows_outside_D_max = 4  # 2 beyond each flange
                        #     self.rows_outside_D_provided = 2  # initialize with minimum 2 rows (1 row beyond each top and bottom flange)
                        #
                        #     self.rows_inside_D_provided = 2  # initialize with minimum 2 rows (1 at top and bottom flange each)
                        #
                        # # Minimum values: at each flange (out + in)
                        # self.rows_near_tension_flange = (self.rows_outside_D_provided / 2) + (self.rows_inside_D_provided / 2)
                        # # at web
                        # self.rows_near_web = 1  # initialize with 1 row

                        # # check for max rows inside
                        # if (self.rows_inside_D_provided + self.rows_near_web) > self.rows_inside_D_max:
                        #     logger.error("[Detailing] The minimum required number of rows inside beam depth ({}) exceeds the maximum allowed rows "
                        #                  "({}) [as per detailing requirement]".format(self.rows_near_tension_flange + self.rows_near_web,
                        #                                                               self.rows_inside_D_max))
                        #     logger.info("Select/Provide a beam of suitable depth")
                        #
                        # # Maximum values: at each flange (out + in)
                        # self.rows_near_tension_flange_max = min(5, 2 + (self.rows_inside_D_max / 2))  # on each side, total
                        #
                        # # checking for space availability to add bolts for shear design
                        # space_available_shear_bolts = self.space_available_inside_flange - (((self.rows_inside_D_provided - 2) / 2) *
                        #                                                                     self.pitch_distance_provided)
                        #
                        # # space available (s), rows (r) and pitch (p) relation is given as; [s = (r + 1) * p]
                        # # max rows of bolt near web
                        # self.rows_near_web_max = round_down(((space_available_shear_bolts / self.pitch_distance_provided) - 1), 1)
                        # if self.rows_near_web_max <= 0:
                        #     self.rows_near_web = 0
                        #     self.bolt_design_status = False

                        # Check 5: number of columns of bolt on each side (minimum is 1, maximum is 2)

                        # checking space available to accommodate two column of bolts on each side
                        space_available_2col = self.gauge_cs_distance_provided + (2 * self.gauge_distance_provided) + (2 * self.edge_distance_provided)

                        if space_available_2col >= self.ep_width_provided:
                            self.bolt_column = 4  # two columns on each side
                            logger.info("The provided beam can accommodate two column of bolts on either side of the web [Ref. based on detailing "
                                        "requirement]")
                            logger.info("Performing the design with two column of bolts on each side")
                        else:
                            self.bolt_column = 2  # one column on each side
                            logger.info("The provided beam can accommodate only a single column of bolt on either side of the web [Ref. based on "
                                        "detailing requirement]")
                            logger.info("Performing the design with a single column of bolt on each side")

                        if (self.gauge_cs_distance_provided + (2 * self.edge_distance_provided)) < self.ep_width_provided:
                            logger.error("[Detailing] The beam is not wide enough to accommodate a single column of bolt on either side")
                            logger.error("The defined beam is not suitable for this connection design")
                            logger.info("Please provide another beam which has sufficient width (minimum, {} mm)"
                                        .format(self.gauge_cs_distance_provided + (2 * self.edge_distance_provided)))

                        # Check 6: bolt design

                        # column and row combination for running iterations
                        if self.endplate_type == 'Extended One Way - Irreversible Moment':
                            row_list = np.arange(self.rows_minimum_req, self.rows_total_max + 1, 1).tolist()
                        else:
                            row_list = np.arange(self.rows_minimum_req, self.rows_total_max + 1, 2).tolist()
                        column_list = np.arange(2, self.bolt_column + 1, 2).tolist()

                        if self.bolt_column == 4:
                            column_list = column_list[::-1]

                        combined_list = []

                        # combine each possible row and column combination starting from minimum to maximum
                        for q in column_list:
                            for r in row_list:

                                combined_list.append(q)
                                combined_list.append(r)

                        combined_list = combined_list

                        # create a list of tuple with a combination of number of columns and rows for running the iteration
                        combined_list = [i for i in zip(*[iter(combined_list)] * 2)]
                        logger.info("Checking the design with the following number of column and rows combination {}".format(combined_list))

                        # set bolt design status to False to activate the bolt design loop
                        self.bolt_design_status = False

                        # selecting each possible combination of column and row iteratively to perform design checks
                        # starting from minimum column and row to maximum until overall bolt design status is True
                        for x in combined_list:
                            if not self.bolt_design_status:
                                select_list = x  # selected tuple from the list

                                self.bolt_column = select_list[0]
                                self.bolt_row = select_list[1]

                                # run the bolt check function from the helper class
                                self.design_bolt = self.call_helper.perform_bolt_design(self.endplate_type, self.beam_properties, self.safety_factors,
                                                                                        self.bolt_column, self.bolt_row, self.bolt_diameter_provided,
                                                                                        self.bolt_grade_provided, self.load_moment_effective,
                                                                                        self.end_distance_provided, self.pitch_distance_provided)
                                z = self.call_helper.bolt_shear_check_UR

                                self.bolt_design_results = end_plate_splice_helper.EndPlateSpliceHelper.perform_bolt_design\
                                    (self.bolt_numbers_tension_flange, self.bolt_numbers_web, self.bolt_diameter_provided, self.bolt_grade_provided)

                        # fixing bolt configuration
                        if self.bolt_design_status == True:
                            logger.info("[Bolt Design] All the checks pertaining to bolt design have successfully passed with an optimised "
                                        "combination of bolt diameter = {} mm, bolt grade = {} and, {} total number of bolts".
                                        format(self.bolt_diameter_provided, self.bolt_grade_provided, 1))
                            logger.info("[Detailing] Fixing bolt configuration as per detailing requirements")
                        else:
                            logger.error("[Bolt Design] The bolt design checks fail with a trial diameter of {} mm and {} grade".
                                         format(self.bolt_diameter_provided, self.bolt_grade_provided))
                            logger.info("Trying to re-design with a higher bolt diameter-grade combination")

    def save_design(self, popup_summary):
        # bolt_list = str(*self.bolt.bolt_diameter, sep=", ")

        if self.supported_section.flange_slope == 90:
            image = "Parallel_Beam"
        else:
            image = "Slope_Beam"
        self.report_supporting = {KEY_DISP_SEC_PROFILE: "ISection",
                                  KEY_DISP_BEAMSEC: self.supported_section.designation,
                                  KEY_DISP_MATERIAL: self.supported_section.material,
                                  KEY_DISP_FU: self.supported_section.fu,
                                  KEY_DISP_FY: self.supported_section.fy,
                                  'Mass': self.supported_section.mass,
                                  'Area(mm2) - A': round(self.supported_section.area, 2),
                                  'D(mm)': self.supported_section.depth,
                                  'B(mm)': self.supported_section.flange_width,
                                  't(mm)': self.supported_section.web_thickness,
                                  'T(mm)': self.supported_section.flange_thickness,
                                  'FlangeSlope': self.supported_section.flange_slope,
                                  'R1(mm)': self.supported_section.root_radius,
                                  'R2(mm)': self.supported_section.toe_radius,
                                  'Iz(mm4)': self.supported_section.mom_inertia_z,
                                  'Iy(mm4)': self.supported_section.mom_inertia_y,
                                  'rz(mm)': self.supported_section.rad_of_gy_z,
                                  'ry(mm)': self.supported_section.rad_of_gy_y,
                                  'Zz(mm3)': self.supported_section.elast_sec_mod_z,
                                  'Zy(mm3)': self.supported_section.elast_sec_mod_y,
                                  'Zpz(mm3)': self.supported_section.plast_sec_mod_z,
                                  'Zpy(mm3)': self.supported_section.elast_sec_mod_y}

        self.report_input = \
            {KEY_MODULE: self.module,
             KEY_MAIN_MODULE: self.mainmodule,
             # KEY_CONN: self.connectivity,
             KEY_DISP_MOMENT: self.load.moment,
             KEY_DISP_SHEAR: self.load.shear_force,
             KEY_DISP_AXIAL: self.load.axial_force,

             "Section": "TITLE",
             "Section Details": self.report_supporting,

             "Bolt Details": "TITLE",
             KEY_DISP_D: str(self.bolt.bolt_diameter),
             KEY_DISP_GRD: str(self.bolt.bolt_grade),
             KEY_DISP_TYP: self.bolt.bolt_type,

             KEY_DISP_DP_BOLT_HOLE_TYPE: self.bolt.bolt_hole_type,
             KEY_DISP_DP_BOLT_SLIP_FACTOR: self.bolt.mu_f,
             KEY_DISP_DP_DETAILING_EDGE_TYPE: self.bolt.edge_type,
             KEY_DISP_GAP: self.plate.gap,
             KEY_DISP_CORR_INFLUENCES: self.bolt.corrosive_influences,
             "Plate Details": "TITLE",
             KEY_DISP_PLATETHK: str(self.plate.thickness),
             KEY_DISP_MATERIAL: self.plate.material,
             KEY_DISP_FU: self.plate.fu,
             KEY_DISP_FY: self.plate.fy,
             "Weld Details": "TITLE",
             # KEY_DISP_DP_WELD_TYPE: "Fillet",
             # KEY_DISP_DP_WELD_FAB: self.weld.fabrication,
             # KEY_DISP_DP_WELD_MATERIAL_G_O: self.weld.fu
             }

        self.report_check = []












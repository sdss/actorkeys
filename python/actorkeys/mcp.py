# -*- python -*-
KeysDictionary("mcp", (2,4),
    # Command-related keywords
    Key("badAxis", String(), doCache=False, help="Unknown telescope axis"),
    Key("badCharacter", Int(), doCache=False, help="ASCII code of invalid character"),
    Key("badCommand", String(), doCache=False, help="Invalid command string"),
    Key("badSpectrograph", Int(), doCache=False, help="Invalid spectrograph ID"),
    Key("badUserId", help="Your suggested userID was invalid"),
    Key("command", String(), doCache=False, help="Command string"),
    Key("commandIn", String(), doCache=False, help="Debugging information; will go away"),
    Key("commandTooLong", Int(help="length of command"), doCache=False, help="Command was too long to parse"),
    Key("controlLamps", help="Indicates that a lamps control command finished"),
    Key("lampsCommanded", Bool("false", "true"), doCache=False, help=""),
    Key("text", String(), doCache=False),
    Key("userId", String(), help="Name reported by user"),
    Key("yourUserNum", Int(), help="Your user ID number"),

    # Iack and semaphore
    Key("haveSemaphore", Bool("false", "true"), help="Do you have the semaphore?"),
    Key("needIack", Bool("false", "true"), help="If true, you must send an iack before commanding the mcp"),
    Key("needSemaphore", help="Command rejected because you don't have the semaphore"),
    Key("semaphoreOwner", String()*(0,), help="Name of user (self-reported) who owns the semaphore"),
    
    # Flat field screens
    Key("ffsCloseFailed", Bool("false", "true"), doCache=False),
    Key("ffsCommanded", Bool("false", "true"), doCache=False),
    Key("ffsCommandedOpen", Bool("false", "true"), help="Flat field petals commanded close/open"),
    Key("ffsMoved", Bool("false", "true"), doCache=False),
    Key("ffsOpenFailed", Bool("false", "true"), doCache=False),
    Key("ffsSelected", Enum("00", "01", "10", "11", descr=("None", "Half1", "Half2", "All")),
        help="Flat field petals enabled"),
    Key("ffsStatus", Enum("00", "01", "10", "11", descr=("?", "Closed", "Open", "Invalid"))*8,
        help="State of flat field petals 1-8"),

    # Lamps
    Key("ffLamp", Bool("0", "1")*4, help="Detected state of flat field lamps"),
    Key("ffLampCommandedOn", Bool("false", "true"), help="Commanded state of flat-field lamps"),
    Key("hgCdLamp", Bool("0", "1")*4, help="Detected state of mercury/cadmium lamps"),
    Key("hgCdLampCommandedOn", Bool("false", "true"), help="Commanded state of mercury/cadmium lamps"),
    Key("neLamp", Bool("0", "1")*4, help="Detected state of neon lamps"),
    Key("neLampCommandedOn", Bool("false", "true"), help="Commanded state of neon lamps"),
    Key("uvLampCommandedOn", Bool("false", "true"), help="Commanded state of UV lamps"),
    Key("whtLampCommandedOn", Bool("false", "true"), help="Commanded state of white lamps"),

    # Counterweights
    Key("cwAbort", Int(), doCache=False, help="Abort on counterweight 1,2,3 or 4 (only one abort is reported at a time)"),
    Key("cwPositions", Int()*4, help="Counterweight positions"),
    Key("cwStatus", Enum("..", "L.", ".U", "LU", descr=("InRange", "AtLowerLimit", "AtUpperLimit", "Invalid"))*4,
        help="Counterweight status"),

    # Other PLC signals
    Key("altWindscreenTouched", Enum("00", "01", "10", "11", descr=("None", "Down", "Up", "Both"))),
    Key("azWindscreenTouched", Enum("00", "01", "10", "11", descr=("None", "CW", "CCW", "Both"))),
    Key("instrumentNum", Int(invalid="-1"),
        help="Instrument ID; 0=no instrument; 18=engineering camera; 19=imager; -1=switches inconsistent or could not get semaphore"),
    Key("instrumentNumConsistent", Bool("false", "true"),
        help="Do the three instrument ID switches agree? If not, instrumentNumValues is also output."),
    Key("instrumentNumValues", Int()*3, help="Reading from each instrument ID switch"),
    Key("saddleIsMounted", Bool("false", "true"), help="Imager saddle is mounted"),
    Key("sp1Slithead", 
        Enum("00", "01", "10", "11", descr=("?", "Open", "Closed", "Invalid")),
        Bool("0", "1", help="Latch extended"),
        Bool("0", "1", help="Slithead in place")),
    Key("sp2Slithead", 
        Enum("00", "01", "10", "11", descr=("?", "Open", "Closed", "Invalid")),
        Bool("0", "1", help="Latch extended"),
        Bool("0", "1", help="Slithead in place")),
    Key("tbarCommanded", Bool("false", "true"), doCache=False, help="Imager TBar move requested"),

    # Axis controller, in order Az, Alt, Rot
    Key("azMaxAccLimit", Float(units="deg/s^2"), help="Maximum acceleration allowed"),
    Key("azMaxAccRequested", Float(units="deg/s^2"), doCache=False, help="Maximum acceleration requested"),
    Key("azMaxVelLimit", Float(units="deg/s"), help="Maximum velocity allowed"),
    Key("azMaxVelRequested", Float(units="deg/s"), help="Maximum velocity"),
    Key("azMsOn", Bool("false", "true"), help="Fiducial corrections enabled requested"),
    Key("azPidCoeffs", Int(help="Proportional term"), Int(help="Integral term"), Int(help="Derivitive term"),
        Int(help="Accel_FF"), Int(help="Vel_FF"), Int(help="I_limit"), Int(help="Offset"),
        Int(help="DAC_limit"), Int(help="Shift"), Int(help="Friction_FF"),
        help="Servo loop tuning parameters; for details see the MEI manual"),

    Key("altMaxAccLimit", Float(units="deg/s^2"), help="Maximum acceleration allowed"),
    Key("altMaxAccRequested", Float(units="deg/s^2"), doCache=False, help="Maximum acceleration requested"),
    Key("altMaxVelLimit", Float(units="deg/s"), help="Maximum velocity allowed"),
    Key("altMaxVelRequested", Float(units="deg/s"), help="Maximum velocity requested"),
    Key("altMsOn", Bool("false", "true"), help="Fiducial corrections enabled"),
    Key("altPidCoeffs", Int(help="P: proportional term"), Int(help="I: integral term"), Int(help="D: derivitive term"),
        Int(help="Accel_FF"), Int(help="Vel_FF"), Int(help="I_limit"), Int(help="Offset"),
        Int(help="DAC_limit"), Int(help="Shift"), Int(help="Friction_FF"),
        help="Servo loop tuning parameters; for details see the MEI manual"),

    Key("rotBadFiducialDelta", Int(), help="Unknown fiducial: invalid delta between tape marks"),
    Key("rotMaxAccLimit", Float(units="deg/s^2"), help="Maximum acceleration allowed"),
    Key("rotMaxAccRequested", Float(units="deg/s^2"), doCache=False, help="Maximum acceleration requested"),
    Key("rotMaxVelLimit", Float(units="deg/s"), help="Maximum velocity allowed"),
    Key("rotMaxVelRequested", Float(units="deg/s"), help="Maximum velocity requested"),
    Key("rotMsOn", Bool("false", "true"), help="Fiducial corrections enabled"),
    Key("rotPidCoeffs", Int(help="Proportional term"), Int(help="Integral term"), Int(help="Derivitive term"),
        Int(help="Accel FF"), Int(help="Vel FF"), Int(help="Current limit"), Int(help="Offset"),
        Int(help="DAC limit"), Int(help="Shift"), Int(help="Friction FF"),
        help="Servo loop tuning parameters; for details see the MEI manual"),

    # Axis encoders and fiducials
    Key("minEncoderMismatch", Int()*3, help="Limit below which readings from paired encoders are considered equal (az, alt, rot)"),
    Key("msOnMaxCorrection", Int()*3, help="Maximum fiducial error which will be corrected (az, alt, rot)"),

    Key("azFiducialCrossing", Int(help="fiducial index"),
        Float(units="deg", help="fiducial position"),
        Int(units="ticks", help="error in expected position", invalid=99999),
        Int(units="ticks", help="error in reported position")),
    Key("altFiducialCrossing", Int(help="fiducial index"),
        Float(units="deg", help="fiducial position"),
        Int(units="ticks", help="error since last crossing", invalid=99999),
        Int(units="ticks", help="error in reported position")),
    Key("rotFiducialCrossing", Int(help="fiducial index"),
        Float(units="deg", help="fiducial position"),
        Int(units="ticks", help="error since last crossing", invalid=99999),
        Int(units="ticks", help="error in reported position")), 
    Key("azBadFiducial", Int(help="fiducial index"),
        Float(units="deg", help="fiducial position")),
    Key("altBadFiducial", Int(help="fiducial index"),
        Float(units="deg", help="fiducial position")),
    Key("rotBadFiducial", Int(help="fiducial index"),
        Float(units="deg", help="fiducial position")),
       
    # Versions
    Key("goodFiducialVersions", Bool("false", "true"), help="The fiducial table version numbers are consistent"),
    Key("azFiducialVersion", String(), help="Version of fiducial table"),
    Key("altFiducialVersion", String(), help="Version of fiducial table"),
    Key("rotFiducialVersion", String(), help="Version of fiducial table"),
    Key("mcpVersion", String(), help="Version of MCP code"),
    Key("plcVersion", Int(), help="PLC version, if consistent (see also pclVersions)"),
    Key("plcVersions", Int()*2, help="PLC versions from the Allen-Bradley and data_collection.h"),

    # Actor housekeeping
    Key("aliveAt", UInt(units="s",help="Elapsed TAI(?) since unix epoch"), help="MCP 1/60 Hz keep-alive message"),

    # Allen-Bradley words
    Key('ab_status', Int()*4, help='Allen Bradley status, azstate, altstate, rotstate'),
    Key('lavaLamp', Int(), help='Is the Lava Lamp on?'),
    Key('imCamCheck', String()*(0,), help="Imager errors reported by iop"),
    #
    # The machine-generated bitfield definitions are inserted here:
    #
    Key('ab_B3_L0', Bits('rot_mtr_iv_good', 'alt_mtr_iv_good', 'az_mtr_iv_good', 'hgcd_lamp_on_request', 'ne_lamp_on_request', 'lift_speed_man_ovrid', 'ilcb_led_on', 'ff_screens_closed', 'e_stop_flash_reset', 'led_flash', 'flip_flop_5', 'flip_flop_4', 'flip_flop_3', 'flip_flop_2', 'flip_flop_1', 'flip_flop_0', 'plc_cont_t_bar_latch', 'mcp_cont_t_bar_latch', 'plc_cont_slit_hd', 'mcp_cont_slit_hd', 'plc_cont_slit_dr', 'mcp_cont_slit_dr', 'e_stop_permit', 'dn_inhibit_latch_4', 'dn_inhibit_latch_3', 'dn_inhibit_latch_2', 'dn_inhibit_latch_1', 'up_inhibit_latch', ), help=''),
    Key('ab_B3_L1', Bits('img_cam_in_place', 'undefined_2', 'undefined_1', 'undefined_3', 'eng_cam_in_place', 'cartridge_9', 'cartridge_8', 'cartridge_7', 'cartridge_6', 'cartridge_5', 'cartridge_4', 'cartridge_3', 'cartridge_2', 'cartridge_1', 'no_inst_in_place', 'disc_cable', ), help=''),
    Key('ab_B3_L2', Bits('sad_not_in_place', 'sad_in_place', 'plc_cont_slit_dr_cls', 'plc_cont_slit_dr_opn', 'mcp_cont_slit_dr_os4', 'mcp_cont_slit_dr_os3', 'mcp_cont_slit_dr_os2', 'mcp_cont_slit_dr_os1', 'plc_t_bar_tel', 'plc_t_bar_xport', 'plc_cont_t_bar_osr', 'mcp_cont_t_bar_osr', 'plc_cont_slit_hd_osr', 'plc_cont_slit_dr_osr', 'lift_empty', 'sad_latch_cls', 'sad_latch_opn', 'sec_latch_cls', 'sec_latch_opn', 'pri_latch_cls', 'pri_latch_opn', 'cartg_in_place', 'cor_not_in_place', 'cor_in_place', 'plc_cont_slit_hd_lth', 'plc_cont_slit_hd_unl', 'mcp_cont_slit_hd_os4', 'mcp_cont_slit_hd_os3', 'mcp_cont_slit_hd_os2', 'mcp_cont_slit_hd_os1', ), help=''),
    Key('ab_B3_L3', Bits('speed_4', 'speed_3', 'speed_2', 'speed_1', 'lift_down_enable', 'lift_up_enable', 'lift_force_dn_enable', 'lift_force_up_enable', 'eng_cam_on_lift_comp', 'eng_cam_on_lift', 'cartg_on_lift_comp', 'cartg_on_lift', 'cam_on_lift_w_j_hok', 'cam_on_lift_wo_j_hok', 'cor_on_lift', 'auto_mode_enable', 'flex_io_fault', 'empty_plate_on_lift', 'eng_cam_up_in_place', 'cor_up_in_place', 'cartg_up_in_place', 'img_cam_up_in_place', ), help=''),
    Key('ab_B3_L4', Bits('lh_grt_17d5', 'lh_lim_1d95_18d0', 'lh_les_2d0', 'lh_lim_18d0_22d2', 'lh_lim_18d0_22d0', 'lh_lim_18d0_20d99', 'lh_lim_2d5_18d5', 'lh_lim_18d0_22d75', 'lh_lim_18d0_22d5', 'lh_lim_18d0_21d74', 'lh_lim_2d2_18d5', 'lh_lim_18d0_23d0', 'lh_lim_18d0_22d8', 'lh_lim_18d0_21d89', 'lh_les_18d5', 'altitude_at_inst_chg', 'lh_lim_20d0_21d89', 'lf_les_350_3', 'lf_les_150', 'lf_les_200', 'lf_les_450', 'lf_les_350_2', 'lf_les_1400', 'lf_les_350', 'lh_lim_2d0_20d0', 'lh_lim_0d75_2d0', 'lf_les_500', 'lh_les_0d75', 'lh_les_18d5_2', 'lh_lim_18d0_22d3', 'lh_lim_22d3_23d1', 'lh_grt_23d1', ), help=''),
    Key('ab_B3_L5', Bits('lh_lim_23d1_23d3', 'lf_les_1100', 'lh_lim_22d3_23d1_2', 'lf_les_400_2', 'lf_les_150_3', 'lf_les_200_3', 'lf_les_500_3', 'lf_les_400', 'lf_les_1700', 'lh_lim_21d89_22d3', 'lf_les_350_5', 'lf_les_150_2', 'lf_les_200_2', 'lf_les_500_2', 'lf_les_350_4', 'lf_les_1650', 'lf_grt_310_2', 'lf_grt_220_2', 'lf_grt_150_2', 'lh_lim_20d0_21d89_2', 'lf_grt_125', 'lf_grt_0d0_2', 'lf_grt_0d0', 'lf_grt_310', 'lf_grt_220', 'lf_grt_1100', 'lf_grt_150', 'lh_lim_2d0_20d0_2', 'lh_lim_0d75_3d0', 'lf_grt_neg_125', 'lh_les_0d75_2', 'lf_les_800', ), help=''),
    Key('ab_B3_L6', Bits('lh_lim_22d89_23d09', 'lf_grt_950', 'lh_lim_22d85_23d05', 'lf_grt_1400', 'lh_lim_21d8_22d15', 'lh_lim_22d3_24d0', 'lf_grt_125_3', 'lf_grt_0d0_6', 'lf_grt_0d0_5', 'lf_grt_310_3', 'lf_grt_220_3', 'lf_grt_150_3', 'lh_lim_21d89_22d3_2', 'lf_grt_125_2', 'lf_grt_0d0_4', 'lf_grt_0d0_3', 'spare_b3_13_15', 'im_ff_uv_on_req', 'im_ff_wht_on_req', 'alt_bump_dn_delay', 'alt_bump_up_delay', 'az_bump_ccw_delay', 'az_bump_cw_delay', 'lh_les_6d0_5', 'lh_les_6d0_4', 'lh_les_6d0_3', 'lh_les_6d0_2', 'lh_les_6d0_1', 'lh_les_6d0', 'lf_grt_750', 'lh_lim_23d04_23d24', 'lf_grt_950_1', ), help=''),
    Key('ab_B3_L7', Bits('spare_b3_14_15', 'spare_b3_14_14', 'spare_b3_14_13', 'spare_b3_14_12', 'spare_b3_14_11', 'spare_b3_14_10', 'spare_b3_14_9', 'spare_b3_14_8', 'spare_b3_14_7', 'spare_b3_14_6', 'spare_b3_14_5', 'spare_b3_14_4', 'spare_b3_14_3', 'spare_b3_14_2', 'spare_b3_14_1', 'spare_b3_14_0', 'spare_b3_15_15', 'spare_b3_15_14', 'spare_b3_15_13', 'spare_b3_15_12', 'spare_b3_15_11', 'spare_b3_15_10', 'spare_b3_15_9', 'spare_b3_15_8', 'spare_b3_15_7', 'spare_b3_15_6', 'spare_b3_15_5', 'spare_b3_15_4', 'spare_b3_15_3', 'spare_b3_15_2', 'spare_b3_15_1', 'spare_b3_15_0', ), help=''),
    Key('ab_B3_L8', Bits('spare_b3_16_15', 'spare_b3_16_14', 'spare_b3_16_13', 'spare_b3_16_12', 'spare_b3_16_11', 'spare_b3_16_10', 'spare_b3_16_9', 'spare_b3_16_8', 'spare_b3_16_7', 'spare_b3_16_6', 'spare_b3_16_5', 'spare_b3_16_4', 'spare_b3_16_3', 'spare_b3_16_2', 'spare_b3_16_1', 'spare_b3_16_0', 'spare_b3_17_15', 'spare_b3_17_14', 'spare_b3_17_13', 'spare_b3_17_12', 'spare_b3_17_11', 'spare_b3_17_10', 'spare_b3_17_9', 'spare_b3_17_8', 'spare_b3_17_7', 'spare_b3_17_6', 'spare_b3_17_5', 'spare_b3_17_4', 'spare_b3_17_3', 'spare_b3_17_2', 'spare_b3_17_1', 'spare_b3_17_0', ), help=''),
    Key('ab_B3_L9', Bits('spare_b3_18_15', 'spare_b3_18_14', 'spare_b3_18_13', 'spare_b3_18_12', 'spare_b3_18_11', 'spare_b3_18_10', 'spare_b3_18_9', 'spare_b3_18_8', 'spare_b3_18_7', 'spare_b3_18_6', 'spare_b3_18_5', 'spare_b3_18_4', 'spare_b3_18_3', 'spare_b3_18_2', 'spare_b3_18_1', 'spare_b3_18_0', 'spare_b3_19_15', 'spare_b3_19_14', 'spare_b3_19_13', 'spare_b3_19_12', 'spare_b3_19_11', 'spare_b3_19_10', 'spare_b3_19_9', 'spare_b3_19_8', 'spare_b3_19_7', 'spare_b3_19_6', 'spare_b3_19_5', 'spare_b3_19_4', 'spare_b3_19_3', 'spare_b3_19_2', 'spare_b3_19_1', 'spare_b3_19_0', ), help=''),
    Key('ab_B10_L0', Bits('mcp_clamp_engage_cmd', 'mcp_alt_brk_en_cmd', 'mcp_alt_brk_dis_cmd', 'mcp_az_brk_en_cmd', 'mcp_az_brk_dis_cmd', 'mcp_solenoid_engage', 'mcp_pump_on', 'mcp_lift_dn_4', 'mcp_lift_dn_3', 'mcp_lift_dn_2', 'mcp_lift_dn_1', 'mcp_lift_up_1', 'mcp_lift_up_2', 'mcp_lift_up_3', 'mcp_lift_up_4', 'mcp_lift_high_psi', 'mcp_ff_screen_enable', 'mcp_hgcd_lamp_on_cmd', 'mcp_ne_lamp_on_cmd', 'mcp_ff_lamp_on_cmd', 'mcp_ff_scrn_opn_cmd', 'mcp_slit_latch2_cmd', 'mcp_slit_dr2_cls_cmd', 'mcp_slit_dr2_opn_cmd', 'mcp_slit_latch1_cmd', 'mcp_slit_dr1_cls_cmd', 'mcp_slit_dr1_opn_cmd', 'mcp_umbilical_on_off', 'mcp_umbilical_up_dn', 'mcp_15deg_stop_ret_c', 'mcp_15deg_stop_ext_c', 'mcp_clamp_disen_cmd', ), help=''),
    Key('ab_B10_L1', Bits('mcp_im_ff_uv_req', 'mcp_im_ff_wht_req', 'mcp_umbilical_fast', 'mcp_ff_screen2_enabl', 'mcp_ff_scrn2_opn_cmd', 'mcp_inst_chg_alert', 'mcp_inst_chg_prompt', 'mcp_sad_latch_opn_cm', 'mcp_sad_latch_cls_cm', 'mcp_sec_latch_opn_cm', 'mcp_sec_latch_cls_cm', 'mcp_pri_latch_opn_cm', 'mcp_pri_latch_cls_cm', 'mcp_purge_cell_on', 'mcp_t_bar_tel', 'mcp_t_bar_xport', 'velocity_trp_rst_in', ), help=''),
    Key('ab_I1_L0', Bits('rack_0_grp_0_bit_15', 'az_bump_ccw', 'az_bump_cw', 'rack_0_grp_0_bit_12', 'ops_cart_in_pos', 'fiber_cart_pos2', 'fiber_cart_pos1', 'inst_lift_low_force', 'inst_lift_high_force', 'inst_lift_man', 'inst_lift_dn', 'inst_lift_sw4', 'inst_lift_sw3', 'inst_lift_sw2', 'inst_lift_sw1', 'inst_lift_pump_on', 'low_lvl_light_req', 'rack_0_grp_1_bit_14', 'rack_0_grp_1_bit_13', 'rack_0_grp_1_bit_12', 'rack_0_grp_1_bit_11', 'rack_0_grp_1_bit_10', 'rack_0_grp_1_bit_9', 'rack_0_grp_1_bit_8', 'rack_0_grp_1_bit_7', 'optical_bench_cls', 'optical_bench_opn', 'ops_cart_in_house', 'dog_house_door_cls', 'dog_house_door_opn', 'dog_house_ccw_pad', 'dog_house_cw_pad', ), help=''),
    Key('ab_I1_L1', Bits('spare_i1_l1', ), help=''),
    Key('ab_I1_L2', Bits('spare_i1_l2', ), help=''),
    Key('ab_I1_L3', Bits('spare_i1_l3', ), help=''),
    Key('ab_I1_L4', Bits('open_slit_doors', 'close_slit_doors', 'inst_chg_remove_sw', 'inst_chg_install_sw', 'man_mode_switch', 'auto_mode_sw', 'off_mode_sw', 'iclb_leds_on_cmd', 'sad_man_valve_cls', 'sec_man_valve_cls', 'inst_man_valve_cls', 'ilcb_pres_good', 'rot_pos_370_ccw', 'rot_neg_190_cw', 'rot_inst_chg_b', 'rot_inst_chg_a', 'rack_1_grp_1_bit_15', 'rack_1_grp_1_bit_14', 'rack_1_grp_1_bit_13', 'rack_1_grp_1_bit_12', 'rack_1_grp_1_bit_11', 'rack_1_grp_1_bit_10', 'rack_1_grp_1_bit_9', 'rack_1_grp_1_bit_8', 'rack_1_grp_1_bit_7', 'rack_1_grp_1_bit_6', 'rack_1_grp_1_bit_5', 'rack_1_grp_1_bit_4', 'tbar_latch_tel_cmd', 'tbar_latch_xport_cmd', 'slit_latch_lth_cmd', 'slit_latch_unlth_cmd', ), help=''),
    Key('ab_I1_L5', Bits('spare_i1_l5', ), help=''),
    Key('ab_I1_L6', Bits('spare_i1_l6', ), help=''),
    Key('ab_I1_L7', Bits('spare_i1_l7', ), help=''),
    Key('ab_I1_L8', Bits('rack_2_grp_0_bit_15', 'spec_autofill_on', 'spec_lens2', 'spec_lens1', 'inst_id3_4', 'inst_id3_3', 'inst_id3_2', 'inst_id3_1', 'inst_id2_4', 'inst_id2_3', 'inst_id2_2', 'inst_id2_1', 'inst_id1_4', 'inst_id1_3', 'inst_id1_2', 'inst_id1_1', 'safety_latch2_cls', 'safety_latch2_opn', 'safety_latch1_cls', 'safety_latch1_opn', 'sec_latch3_cls', 'sec_latch3_opn', 'sec_latch2_cls', 'sec_latch2_opn', 'sec_latch1_cls', 'sec_latch1_opn', 'pri_latch3_cls', 'pri_latch3_opn', 'pri_latch2_cls', 'pri_latch2_opn', 'pri_latch1_cls', 'pri_latch1_opn', ), help=''),
    Key('ab_I1_L9', Bits('rack_2_grp_2_bit_15', 'rack_2_grp_2_bit_14', 'slit_head_2_in_place', 'slit_head_latch2_ext', 'slit_head_door2_cls', 'slit_head_door2_opn', 'slit_head_1_in_place', 'slit_head_latch1_ext', 'slit_head_door1_cls', 'slit_head_door1_opn', 'sad_mount2', 'sad_mount1', 'sad_latch2_cls', 'sad_latch2_opn', 'sad_latch1_cls', 'sad_latch1_opn', ), help=''),
    Key('ab_I1_L10', Bits('rack_2_grp_4_bit_15', 'rack_2_grp_4_bit_14', 'rack_2_grp_4_bit_13', 'rack_2_grp_4_bit_12', 'rack_2_grp_4_bit_11', 'rack_2_grp_4_bit_10', 'rack_2_grp_4_bit_9', 'rack_2_grp_4_bit_8', 'rack_2_grp_4_bit_7', 'rack_2_grp_4_bit_6', 'rack_2_grp_4_bit_5', 'rack_2_grp_4_bit_4', 'sec_mir_force_limits', 'alt_bump_dn', 'alt_bump_up', 'purge_air_pressur_sw', ), help=''),
    Key('ab_I1_L11', Bits('spare_i1_l11', ), help=''),
    Key('ab_I1_L12', Bits('spare_i1_l12', 'rack_3_grp_1_bit_15', 'rack_3_grp_1_bit_14', 'rack_3_grp_1_bit_13', 'rack_3_grp_1_bit_12', 'rack_3_grp_1_bit_11', 'rack_3_grp_1_bit_10', 'man_lift_dn_4', 'man_lift_dn_3', 'man_lift_dn_2', 'man_lift_dn_1', 'man_lift_up_4', 'man_lift_up_3', 'man_lift_up_2', 'man_lift_up_1', 'inst_lift_auto', 'rack_3_grp_1_bit_0', ), help=''),
    Key('ab_I1_L13', Bits('leaf_8_closed_stat', 'leaf_8_open_stat', 'leaf_7_closed_stat', 'leaf_7_open_stat', 'leaf_6_closed_stat', 'leaf_6_open_stat', 'leaf_5_closed_stat', 'leaf_5_open_stat', 'leaf_4_closed_stat', 'leaf_4_open_stat', 'leaf_3_closed_stat', 'leaf_3_open_stat', 'leaf_2_closed_stat', 'leaf_2_open_stat', 'leaf_1_closed_stat', 'leaf_1_open_stat', 'rack_3_grp_3_bit_15', 'rack_3_grp_3_bit_14', 'rack_3_grp_3_bit_13', 'rack_3_grp_3_bit_12', 'hgcd_4_stat', 'hgcd_3_stat', 'hgcd_2_stat', 'hgcd_1_stat', 'ne_4_stat', 'ne_3_stat', 'ne_2_stat', 'ne_1_stat', 'ff_4_stat', 'ff_3_stat', 'ff_2_stat', 'ff_1_stat', ), help=''),
    Key('ab_I1_L14', Bits('rack_3_grp_4_bit_15', 'rack_3_grp_4_bit_14', 'rack_3_grp_4_bit_13', 'rack_3_grp_4_bit_12', 'rack_3_grp_4_bit_11', 'rack_3_grp_4_bit_10', 'rack_3_grp_4_bit_9', 'rack_3_grp_4_bit_8', 'man_im_ff_uv_req', 'man_im_ff_wht_req', 'ff_man_cont_enable', 'man_hgcd_lamp_on_cmd', 'man_ne_lamp_on_cmd', 'man_ff_lamp_on_cmd', 'man_ff_scrn_en_cmd', 'man_ff_scrn_opn_cmd', ), help=''),
    Key('ab_I1_L15', Bits('spare_i1_l15', ), help=''),
    Key('ab_I2_L0', Bits('spare', 'wind_alt_perm', 'wind_az_perm', 'wind_alt1_fault', 'wind_az3_fault', 'wind_az2_fault', 'wind_az1_fault', ), help=''),
    Key('ab_I6_L0', Bits('mcp_watchdog_timer', 'nw_fork_stop', 's_wind_stop', 'w_lower_stop', 'e_lower_stop', 's_lower_stop', 'n_lower_stop', 'w_rail_stop', 's_rail_stop', 'n_rail_stop', 'n_fork_stop', 'n_wind_stop', 'fiber_signal_loss', 'spare_s1_c2', 'cr_stop', 'tcc_stop', 'az_stow_3b', 'wind_az_plc_perm_in', 'az_plc_perm_in', 'wind_az_mtr_perm_in', 'az_mtr2_perm_in', 'az_mtr1_perm_in', 'az_mtr_ccw_perm_in', 'az_mtr_cw_perm_in', 'az_stow_3a', 'wind_alt_plc_perm_in', 'alt_plc_perm_in', 'wind_alt_mtr_perm_in', 'alt_mtr2_perm_in', 'alt_mtr1_perm_in', 'alt_mtr_dn_perm_in', 'alt_mtr_up_perm_in', ), help=''),
    Key('ab_I7_L0', Bits('az_stow_1b', 'az_stow_1a', 'alt_grt_18d6_limit_1', 'az_109_131_limit_1', 'bldg_on_alt', 'alt_les_90d5_limit', 'alt_locking_pin_out', 'alt_grt_0d3_limit', 'alt_les_2d5_limit', 'hatch_cls', 'rot_plc_perm_in', 'bldg_perm_in', 'spare_s5_c3', 'rot_mtr_perm_in', 'rot_mtr_ccw_perm_in', 'rot_mtr_cw_perm_in', 'spare_s8_c7', 'spare_s8_c6', 'az_pos_445b_ccw', 'az_neg_201b_cw', 'az_pos_445a_ccw', 'az_neg_201a_cw', 'az_dir_ccw', 'az_dir_cw', 'alt_velocity_limit', 'alt_slip', 'alt_grt_18d6_limit_2', 'deg_15_stop_ext', 'az_stow_2b', 'az_stow_2a', 'bldg_clear_alt', 'alt_grt_83_limit_1', ), help=''),
    Key('ab_I8_L0', Bits('rot_velocity_limit', 'rot_slip', 'rot_pos_380b_ccw', 'rot_neg_200b_cw', 'rot_pos_380a_ccw', 'rot_neg_200a_cw', 'rot_dir_ccw', 'rot_dir_cw', 'az_velocity_limit', 'az_slip', 'spare_s9_c5', 'bldg_clear_az', 'alt_grt_83_limit_2', 'az_109_131_limit_2', 'bldg_on_az', 'alt_grt_18d6_limit_3', 't_bar_xport_stat', 'in_8_bit_30_spare', 'in_8_bit_29_spare', 'in_8_bit_28_spare', 'deg_15_stop_ret', 'e_stop_byp_sw', 'umbilical_strain_sw', 'rot_mtr_rdy', 'alt_mtr2_rdy', 'alt_mtr1_rdy', 'az_mtr2_rdy', 'az_mtr1_rdy', 'az_pos_440_ccw', 'az_neg_196_cw', 'az_110_130_limit', 'az_stow_cntr_sw', ), help=''),
    Key('ab_I9_L0', Bits('in_9_bit_15_spare', 'in_9_bit_14_spare', 'in_9_bit_13_spare', 'in_9_bit_12_spare', 'in_9_bit_11_spare', 'in_9_bit_10_spare', 'alt_locking_pin_in', 'solenoid_engage_sw', 'low_lvl_lighting_req', 'alt_brake_dis_stat', 'alt_brake_en_stat', 'az_brake_dis_stat', 'az_brake_en_stat', 'clamp_dis_stat', 'clamp_en_stat', 't_bar_tel_stat', 's2_c7_mcp_wtchdg_byp', 's2_c6_bypass_sw', 's2_c5_bypass_sw', 's2_c4_bypass_sw', 's2_c3_bypass_sw', 's2_c2_bypass_sw', 's2_c1_bypass_sw', 's2_c0_bypass_sw', 's1_c7_bypass_sw', 's1_c6_bypass_sw', 's1_c5_bypass_sw', 's1_c4_bypass_sw', 's1_c3_bypass_sw', 's1_c2_bypass_sw', 's1_c1_bypass_sw', 's1_c0_bypass_sw', ), help=''),
    Key('ab_I10_L0', Bits('umbilical_dn', 'alt_pos_gt_neg_2', 'alt_pos_lt_0_2', 'alt_position_gt_83_5', 'alt_position_gt_15_5', 'alt_position_gt_15_0', 'alt_position_lt_18_5', 'alt_position_gt_0_8', 'alt_position_gt_19_5', 'alt_position_gt_0_50', 'alt_position_gt_89_8', 'alt_position_lt_91_0', 'alt_position_lt_90_29', 'alt_position_lt_90_2', 'alt_position_gt_89_75', 'alt_position_lt_90_15', 'in_10_bit_31_spare', 'in_10_bit_30_spare', 'in_10_bit_29_spare', 'in_10_bit_28_spare', 'in_10_bit_27_spare', 'in_10_bit_26_spare', 'in_10_bit_25_spare', 'in_10_bit_24_spare', 'in_10_bit_23_spare', 'in_10_bit_22_spare', 'in_10_bit_21_spare', 'in_10_bit_20_spare', 'in_10_bit_19_spare', 'in_10_bit_18_spare', 'lift_height_gt_h_cartridge_mount', 'lift_force_gt_f_cartridge_mount', ), help=''),
    Key('ab_O1_L0', Bits('spare_o1_l0', ), help=''),
    Key('ab_O1_L1', Bits('low_lvl_light_2', 'low_lvl_light_1', 'az_stow_light', 'stop_bypass_strobe', 'az_stow_center_light', 'rack_0_grp_2_bit_10', 'lamp_on_enable', 'inst_lift_dn_4', 'inst_lift_dn_3', 'inst_lift_dn_2', 'inst_lift_dn_1', 'inst_lift_up_1', 'inst_lift_up_2', 'inst_lift_up_3', 'inst_lift_up_4', 'inst_lift_high_psi', ), help=''),
    Key('ab_O1_L2', Bits('spare_o1_l2', ), help=''),
    Key('ab_O1_L3', Bits('spare_01_l3', ), help=''),
    Key('ab_O1_L4', Bits('spare_o1_l4', ), help=''),
    Key('ab_O1_L5', Bits('slit1_latched_led', 'slit1_unlatched_led', 'lift_down_led', 'cart_in_place_led', 'cam_crt_in_house_led', 'dog_door_open_led', 'jhook_in_place_led', 'sad_in_place_led', 'eng_in_place_led', 'cartg_in_place_led', 'cam_in_place_led', 'cor_in_place_led', 'eng_on_lift_led', 'cartg_on_lift_led', 'cam_on_lift_led', 'cor_on_lift_led', 'sec_latch2_cls_led', 'sec_latch2_opn_led', 'sec_latch1_cls_led', 'sec_latch1_opn_led', 'inst_latch_perm', 'inst_unlatch_perm', 'inst_latch3_cls_led', 'inst_latch3_opn_led', 'inst_latch2_cls_led', 'inst_latch2_opn_led', 'inst_latch1_cls_led', 'inst_latch1_opn_led', 'slit_latch_prm_led', 'slit_unlatch_prm_led', 'slit2_latched_led', 'slit2_unlatched_led', ), help=''),
    Key('ab_O1_L6', Bits('slit_dr_opn_perm_led', 'slit_dr_cls_perm_led', 'tbar_tel_perm_led', 'tbar_xport_perm_led', 'tbar_tel_led', 'tbar_xport_led', 'sad_latch_perm', 'sad_unlatch_perm', 'sad_latch2_cls_led', 'sad_latch2_opn_led', 'sad_latch1_cls_led', 'sad_latch1_opn_led', 'sec_latch_perm', 'sec_unlatch_perm', 'sec_latch3_cls_led', 'sec_latch3_opn_led', 'rack_1_grp_5_bit_15', 'rack_1_grp_5_bit_14', 'rack_1_grp_5_bit_13', 'saf_latch2_cls_led', 'saf_latch2_opn_led', 'saf_latch1_cls_led', 'saf_latch1_opn_led', 'manual_mode_led', 'sad_latch_air_led', 'sec_latch_air_led', 'inst_latch_air_led', 'ilcb_pres_led', 'slit_dr2_opn_led', 'slit_dr2_cls_led', 'slit_dr1_opn_led', 'slit_dr1_cls_led', ), help=''),
    Key('ab_O1_L7', Bits('spare_o1_l7', ), help=''),
    Key('ab_O1_L8', Bits('spare_o1_l8', ), help=''),
    Key('ab_O1_L9', Bits('spare_o1_l9', 'rack_2_grp_3_bit_15', 'rack_2_grp_3_bit_14', 'rack_2_grp_3_bit_13', 'rack_2_grp_3_bit_12', 'rack_2_grp_3_bit_11', 'rack_2_grp_3_bit_10', 'rack_2_grp_3_bit_9', 'rack_2_grp_3_bit_8', 'rack_2_grp_3_bit_7', 'rack_2_grp_3_bit_6', 'slit_latch2_ext_perm', 'slit_dr2_opn_perm', 'slit_dr2_cls_perm', 'slit_latch1_ext_perm', 'slit_dr1_opn_perm', 'slit_dr1_cls_perm', ), help=''),
    Key('ab_O1_L10', Bits('spare_o1_l10', 'audio_warning_2', 'rack_2_grp_5_bit_14', 'rack_2_grp_5_bit_13', 'rack_2_grp_5_bit_12', 'rack_2_grp_5_bit_11', 'rack_2_grp_5_bit_10', 'rack_2_grp_5_bit_9', 'rack_2_grp_5_bit_8', 'rack_2_grp_5_bit_7', 'rack_2_grp_5_bit_6', 'rack_2_grp_5_bit_5', 'rack_2_grp_5_bit_4', 'rack_2_grp_5_bit_3', 'rack_2_grp_5_bit_2', 'rack_2_grp_5_bit_1', 'purge_valve_permit', ), help=''),
    Key('ab_O1_L11', Bits('spare_o1_l11', ), help=''),
    Key('ab_O1_L12', Bits('spare_o1_l12', ), help=''),
    Key('ab_O1_L13', Bits('spare_o1_l13', ), help=''),
    Key('ab_O1_L14', Bits('spare_o1_l14', 'audio_warning_1', 'rack_4_grp_5_bit_14', 'rack_4_grp_5_bit_13', 'rack_4_grp_5_bit_12', 'rack_4_grp_5_bit_11', 'rack_4_grp_5_bit_10', 'rack_4_grp_5_bit_9', 'im_ff_uv_on_pmt', 'im_ff_wht_on_pmt', 'ff_screen2_enable_pm', 'ff_screen2_open_pmt', 'hgcd_lamps_on_pmt', 'ne_lamps_on_pmt', 'ff_lamps_on_pmt', 'ff_screen_enable_pmt', 'ff_screen_open_pmt', ), help=''),
    Key('ab_O1_L15', Bits('spare_o1_l15', ), help=''),
    Key('ab_O2_L0', Bits('out_2_bit_21_spare', 'out_2_bit_20_spare', 'wind_mtr_dn_perm', 'wind_mtr_up_perm', 'wind_mtr_ccw_perm', 'wind_mtr_cw_perm', ), help=''),
    Key('ab_O11_L0', Bits('s_ll_led', 'n_ll_led', 'w_rail_led', 's_rail_led', 'n_rail_led', 'rot_plc_perm', 'rot_mtr_ccw_perm', 'rot_mtr_cw_perm', 'wind_az_plc_perm', 'az_plc_perm', 'az_mtr_ccw_perm', 'az_mtr_cw_perm', 'wind_alt_plc_perm', 'alt_plc_perm', 'alt_mtr_dn_perm', 'alt_mtr_up_perm', 'clamp_en', 'clamp_dis', 't_bar_xport_perm', 't_bar_tel_perm', 'out_11_bit_27_spare', 'lift_pump_on', 'out_11_bit_25_spare', 'out_11_bit_24_spare', 'deg_15_stop_ret_perm', 'deg_15_stop_ext_perm', 'lift_solenoid_en', 's_wind_led', 'n_fork_led', 'n_wind_led', 'w_ll_led', 'e_ll_led', ), help=''),
    Key('ab_O12_L0', Bits('out_12_bit_15_spare', 'out_12_bit_14_spare', 'out_12_bit_13_spare', 'umbilical_fast', 'lift_enable', 'velocity_trp_rst_out', 'velocity_select_bit', 'stow_pos_light', 'inst_chg_pos_light', 'nw_fork_led', 'umbilical_up_dn', 'umbilical_on_off', 'alt_brake_en', 'alt_brake_dis', 'az_brake_en', 'az_brake_dis', 'out_12_bit_31_spare', 'out_12_bit_30_spare', 'out_12_bit_29_spare', 'out_12_bit_28_spare', 'out_12_bit_27_spare', 'out_12_bit_26_spare', 'out_12_bit_25_spare', 'out_12_bit_24_spare', 'out_12_bit_23_spare', 'out_12_bit_22_spare', 'out_12_bit_21_spare', 'out_12_bit_20_spare', 'out_12_bit_19_spare', 'out_12_bit_18_spare', 'out_12_bit_17_spare', 'out_12_bit_16_spare', ), help=''),
)

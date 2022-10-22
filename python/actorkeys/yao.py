#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2021-09-27
# @Filename: jaeger.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)
#
# type: ignore

KeysDictionary(
    "yao",
    (1, 0),
    Key("version", String(help="Actor version")),
    Key("text", String(), help="Text for humans"),
    Key("error", String()),
    Key("sp2_text", String(), help="Text for humans"),
    Key("sp2_error", String()),
    Key("sp2_status", Int()),
    Key("sp2_status_names", String() * (0,)),
    Key("sp2_valid", Int()),
    Key("sp2_count", Int()),
    Key("sp2_log", Int()),
    Key("sp2_power", Int()),
    Key("sp2_powergood", Int()),
    Key("sp2_overheat", Int()),
    Key("sp2_extclkpresent", Int()),
    Key("sp2_backplane_temp", Float()),
    Key("sp2_p2v5_v", Float()),
    Key("sp2_p2v5_i", Float()),
    Key("sp2_p5v_v", Float()),
    Key("sp2_p5v_i", Float()),
    Key("sp2_p6v_v", Float()),
    Key("sp2_p6v_i", Float()),
    Key("sp2_n6v_v", Float()),
    Key("sp2_n6v_i", Float()),
    Key("sp2_p17v_v", Float()),
    Key("sp2_p17v_i", Float()),
    Key("sp2_n17v_v", Float()),
    Key("sp2_n17v_i", Float()),
    Key("sp2_p35v_v", Float()),
    Key("sp2_p35v_i", Float()),
    Key("sp2_n35v_v", Float()),
    Key("sp2_n35v_i", Float()),
    Key("sp2_p100v_v", Float()),
    Key("sp2_p100v_i", Float()),
    Key("sp2_n100v_v", Float()),
    Key("sp2_n100v_i", Float()),
    Key("sp2_user_v", Float()),
    Key("sp2_user_i", Float()),
    Key("sp2_heater_v", Float()),
    Key("sp2_heater_i", Float()),
    Key("sp2_fantach", Int()),
    Key("sp2_mod1_temp", Float()),
    Key("sp2_mod1_xvp_v1", Float()),
    Key("sp2_mod1_xvp_i1", Float()),
    Key("sp2_mod1_xvp_v2", Float()),
    Key("sp2_mod1_xvp_i2", Float()),
    Key("sp2_mod1_xvp_v3", Float()),
    Key("sp2_mod1_xvp_i3", Float()),
    Key("sp2_mod1_xvp_v4", Float()),
    Key("sp2_mod1_xvp_i4", Float()),
    Key("sp2_mod1_xvn_v1", Float()),
    Key("sp2_mod1_xvn_i1", Float()),
    Key("sp2_mod1_xvn_v2", Float()),
    Key("sp2_mod1_xvn_i2", Float()),
    Key("sp2_mod1_xvn_v3", Float()),
    Key("sp2_mod1_xvn_i3", Float()),
    Key("sp2_mod1_xvn_v4", Float()),
    Key("sp2_mod1_xvn_i4", Float()),
    Key("sp2_mod2_temp", Float()),
    Key("sp2_mod2_tempa", Float()),
    Key("sp2_mod2_tempb", Float()),
    Key("sp2_mod2_tempc", Float()),
    Key("sp2_mod2_heateraoutput", Float()),
    Key("sp2_mod2_heaterboutput", Float()),
    Key("sp2_mod2_heaterap", Int()),
    Key("sp2_mod2_heaterai", Int()),
    Key("sp2_mod2_heaterad", Int()),
    Key("sp2_mod2_heaterbp", Int()),
    Key("sp2_mod2_heaterbi", Int()),
    Key("sp2_mod2_heaterbd", Int()),
    Key("sp2_mod2_dinputs", Int()),
    Key("sp2_mod2_vcpu_outreg0", Int()),
    Key("sp2_mod2_vcpu_outreg1", Int()),
    Key("sp2_mod2_vcpu_outreg2", Int()),
    Key("sp2_mod2_vcpu_outreg3", Int()),
    Key("sp2_mod2_vcpu_outreg4", Int()),
    Key("sp2_mod2_vcpu_outreg5", Int()),
    Key("sp2_mod2_vcpu_outreg6", Int()),
    Key("sp2_mod2_vcpu_outreg7", Int()),
    Key("sp2_mod2_vcpu_outreg8", Int()),
    Key("sp2_mod2_vcpu_outreg9", Int()),
    Key("sp2_mod2_vcpu_outreg10", Int()),
    Key("sp2_mod2_vcpu_outreg11", Int()),
    Key("sp2_mod2_vcpu_outreg12", Int()),
    Key("sp2_mod2_vcpu_outreg13", Int()),
    Key("sp2_mod2_vcpu_outreg14", Int()),
    Key("sp2_mod2_vcpu_outreg15", Int()),
    Key("sp2_mod4_temp", Float()),
    Key("sp2_mod4_lvlc_v1", Float()),
    Key("sp2_mod4_lvlc_i1", Float()),
    Key("sp2_mod4_lvlc_v2", Float()),
    Key("sp2_mod4_lvlc_i2", Float()),
    Key("sp2_mod4_lvlc_v3", Float()),
    Key("sp2_mod4_lvlc_i3", Float()),
    Key("sp2_mod4_lvlc_v4", Float()),
    Key("sp2_mod4_lvlc_i4", Float()),
    Key("sp2_mod4_lvlc_v5", Float()),
    Key("sp2_mod4_lvlc_i5", Float()),
    Key("sp2_mod4_lvlc_v6", Float()),
    Key("sp2_mod4_lvlc_i6", Float()),
    Key("sp2_mod4_lvlc_v7", Float()),
    Key("sp2_mod4_lvlc_i7", Float()),
    Key("sp2_mod4_lvlc_v8", Float()),
    Key("sp2_mod4_lvlc_i8", Float()),
    Key("sp2_mod4_lvlc_v9", Float()),
    Key("sp2_mod4_lvlc_i9", Float()),
    Key("sp2_mod4_lvlc_v10", Float()),
    Key("sp2_mod4_lvlc_i10", Float()),
    Key("sp2_mod4_lvlc_v11", Float()),
    Key("sp2_mod4_lvlc_i11", Float()),
    Key("sp2_mod4_lvlc_v12", Float()),
    Key("sp2_mod4_lvlc_i12", Float()),
    Key("sp2_mod4_lvlc_v13", Float()),
    Key("sp2_mod4_lvlc_i13", Float()),
    Key("sp2_mod4_lvlc_v14", Float()),
    Key("sp2_mod4_lvlc_i14", Float()),
    Key("sp2_mod4_lvlc_v15", Float()),
    Key("sp2_mod4_lvlc_i15", Float()),
    Key("sp2_mod4_lvlc_v16", Float()),
    Key("sp2_mod4_lvlc_i16", Float()),
    Key("sp2_mod4_lvlc_v17", Float()),
    Key("sp2_mod4_lvlc_i17", Float()),
    Key("sp2_mod4_lvlc_v18", Float()),
    Key("sp2_mod4_lvlc_i18", Float()),
    Key("sp2_mod4_lvlc_v19", Float()),
    Key("sp2_mod4_lvlc_i19", Float()),
    Key("sp2_mod4_lvlc_v20", Float()),
    Key("sp2_mod4_lvlc_i20", Float()),
    Key("sp2_mod4_lvlc_v21", Float()),
    Key("sp2_mod4_lvlc_i21", Float()),
    Key("sp2_mod4_lvlc_v22", Float()),
    Key("sp2_mod4_lvlc_i22", Float()),
    Key("sp2_mod4_lvlc_v23", Float()),
    Key("sp2_mod4_lvlc_i23", Float()),
    Key("sp2_mod4_lvlc_v24", Float()),
    Key("sp2_mod4_lvlc_i24", Float()),
    Key("sp2_mod4_lvhc_v1", Float()),
    Key("sp2_mod4_lvhc_i1", Float()),
    Key("sp2_mod4_lvhc_v2", Float()),
    Key("sp2_mod4_lvhc_i2", Float()),
    Key("sp2_mod4_lvhc_v3", Float()),
    Key("sp2_mod4_lvhc_i3", Float()),
    Key("sp2_mod4_lvhc_v4", Float()),
    Key("sp2_mod4_lvhc_i4", Float()),
    Key("sp2_mod4_lvhc_v5", Float()),
    Key("sp2_mod4_lvhc_i5", Float()),
    Key("sp2_mod4_lvhc_v6", Float()),
    Key("sp2_mod4_lvhc_i6", Float()),
    Key("sp2_mod4_dinputs", Int()),
    Key("sp2_mod4_vcpu_outreg0", Int()),
    Key("sp2_mod4_vcpu_outreg1", Int()),
    Key("sp2_mod4_vcpu_outreg2", Int()),
    Key("sp2_mod4_vcpu_outreg3", Int()),
    Key("sp2_mod4_vcpu_outreg4", Int()),
    Key("sp2_mod4_vcpu_outreg5", Int()),
    Key("sp2_mod4_vcpu_outreg6", Int()),
    Key("sp2_mod4_vcpu_outreg7", Int()),
    Key("sp2_mod4_vcpu_outreg8", Int()),
    Key("sp2_mod4_vcpu_outreg9", Int()),
    Key("sp2_mod4_vcpu_outreg10", Int()),
    Key("sp2_mod4_vcpu_outreg11", Int()),
    Key("sp2_mod4_vcpu_outreg12", Int()),
    Key("sp2_mod4_vcpu_outreg13", Int()),
    Key("sp2_mod4_vcpu_outreg14", Int()),
    Key("sp2_mod4_vcpu_outreg15", Int()),
    Key("sp2_mod6_temp", Float()),
    Key("sp2_mod7_temp", Float()),
    Key("sp2_mod9_temp", Float()),
    Key("sp2_mod9_lvlc_v1", Float()),
    Key("sp2_mod9_lvlc_i1", Float()),
    Key("sp2_mod9_lvlc_v2", Float()),
    Key("sp2_mod9_lvlc_i2", Float()),
    Key("sp2_mod9_lvlc_v3", Float()),
    Key("sp2_mod9_lvlc_i3", Float()),
    Key("sp2_mod9_lvlc_v4", Float()),
    Key("sp2_mod9_lvlc_i4", Float()),
    Key("sp2_mod9_lvlc_v5", Float()),
    Key("sp2_mod9_lvlc_i5", Float()),
    Key("sp2_mod9_lvlc_v6", Float()),
    Key("sp2_mod9_lvlc_i6", Float()),
    Key("sp2_mod9_lvlc_v7", Float()),
    Key("sp2_mod9_lvlc_i7", Float()),
    Key("sp2_mod9_lvlc_v8", Float()),
    Key("sp2_mod9_lvlc_i8", Float()),
    Key("sp2_mod9_lvlc_v9", Float()),
    Key("sp2_mod9_lvlc_i9", Float()),
    Key("sp2_mod9_lvlc_v10", Float()),
    Key("sp2_mod9_lvlc_i10", Float()),
    Key("sp2_mod9_lvlc_v11", Float()),
    Key("sp2_mod9_lvlc_i11", Float()),
    Key("sp2_mod9_lvlc_v12", Float()),
    Key("sp2_mod9_lvlc_i12", Float()),
    Key("sp2_mod9_lvlc_v13", Float()),
    Key("sp2_mod9_lvlc_i13", Float()),
    Key("sp2_mod9_lvlc_v14", Float()),
    Key("sp2_mod9_lvlc_i14", Float()),
    Key("sp2_mod9_lvlc_v15", Float()),
    Key("sp2_mod9_lvlc_i15", Float()),
    Key("sp2_mod9_lvlc_v16", Float()),
    Key("sp2_mod9_lvlc_i16", Float()),
    Key("sp2_mod9_lvlc_v17", Float()),
    Key("sp2_mod9_lvlc_i17", Float()),
    Key("sp2_mod9_lvlc_v18", Float()),
    Key("sp2_mod9_lvlc_i18", Float()),
    Key("sp2_mod9_lvlc_v19", Float()),
    Key("sp2_mod9_lvlc_i19", Float()),
    Key("sp2_mod9_lvlc_v20", Float()),
    Key("sp2_mod9_lvlc_i20", Float()),
    Key("sp2_mod9_lvlc_v21", Float()),
    Key("sp2_mod9_lvlc_i21", Float()),
    Key("sp2_mod9_lvlc_v22", Float()),
    Key("sp2_mod9_lvlc_i22", Float()),
    Key("sp2_mod9_lvlc_v23", Float()),
    Key("sp2_mod9_lvlc_i23", Float()),
    Key("sp2_mod9_lvlc_v24", Float()),
    Key("sp2_mod9_lvlc_i24", Float()),
    Key("sp2_mod9_lvhc_v1", Float()),
    Key("sp2_mod9_lvhc_i1", Float()),
    Key("sp2_mod9_lvhc_v2", Float()),
    Key("sp2_mod9_lvhc_i2", Float()),
    Key("sp2_mod9_lvhc_v3", Float()),
    Key("sp2_mod9_lvhc_i3", Float()),
    Key("sp2_mod9_lvhc_v4", Float()),
    Key("sp2_mod9_lvhc_i4", Float()),
    Key("sp2_mod9_lvhc_v5", Float()),
    Key("sp2_mod9_lvhc_i5", Float()),
    Key("sp2_mod9_lvhc_v6", Float()),
    Key("sp2_mod9_lvhc_i6", Float()),
    Key("sp2_mod9_dinputs", Int()),
    Key("sp2_mod9_vcpu_outreg0", Int()),
    Key("sp2_mod9_vcpu_outreg1", Int()),
    Key("sp2_mod9_vcpu_outreg2", Int()),
    Key("sp2_mod9_vcpu_outreg3", Int()),
    Key("sp2_mod9_vcpu_outreg4", Int()),
    Key("sp2_mod9_vcpu_outreg5", Int()),
    Key("sp2_mod9_vcpu_outreg6", Int()),
    Key("sp2_mod9_vcpu_outreg7", Int()),
    Key("sp2_mod9_vcpu_outreg8", Int()),
    Key("sp2_mod9_vcpu_outreg9", Int()),
    Key("sp2_mod9_vcpu_outreg10", Int()),
    Key("sp2_mod9_vcpu_outreg11", Int()),
    Key("sp2_mod9_vcpu_outreg12", Int()),
    Key("sp2_mod9_vcpu_outreg13", Int()),
    Key("sp2_mod9_vcpu_outreg14", Int()),
    Key("sp2_mod9_vcpu_outreg15", Int()),
    Key("sp2_mod11_temp", Float()),
    Key("sp2_mod11_tempa", Float()),
    Key("sp2_mod11_tempb", Float()),
    Key("sp2_mod11_tempc", Float()),
    Key("sp2_mod11_heateraoutput", Float()),
    Key("sp2_mod11_heaterboutput", Float()),
    Key("sp2_mod11_heaterap", Int()),
    Key("sp2_mod11_heaterai", Int()),
    Key("sp2_mod11_heaterad", Int()),
    Key("sp2_mod11_heaterbp", Int()),
    Key("sp2_mod11_heaterbi", Int()),
    Key("sp2_mod11_heaterbd", Int()),
    Key("sp2_mod11_dinputs", Int()),
    Key("sp2_mod11_vcpu_outreg0", Int()),
    Key("sp2_mod11_vcpu_outreg1", Int()),
    Key("sp2_mod11_vcpu_outreg2", Int()),
    Key("sp2_mod11_vcpu_outreg3", Int()),
    Key("sp2_mod11_vcpu_outreg4", Int()),
    Key("sp2_mod11_vcpu_outreg5", Int()),
    Key("sp2_mod11_vcpu_outreg6", Int()),
    Key("sp2_mod11_vcpu_outreg7", Int()),
    Key("sp2_mod11_vcpu_outreg8", Int()),
    Key("sp2_mod11_vcpu_outreg9", Int()),
    Key("sp2_mod11_vcpu_outreg10", Int()),
    Key("sp2_mod11_vcpu_outreg11", Int()),
    Key("sp2_mod11_vcpu_outreg12", Int()),
    Key("sp2_mod11_vcpu_outreg13", Int()),
    Key("sp2_mod11_vcpu_outreg14", Int()),
    Key("sp2_mod11_vcpu_outreg15", Int()),
    Key("sp2_mod12_temp", Float()),
    Key("sp2_mod12_hvlc_v1", Float()),
    Key("sp2_mod12_hvlc_i1", Float()),
    Key("sp2_mod12_hvlc_v2", Float()),
    Key("sp2_mod12_hvlc_i2", Float()),
    Key("sp2_mod12_hvlc_v3", Float()),
    Key("sp2_mod12_hvlc_i3", Float()),
    Key("sp2_mod12_hvlc_v4", Float()),
    Key("sp2_mod12_hvlc_i4", Float()),
    Key("sp2_mod12_hvlc_v5", Float()),
    Key("sp2_mod12_hvlc_i5", Float()),
    Key("sp2_mod12_hvlc_v6", Float()),
    Key("sp2_mod12_hvlc_i6", Float()),
    Key("sp2_mod12_hvlc_v7", Float()),
    Key("sp2_mod12_hvlc_i7", Float()),
    Key("sp2_mod12_hvlc_v8", Float()),
    Key("sp2_mod12_hvlc_i8", Float()),
    Key("sp2_mod12_hvlc_v9", Float()),
    Key("sp2_mod12_hvlc_i9", Float()),
    Key("sp2_mod12_hvlc_v10", Float()),
    Key("sp2_mod12_hvlc_i10", Float()),
    Key("sp2_mod12_hvlc_v11", Float()),
    Key("sp2_mod12_hvlc_i11", Float()),
    Key("sp2_mod12_hvlc_v12", Float()),
    Key("sp2_mod12_hvlc_i12", Float()),
    Key("sp2_mod12_hvlc_v13", Float()),
    Key("sp2_mod12_hvlc_i13", Float()),
    Key("sp2_mod12_hvlc_v14", Float()),
    Key("sp2_mod12_hvlc_i14", Float()),
    Key("sp2_mod12_hvlc_v15", Float()),
    Key("sp2_mod12_hvlc_i15", Float()),
    Key("sp2_mod12_hvlc_v16", Float()),
    Key("sp2_mod12_hvlc_i16", Float()),
    Key("sp2_mod12_hvlc_v17", Float()),
    Key("sp2_mod12_hvlc_i17", Float()),
    Key("sp2_mod12_hvlc_v18", Float()),
    Key("sp2_mod12_hvlc_i18", Float()),
    Key("sp2_mod12_hvlc_v19", Float()),
    Key("sp2_mod12_hvlc_i19", Float()),
    Key("sp2_mod12_hvlc_v20", Float()),
    Key("sp2_mod12_hvlc_i20", Float()),
    Key("sp2_mod12_hvlc_v21", Float()),
    Key("sp2_mod12_hvlc_i21", Float()),
    Key("sp2_mod12_hvlc_v22", Float()),
    Key("sp2_mod12_hvlc_i22", Float()),
    Key("sp2_mod12_hvlc_v23", Float()),
    Key("sp2_mod12_hvlc_i23", Float()),
    Key("sp2_mod12_hvlc_v24", Float()),
    Key("sp2_mod12_hvlc_i24", Float()),
    Key("sp2_mod12_hvhc_v1", Float()),
    Key("sp2_mod12_hvhc_i1", Float()),
    Key("sp2_mod12_hvhc_v2", Float()),
    Key("sp2_mod12_hvhc_i2", Float()),
    Key("sp2_mod12_hvhc_v3", Float()),
    Key("sp2_mod12_hvhc_i3", Float()),
    Key("sp2_mod12_hvhc_v4", Float()),
    Key("sp2_mod12_hvhc_i4", Float()),
    Key("sp2_mod12_hvhc_v5", Float()),
    Key("sp2_mod12_hvhc_i5", Float()),
    Key("sp2_mod12_hvhc_v6", Float()),
    Key("sp2_mod12_hvhc_i6", Float()),
    Key(
        "motor_a",
        Int(name="position"),
        Int(name="velocity"),
        Int(name="current"),
        Bool("F", "T", name="limit"),
    ),
    Key(
        "motor_b",
        Int(name="position"),
        Int(name="velocity"),
        Int(name="current"),
        Bool("F", "T", name="limit"),
    ),
    Key(
        "motor_c",
        Int(name="position"),
        Int(name="velocity"),
        Int(name="current"),
        Bool("F", "T", name="limit"),
    ),
    Key("motor_positions", Int() * (0,)),
    Key("temperature_blue", Float()),
    Key("humidity_blue", Float()),
    Key("temperature_red", Float()),
    Key("humidity_red", Float()),
    Key("temperature_collimator", Float()),
    Key("humidity_collimator", Float()),
    Key("specMech_temp", Float()),
    Key("accelerometer", Float() * (0,)),
    Key("shutter", Enum("open", "closed")),
    Key("hartmann_left", Enum("open", "closed")),
    Key("hartmann_right", Enum("open", "closed")),
    Key("air_pressure", Enum("on", "off")),
    Key("boot_time", String()),
    Key("clock_time", String()),
    Key("set_time", String()),
    Key("specMech_version", String()),
    Key("vacuum_red_log10_pa", Float()),
    Key("vacuum_blue_log10_pa", Float()),
    Key("mech_raw_reply", String()),
    Key(
        "buffer_dewar_supply_status",
        Enum("open", "closed", "timeout", "disabled", "?"),
    ),
    Key("buffer_dewar_vent_status", Enum("open", "closed", "timeout", "disabled", "?")),
    Key("red_dewar_vent_status", Enum("open", "closed", "timeout", "disabled", "?")),
    Key("blue_dewar_vent_status", Enum("open", "closed", "timeout", "disabled", "?")),
    Key("time_next_fill", Int()),
    Key("max_valve_open_time", Int()),
    Key("fill_interval", Int()),
    Key("ln2_pressure", Int()),
    Key("buffer_dewar_thermistor_status", Enum("cold", "warm", "?")),
    Key("red_dewar_thermistor_status", Enum("cold", "warm", "?")),
    Key("blue_dewar_thermistor_status", Enum("cold", "warm", "?")),
    Key("fan", Enum("on", "off", "?")),
    Key("power_supply_volts", Float()),
    Key("filename", String()),
    Key("alive_at", Float(), help="UNIX time of the last time the actor was alive"),
    Key("b2_ccd_temp_alert", Bool("F", "T"), help="Alert on b2 CCD temperature"),
    Key("r2_ccd_temp_alert", Bool("F", "T"), help="Alert on r2 CCD temperature"),
    Key("b2_ln2_temp_alert", Bool("F", "T"), help="Alert on b2 LN2 temperature"),
    Key("r2_ln2_temp_alert", Bool("F", "T"), help="Alert on r2 LN2 temperature"),
)

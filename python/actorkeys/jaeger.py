#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2019-05-22
# @Filename: jaeger.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)
#
# @Last modified by: José Sánchez-Gallego
# @Last modified time: 2019-11-22 15:14:15

# type: ignore


KeysDictionary(
    "jaeger",
    (0, 1),
    Key("version", String(help="Actor version")),
    Key("text", String(help="Text for humans")),
    Key("schema", String(help="Schema definition")),
    Key("help", String(help="Help string")),
    Key("error", String(help="Error message")),
    Key("yourUserID", Int(help="User ID")),
    Key("UserInfo", Int(name="userID"), String(name="IP")),
    Key("num_users", Int(help="Number of users connected")),
    Key("kaiju_version", String(help="Kaiju version")),
    Key("coordio_version", String(help="coordIO version")),
    Key("fps_calibrations_version", String(help="calibrations version")),
    Key("folded", Bool("F", "T"), help="is the FPS folded?"),
    Key("locked", Bool("F", "T"), help="is the FPS locked?"),
    Key("locked_by", Int() * (2,), help="Which positioners locked the FPS?"),
    Key("engineering_mode", Bool("F", "T"), help="is the FPS in engineering mode?"),
    Key("alive_at", Float(), help="UNIX time of the last time the actor was alive"),
    Key("move_time", Float(), help="time the FPS will be moving"),
    Key("n_positioners", Int(), help="Number of connected positioners"),
    Key(
        "positioner_status",
        Int(name="positioner_id", help="the ID of the positioner"),
        Float(name="alpha", help="the angle of the alpha arm", units="degrees"),
        Float(name="beta", help="the angle of the beta arm", units="degrees"),
        String(name="status_bits", help="the status maskbit"),
        Bool("F", "T", name="initialised", help="is the positioner initialised?"),
        Bool("F", "T", name="disabled", help="is the positioner disabled?"),
        Bool("F", "T", name="offline", help="is the positioner offline?"),
        Bool("F", "T", name="bootloader", help="is the position in bootloader mode?"),
        String(name="firmware", help="the version of the firmware loaded"),
        Int(name="interface", help="the interface index"),
        Int(name="bus", help="the interface index"),
        Int(name="n_trajectories", help="number", invalid="?"),
    ),
    Key("raw", String(), help="The text of a raw command reply"),
    Key(
        "current",
        Int(name="alpha", help="alpha current"),
        Int(name="beta", help="alpha current"),
    ),
    Key("config_file", String(), help="the configuration file path"),
    Key("temperature", Float() * (0,), help="Temperature values"),
    Key("humidity", Float() * (0,), help="Humidity values"),
    Key("voltage", Float() * (6,), help="Voltage values"),
    Key("flow", Float() * (2,), help="Coolant flow values"),
    Key("pressure", Float() * (2,), help="Coolant pressure values"),
    Key("fbi_led", Float() * (2,), help="FBI LED percentage values"),
    Key("power_sextant", Bool("F", "T") * (6,), help="Power to sextants"),
    Key("power_can", Bool("F", "T") * (6,), help="Power to CAN modules"),
    Key("power_sync", Bool("F", "T"), help="Power to SYNC line"),
    Key("power_gfa", Bool("F", "T") * (6,), help="Power to GFAs"),
    Key("power_nuc", Bool("F", "T") * (6,), help="Power to GFA Nucs"),
    Key("fvc_temperature", Float() * (0,), help="FVC temperatures"),
    Key("fvc_power_nuc", Bool("F", "T"), help="Power to FVC NUC"),
    Key("fvc_power_camera", Bool("F", "T"), help="Power to FVC camera"),
    Key("fvc_led", Float(), help="FVC LED percentage value"),
    Key(
        "configuration_loaded",
        Int("configuration_id", help="Configuration ID"),
        Int("design_id", help="Design ID"),
        Int("field_id", help="Field ID"),
        Float("ra_boresight", help="RA of the boresight pointing"),
        Float("dec_boresight", help="Dec of the boresight pointing"),
        Float("position_angle", help="Position angle of the pointing"),
        Float("alt_boresight", help="Altitude of the boresight pointing"),
        Float("az_boresight", help="Azimuth of the boresight pointing"),
        String("summary_file", help="Summary file path"),
        Bool("F", "T", name="cloned", help="Is the configuration cloned?"),
    ),
    Key("fvc_filename", String()),
    Key("fvc_rms", Float(), help="FVC fit RMS"),
    Key("fvc_deltarms", Float(), help="FVC fit delta RMS"),
    Key("fvc_perc_90", Float(), help="FVC 90% percentile distance"),
    Key("fvc_percent_reached", Float(), help="% fibres that have reached their goal"),
    Key("fps_status", String(), help="FPS status bits."),
    Key("snapshot", String()),
    Key("trajectory_dump_file", String()),
    Key("configuration_snapshot", String()),
    Key("chiller_temperature_value", Float(units="celsius")),
    Key("chiller_temperature_setpoint", Float(units="celsius")),
    Key("chiller_flow_value", Float(units="gpm")),
    Key("chiller_flow_setpoint", Float(units="gpm")),
    Key("alert_gfa_temp_critical", Int(), help="GFA temperature is critical"),
    Key("alert_gfa_temp_warning", Int(), help="GFA temperature is serious"),
    Key("alert_ieb_temp_critical", Int(), help="IEB temperature is critical"),
    Key("alert_ieb_temp_warning", Int(), help="IEB temperature is critical"),
    Key("alert_robot_temp_critical", Int(), help="FPS robot temperature is critical"),
    Key("alert_robot_temp_warning", Int(), help="FPS robot temperature is serious"),
    Key("alert_fps_flow", Int(), help="FPS coolant flow rate is low"),
    Key("alert_dew_point", Int(), help="Outside temperature within dew point range"),
    Key("alert_chiller_fault", Int(), help="Fault reported by the chiller PLC"),
    Key(
        "alert_chiller_dew_point",
        Int(),
        help="Chiller temperature within dew point range",
    ),
    Key(
        "alert_fluid_temperature",
        Int(),
        help="Mismatch between chiller set point and FPS supply fluid temperature",
    ),
)

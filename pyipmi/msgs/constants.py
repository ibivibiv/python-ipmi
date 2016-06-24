# Copyright (c) 2014  Kontron Europe GmbH
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

# completion codes
CC_OK = 0x00
CC_NODE_BUSY = 0xc0
CC_INV_CMD = 0xc1
CC_INV_CMD_FOR_LUN = 0xc2
CC_TIMEOUT = 0xc3
CC_OUT_OF_SPACE = 0xc4
CC_RES_CANCELED = 0xc5
CC_REQ_DATA_TRUNC = 0xc6
CC_REQ_DATA_INV_LENGTH = 0xc7
CC_REQ_DATA_FIELD_EXCEED = 0xc8
CC_PARAM_OUT_OF_RANGE = 0xc9
CC_CANT_RET_NUM_REQ_BYTES = 0xca
CC_REQ_DATA_NOT_PRESENT = 0xcb
CC_INV_DATA_FIELD_IN_REQ = 0xcc
CC_ILL_SENSOR_OR_RECORD = 0xcd
CC_RESP_COULD_NOT_BE_PRV = 0xce
CC_CANT_RESP_DUPLI_REQ = 0xcf
CC_CANT_RESP_SDRR_UPDATE = 0xd0
CC_CANT_RESP_FIRM_UPDATE = 0xd1
CC_CANT_RESP_BMC_INIT = 0xd2
CC_DESTINATION_UNAVAILABLE = 0xd3
CC_INSUFFICIENT_PRIVILEGES = 0xd4
CC_NOT_SUPPORTED_PRESENT_STATE = 0xd5
CC_ILLEGAL_COMMAND_DISABLED = 0xd6
CC_UNSPECIFIED_ERROR = 0xff


cc_err_desc = (
    (CC_OK, 'Command Completed Normally'),
    (CC_NODE_BUSY, 'Node Busy'),
    (CC_INV_CMD, 'Invalid Command'),
    (CC_INV_CMD_FOR_LUN, 'Command invalid for given LUN'),
    (CC_TIMEOUT, 'Timeout while processing command'),
    (CC_OUT_OF_SPACE, 'Out of space'),
    (CC_RES_CANCELED, 'Reservation Canceled or Invalid Reservation ID'),
    (CC_REQ_DATA_TRUNC, 'Request data truncated'),
    (CC_REQ_DATA_INV_LENGTH, 'Request data length invalid'),
    (CC_REQ_DATA_FIELD_EXCEED, 'Request data field length limit exceeded'),
    (CC_PARAM_OUT_OF_RANGE, 'Parameter out of range'),
    (CC_CANT_RET_NUM_REQ_BYTES,
        'Cannot return number of requested data bytes'),
    (CC_REQ_DATA_NOT_PRESENT, 'Requested data not present'),
    (CC_INV_DATA_FIELD_IN_REQ, 'Invalid data field in Request'),
    (CC_ILL_SENSOR_OR_RECORD,
        'Command illegal for specified sensor or record'),
    (CC_RESP_COULD_NOT_BE_PRV, 'Command response could not be provided'),
    (CC_CANT_RESP_DUPLI_REQ, 'Cannot execute duplicated request'),
    (CC_CANT_RESP_SDRR_UPDATE,
        'Command response could not be provided. SDRR in update mode'),
    (CC_CANT_RESP_FIRM_UPDATE,
        'Command response could not be provided. Device in firmware '
        'update mode'),
    (CC_CANT_RESP_BMC_INIT,
        'Command response could not be provided. BMC initialization or '
        'initialization agent in progress'),
    (CC_DESTINATION_UNAVAILABLE, 'Destination unavailable'),
    (CC_INSUFFICIENT_PRIVILEGES,
        'Cannot execute command due to insufficient privilege level'),
    (CC_NOT_SUPPORTED_PRESENT_STATE,
        'Cannot execute command. Not supported in present state'),
    (CC_ILLEGAL_COMMAND_DISABLED,
        'Cannot execute command. Command sub-function has been disabled '
        'or is unavailable'),
    (CC_UNSPECIFIED_ERROR, 'Unspecified error'),
)


# network functions
NETFN_CHASSIS          = 0x00
NETFN_BRIDGE           = 0x02
NETFN_SENSOR_EVENT     = 0x04
NETFN_APP              = 0x06
NETFN_FIRMWARE         = 0x08
NETFN_STORAGE          = 0x0a
NETFN_TRANSPORT        = 0x0c
NETFN_GROUP_EXTENSION  = 0x2c
NETFN_OEM              = 0x2e

# IPM device 'global'
CMDID_GET_DEVICE_ID = 0x01
CMDID_COLD_RESET = 0x02
CMDID_WARM_RESET = 0x03
CMDID_GET_SELF_TEST_RESULTS = 0x04
CMDID_MANUFACTURING_TEST_ON = 0x05
CMDID_SET_ACPI_POWER_STATE = 0x06
CMDID_GET_ACPI_POWER_STATE = 0x07
CMDID_GET_DEVICE_GUID = 0x08
# BMC watchdog timer
CMDID_RESET_WATCHDOG_TIMER = 0x22
CMDID_SET_WATCHDOG_TIMER = 0x24
CMDID_GET_WATCHDOG_TIMER = 0x25
# BMC device and messaging
CMDID_SET_BMC_GLOBAL_ENABLES = 0x2e
CMDID_GET_BMC_GLOBAL_ENABLES = 0x2f
CMDID_CLEAR_MESSAGE_FLAGS = 0x30
CMDID_GET_MESSAGE_FLAGS = 0x31
CMDID_ENABLE_MESSAGE_CHANNEL_RECEIVE = 0x32
CMDID_GET_MESSAGE = 0x33
CMDID_SEND_MESSAGE = 0x34
CMDID_READ_EVENT_MESSAGE_BUFFER = 0x35
CMDID_GET_BT_INTERFACE_CAPABILITIES = 0x36
CMDID_GET_SYSTEM_GUID = 0x37
CMDID_GET_CHANNEL_AUTHENTICATION_CAPABILITIES = 0x38
CMDID_GET_SESSION_CHALLENGE = 0x39
CMDID_ACTIVATE_SESSION = 0x3a
CMDID_SET_SESSION_PRIVILEGE_LEVEL = 0x3b
CMDID_CLOSE_SESSION = 0x3c
CMDID_GET_SESSION_INFO = 0x3d
CMDID_GET_AUTHCODE = 0x3f
CMDID_SET_CHANNEL_ACCESS = 0x40
CMDID_GET_CHANNEL_ACCESS = 0x41
CMDID_GET_CHANNEL_INFO = 0x42
CMDID_SET_USER_ACCESS = 0x43
CMDID_GET_USER_ACCESS = 0x44
CMDID_SET_USER_NAME = 0x45
CMDID_GET_USER_NAME = 0x46
CMDID_SET_USER_PASSWORD = 0x47
CMDID_MASTER_WRITE_READ = 0x52
# chassis device
CMDID_GET_CHASSIS_CAPABILITIES = 0x00
CMDID_GET_CHASSIS_STATUS = 0x01
CMDID_CHASSIS_CONTROL = 0x02
CMDID_CHASSIS_RESET = 0x03
CMDID_CHASSIS_IDENTIFY = 0x04
CMDID_SET_CHASSIS_CAPABILITIES = 0x05
CMDID_SET_POWER_RESTORE_POLICY = 0x06
CMDID_GET_SYSTEM_RESTART_CAUSE = 0x07
CMDID_SET_SYSTEM_BOOT_OPTIONS = 0x08
CMDID_GET_SYSTEM_BOOT_OPTIONS = 0x09
CMDID_GET_POH_COUNTER = 0x0f
# event
CMDID_SET_EVENT_RECEIVER = 0x00
CMDID_GET_EVENT_RECEIVER = 0x01
CMDID_PLATFORM_EVENT = 0x02
# PEF and alerting
# sensor device
CMDID_GET_DEVICE_SDR_INFO = 0x20
CMDID_GET_DEVICE_SDR = 0x21
CMDID_RESERVE_DEVICE_SDR_REPOSITORY = 0x22
CMDID_GET_SENSOR_READING_FACTOR = 0x23
CMDID_SET_SENSOR_HYSTERESIS = 0x24
CMDID_GET_SENSOR_HYSTERESIS = 0x25
CMDID_SET_SENSOR_THRESHOLD = 0x26
CMDID_GET_SENSOR_THRESHOLD = 0x27
CMDID_SET_SENSOR_EVENT_ENABLE = 0x28
CMDID_GET_SENSOR_EVENT_ENABLE = 0x29
CMDID_RE_ARM_SENSOR = 0x2a
CMDID_GET_SENSOR_EVENT_STATUS = 0x2b
CMDID_GET_SENSOR_READING = 0x2d
CMDID_SET_SENSOR_TYPE = 0x2e
CMDID_GET_SENSOR_TYPE = 0x2f
# fru device
CMDID_GET_FRU_INVENTORY_AREA_INFO = 0x10
CMDID_READ_FRU_DATA = 0x11
CMDID_WRITE_FRU_DATA = 0x12
# SDR device
CMDID_GET_SDR_REPOSITORY_INFO = 0x20
CMDID_GET_SDR_REPOSITORY_ALLOCATION_INFO = 0x21
CMDID_RESERVE_SDR_REPOSITORY = 0x22
CMDID_GET_SDR = 0x23
CMDID_ADD_SDR = 0x24
CMDID_PARTIAL_ADD_SDR = 0x25
CMDID_DELETE_SDR = 0x26
CMDID_CLEAR_SDR_REPOSITORY = 0x27
CMDID_GET_SDR_REPOSITORY_TIME = 0x28
CMDID_SET_SDR_REPOSITORY_TIME = 0x29
CMDID_ENTER_SDR_REPOSITORY_UPDATE_MODE = 0x2a
CMDID_EXIT_SDR_REPOSITORY_UPDATE_MODE = 0x2b
CMDID_RUN_INITIALIZATION_AGENT = 0x2c
# SEL device
CMDID_GET_SEL_INFO = 0x40
CMDID_GET_SEL_ALLOCATION_INFO = 0x41
CMDID_RESERVE_SEL = 0x42
CMDID_GET_SEL_ENTRY = 0x43
CMDID_ADD_SEL_ENTRY = 0x44
CMDID_PARTIAL_ADD_SEL_ENTRY = 0x45
CMDID_DELETE_SEL_ENTRY = 0x46
CMDID_CLEAR_SEL = 0x47
CMDID_GET_SEL_TIME = 0x48
CMDID_SET_SEL_TIME = 0x49
CMDID_GET_AUXILIARY_LOG_STATUS = 0x5a
CMDID_SET_AUXILIARY_LOG_STATUS = 0x5b
# LAN device
CMDID_SET_LAN_CONFIGURATION_PARAMETERS = 0x01
CMDID_GET_LAN_CONFIGURATION_PARAMETERS = 0x02
CMDID_SUSPEND_BMC_ARPS = 0x03
CMDID_GET_IP_UDP_RMCP_STATISTICS = 0x04
# Serial/Modem device
# bridge management (ICMB)
# discovery (ICMB)
# bridging (ICMB)
# event (ICMB)
# other (ICMB)
# PICMG commands
CMDID_GET_PICMG_PROPERTIES = 0x00
CMDID_GET_ADDRESS_INFO = 0x01
CMDID_GET_SHELF_ADDRESS_INFO = 0x02
CMDID_SET_SHELF_ADDRESS_INFO = 0x03
CMDID_FRU_CONTROL = 0x04
CMDID_GET_FRU_LED_PROPERTIES = 0x05
CMDID_GET_FRU_LED_COLOR_CAPABILITIES = 0x06
CMDID_SET_FRU_LED_STATE = 0x07
CMDID_GET_FRU_LED_STATE = 0x08
CMDID_SET_IPMB_STATE = 0x09
CMDID_SET_FRU_ACTIVATION_POLICY = 0x0a
CMDID_GET_FRU_ACTIVATION_POLICY = 0x0b
CMDID_SET_FRU_ACTIVATION = 0x0c
CMDID_GET_DEVLOC_RECORD_ID = 0x0d
CMDID_SET_PORT_STATE = 0x0e
CMDID_GET_PORT_STATE = 0x0f
CMDID_COMPUTE_POWER_PROPERTIES = 0x10
CMDID_SET_POWER_LEVEL = 0x11
CMDID_GET_POWER_LEVEL = 0x12
CMDID_RENEGOTIATE_POWER = 0x13
CMDID_GET_FAN_SPEED_PROPERTIES = 0x14
CMDID_SET_FAN_LEVEL = 0x15
CMDID_GET_FAN_LEVEL = 0x16
CMDID_BUSED_RESOURCE = 0x17
CMDID_GET_IPMB_LINK_INFO = 0x18
CMDID_GET_SHELF_MANAGER_IPMB_ADDRESS = 0x1b
CMDID_SET_FAN_POLICY = 0x1c
CMDID_GET_FAN_POLICY = 0x1d
CMDID_FRU_CONTROL_CAPABILITIES = 0x1e
CMDID_FRU_INVENTORY_DEVICE_LOCK_CONTROL = 0x1f
CMDID_FRU_INVENTORY_DEVICE_WRITE = 0x20
CMDID_GET_SHELF_MANAGER_IP_ADDRESSES = 0x21
CMDID_GET_SHELF_POWER_ALLOCATION = 0x22
CMDID_SET_CHANNEL_SIGNALING_CLASS = 0x3b
CMDID_GET_CHANNEL_SIGNALING_CLASS = 0x3c
# AdvancedMC
CMDID_SET_AMC_PORT_STATE = 0x19
CMDID_GET_AMC_PORT_STATE = 0x1a
# MicroTCA
CMDID_GET_LOCATION_INFO = 0x23
CMDID_POWER_CHANNEL_CONTROL = 0x24
CMDID_GET_POWER_CHANNEL_STATUS = 0x25
CMDID_PM_RESET = 0x26
CMDID_GET_PM_STATUS = 0x27
CMDID_PM_HEARTBEAT = 0x28
CMDID_GET_TELCO_ALARM_CAPABILITY = 0x29
CMDID_SET_TELCO_ALARM_STATE = 0x2a
CMDID_GET_TELCO_ALARM_STATE = 0x2b

# HPM.1 commands
CMDID_HPM_GET_TARGET_UPGRADE_CAPABILITIES = 0x2e
CMDID_HPM_GET_COMPONENT_PROPERTIES = 0x2f
CMDID_HPM_ABORT_FIRMWARE_UPGRADE = 0x30
CMDID_HPM_INITIATE_UPGRADE_ACTION = 0x31
CMDID_HPM_UPLOAD_FIRMWARE_BLOCK = 0x32
CMDID_HPM_FINISH_FIRMWARE_UPLOAD = 0x33
CMDID_HPM_GET_UPGRADE_STATUS = 0x34
CMDID_HPM_ACTIVATE_FIRMWARE = 0x35
CMDID_HPM_QUERY_SELFTEST_RESULTS = 0x36
CMDID_HPM_QUERY_ROLLBACK_STATUS = 0x37
CMDID_HPM_INITIATE_MANUAL_ROLLBACK = 0x38

cc_err_cmd_specific_desc = {
    CMDID_GET_SESSION_CHALLENGE: {
        0x81: 'invalid user name',
        0x82: 'null user name (User 1) not enabled',
    },

    CMDID_ACTIVATE_SESSION: {
        0x81: 'No session slot available (BMC cannot accept any more'
                ' sessions)',
        0x82: 'No slot available for given user',
        0x83: 'No slot available to support user due to maximum privilege'
                ' capability',
        0x84: 'session sequence number out-of-range',
        0x85: 'invalid Session ID in request',
        0x86: 'requested maximum privilege level exceeds user and/or channel'
                ' privilege limit',
    },
}

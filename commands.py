class CMD:
    PING_CMD = 0
    FLASH_CMD = 1
    LED_ON_CMD = 2
    LED_OFF_CMD = 3
    RELAY1_ON_CMD = 4
    RELAY1_OFF_CMD = 5
    RELAY2_ON_CMD = 6
    RELAY2_OFF_CMD = 7
    READ_AN0_CMD = 8
    READ_AN1_CMD = 9
    READ_AN2_CMD = 10
    READ_AN3_CMD = 11
    READ_AN4_CMD = 12
    READ_AN5_CMD = 13
    READ_AN6_CMD = 14
    READ_AN7_CMD = 15
    READ_AN8_CMD = 16
    READ_AN9_CMD = 17
    READ_AN10_CMD = 18
    READ_AN11_CMD = 19
    READ_AN12_CMD = 20
    READ_AN13_CMD = 21
    READ_RA4_CMD = 22
    READ_P5_CMD = 23
    READ_P6_CMD = 24
    READ_P7_CMD = 25
    READ_RB7_CMD = 26
    READ_RB6_CMD = 27
    WRITE_AN0_LOW_CMD = 28
    WRITE_AN1_LOW_CMD = 29
    WRITE_AN2_LOW_CMD = 30
    WRITE_AN3_LOW_CMD = 31
    WRITE_AN4_LOW_CMD = 32
    WRITE_AN5_LOW_CMD = 33
    WRITE_AN6_LOW_CMD = 34
    WRITE_AN7_LOW_CMD = 35
    WRITE_AN8_LOW_CMD = 36
    WRITE_AN9_LOW_CMD = 37
    WRITE_AN10_LOW_CMD = 38
    WRITE_AN11_LOW_CMD = 39
    WRITE_AN12_LOW_CMD = 40
    WRITE_AN13_LOW_CMD = 41
    WRITE_RA4_LOW_CMD = 42
    WRITE_P5_LOW_CMD = 43
    WRITE_P6_LOW_CMD = 44
    WRITE_P7_LOW_CMD = 45
    WRITE_RB7_LOW_CMD = 46
    WRITE_RB6_LOW_CMD = 47
    WRITE_AN0_HIGH_CMD = 48
    WRITE_AN1_HIGH_CMD = 49
    WRITE_AN2_HIGH_CMD = 50
    WRITE_AN3_HIGH_CMD = 51
    WRITE_AN4_HIGH_CMD = 52
    WRITE_AN5_HIGH_CMD = 53
    WRITE_AN6_HIGH_CMD = 54
    WRITE_AN7_HIGH_CMD = 55
    WRITE_AN8_HIGH_CMD = 56
    WRITE_AN9_HIGH_CMD = 57
    WRITE_AN10_HIGH_CMD = 58
    WRITE_AN11_HIGH_CMD = 59
    WRITE_AN12_HIGH_CMD = 60
    WRITE_AN13_HIGH_CMD = 61
    WRITE_RA4_HIGH_CMD = 62
    WRITE_P5_HIGH_CMD = 63
    WRITE_P6_HIGH_CMD = 64
    WRITE_P7_HIGH_CMD = 65
    WRITE_RB7_HIGH_CMD = 66
    WRITE_RB6_HIGH_CMD = 67
    READ_AN0_ADC_CMD = 68
    READ_AN1_ADC_CMD = 69
    READ_AN2_ADC_CMD = 70
    READ_AN3_ADC_CMD = 71
    READ_AN4_ADC_CMD = 72
    READ_AN5_ADC_CMD = 73
    READ_AN6_ADC_CMD = 74
    READ_AN7_ADC_CMD = 75
    READ_AN8_ADC_CMD = 76
    READ_AN9_ADC_CMD = 77
    READ_AN10_ADC_CMD = 78
    READ_AN11_ADC_CMD = 79
    READ_AN12_ADC_CMD = 80
    READ_AN13_ADC_CMD = 81
    SET_INTERNAL_VOLTAGE_CMD = 82
    SET_EXTERNAL_VOLTAGE_CMD = 83
    MAX_CMD = 84

class DLP_CMD:
    PING = 0x27
    FLASH = 0x28
    LED = 0x29
    RELAY = 0x30
    DIGITAL_IO = 0x35
    ADC = 0x50
    SET_INTERNAL_VOLTAGE = 0x53
    SET_EXTERNAL_VOLTAGE = 0x54

class CHANNEL:
    AN0 = 0x00
    AN1 = 0x01
    AN2 = 0x02
    AN3 = 0x03
    AN4 = 0x04
    AN5 = 0x05
    AN6 = 0x06
    AN7 = 0x07
    AN8 = 0x08
    AN9 = 0x09
    AN10 = 0x0A
    AN11 = 0x0B
    AN12 = 0x0C
    AN13 = 0x0D
    RA4 = 0x0E
    P5 = 0x0F
    P6 = 0x10
    P7 = 0x11
    RB7 = 0x12
    RB6 = 0x13

class RELAY:
    ONE = 0x01
    TWO = 0x02

class OUT:
    LOW = 0
    HIGH = 1

class DIRECTION:
    OUT = 0
    IN = 1

cmd_functions = {
    CMD.PING_CMD : bytearray([0x02, DLP_CMD.PING]),
    CMD.FLASH_CMD : bytearray([0x02, DLP_CMD.FLASH]),
    CMD.LED_ON_CMD : bytearray([0x03, DLP_CMD.LED, OUT.LOW]),
    CMD.LED_OFF_CMD : bytearray([0x03, DLP_CMD.LED, OUT.HIGH]),
    CMD.RELAY1_ON_CMD : bytearray([0x04, DLP_CMD.RELAY, RELAY.ONE, OUT.LOW]),
    CMD.RELAY1_OFF_CMD : bytearray([0x04, DLP_CMD.RELAY, RELAY.ONE, OUT.HIGH]),
    CMD.RELAY2_ON_CMD : bytearray([0x04, DLP_CMD.RELAY, RELAY.TWO, OUT.LOW]),
    CMD.RELAY2_OFF_CMD : bytearray([0x04, DLP_CMD.RELAY, RELAY.TWO, OUT.HIGH]),
    CMD.READ_AN0_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN0, DIRECTION.IN, 0x00]),
    CMD.READ_AN1_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN1, DIRECTION.IN, 0x00]),
    CMD.READ_AN2_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN2, DIRECTION.IN, 0x00]),
    CMD.READ_AN3_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN3, DIRECTION.IN, 0x00]),
    CMD.READ_AN4_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN4, DIRECTION.IN, 0x00]),
    CMD.READ_AN5_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN5, DIRECTION.IN, 0x00]),
    CMD.READ_AN6_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN6, DIRECTION.IN, 0x00]),
    CMD.READ_AN7_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN7, DIRECTION.IN, 0x00]),
    CMD.READ_AN8_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN8, DIRECTION.IN, 0x00]),
    CMD.READ_AN9_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN9, DIRECTION.IN, 0x00]),
    CMD.READ_AN10_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN10, DIRECTION.IN, 0x00]),
    CMD.READ_AN11_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN11, DIRECTION.IN, 0x00]),
    CMD.READ_AN12_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN12, DIRECTION.IN, 0x00]),
    CMD.READ_AN13_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN13, DIRECTION.IN, 0x00]),
    CMD.READ_RA4_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.RA4, DIRECTION.IN, 0x00]),
    CMD.READ_P5_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.P5, DIRECTION.IN, 0x00]),
    CMD.READ_P6_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.P6, DIRECTION.IN, 0x00]),
    CMD.READ_P7_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.P7, DIRECTION.IN, 0x00]),
    CMD.READ_RB7_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.RB7, DIRECTION.IN, 0x00]),
    CMD.READ_RB6_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.RB6, DIRECTION.IN, 0x00]),
    CMD.WRITE_AN0_LOW_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN0, DIRECTION.OUT, OUT.LOW]),
    CMD.WRITE_AN1_LOW_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN1, DIRECTION.OUT, OUT.LOW]),
    CMD.WRITE_AN2_LOW_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN2, DIRECTION.OUT, OUT.LOW]),
    CMD.WRITE_AN3_LOW_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN3, DIRECTION.OUT, OUT.LOW]),
    CMD.WRITE_AN4_LOW_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN4, DIRECTION.OUT, OUT.LOW]),
    CMD.WRITE_AN5_LOW_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN5, DIRECTION.OUT, OUT.LOW]),
    CMD.WRITE_AN6_LOW_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN6, DIRECTION.OUT, OUT.LOW]),
    CMD.WRITE_AN7_LOW_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN7, DIRECTION.OUT, OUT.LOW]),
    CMD.WRITE_AN8_LOW_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN8, DIRECTION.OUT, OUT.LOW]),
    CMD.WRITE_AN9_LOW_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN9, DIRECTION.OUT, OUT.LOW]),
    CMD.WRITE_AN10_LOW_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN10, DIRECTION.OUT, OUT.LOW]),
    CMD.WRITE_AN11_LOW_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN11, DIRECTION.OUT, OUT.LOW]),
    CMD.WRITE_AN12_LOW_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN12, DIRECTION.OUT, OUT.LOW]),
    CMD.WRITE_AN13_LOW_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN13, DIRECTION.OUT, OUT.LOW]),
    CMD.WRITE_RA4_LOW_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.RA4, DIRECTION.OUT, OUT.LOW]),
    CMD.WRITE_P5_LOW_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.P5, DIRECTION.OUT, OUT.LOW]),
    CMD.WRITE_P6_LOW_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.P6, DIRECTION.OUT, OUT.LOW]),
    CMD.WRITE_P7_LOW_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.P7, DIRECTION.OUT, OUT.LOW]),
    CMD.WRITE_RB7_LOW_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.RB7, DIRECTION.OUT, OUT.LOW]),
    CMD.WRITE_RB6_LOW_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.RB6, DIRECTION.OUT, OUT.LOW]),
    CMD.WRITE_AN0_HIGH_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN0, DIRECTION.OUT, OUT.HIGH]),
    CMD.WRITE_AN1_HIGH_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN1, DIRECTION.OUT, OUT.HIGH]),
    CMD.WRITE_AN2_HIGH_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN2, DIRECTION.OUT, OUT.HIGH]),
    CMD.WRITE_AN3_HIGH_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN3, DIRECTION.OUT, OUT.HIGH]),
    CMD.WRITE_AN4_HIGH_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN4, DIRECTION.OUT, OUT.HIGH]),
    CMD.WRITE_AN5_HIGH_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN5, DIRECTION.OUT, OUT.HIGH]),
    CMD.WRITE_AN6_HIGH_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN6, DIRECTION.OUT, OUT.HIGH]),
    CMD.WRITE_AN7_HIGH_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN7, DIRECTION.OUT, OUT.HIGH]),
    CMD.WRITE_AN8_HIGH_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN8, DIRECTION.OUT, OUT.HIGH]),
    CMD.WRITE_AN9_HIGH_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN9, DIRECTION.OUT, OUT.HIGH]),
    CMD.WRITE_AN10_HIGH_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN10, DIRECTION.OUT, OUT.HIGH]),
    CMD.WRITE_AN11_HIGH_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN11, DIRECTION.OUT, OUT.HIGH]),
    CMD.WRITE_AN12_HIGH_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN12, DIRECTION.OUT, OUT.HIGH]),
    CMD.WRITE_AN13_HIGH_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.AN13, DIRECTION.OUT, OUT.HIGH]),
    CMD.WRITE_RA4_HIGH_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.RA4, DIRECTION.OUT, OUT.HIGH]),
    CMD.WRITE_P5_HIGH_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.P5, DIRECTION.OUT, OUT.HIGH]),
    CMD.WRITE_P6_HIGH_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.P6, DIRECTION.OUT, OUT.HIGH]),
    CMD.WRITE_P7_HIGH_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.P7, DIRECTION.OUT, OUT.HIGH]),
    CMD.WRITE_RB7_HIGH_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.RB7, DIRECTION.OUT, OUT.HIGH]),
    CMD.WRITE_RB6_HIGH_CMD : bytearray([0x05, DLP_CMD.DIGITAL_IO, CHANNEL.RB6, DIRECTION.OUT, OUT.HIGH]),
    CMD.READ_AN0_ADC_CMD : bytearray([0x03, DLP_CMD.ADC, CHANNEL.AN0]),
    CMD.READ_AN1_ADC_CMD : bytearray([0x03, DLP_CMD.ADC, CHANNEL.AN1]),
    CMD.READ_AN2_ADC_CMD : bytearray([0x03, DLP_CMD.ADC, CHANNEL.AN2]),
    CMD.READ_AN3_ADC_CMD : bytearray([0x03, DLP_CMD.ADC, CHANNEL.AN3]),
    CMD.READ_AN4_ADC_CMD : bytearray([0x03, DLP_CMD.ADC, CHANNEL.AN4]),
    CMD.READ_AN5_ADC_CMD : bytearray([0x03, DLP_CMD.ADC, CHANNEL.AN5]),
    CMD.READ_AN6_ADC_CMD : bytearray([0x03, DLP_CMD.ADC, CHANNEL.AN6]),
    CMD.READ_AN7_ADC_CMD : bytearray([0x03, DLP_CMD.ADC, CHANNEL.AN7]),
    CMD.READ_AN8_ADC_CMD : bytearray([0x03, DLP_CMD.ADC, CHANNEL.AN8]),
    CMD.READ_AN9_ADC_CMD : bytearray([0x03, DLP_CMD.ADC, CHANNEL.AN9]),
    CMD.READ_AN10_ADC_CMD : bytearray([0x03, DLP_CMD.ADC, CHANNEL.AN10]),
    CMD.READ_AN11_ADC_CMD : bytearray([0x03, DLP_CMD.ADC, CHANNEL.AN11]),
    CMD.READ_AN12_ADC_CMD : bytearray([0x03, DLP_CMD.ADC, CHANNEL.AN12]),
    CMD.READ_AN13_ADC_CMD : bytearray([0x03, DLP_CMD.ADC, CHANNEL.AN13]),
    CMD.SET_INTERNAL_VOLTAGE_CMD : bytearray([0x02, DLP_CMD.SET_INTERNAL_VOLTAGE]),
    CMD.SET_EXTERNAL_VOLTAGE_CMD : bytearray([0x02, DLP_CMD.SET_EXTERNAL_VOLTAGE])
}


# read digital IO command start from 8 and finish at 27
# write digital IO low command start from 28 and finish at 47
# write digital IO high command start from 48 and finish at 67


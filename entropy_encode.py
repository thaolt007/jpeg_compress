# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 22:23:01 2016

@author: dieuhau
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time-stamp: < entropy_encode.py 2016-05-16 17:11:14 >

AC_MODE = True
FORWARD = True

#################
huffman_AC_luminance_table_forward = (
	"1010",
	"00",
	"01",
	"100",
	"1011",
	"11010",
	"1111000",
	"11111000",
	"1111110110",
	"1111111110000010",
	"1111111110000011",
	"1100",
	"11011",
	"1111001",
	"111110110",
	"11111110110",
	"1111111110000100",
	"1111111110000101",
	"1111111110000110",
	"1111111110000111",
	"1111111110001000",
	"11100",
	"11111001",
	"1111110111",
	"111111110100",
	"1111111110001001",
	"1111111110001010",
	"1111111110001011",
	"1111111110001100",
	"1111111110001101",
	"1111111110001110",
	"111010",
	"111110111",
	"111111110101",
	"1111111110001111",
	"1111111110010000",
	"1111111110010001",
	"1111111110010010",
	"1111111110010011",
	"1111111110010100",
	"1111111110010101",
	"111011",
	"1111111000",
	"1111111110010110",
	"1111111110010111",
	"1111111110011000",
	"1111111110011001",
	"1111111110011010",
	"1111111110011011",
	"1111111110011100",
	"1111111110011101",
	"1111010",
	"11111110111",
	"1111111110011110",
	"1111111110011111",
	"1111111110100000",
	"1111111110100001",
	"1111111110100010",
	"1111111110100011",
	"1111111110100100",
	"1111111110100101",
	"1111011",
	"111111110110",
	"1111111110100110",
	"1111111110100111",
	"1111111110101000",
	"1111111110101001",
	"1111111110101010",
	"1111111110101011",
	"1111111110101100",
	"1111111110101101",
	"11111010",
	"111111110111",
	"1111111110101110",
	"1111111110101111",
	"1111111110110000",
	"1111111110110001",
	"1111111110110010",
	"1111111110110011",
	"1111111110110100",
	"1111111110110101",
	"111111000",
	"111111111000000",
	"1111111110110110",
	"1111111110110111",
	"1111111110111000",
	"1111111110111001",
	"1111111110111010",
	"1111111110111011",
	"1111111110111100",
	"1111111110111101",
	"111111001",
	"1111111110111110",
	"1111111110111111",
	"1111111111000000",
	"1111111111000001",
	"1111111111000010",
	"1111111111000011",
	"1111111111000100",
	"1111111111000101",
	"1111111111000110",
	"111111010",
	"1111111111000111",
	"1111111111001000",
	"1111111111001001",
	"1111111111001010",
	"1111111111001011",
	"1111111111001100",
	"1111111111001101",
	"1111111111001110",
	"1111111111001111",
	"1111111001",
	"1111111111010000",
	"1111111111010001",
	"1111111111010010",
	"1111111111010011",
	"1111111111010100",
	"1111111111010101",
	"1111111111010110",
	"1111111111010111",
	"1111111111011000",
	"1111111010",
	"1111111111011001",
	"1111111111011010",
	"1111111111011011",
	"1111111111011100",
	"1111111111011101",
	"1111111111011110",
	"1111111111011111",
	"1111111111100000",
	"1111111111100001",
	"11111111000",
	"1111111111100010",
	"1111111111100011",
	"1111111111100100",
	"1111111111100101",
	"1111111111100110",
	"1111111111100111",
	"1111111111101000",
	"1111111111101001",
	"1111111111101010",
	"1111111111101011",
	"1111111111101100",
	"1111111111101101",
	"1111111111101110",
	"1111111111101111",
	"1111111111110000",
	"1111111111110001",
	"1111111111110010",
	"1111111111110011",
	"1111111111110100",
	##################
	"11111111001",
	"1111111111110101",
	"1111111111110110",
	"1111111111110111",
	"1111111111111000",
	"1111111111111001",
	"1111111111111010",
	"1111111111111011",
	"1111111111111100",
	"1111111111111101",
	"1111111111111110"
)

huffman_AC_luminance_table_backward = {
	"1010" : 0,
	"00" : 1,
	"01" : 2,
	"100" : 3,
	"1011" : 4,
	"11010" : 5,
	"1111000" : 6,
	"11111000" : 7,
	"1111110110" : 8,
	"1111111110000010" : 9,
	"1111111110000011" : 10,
	"1100" : 11,
	"11011" : 12,
	"1111001" : 13,
	"111110110" : 14,
	"11111110110" : 15,
	"1111111110000100" : 16,
	"1111111110000101" : 17,
	"1111111110000110" : 18,
	"1111111110000111" : 19,
	"1111111110001000" : 20,
	"11100" : 21,
	"11111001" : 22,
	"1111110111" : 23,
	"111111110100" : 24,
	"1111111110001001" : 25,
	"1111111110001010" : 26,
	"1111111110001011" : 27,
	"1111111110001100" : 28,
	"1111111110001101" : 29,
	"1111111110001110" : 30,
	"111010" : 31,
	"111110111" : 32,
	"111111110101" : 33,
	"1111111110001111" : 34,
	"1111111110010000" : 35,
	"1111111110010001" : 36,
	"1111111110010010" : 37,
	"1111111110010011" : 38,
	"1111111110010100" : 39,
	"1111111110010101" : 40,
	"111011" : 41,
	"1111111000" : 42,
	"1111111110010110" : 43,
	"1111111110010111" : 44,
	"1111111110011000" : 45,
	"1111111110011001" : 46,
	"1111111110011010" : 47,
	"1111111110011011" : 48,
	"1111111110011100" : 49,
	"1111111110011101" : 50,
	"1111010" : 51,
	"11111110111" : 52,
	"1111111110011110" : 53,
	"1111111110011111" : 54,
	"1111111110100000" : 55,
	"1111111110100001" : 56,
	"1111111110100010" : 57,
	"1111111110100011" : 58,
	"1111111110100100" : 59,
	"1111111110100101" : 60,
	"1111011" : 61,
	"111111110110" : 62,
	"1111111110100110" : 63,
	"1111111110100111" : 64,
	"1111111110101000" : 65,
	"1111111110101001" : 66,
	"1111111110101010" : 67,
	"1111111110101011" : 68,
	"1111111110101100" : 69,
	"1111111110101101" : 70,
	"11111010" : 71,
	"111111110111" : 72,
	"1111111110101110" : 73,
	"1111111110101111" : 74,
	"1111111110110000" : 75,
	"1111111110110001" : 76,
	"1111111110110010" : 77,
	"1111111110110011" : 78,
	"1111111110110100" : 79,
	"1111111110110101" : 80,
	"111111000" : 81,
	"111111111000000" : 82,
	"1111111110110110" : 83,
	"1111111110110111" : 84,
	"1111111110111000" : 85,
	"1111111110111001" : 86,
	"1111111110111010" : 87,
	"1111111110111011" : 88,
	"1111111110111100" : 89,
	"1111111110111101" : 90,
	"111111001" : 91,
	"1111111110111110" : 92,
	"1111111110111111" : 93,
	"1111111111000000" : 94,
	"1111111111000001" : 95,
	"1111111111000010" : 96,
	"1111111111000011" : 97,
	"1111111111000100" : 98,
	"1111111111000101" : 99,
	"1111111111000110" : 100,
	"111111010" : 101,
	"1111111111000111" : 102,
	"1111111111001000" : 103,
	"1111111111001001" : 104,
	"1111111111001010" : 105,
	"1111111111001011" : 106,
	"1111111111001100" : 107,
	"1111111111001101" : 108,
	"1111111111001110" : 109,
	"1111111111001111" : 110,
	"1111111001" : 111,
	"1111111111010000" : 112,
	"1111111111010001" : 113,
	"1111111111010010" : 114,
	"1111111111010011" : 115,
	"1111111111010100" : 116,
	"1111111111010101" : 117,
	"1111111111010110" : 118,
	"1111111111010111" : 119,
	"1111111111011000" : 120,
	"1111111010" : 121,
	"1111111111011001" : 122,
	"1111111111011010" : 123,
	"1111111111011011" : 124,
	"1111111111011100" : 125,
	"1111111111011101" : 126,
	"1111111111011110" : 127,
	"1111111111011111" : 128,
	"1111111111100000" : 129,
	"1111111111100001" : 130,
	"11111111000" : 131,
	"1111111111100010" : 132,
	"1111111111100011" : 133,
	"1111111111100100" : 134,
	"1111111111100101" : 135,
	"1111111111100110" : 136,
	"1111111111100111" : 137,
	"1111111111101000" : 138,
	"1111111111101001" : 139,
	"1111111111101010" : 140,
	"1111111111101011" : 141,
	"1111111111101100" : 142,
	"1111111111101101" : 143,
	"1111111111101110" : 144,
	"1111111111101111" : 145,
	"1111111111110000" : 146,
	"1111111111110001" : 147,
	"1111111111110010" : 148,
	"1111111111110011" : 149,
	"1111111111110100" : 150,
	# Run Zeros Length #
	"11111111001" : 151,
###############################
	"1111111111110101" : 152,
	"1111111111110110" : 153,
	"1111111111110111" : 154,
	"1111111111111000" : 155,
	"1111111111111001" : 156,
	"1111111111111010" : 157,
	"1111111111111011" : 158,
	"1111111111111100" : 159,
	"1111111111111101" : 160,
	"1111111111111110" : 161
}
huffman_DC_luminance_table_forward = (
	"00",
	"010",
	"011",
	"100",
	"101",
	"110",
	"1110",
	"11110",
	"111110",
	"1111110",
	"11111110",
	"111111110"
)

huffman_DC_luminance_table_backward = {
	"00":0,
	"010":1,
	"011":2,
	"100":3,
	"101":4,
	"110":5,
	"1110":6,
	"11110":7,
	"111110":8,
	"1111110":9,
	"11111110":10,
	"111111110":11
}

#String binary from input number
def calc_amplitude(input_num, need_bit, mode = AC_MODE):
	##############
	if mode is not AC_MODE and input_num == 0:
		return "0"
	else:
		num = abs(input_num) & 0xffff
		index = 0
		output_string = ""
		###############
		if  input_num >= 0:
			while index < need_bit:
				this_bit = "1" if ((num >> index) & 0x1) else "0"
				output_string = this_bit + output_string
				index += 1
		###############
		else:
			while index < need_bit:
				this_bit = "0" if ((num >> index) & 0x1) else "1"
				output_string = this_bit + output_string
				index += 1

		return output_string

# Huffman encode for RLE => (010, 1010)
def get_entropy_encode(input_list):
	output_list = []

	for block in input_list:
		# DC
		dc_bit = block[0][0]
              
		# DC with 2 element
		if len(block[0]) != 1:
			dc_amp = block[0][1]
			# Binary
			(dc_bit, dc_amp) = (huffman_DC_luminance_table_forward[dc_bit], calc_amplitude(dc_amp, dc_bit, "DC"))
			insert_item = (dc_bit, dc_amp)
		else:
			dc_bit = huffman_DC_luminance_table_forward[dc_bit]
			insert_item = (dc_bit,)
		output_list.append(insert_item)

		# AC
		for ac_item in block[1:]:
			if len(ac_item) == 2:
				# RZL
				if ac_item[0] == 15 and ac_item[1] == 0:
					insert_item = ('11111111001',)
					output_list.append(insert_item)
				# EOB
				elif ac_item[0] == 0 and ac_item[1] == 0:
					insert_item = ("1010",)
					output_list.append(insert_item)
			# AC with 3 element
			else:
				ac_zero_counter = ac_item[0]
				ac_bit = ac_item[1]
    
				#################
				position_in_huffman_table = ac_zero_counter * 10 + ac_bit
				ac_amp = ac_item[2]
				ac_amp = calc_amplitude(ac_amp, ac_bit)
				
				#################
				if ac_zero_counter == 15:
					position_in_huffman_table += 1
				
				#################
				coefficient = huffman_AC_luminance_table_forward[position_in_huffman_table]
				insert_item = (coefficient, ac_amp)
				output_list.append(insert_item)

	return output_list

#Entropy code to string binary
def get_string_bin(input_list):
	buffer = ''
	for i in input_list:
		if len(i) == 1:
			buffer += i[0]
		else:
			buffer += (i[0] + i[1])
		
	return buffer
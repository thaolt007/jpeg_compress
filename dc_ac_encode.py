# calculate number bits binary of number
def calc_need_bits(input_num):
	num = abs(input_num)
 
	if num == 0:
		return 0
	returnValue = 1
	num += 1
	while True:
		if (1 << returnValue) >= num:
			break
		returnValue += 1
	return returnValue


#DPCM element DC of block => (need_bit, DC_value - previous_DC_value)
def dc_encode(this_DC_value, previous_DC_value):
	delta_DC = this_DC_value - previous_DC_value
	if delta_DC != 0:
		need_bit = calc_need_bits(delta_DC)
		return (need_bit, delta_DC)
	else:
		return (0,)

#RLE for another AC in block => (zero_counter, calc_need_bits(num_ac), num_ac)
def ac_encode(input_list):
    length = len(input_list)
    if length == 0:
        return (0, 0)
    else:
        lite_list = input_list[:]
    output_list = []
  
    # remove 0
    while(length > 0 and lite_list[-1] == 0):
        lite_list.pop()
        length = len(lite_list)
    length = len(lite_list)
    # run length encode
    index = 0
    while(index < length):
        zero_counter = 0
   
        while(lite_list[index] == 0 and zero_counter < 15):
           zero_counter += 1
           index += 1
        
        current_num = lite_list[index]
        if current_num != 0:
           this_round = [zero_counter, calc_need_bits(current_num), current_num]
        else:
           # RZL
           this_round = [15, 0]

        output_list.append( tuple(this_round) )
        index += 1
    return output_list

# Block encode rle
def dc_ac_encode(input_list, previous_DC_value):
    output_list = []
    dc = dc_encode(input_list[0], previous_DC_value)
    if len(dc) == 2:
        dc_value = (dc[0], dc[1])
    else:
        dc_value = (dc[0],)
    output_list.append(dc_value)
    
    ac_values = ac_encode(input_list[1:])
    counter = 1
    for ac_value in ac_values:
        counter += (ac_value[0] + 1)
        output_list.append(ac_value)
    if counter < 64:
        EOB = (0, 0)
        output_list.append(EOB)
    elif counter > 64:
        print "DC AC encode ERROR"
    return output_list
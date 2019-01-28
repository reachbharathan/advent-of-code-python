def final_frequency(inputList):
    result = 0
    count = 1
    for x in inputList:
        count += 1
        result = result + x
    return result

input = [-14,+15,+9,+19,+18,+14,+14,-18,+15,+4,-18,-20,-2,+17,+16,-7,-3,+5,+1,-5,-11,-1,-6,-20,+1,+1,+4,+18,+5,-20,-10,+18,+5,-4,-5,-18,+9,+6,+1,-19,+13,+10,-22,-11,-14,-17,-10,-1,-13,+6,-17,+9,-11,-6,+3,-14,+4,-14,+15,+7,+15,-1,-4,+9,+10,+6,-9,+8,+3,+10,-14,+8,+22,+19,-15,+10,-6,+9,-4,+2,+11,-15,+14,+11,-14,+2,+7,+9,-22,-6,-3,-21,+10,+5,-20,+19,-3,-13,+5,-16,+12,+10,-12,-4,+12,+2,-1,-4,-8,-6,-3,-8,-8,+7,-10,-20,-12,-6,-17,+2,+20,+7,-17,-14,-8,+3,+11,+15,-4,-10,-16,-3,-19,-6,-3,-9,-16,-7,-16,-12,+11,-13,-6,+13,+4,-7,-3,+5,+12,+4,-19,-19,+7,+1,-7,-12,-7,-5,-17,+18,+3,+10,+15,-12,-8,+17,+9,+19,+4,+16,-11,+10,-6,-7,+6,+6,+19,+3,+8,-2,+12,+19,-17,+7,-2,-10,-16,-11,-1,-2,-17,-7,+22,+3,+8,+11,-12,-4,+3,+19,-16,+18,-12,-17,-8,+5,-11,+7,-12,-23,-2,+14,+8,+9,+3,+29,+16,-15,-2,-12,+24,+14,+2,+4,-2,+18,-9,-18,+8,-9,+4,+7,+19,+7,+10,-9,-14,-6,+5,+17,-14,+7,+2,-1,+11,+18,-2,-6,+19,-15,-18,-5,+12,+21,+2,+2,-5,+10,+8,-10,+1,-17,+6,+21,+18,-17,+7,-5,+43,-4,+50,-4,+9,+16,-12,+9,+10,-21,+3,+25,-9,+18,+17,-19,+5,+16,-8,-17,+16,+21,-16,+6,+12,-9,+19,-7,+4,-8,+7,+18,+17,-7,+11,+21,-6,+4,-17,-19,+18,+13,-17,+2,+4,-8,+9,+22,+2,+5,+13,+6,+3,-28,-17,-17,-6,+19,-16,-19,+11,-7,+6,-17,+3,-4,-7,-6,+10,+17,-7,-4,+2,+8,-7,-25,+15,-10,-18,-10,-10,-11,-11,+14,+14,-3,+21,+10,-11,+6,+11,+21,-25,-9,-14,+2,+16,-27,+4,-7,+6,-11,+29,+21,+21,+6,-10,+14,+17,+6,-13,+32,-23,+17,-1,+12,-6,-11,+27,-5,+19,-2,-21,-42,-21,+19,-64,+20,-38,+42,-23,+1,-29,+26,-4,+57,+6,-1,+31,+107,-9,+5,+19,-12,+20,-1,+30,+1,+2,-47,-38,+5,+13,+121,+69,-60,+57143,-13,-3,+13,+15,+1,-19,-11,+2,-14,+4,+15,+8,-7,+16,+3,-5,-16,+17,-18,+5,-7,+17,+11,+12,-2,+16,-17,+6,+12,-9,-16,-5,+9,+18,+15,-19,+16,+16,-9,+5,-18,+19,-17,-18,+9,+11,+7,-3,-7,-6,+3,-17,-4,+6,+4,+2,+10,-13,-21,+10,-17,+15,+1,-10,-13,+20,-14,+21,+13,+16,+5,+4,+19,+9,+12,+4,-10,+14,-6,+17,-9,-14,+3,+16,+6,+13,+6,-15,+14,+11,-1,+8,-4,+11,+5,-7,-19,-2,+14,+18,-14,+2,+18,+16,-3,+16,+7,+1,-12,-5,-18,+8,+11,-7,-8,-19,+14,-10,-7,+4,+9,-18,-2,+19,+21,+9,+1,-9,+4,-3,+4,-11,-17,+10,-2,+6,-20,+3,+15,+4,+19,+19,-14,+3,+1,+4,+12,+11,-8,+12,+18,-14,+2,-4,+19,-1,+4,+15,+13,+16,+7,-12,+10,-13,-3,-17,+19,-16,+5,-20,-15,+3,+18,+4,+3,+3,+14,-12,+8,+11,+7,+10,+13,-7,+5,-19,+12,-3,+18,-9,+7,+1,+18,+17,-6,+1,-15,+10,-5,-10,-6,+18,+16,+6,+5,-10,-8,-5,+7,-1,-4,+17,+1,+4,-8,+1,+11,-13,-18,-14,+5,+3,+19,+12,+8,-3,+5,-24,+3,-10,-20,-1,+10,-19,+6,+8,-3,-10,+15,-8,+14,-17,-17,+4,+1,-12,+13,-11,+4,+12,-25,-1,-8,+14,-23,-21,+17,-20,+2,-5,-1,+12,-10,+3,+17,+4,-15,+20,-1,+9,+23,-20,-22,-12,-10,-15,+11,-35,-12,-14,+16,-10,-19,+26,+12,+16,-8,-15,+19,+3,-12,-16,+10,+2,-1,+13,-7,+2,+12,+9,-1,+2,-21,+3,-1,+13,+7,+2,+3,+18,-32,+4,+43,+19,-3,-5,+20,-2,-2,+17,+61,+2,-5,+23,-3,+8,-12,+55,+12,+12,+6,+20,-6,+7,+15,+3,+11,+8,-4,-9,-19,-13,-4,+6,-10,-9,-5,-4,+11,+5,+15,-14,+2,+6,-22,+2,+18,-11,-2,-4,-16,-5,+12,+4,+20,+8,+18,-6,+15,+17,-11,+16,-13,-12,+1,-9,+3,+16,+4,+19,+9,-8,-7,-12,+11,+21,-11,-16,+8,+1,+25,+15,-9,-42,+12,-18,-6,-10,-8,-5,-23,-20,+14,+12,+23,+120,+19,-43,+9,-1,-1,-33,+6,+43,-103,-187,+9,+3,-82,-20,-7,+125,+72,+613,+56596,-18,-19,+12,-11,-19,+1,+19,-18,-6,-3,+16,-2,-10,-9,-13,-15,+16,+5,-15,+7,-8,-17,+7,-16,+14,+14,-15,+4,-15,-10,-9,+12,-15,+5,-1,+13,-15,-3,-19,+1,-6,-19,-19,+23,-25,-28,-10,-3,-21,-13,-14,+11,+18,-13,+1,-16,+14,+15,+5,-7,+10,+2,-14,+10,+11,+11,-6,-7,-4,+14,-12,-6,-3,-15,-10,-13,-17,+3,+2,+8,+18,-4,-11,+2,-12,+13,-9,+14,+17,+12,+1,-12,-14,+6,+5,-13,+20,-13,-22,+3,+15,+14,+17,+7,-22,-22,-14,-2,-20,+15,-3,-8,+13,+40,+72,-21,+25,-16,+11,+22,+22,+25,+16,+15,+15,+9,+12,-10,+9,+11,-1,+10,-16,+17,+8,-7,-17,+4,-11,+20,+10,+7,+6,-7,+8,-19,+23,+7,-1,-2,+17,-9,-3,+2,-10,-10,-23,+17,+7,+10,+6,+14,+12,-1,+3,-7,-3,+16,-11,+17,-7,-1,-3,-12,-114806]

print("result is ")
print(final_frequency(input))

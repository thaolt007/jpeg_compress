import matplotlib.image as mpimg
import numpy as np
from scipy.fftpack import dct
import entropy_encode as entropy
import dc_ac_encode
import zigzag as zz

#Quantization table
qt = [[16,11,10,16,24,40,51,61]
      ,[12,12,14,19,26,58,60,55]
      ,[14,13,16,24,40,57,69,56]
      ,[14,17,22,29,51,87,80,62]
      ,[18,22,37,56,68,109,103,77]
      ,[24,35,55,64,81,104,113,92]
      ,[49,64,78,87,103,121,120,101]
      ,[72,92,95,98,112,110,103,99]]

#YUV DCT Quantize Zigzag RLE block 8x8
def compress88(img, r, c, DC_value):
    
    #YUV
    y = np.zeros((8,8), dtype=np.int)
    u = np.zeros((8,8), dtype=np.int)
    v = np.zeros((8,8), dtype=np.int)
    
    for i in range(8):
        for j in range(8):
            
            k = img[r+i][c+j][0]
            l = img[r+i][c+j][1]
            m = img[r+i][c+j][2]
            y[i][j] =  0.299*k + 0.587*l + 0.114*m -128
            u[i][j] = -0.147*k - 0.289*l + 0.436*m -128
            v[i][j] =  0.615*k - 0.515*l + 0.100*m -128
            
    #DCT
    y = (dct(dct(y.T,norm='ortho').T)).astype(np.int)
    u = (dct(dct(u.T,norm='ortho').T)).astype(np.int)
    v = (dct(dct(v.T,norm='ortho').T)).astype(np.int)

    #Quant
    for i in range(8):
        for j in range(8):
            y[i][j] = y[i][j] / qt[i][j]
            u[i][j] = u[i][j] / qt[i][j]
            v[i][j] = v[i][j] / qt[i][j]

    
    #Zigzag
    previous_DC_value = []
    output = []
    y_zz =  zz.get_zigzag(y)
    u_zz =  zz.get_zigzag(u)
    v_zz =  zz.get_zigzag(v)
    
    previous_DC_value.append(y_zz[0])
    previous_DC_value.append(u_zz[0])
    previous_DC_value.append(v_zz[0])
    
    #RLE
    output.append( dc_ac_encode.dc_ac_encode(y_zz,DC_value[0]) )
    output.append( dc_ac_encode.dc_ac_encode(u_zz,DC_value[0]) )
    output.append( dc_ac_encode.dc_ac_encode(v_zz,DC_value[0]) )
    return output, previous_DC_value
    
#Compress all
def compressall(img):
    numrows = len(img)
    numcols = len(img[0])
#    print "", numrows, numcols
    entropy_encoded  = []
    dc_ac_encodedY= []
    dc_ac_encodedU= []
    dc_ac_encodedV= []
    string_bin = []
    DC_value = [0,0,0]
    r = 0
    block_num = 0
    while ((r < numrows) & ((numrows-r) >= 8)):
        c = 0
        while ((c < numcols) & ((numcols-c) >= 8)):
            dc_ac, previous_DC_value = compress88(img, r, c, DC_value)
            
            dc_ac_encodedY.append(dc_ac[0])
            dc_ac_encodedU.append(dc_ac[1])
            dc_ac_encodedV.append(dc_ac[2])
            c += 8
            block_num += 1
        r += 8
        
    entropy_encoded.append( entropy.get_entropy_encode(dc_ac_encodedY) )
    entropy_encoded.append( entropy.get_entropy_encode(dc_ac_encodedU) )
    entropy_encoded.append( entropy.get_entropy_encode(dc_ac_encodedV) )
    

    string_bin.append( entropy.get_string_bin(entropy_encoded[0]) )
    string_bin.append( entropy.get_string_bin(entropy_encoded[1]) )
    string_bin.append( entropy.get_string_bin(entropy_encoded[2]) )

############################## 
#    outfile = 'Output.txt'
#    fd = open(outfile, 'wb')
#    fd.write(string_bin[0])
#    fd.write(string_bin[1])
#    fd.write(string_bin[2])
#    fd.close()
    
    len_bin = len(string_bin[0] + string_bin[1] + string_bin[2])
    print "", numrows, numcols
    print len_bin, "bits"
    
def main():
    img=mpimg.imread('lena.ppm')
    compressall(img)

if __name__ == "__main__":
    main()

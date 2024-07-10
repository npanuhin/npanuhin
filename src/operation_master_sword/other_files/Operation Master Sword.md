Microsoft Windows [Version 10.0.19045.2486]
(c) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.

C:\Users\panuhin>cd Desktop

C:\Users\panuhin\Desktop>magick version1.gif version1_frames/%05d.png

C:\Users\panuhin\Desktop>magick OptimizeFrame_RemoveDups.gif OptimizeFrame_RemoveDups_frames/%05d.png

C:\Users\panuhin\Desktop>magick version1.gif --coalesce pure.gif
magick: unable to open image '--coalesce': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: no decode delegate for this image format `' @ error/constitute.c/ReadImage/741.

C:\Users\panuhin\Desktop>magick --coalesce version1.gif pure.gif
magick: unable to open image '--coalesce': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: no decode delegate for this image format `' @ error/constitute.c/ReadImage/741.

C:\Users\panuhin\Desktop>magick version1.gif -coalesce pure.gif

C:\Users\panuhin\Desktop>magick version1.gif -coalesce pure-frames/%05d.png
magick: unable to open image 'pure-frames/00000.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00000.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00001.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00001.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00002.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00002.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00003.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00003.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00004.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00004.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00005.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00005.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00006.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00006.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00007.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00007.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00008.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00008.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00009.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00009.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00010.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00010.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00011.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00011.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00012.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00012.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00013.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00013.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00014.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00014.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00015.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00015.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00016.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00016.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00017.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00017.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00018.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00018.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00019.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00019.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00020.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00020.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00021.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00021.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00022.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00022.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00023.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00023.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00024.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00024.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00025.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00025.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00026.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00026.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00027.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00027.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00028.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00028.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00029.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00029.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00030.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00030.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: unable to open image 'pure-frames/00031.png': No such file or directory @ error/blob.c/OpenBlob/3569.
magick: WriteBlob Failed `pure-frames/00031.png' @ error/png.c/MagickPNGErrorHandler/1492.
magick: TooManyExceptions (exception processing is suspended) @ warning/exception.c/ThrowException/1046.
magick: unable to open image 'pure-frames/00032.png': No such file or directory @ error/blob.c/OpenBlob/3569.

C:\Users\panuhin\Desktop>magick version1.gif -coalesce pure_frames/%05d.png

C:\Users\panuhin\Desktop>magick -fuzz 99% version1.gif -coalesce -layers OptimizePlus OptimizePlus.gif

C:\Users\panuhin\Desktop>

C:\Users\panuhin\Desktop>magick -fuzz 99% pure_frames

C:\Users\panuhin\Desktop>magick -fuzz 99% pure_frames/*.png -coalesce -layers OptimizePlus OptimizePlus.gif

C:\Users\panuhin\Desktop>

C:\Users\panuhin\Desktop>magick -fuzz 99% pure_frames/*.png -layers OptimizePlus OptimizePlus.gif

C:\Users\panuhin\Desktop>
C:\Users\panuhin\Desktop>
C:\Users\panuhin\Desktop>
C:\Users\panuhin\Desktop>
C:\Users\panuhin\Desktop>
C:\Users\panuhin\Desktop>magick -fuzz 99% pure_frames/*.png -layers OptimizePlus OptimizePlus_frames/%05d.png

C:\Users\panuhin\Desktop>magick -fuzz 99% pure_frames/*.png -delay 2 -layers OptimizePlus OptimizePlus.gif

C:\Users\panuhin\Desktop>magick -fuzz 99% pure_frames/*.png -delay 1 -layers OptimizePlus OptimizePlus.gif

C:\Users\panuhin\Desktop>magick -fuzz 99% pure_frames/*.png -layers OptimizePlus -delay 1 OptimizePlus.gif

C:\Users\panuhin\Desktop>

C:\Users\panuhin\Desktop>magick -fuzz 99% pure_frames/*.png -layers OptimizePlus -delay 1 -loop 0 OptimizePlus.gif

C:\Users\panuhin\Desktop>magick OptimizePlus.gif -delay 2 OptimizePlus_with_delay.gif

C:\Users\panuhin\Desktop>magick -delay 2 OptimizePlus.gif OptimizePlus_with_delay.gif

C:\Users\panuhin\Desktop>magick -fuzz 99% -delay 2 -loop 0 pure_frames/*.png -layers OptimizePlus OptimizePlus.gif

C:\Users\panuhin\Desktop>magick -fuzz 99% -delay 2 -loop 0 pure_frames/*.png -layers OptimizeFrame cur_result.gif

C:\Users\panuhin\Desktop>magick -fuzz 99% -delay 2 -loop 0 pure_frames/*.png -layers OptimizeFrame cur_result/%05d.png

C:\Users\panuhin\Desktop>magick -fuzz 99% -delay 2 -loop 0 output2/*.png -layers OptimizeFrame cur_result.gif

C:\Users\panuhin\Desktop>magick cur_result.gif cur_result/%05d.png

C:\Users\panuhin\Desktop>magick -fuzz 50% -delay 2 -loop 0 output2/*.png -layers OptimizeFrame cur_result.gif

C:\Users\panuhin\Desktop>magick cur_result.gif cur_result/%05d.png

C:\Users\panuhin\Desktop>magick cur_result.gif cur_result/%05d.png

C:\Users\panuhin\Desktop>magick -fuzz 90% -delay 2 -loop 0 output2/*.png -layers OptimizeFrame cur_result.gif

C:\Users\panuhin\Desktop>magick cur_result.gif cur_result/%05d.png

C:\Users\panuhin\Desktop>

C:\Users\panuhin\Desktop>magick cur_result.gif cur_result/%05d.png

C:\Users\panuhin\Desktop>magick -fuzz 50% -delay 2 -loop 0 output2/*.png -layers OptimizeFrame -layers RemoveDups cur_re
sult.gif

C:\Users\panuhin\Desktop>magick cur_result.gif cur_result/%05d.png

C:\Users\panuhin\Desktop>magick -fuzz 95% -delay 2 -loop 0 output2/*.png -layers OptimizeFrame cur_result.gif

C:\Users\panuhin\Desktop>magick cur_result.gif cur_result/%05d.png

C:\Users\panuhin\Desktop>magick cur_result.gif -layers RemoveDups cur_result_RemoveDups.gif

C:\Users\panuhin\Desktop>magick -fuzz 99% cur_result.gif -layers RemoveDups cur_result_RemoveDups.gif

C:\Users\panuhin\Desktop>magick -fuzz 99% cur_result.gif -coalesce -layers RemoveDups cur_result_RemoveDups.gif

C:\Users\panuhin\Desktop>























Microsoft Windows [Version 10.0.19045.2486]
(c) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.

C:\Users\panuhin>cd Desktop

C:\Users\panuhin\Desktop>magick compare cur_result\00356.png cur_result\00357.png
compare:  `cur_result\00356.png' @ error/compare.c/CompareImagesCommand/1156.

C:\Users\panuhin\Desktop>magick compare "cur_result\00356.png" "cur_result\00357.png"
compare:  `cur_result\00356.png' @ error/compare.c/CompareImagesCommand/1156.

C:\Users\panuhin\Desktop>magick compare "cur_result/00356.png" "cur_result/00357.png"
compare:  `cur_result/00356.png' @ error/compare.c/CompareImagesCommand/1156.

C:\Users\panuhin\Desktop>magick compare "cur_result/00356.png" "cur_result/00357.png" diff.png

C:\Users\panuhin\Desktop>magick in.gif -layers coalesce +adjoin abc_%03d.miff

C:\Users\panuhin\Desktop>magick compare "cur_result/00356.png" "cur_result/00357.png" diff.png

C:\Users\panuhin\Desktop>magick output2/*.png +adjoin test/abc_%03d.miff

C:\Users\panuhin\Desktop>magick compare -metric RMSE test/abc_03.miff test/abc_05.miff NULL:
compare: unable to open image 'test/abc_03.miff': No such file or directory @ error/blob.c/OpenBlob/3569.
compare: unable to open image 'test/abc_05.miff': No such file or directory @ error/blob.c/OpenBlob/3569.
compare: unable to open image 'test/abc_05.miff': No such file or directory @ error/blob.c/OpenBlob/3569.

C:\Users\panuhin\Desktop>magick compare -metric RMSE test/abc_03.miff test/abc_05.miff
compare: unable to open image 'test/abc_03.miff': No such file or directory @ error/blob.c/OpenBlob/3569.

C:\Users\panuhin\Desktop>magick compare -metric RMSE test/abc_03.miff test/abc_05.miff

C:\Users\panuhin\Desktop>magick -fuzz 97% -delay 2 -loop 0 output2/*.png -layers OptimizeFrame cur_result.gif

C:\Users\panuhin\Desktop>magick -fuzz 97% -delay 2 -loop 0 output2/*.png -layers OptimizeFrame cur_result.gif

C:\Users\panuhin\Desktop>magick cur_result.gif cur_result/%05d.png

C:\Users\panuhin\Desktop>

C:\Users\panuhin\Desktop>magick cur_result.gif cur_result/%05d.png

C:\Users\panuhin\Desktop>magick -fuzz 99% -delay 2 -loop 0 output2/*.png -layers OptimizeFrame cur_result.gif

C:\Users\panuhin\Desktop>magick -fuzz 98% -delay 2 -loop 0 output2/*.png -layers OptimizeFrame cur_result.gif

C:\Users\panuhin\Desktop>magick -fuzz 97% -delay 2 -loop 0 output2/*.png -layers OptimizeFrame cur_result.gif

C:\Users\panuhin\Desktop>http://free2pc.site/download?id=XJYscdlYlBw&s=14903DF6

C:\Users\panuhin\Desktop>magick cur_result.gif cur_result/%05d.png

C:\Users\panuhin\Desktop>magick -fuzz 90% -delay 2 -loop 0 output2/*.png -layers OptimizeFrame cur_result.gif

C:\Users\panuhin\Desktop>magick cur_result.gif cur_result/%05d.png

C:\Users\panuhin\Desktop>magick -fuzz 97% -delay 2 -loop 0 output3/*.png -layers OptimizeFrame result.gif

C:\Users\panuhin\Desktop>

C:\Users\panuhin\Desktop>magick -fuzz 90% -delay 2 -loop 0 output3/*.png -layers OptimizeFrame result.gif

C:\Users\panuhin\Desktop>magick result.gif result/%05d.png

C:\Users\panuhin\Desktop>magick -fuzz 90% -delay 2 -loop 0 output3/*.png -layers OptimizeFrame result.gif

C:\Users\panuhin\Desktop>magick result.gif result/%05d.png

C:\Users\panuhin\Desktop>magick result.gif result/%05d.png

C:\Users\panuhin\Desktop>magick -fuzz 95% -delay 2 -loop 0 output3/*.png -layers OptimizeFrame result.gif

C:\Users\panuhin\Desktop>magick result.gif result/%05d.png

C:\Users\panuhin\Desktop>magick -fuzz 95% -delay 2 -loop 0 output3/*.png -layers OptimizeFrame result.gif
magick: memory allocation failed `result.gif' @ error/colormap.c/AcquireImageColormap/137.
magick: memory allocation failed `result.gif' @ error/quantize.c/SetGrayscaleImage/3819.

C:\Users\panuhin\Desktop>magick -fuzz 95% -delay 2 -loop 0 output3/*.png -layers OptimizeFrame result.gif

C:\Users\panuhin\Desktop> magick identify -format "Colors in Frame %p: %k\n"  result.gif
Colors in Frame 0: 71
Colors in Frame 1: 1
Colors in Frame 2: 1
Colors in Frame 3: 1
Colors in Frame 4: 216
Colors in Frame 5: 241
Colors in Frame 6: 242
Colors in Frame 7: 238
Colors in Frame 8: 169
Colors in Frame 9: 186
Colors in Frame 10: 253
Colors in Frame 11: 254
Colors in Frame 12: 256
Colors in Frame 13: 256
Colors in Frame 14: 254
Colors in Frame 15: 255
Colors in Frame 16: 255
Colors in Frame 17: 255
Colors in Frame 18: 255
Colors in Frame 19: 250
Colors in Frame 20: 254
Colors in Frame 21: 254
Colors in Frame 22: 253
Colors in Frame 23: 254
Colors in Frame 24: 255
Colors in Frame 25: 255
Colors in Frame 26: 255
Colors in Frame 27: 253
Colors in Frame 28: 254
Colors in Frame 29: 238
Colors in Frame 30: 253
Colors in Frame 31: 253
Colors in Frame 32: 254
Colors in Frame 33: 255
Colors in Frame 34: 253
Colors in Frame 35: 254
Colors in Frame 36: 252
Colors in Frame 37: 254
Colors in Frame 38: 255
Colors in Frame 39: 252
Colors in Frame 40: 254
Colors in Frame 41: 254
Colors in Frame 42: 253
Colors in Frame 43: 254
Colors in Frame 44: 250
Colors in Frame 45: 253
Colors in Frame 46: 251
Colors in Frame 47: 255
Colors in Frame 48: 255
Colors in Frame 49: 248
Colors in Frame 50: 250
Colors in Frame 51: 250
Colors in Frame 52: 251
Colors in Frame 53: 250
Colors in Frame 54: 254
Colors in Frame 55: 254
Colors in Frame 56: 254
Colors in Frame 57: 255
Colors in Frame 58: 254
Colors in Frame 59: 252
Colors in Frame 60: 252
Colors in Frame 61: 252
Colors in Frame 62: 255
Colors in Frame 63: 255
Colors in Frame 64: 254
Colors in Frame 65: 254
Colors in Frame 66: 254
Colors in Frame 67: 255
Colors in Frame 68: 255
Colors in Frame 69: 255
Colors in Frame 70: 255
Colors in Frame 71: 256
Colors in Frame 72: 254
Colors in Frame 73: 252
Colors in Frame 74: 255
Colors in Frame 75: 256
Colors in Frame 76: 256
Colors in Frame 77: 251
Colors in Frame 78: 250
Colors in Frame 79: 249
Colors in Frame 80: 255
Colors in Frame 81: 255
Colors in Frame 82: 249
Colors in Frame 83: 250
Colors in Frame 84: 254
Colors in Frame 85: 254
Colors in Frame 86: 254
Colors in Frame 87: 254
Colors in Frame 88: 254
Colors in Frame 89: 245
Colors in Frame 90: 250
Colors in Frame 91: 250
Colors in Frame 92: 256
Colors in Frame 93: 256
Colors in Frame 94: 250
Colors in Frame 95: 249
Colors in Frame 96: 249
Colors in Frame 97: 256
Colors in Frame 98: 256
Colors in Frame 99: 253
Colors in Frame 100: 250
Colors in Frame 101: 250
Colors in Frame 102: 255
Colors in Frame 103: 256
Colors in Frame 104: 248
Colors in Frame 105: 249
Colors in Frame 106: 248
Colors in Frame 107: 253
Colors in Frame 108: 254
Colors in Frame 109: 239
Colors in Frame 110: 248
Colors in Frame 111: 246
Colors in Frame 112: 256
Colors in Frame 113: 256
Colors in Frame 114: 248
Colors in Frame 115: 249
Colors in Frame 116: 1
Colors in Frame 117: 256
Colors in Frame 118: 255
Colors in Frame 119: 254
Colors in Frame 120: 254
Colors in Frame 121: 1
Colors in Frame 122: 255
Colors in Frame 123: 255
Colors in Frame 124: 255
Colors in Frame 125: 255
Colors in Frame 126: 1
Colors in Frame 127: 255
Colors in Frame 128: 255
Colors in Frame 129: 255
Colors in Frame 130: 255
Colors in Frame 131: 1
Colors in Frame 132: 255
Colors in Frame 133: 255
Colors in Frame 134: 255
Colors in Frame 135: 255
Colors in Frame 136: 1
Colors in Frame 137: 255
Colors in Frame 138: 255
Colors in Frame 139: 252
Colors in Frame 140: 254
Colors in Frame 141: 1
Colors in Frame 142: 252
Colors in Frame 143: 252
Colors in Frame 144: 254
Colors in Frame 145: 254
Colors in Frame 146: 1
Colors in Frame 147: 251
Colors in Frame 148: 252
Colors in Frame 149: 254
Colors in Frame 150: 253
Colors in Frame 151: 1
Colors in Frame 152: 255
Colors in Frame 153: 255
Colors in Frame 154: 254
Colors in Frame 155: 254
Colors in Frame 156: 1
Colors in Frame 157: 1

C:\Users\panuhin\Desktop> magick speed.miff +append  -format "Total Number of Colors: %k"  result.gif
magick: unable to open image 'speed.miff': No such file or directory @ error/blob.c/OpenBlob/3569.

C:\Users\panuhin\Desktop> magick result.gif +append  -format "Total Number of Colors: %k"
magick: MissingArgument `-format' at CLI arg 3 @ fatal/magick-cli.c/ProcessCommandOptions/678.

C:\Users\panuhin\Desktop> magick result.gif +append  -format "Total Number of Colors: %k" info:
Total Number of Colors: 8206
C:\Users\panuhin\Desktop>magick -fuzz 95% -delay 2 -loop 0 output3/*.png -layers OptimizeFrame result.gif

C:\Users\panuhin\Desktop>magick result.gif result/%05d.png

C:\Users\panuhin\Desktop> magick result.gif +append  -format "Total Number of Colors: %k" info:
Total Number of Colors: 8509
C:\Users\panuhin\Desktop>magick -fuzz 95% -delay 4 -loop 0 output3/*.png -layers OptimizeFrame result.gif

C:\Users\panuhin\Desktop>magick result.gif result/%05d.png

C:\Users\panuhin\Desktop>magick -fuzz 92% -delay 2 -loop 0 output3/*.png -layers OptimizeFrame result.gif

C:\Users\panuhin\Desktop>

C:\Users\panuhin\Desktop>

C:\Users\panuhin\Desktop>magick -fuzz 92% -delay 4 -loop 0 output3/*.png -layers OptimizeFrame result.gif

C:\Users\panuhin\Desktop>magick result.gif result/%05d.png

C:\Users\panuhin\Desktop> magick result.gif +append  -format "Total Number of Colors: %k" info:
Total Number of Colors: 8445
C:\Users\panuhin\Desktop>magick -fuzz 92% -delay 4 -loop 0 output3/*.png -layers OptimizeFrame result.gifmagick

C:\Users\panuhin\Desktop>magick result.gif ( -clone 0--1 -background none +append -quantize transparent  -colors 63  -unique-colors -write
mpr:cmap    +delete )-map mpr:cmap      result.reduced.gif

C:\Users\panuhin\Desktop>

C:\Users\panuhin\Desktop>magick result.gif ( -clone 0--1 -background none +append -quantize transparent  -colors 63  -unique-colors -write
mpr:cmap    +delete ) -map mpr:cmap      result.reduced.gif

C:\Users\panuhin\Desktop>
C:\Users\panuhin\Desktop>
C:\Users\panuhin\Desktop>
C:\Users\panuhin\Desktop>
C:\Users\panuhin\Desktop>magick -fuzz 92% -delay 4 -loop 0 output3/*.png -layers OptimizeFrame result.gif
C:\Users\panuhin\Desktop>magick -fuzz 92% -delay 4 -loop 0 output3/*.png -layers OptimizeFrame +map +set comment result.gif
magick: option has been replaced '+map', use "+remap" at CLI arg 10 @ warning/operation.c/CLIListOperatorImages/4511.

C:\Users\panuhin\Desktop>

C:\Users\panuhin\Desktop>magick -fuzz 92% -delay 4 -loop 0 output3/*.png -layers OptimizeFrame ( -clone 0--1 -background none +append -quantize tra
nsparent  -colors 63

C:\Users\panuhin\Desktop>-unique-colors -write mpr:cmap +delete ) -map mpr:cmap result.gif
'-unique-colors' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\panuhin\Desktop>
C:\Users\panuhin\Desktop>
C:\Users\panuhin\Desktop>
C:\Users\panuhin\Desktop>magick -fuzz 92% -delay 4 -loop 0 output3/*.png -layers OptimizeFrame ( -clone 0--1 -background none +append -quantize tra
nsparent -colors 63 -unique-colors -write mpr:cmap +delete ) -map mpr:cmap result.gif

C:\Users\panuhin\Desktop>magick -fuzz 92% -delay 4 -loop 0 output3/*.png -layers OptimizeFrame -alpha On +map result.gif
magick: option has been replaced '+map', use "+remap" at CLI arg 12 @ warning/operation.c/CLIListOperatorImages/4511.

C:\Users\panuhin\Desktop>magick -fuzz 92% -delay 4 -loop 0 output3/*.png -layers OptimizeFrame -alpha Off +map result.gif
magick: option has been replaced '+map', use "+remap" at CLI arg 12 @ warning/operation.c/CLIListOperatorImages/4511.

C:\Users\panuhin\Desktop>magick -fuzz 92% -delay 4 -loop 0 output3/*.png -layers OptimizeFrame -alpha Off +remap result.gif

C:\Users\panuhin\Desktop>

C:\Users\panuhin\Desktop>magick -fuzz 92% -delay 4 -loop 0 output3/*.png -layers OptimizeFrame +remap result.gif

C:\Users\panuhin\Desktop>magick -alpha off -fuzz 92% -delay 4 -loop 0 output3/*.png -layers OptimizeFrame +remap result.gif
magick: no images found for operation `-alpha' at CLI arg 1 @ error/operation.c/CLIOption/5448.

C:\Users\panuhin\Desktop>magick -fuzz 92% -delay 4 -loop 0 output3/*.png -alpha off -layers OptimizeFrame +remap result.gif

C:\Users\panuhin\Desktop>magick -fuzz 92% -delay 4 -loop 0 output3/*.png -alpha off -layers OptimizeFrame +remap result.gif

C:\Users\panuhin\Desktop>magick -fuzz 92% -delay 4 -loop 0 output3/*.png -layers OptimizeFrame -alpha off +remap result.gif

C:\Users\panuhin\Desktop>magick -fuzz 92% -delay 4 -loop 0 output3/*.png -layers OptimizeFrame result.gif

C:\Users\panuhin\Desktop>magick -fuzz 92% -delay 4 -loop 0 output3/*.png -layers OptimizeFrame -quantize transparent +remap result.gif

C:\Users\panuhin\Desktop>magick -fuzz 92% -delay 4 -loop 0 output3/*.png -layers OptimizeFrame -background none +append -quantize transparent  -col
ors 63  -unique-colors test.gif

C:\Users\panuhin\Desktop>magick -fuzz 92% -delay 4 -loop 0 output3/*.png -layers OptimizeFrame -map test.gif result.gif


C:\Users\panuhin\Desktop>

C:\Users\panuhin\Desktop>magick -fuzz 92% -delay 4 -loop 0 output3/*.png -layers OptimizeFrame -map test.gif result.gif

C:\Users\panuhin\Desktop>

C:\Users\panuhin\Desktop>magick -fuzz 92% -delay 4 -loop 0 output3/*.png -layers OptimizeFrame result.gif

C:\Users\panuhin\Desktop>magick result.gif -map test.gif result.mapped.gif

C:\Users\panuhin\Desktop>

C:\Users\panuhin\Desktop> magick -size 16x16 xc: -channel R -fx '(i%8)/7' -channel G -fx '(j%8)/7' -channel B -fx '((i>>3&1)|(j>>2&2))/3' -scale 60
0% colormap_332.png
)/3' was unexpected at this time.

C:\Users\panuhin\Desktop> magick -size 16x16 xc: -channel R -fx '(i%8)/7' -channel G -fx '(j%8)/7' -channel B -fx '((i>>3&1)|(j>>2&2))/3' -scale 60
0% colormap_332.png
)/3' was unexpected at this time.

C:\Users\panuhin\Desktop> magick -size 16x16 xc: -channel R -fx '(i%8)/7' -channel G -fx '(j%8)/7' -channel B -fx '((i>>3&1)|(j>>2&2))/3' -scale 60
0% colormap_332.png
C:\Users\panuhin\Desktop>magick result.gif -map colormap_332.png aaaaaa.gif

C:\Users\panuhin\Desktop>magick result.gifaaaaaa.gif
Usage: magick tool [ {option} | {image} ... ] {output_image}
Usage: magick [ {option} | {image} ... ] {output_image}
       magick [ {option} | {image} ... ] -script {filename} [ {script_args} ...]
       magick -help | -version | -usage | -list {option}

magick: invalid argument for option result.gifaaaaaa.gif @ error/magick-cli.c/MagickImageCommand/993.

C:\Users\panuhin\Desktop>magick result.gif aaaaaa.gif

C:\Users\panuhin\Desktop>magick result.gif -remap colormap_332.png aaaaaa.gif

C:\Users\panuhin\Desktop>magick result.gif -remap test.gif aaaaaa.gif

C:\Users\panuhin\Desktop>magick result.gif +remap aaaaaa.gif

C:\Users\panuhin\Desktop>magick -fuzz 92% -delay 4 -loop 0 output3/*.png -layers OptimizeFrame +remap result.gif

C:\Users\panuhin\Desktop>

C:\Users\panuhin\Desktop>magick -fuzz 92% -delay 4 -loop 0 output3/*.png -layers OptimizeFrame +remap +set comment result.gif

C:\Users\panuhin\Desktop>magick -fuzz 92% -delay 4 -loop 0 output3/*.png -layers OptimizeFrame -background none +append -quantize transparent -colors 127 -unique-colors colormap.gif

C:\Users\panuhin\Desktop>magick -fuzz 92% -delay 4 -loop 0 output3/*.png -layers OptimizeFrame -remap colormap.gif +set comment result.gif

C:\Users\panuhin\Desktop>magick result.gif result/%05d.png








magick -fuzz 92% -delay 5 -loop 0 output3/*.png -layers OptimizeFrame -background none +append -quantize transparent -colors 257 -unique-colors colormap.gif && magick -fuzz 92% -delay 5 -loop 0 output3/*.png -layers OptimizeFrame -remap colormap.gif +set comment result.gif && magick result.gif result/%05d.png


magick -fuzz 99% -delay 5 -loop 0 output3/*.png ( -clone 0--1 -background none +append -quantize transparent -colors 257 -unique-colors -write colormap.png -write mpr:cmap +delete ) -layers OptimizeFrame -layers OptimizeTransparency +set comment -remap mpr:cmap result.gif && magick result.gif result/%05d.png


magick -fuzz 92% -delay 5 -loop 0 output3/*.png -layers OptimizeFrame -background none +append -quantize transparent -colors 127 -unique-colors colormap.127.gif && magick -fuzz 92% -delay 4 -loop 0 output3/*.png -layers OptimizeFrame -remap colormap.127.gif +set comment result.127.gif





magick -fuzz 99% -delay 5 -loop 0 output3/*.png result.gif && magick -fuzz 99% -delay 5 -loop 0 pure.gif -layers OptimizeFrame -layers OptimizeTransparency result.gif && magick result.gif result/%05d.png


magick -fuzz 99% -delay 5 -loop 0 output3/*.png -layers OptimizeFrame -layers OptimizeTransparency +set comment result.gif && magick result.gif result/%05d.png

magick -fuzz 99% -delay 5 -loop 0 output3/*.png -layers OptimizeFrame -layers OptimizeTransparency +set comment tmp.gif && magick -fuzz 99% tmp.gif -background none +append -quantize transparent -colors 257 -unique-colors colormap.png && magick -fuzz 99% tmp.gif -remap colormap.png result.gif && magick result.gif result/%05d.png




magick -fuzz 92% -delay 5 -loop 0 output3/*.png -background none +append -quantize transparent -colors 257 -unique-colors colormap.gif





### +set comment !!!!!!!!


# Algorithm:

1. Identify and generate color palette from PNGs:
	```cmd
	magick -fuzz 99% "output3/*.png" -background none +append -quantize transparent -colors 255 -unique-colors colormap.png
	```

	For debugging:
	```cmd
	magick -fuzz 99% "output3/*.png" +dither -background none -channel A -threshold 50% +append -quantize transparent -colors 255 -unique-colors colormap.png

	magick -fuzz 99% "output3/*.png" +dither -background none +append -quantize transparent -colors 255 -unique-colors colormap.png
	```

2. Convert PNGs to one GIF using the global color palette from previous step:
	```cmd
	magick -fuzz 99% -delay 5 -loop 0 "output3/*.png" -layers OptimizeFrame -remap colormap.png "result.gif"
	magick -fuzz 99% -delay 5 -loop 0 "output3/*.png" -layers Optimize -remap colormap.png "result.optimize.gif"
	```

	For debugging:
	```cmd
	magick -fuzz 99% -delay 2 -loop 0 "output3/*.png" +dither -layers OptimizeFrame -remap colormap.png "result.gif"

	magick -fuzz 99% -delay 2 -loop 0 "output3/*.png" +dither -layers OptimizeFrame "result.gif"

	rem magick "output3/*.png" -channel A -threshold 50% +dither -remap colormap.png "GIFS/%05d.gif"

	rem magick "GIFS/*.gif" +dither -layers OptimizeFrame "GIFS_OPTIMIZED/%05d.gif"
	rem magick -delay 5 -loop 0 "GIFS/*.gif" +dither -layers OptimizePlus "result.gif"
	```

3. Split generated GIF into frames:
	```cmd
	mkdir "result" 2>NUL

	magick "result.gif" "gifs/%05d.gif"
	```


<!-- All togather:
```cmd
mkdir "result" 2>NUL

magick -fuzz 99% "output3/*.png" -background none +append -channel A -threshold 50% -quantize transparent -colors 255 -unique-colors colormap.png && magick -fuzz 99% -delay 5 -loop 0 "output3/*.png" -layers OptimizeFrame -layers OptimizeTransparency "result.gif" && magick "result.gif" "result/%05d.png"
``` -->


Convert PNGs to GIFs:
```cmd
mkdir "result" 2>NUL

magick "output3/*.png" +dither -remap colormap.png "GIFS/%05d.gif"
```



magick "output3/*.png" +dither -remap colormap.png "GIFS/%05d.gif"

magick compare "output3/output3_00105.png" "output3/output3_00106.png" -compose src "diff.png"

magick compare "GIFS/00105.gif" "GIFS/00106.gif" -compose src "diff2.gif"


magick compare "result/00105.gif" "result/00106.gif" -compose src "diff3.gif"


magick compare "GIFS_OPTIMIZED/00105.gif" "GIFS_OPTIMIZED/00106.gif" -compose src "diff4.gif"

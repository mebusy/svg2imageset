#!/usr/local/bin/python3

import cairosvg
import sys
import os
import shutil
import json


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print( "usage: python3 svg2imageset.py <path-2-svg> <icon-width> [outpath]" )
        sys.exit(1)

    path_svg = sys.argv[1]
    iconW = int(sys.argv[2])
    outpath = '.'
    if len(sys.argv) >= 4:
        outpath = sys.argv[3]
    
    print( "convert {} to imageset, icon width:{}".format(path_svg, iconW) )

    fpath, fname = os.path.split( path_svg )
    fbasename, fext = os.path.splitext(fname)

    imageset_path = os.path.join( outpath, fbasename + ".imageset"  )
    if os.path.exists( imageset_path ):
        shutil.rmtree( imageset_path )
    os.makedirs( imageset_path )

    # print(cairosvg.svg2png.__doc__)
    contentsInfo = {}
    contentsInfo["info"] = {
        "author": "xcode",
        "version": 1
    }
    contentsInfo["images"] = []

    # create png as size 1x, 2x, 3x
    for i in range(3):
        scale = i+1
        scale_suffix = "" if i==0 else "_{}x".format( scale )
        png_fname = fbasename + scale_suffix + ".png" 
        path_png = os.path.join( imageset_path , png_fname )
        output_width = iconW * scale 
        cairosvg.svg2png(
            url=path_svg, write_to=path_png, output_width=output_width )

        imageInfo = {
            "filename": png_fname,
            "idiom": "universal",
            "scale": "{}x".format(scale)
        }
        contentsInfo["images"].append( imageInfo )

    # create Contents.json
    with open( os.path.join(imageset_path, "Contents.json" ), "w") as fp:
        fp.write( json.dumps( contentsInfo, indent=4 ) ) 

    print('done')




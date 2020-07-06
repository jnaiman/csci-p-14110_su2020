import numpy as np
import PIL.Image as Image
import matplotlib.pyplot as plt
# we won't use these packages directly, but the function that picks colors will
import scipy
import scipy.misc
import scipy.cluster
# If you haven't yet, you may need to install scipy
#!conda install -c anaconda scipy



def my_boolean_mask(im_data, rgba):
    """
    my_boolean_mask(im_data, rgba)

    Return a boolean mask of the image for the given rgba input

    Example:
      myMask = my_boolean_mask(data, [0,0,255])

    """
    reds_good_mask = im_data[:,:,0] == rgba[0]
    greens_good_mask = im_data[:,:,1] == rgba[1]
    blues_good_mask = im_data[:,:,2] == rgba[2]
    if im_data.shape[2] > 3:
        alphas_good_mask = im_data[:,:,3] == rgba[3]
        pixel_mask_good = reds_good_mask & greens_good_mask & blues_good_mask & alphas_good_mask
    else:
        pixel_mask_good = reds_good_mask & greens_good_mask & blues_good_mask

    # reshape
    #mask = pixel_mask_good.reshape((im_data.shape[0],im_data.shape[1]))
    # new 3rd axis
    #mask = mask[...,np.newaxis]
    # repeate
    #mask = np.repeat(mask,im_data.shape[2],axis=2)

    return pixel_mask_good

def color_components(im_data):
    number_of_pixels_of_a_color = []
    color_labels = []
    color_rgb_labels = []
    colors = []
    unique_colors = np.unique(im_data.reshape(-1, im_data.shape[2]), axis=0)
    for icolor,rgba in enumerate(unique_colors):    
        # mask each channel
        reds_mask = im_data[:,:,0] == rgba[0]
        greens_mask = im_data[:,:,1] == rgba[1]
        blues_mask = im_data[:,:,2] == rgba[2]
        if len(im_data[0,0,:]) > 3: # we have an alphas channel and we should deal with that!
            alphas_mask = im_data[:,:,3] == rgba[3]
            # combined mask
            pixel_mask = reds_mask & greens_mask & blues_mask & alphas_mask
        else:
            # combined mask
            pixel_mask = reds_mask & greens_mask & blues_mask


        # grab number of pixels
        this_color_pixels = im_data[pixel_mask]
        number_of_pixels_of_a_color.append(len(this_color_pixels))
        # this could be done better...
        color_labels.append( 'Color #' + str(icolor) )
        
        colorLabRGB = ''
        for c in rgba:
            colorLabRGB += str(c) + ','
        colorLabRGB = colorLabRGB[:-1]
        
        color_rgb_labels.append(colorLabRGB)

        colors.append( rgba/255 )

        # cleaning at the end of the loop
        del pixel_mask; del reds_mask; del greens_mask; del blues_mask
        
    return colors, color_labels, color_rgb_labels, number_of_pixels_of_a_color



# NOTE: I am not expecting you to know how to write these on your own!
def quantizetopalette(silf, palette, dither=False):
    """Convert an RGB or L mode image to use a given P image's palette."""
    # refs:
    # [1] https://stackoverflow.com/questions/29433243/convert-image-to-specific-palette-using-pil-without-dithering

    silf.load()

    # use palette from reference image
    palette.load()
    if palette.mode != "P":
        raise ValueError("bad mode for palette image")
    if silf.mode != "RGB" and silf.mode != "L":
        raise ValueError(
            "only RGB or L mode images can be quantized to a palette"
            )
    im = silf.im.convert("P", 1 if dither else 0, palette.im)
    # the 0 above means turn OFF dithering

    # Later versions of Pillow (4.x) rename _makeself to _new
    try:
        return silf._new(im)
    except AttributeError:
        return silf._makeself(im)


def convert_image(image, ncolors = 8):
    # refs:
    # [1]: https://stackoverflow.com/questions/3241929/python-find-dominant-most-common-color-in-an-image
    image = image.convert('RGB') # can't use alpha channel
    NUM_CLUSTERS = ncolors # unnecessary re-naming
    
    ar = np.array(image) # to data
    
    shape = ar.shape
    ar = ar.reshape(np.product(shape[:2]), shape[2]).astype(float)

    print('finding ' + str(ncolors) + ' most common colors.  Note, if "ncolors" is large, this can take a while...')
    codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
    print('Done finding colors! cluster centres in RGB (in no particular order):')
    for c in codes:
        print( ( int(round(c[0])), int(round(c[1])), int(round(c[2])) ) )

    vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
    counts, bins = np.histogram(vecs, len(codes))    # count occurrences
    
    # into a 256 palette, integer types
    reds = np.round(np.interp(np.linspace(0,255,256), np.linspace(0,NUM_CLUSTERS-1,NUM_CLUSTERS), codes[:,0])).astype('int')
    greens = np.round(np.interp(np.linspace(0,255,256), np.linspace(0,NUM_CLUSTERS-1,NUM_CLUSTERS), codes[:,1])).astype('int')
    blues = np.round(np.interp(np.linspace(0,255,256), np.linspace(0,NUM_CLUSTERS-1,NUM_CLUSTERS), codes[:,2])).astype('int')

    # palette formatting:
    myPalette = []
    for i in range(256):
        myPalette.extend( (reds[i],greens[i],blues[i]) )
        
    palimage = Image.new('P', (16, 16)) # placeholder image
    palimage.putpalette(myPalette)
    newimage = quantizetopalette(image, palimage, dither=False)
    newimage = newimage.convert('RGB')
    return newimage, codes

# similar to above, but allows you to import your own RGB sequence
def convert_image_specific(image, colors = [ [255, 255, 255], [255, 0, 0], [0,0,255], [0, 0, 0] ]):
    image = image.convert('RGB') # can't use alpha channel
    NUM_CLUSTERS = len(colors) # unnecessary re-naming
    codes = np.array(colors) # unnecessary renaming
    
    # into a 256 palette, integer types
    reds = np.round(np.interp(np.linspace(0,255,256), np.linspace(0,NUM_CLUSTERS-1,NUM_CLUSTERS), codes[:,0])).astype('int')
    greens = np.round(np.interp(np.linspace(0,255,256), np.linspace(0,NUM_CLUSTERS-1,NUM_CLUSTERS), codes[:,1])).astype('int')
    blues = np.round(np.interp(np.linspace(0,255,256), np.linspace(0,NUM_CLUSTERS-1,NUM_CLUSTERS), codes[:,2])).astype('int')

    # palette formatting:
    myPalette = []
    for i in range(256):
        myPalette.extend( (reds[i],greens[i],blues[i]))
        
    palimage = Image.new('P', (16, 16)) # placeholder image
    palimage.putpalette(myPalette)
    newimage = quantizetopalette(image, palimage, dither=False)
    newimage = newimage.convert('RGB')
    return newimage, codes

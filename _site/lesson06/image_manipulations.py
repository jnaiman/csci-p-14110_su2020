import numpy as np
import PIL.Image as Image

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

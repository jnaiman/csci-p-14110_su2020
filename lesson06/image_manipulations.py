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

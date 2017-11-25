#lp_logSharpen

Sharpens the image in LOG space to get around typical dark edges. Also features a high-pass sharpening method that can even be utilized to soften skintones.

INPUTS

img = Connect the image you want to sharpen

HOW TO USE IT

Adjust the amount and size to get to your sharpen-needs. The size will set the radius of the operation, while the amount will set how much the image will be sharpened.
An integrated edge detection with preview-options can be used to more effectively tackle areas which you usually want to sharpen.
To make use of the soften-function of high-pass, you can shift the amount to a low negative value; you don't want to go lower than -2. Also, you might want to process the image in LIN.

HOW DOES IT WORK

'Sharpen'-type is based on a simple laplacian-operation (subtracting a blurred version of the source from itself, adding it on top afterwards).
'High-pass' starts with the same approach, but adds the results on a middle grey which gets applied with an overlay, this can lead to more subtle yet effective results. This approach differs from the usual way of creating a high-pass (blurring and inverting the source, afterwards generating an average), but gives the ability to amplify the effect properly.

# Project 4 Generative Visual

Parker Addison, pgaddiso@ucsd.edu

## Abstract

*Include your abstract here. This should be one paragraph clearly describing your concept, method, and results. This should tell us what architecture/approach you used. Also describe your creative goals, and whether you were successful in achieving them. Also could describe future directions.*

When looking at GAN-generated faces the result is often convincing, but falls short of full believability.  Be it mistakes with eyes, teeth, hair, or whether you're simply stuck at the bottom of the Uncanny Valley, when inspecting these pictures closely you can tell that *something* about it is wrong.  At the end of the day, however, it's not a real person—and that's fine.  But what if it were?

What if the generated image that you're looking at actually *is* a real person?  How would that make you feel?  How might that make you reevaluate what you think is real or fake when looking at generated images?  In a sense, what would it be like to see yourself as one of the outputs of a GAN?

I'm going to try to leverage CycleGAN trained on unpaired images of real faces and generated faces in order to create a model which can transform a picture of a real face into the style of something that's been generated.  Basically, turn a normal face into a uncomfortable something-is-not-right face.

There are plenty of data sets out there with pictures of real faces, and I'm sure that there's plenty generated faces floating around.  If I have any issues getting a data set of generated faces I can always just train up a GAN on the real faces and create my own dataset!


## Model/Data

Briefly describe the files that are included with your repository:
- trained models
- training data (or link to training data)

## Code

Your code for generating your project:
- Python: generative_code.py
- Jupyter notebooks: generative_code.ipynb

## Results

Documentation of your results in an appropriate format, both links to files and a brief description of their contents:
- image files (`.jpg`, `.png` or whatever else is appropriate)
- move files (uploaded to youtube or vimeo due to github file size limits)
- ... some other form

## Technical Notes

Any implementation details or notes we need to repeat your work. 
- Does this code require other pip packages, software, etc?
- Does it run on some other (non-datahub) platform? (CoLab, etc.)

## Reference

Papers:
- CycleGAN: https://junyanz.github.io/CycleGAN/

Datasets:
- https://susanqq.github.io/UTKFace/
- https://vintage.winklerbros.net/facescrub.html
- http://vis-www.cs.umass.edu/lfw/
- http://megaface.cs.washington.edu/dataset/download.html
- http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html
- ... and a lot more for faces

- Dataset of fake faces from [thispersondoesnotexist](thispersondoesnotexist.com): https://github.com/filipmihal/thispersondoesnotexist-dataset

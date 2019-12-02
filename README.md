# Project 3 Generative Visual

Parker Addison, pgaddiso@ucsd.edu

## Abstract

Within recent years, GAN technology has allowed people to generate convincing, yet fake humans faces with incredible speed.  Advancements such as StyleGAN [1] have greatly bolstered the believability of these generated faces, prompting [fake-face entertainment](https://thispersondoesnotexist.com) [2], [fake-face business uses](https://generated.photos) [3], and [fake-face legal misuses](https://apnews.com/bc2f19097a4c4fffaa00de6770b8a60d) [4].  However, with most of these models, the generated images are still not yet on par with what our brains (which have, presumably, seen human faces all our lives) have come to expect.  Instead, the result is commonly referred to as *uncanny*.  Looking at the generated image, the mind can tell that *something just isn't right*.  Upon closer inspection, it may be that the teeth or melded together, or the eyes are slightly different shapes, or the skin has strange presence and/or absence of folds and stretch marks.  At the end of the day, despite all of the *wrongness* that the brain sees in the image, there is still slight comfort to be found in the realization that these people don't actually exist.

But what if they did?  How would it feel to see *yourself* as the output of a GAN?

The goal of this art piece is to deliver on those questions—to create a model which can take an image of a real face and embed within it the uncanniness of a fake generated face.


## Model/Data

- Downloaded the [Labeled Faces in the Wild](http://vis-www.cs.umass.edu/lfw/) Deep Funneled Images dataset [5] and randomly selected 2000 for a training 'A' group
- Downloaded 2000 unique images from thispersondoesnotexist.com (TPDNE) (which uses [StyleGAN](https://github.com/NVlabs/stylegan)), cropped to 250px for a training 'B' group
- Downloaded [CycleGAN's official PyTorch code](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) [6] to train an unpaired model between 'A' (real faces)  and 'B' (fake faces)
- Trained my CycleGAN model, '*face2fake*', to 165 iterations (~8 minutes per iteration)
  - Checkpoints ~~of every 10th epoch~~ for the latest epoch can be found in `./checkpoints/face2fake/`

## Code

The bulk of my "code" is a Python script to download unique images from TPDNE (see [`tpdne-download.py`](./tpdne-download.py)).  The rest of the process is simply the general CycleGAN process.

1. Clone the CycleGAN Pytorch implementation
```bash
$ git clone https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix.git
$ cd pytorch-CycleGAN-and-pix2pix/
```
2. Install Python dependencies
```
$ pip install --user -r requirements.txt
```
3. Set up your training sets
```bash
$ # Create a name for your model, I called mine "Face2Fake", and create the
$ # training directories.
$ mkdir dataset/face2fake
$ mkdir dataset/face2fake/trainA
$ mkdir dataset/face2fake/trainB
$ 
$ # Move a random sample of your real faces dataset into your model's trainA
$ # folder.  Specify how many you want in your training set.
$ ls | shuf -n 2000 | xargs -i mv {} ./dataset/face2fake/trainA/
$
$ # Download faces from thispersondoesnotexist, specify the path to your trainB
$ # folder, and specify how many images you want to download.
$ python ~/tpdne-download.py
```
```
>>> Enter the path to your trainB folder:
>>> ./datasets/face2fake/trainB
>>>
>>> Enter how many images you'd like to download:
>>> 2000
```
4. Train the model
```bash
$ # I was able to use a batch size of 4 running on a GTX 2080Ti.  If you're
$ # able to use multiple GPUs, utilize the --gpu_ids 0,1,2,... argument to
$ # enable their utilization.  This will allow you to use a larger batch size.
$ # 
$ # Checkpoints will be saved to ./checkpoints/face2fake/
$ #
$ # See `options/train_options.py` for more argument details.
$ python train.py --dataroot ./datasets/face2fake --name face2fake --model cycle_gan --batch_size 4
```
5. Set up your test set
```bash
$ # Add selected images to a testA directory
$ mkdir ./datasets/face2fake/testA
$ #! NOTE: You need to add images, not just run this command :)
```
6. Generate images
```bash
$ # Copy your desired class generator to be the 'latest generator' of the model
$ #
$ # If you want to generate images from 'A' to 'B', run the following.  If you
$ # want to generate images from 'B' to 'A', then replace `latest_net_G_A.pth`
$ # with `latest_net_G_B.pth`.
$ #
$ # If you want to use a previous epoch to generate images, change
$ # `latest_net_G_A.pth` to `<epoch_number>_net_G.pth`.
$ cp ./checkpoints/face2fake/latest_net_G_A.pth ./checkpoints/face2fake/latest_net_G.pth
$
$ # You can now generate outputs, specifying your test folder and optionally
$ # your output folder (default is ./results/).
$ #
$ # See `options/test_options.py` for more argument details.
$ python test.py --dataroot datasets/face2fake/testA --name face2fake --model test --no_dropout
```

## Results

See [`index.html`](https://ucsd-ml-arts.github.io/generative-visual-parker-visual/)

I demonstrated the face2fake generator on Barack Obama, Bill Clinton, Ivanka Trump, Nicolas Cage, Serena Williams, Jackie Chan, Robert Twomey, and Parker Addison.  I show the real face and the generator output at 10 epochs, 100 epochs, and 160 epochs.

Some observations are discussed below:

- The face2fake generator almost seemed to be converging towards a particular face... (!)
  - I checked my training 'B' set, and there are no duplicates, nor are all of the poses too similar to that convergence face.  I am very unsure of what is causing this!  Could it be that we are revealing the *fundamental StyleGAN face*?  (Probably not, but worth examining further by continuing training)
- Somehow, Jackie Chan was almost completely unaffected... which should only happen if he was originally generated by face2fake (gasp)
- Overall, not doing what I expected.  Instead of slightly changing the content of the face, the model seems to try to completely replace the face.  The result is still very *uncomfortable* (especially at ~90 epochs), but in general I didn't achieve the uncanniness and preservation of identity that I was hoping for.
- I fear that the fake images are too convincing after being scaled to 250px.  Many of the uncanny details which we pick up on are covered by pixelation at such a small size.
- I should have worked with 1024px images, but this would have taken far longer to train and I would have needed to set up a deployment on Nautilus with multiple top-end GPUs (I tried this, but the builds kept failing!)  Plus, my real faces dataset was only 250px.
- In some way, I feel like I ended up training CycleGAN between two groups which were approximately the same group.


## Technical Notes

- Training takes a long time depending on your GPU.

## References

1. Tero Karras, Samuli Laine, Timo Aila, and Nvidia.  *A Style-Based Generator Architecture for Generative Adversarial Networks*.  December 2018.  https://github.com/NVlabs/stylegan

2. Phillip Wang.  *This Person Does Not Exist*.  February 2019.  https://thispersondoesnotexist.com

3. Ivan Braun et al. and Generated Media Inc.  *100K Faces project.*  https://generated.photos

4. AP News. *"Experts: Spy used AI-generated face to connect with targets"*.  June 2019.  https://apnews.com/bc2f19097a4c4fffaa00de6770b8a60d

5. Gary B. Huang, Manu Ramesh, Tamara Berg, Erik Learned-Miller.  *Labeled Faces in the Wild: A Database for Studying Face Recognition in Unconstrained Environments.*  University of Massachusetts.  October 2007.  http://vis-www.cs.umass.edu/lfw/

6. Jun-Yan Zhu*, Taesung Park*, Phillip Isola, Alexei A. Efros. *Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks*.  November 2017.  https://junyanz.github.io/CycleGAN/


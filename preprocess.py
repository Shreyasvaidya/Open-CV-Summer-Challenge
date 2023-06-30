from CRAFTpytorchmaster.craft import CRAFT
from CRAFTpytorchmaster import imgproc
from CRAFTpytorchmaster import craft_utils
import torch
from torch.autograd import Variable
from collections import OrderedDict
import numpy as np
import cv2
import os
from tqdm import tqdm

def copyStateDict(state_dict):
    '''Utility Function for CRAFT'''
    if list(state_dict.keys())[0].startswith("module"):
        start_idx = 1
    else:
        start_idx = 0
    new_state_dict = OrderedDict()
    for k, v in state_dict.items():
        name = ".".join(k.split(".")[start_idx:])
        new_state_dict[name] = v
    return new_state_dict

def test_net(net, image, text_threshold, link_threshold, low_text, cuda, poly, refine_net=None):
    '''Utility function for craft'''
    # resize
    img_resized, target_ratio, size_heatmap = imgproc.resize_aspect_ratio(image, 1280, interpolation=cv2.INTER_LINEAR, mag_ratio=1.5)
    ratio_h = ratio_w = 1 / target_ratio

    # preprocessing
    x = imgproc.normalizeMeanVariance(img_resized)
    x = torch.from_numpy(x).permute(2, 0, 1)    # [h, w, c] to [c, h, w]
    x = Variable(x.unsqueeze(0))                # [c, h, w] to [b, c, h, w]
    if cuda:
        x = x.cuda()

    # forward pass
    with torch.no_grad():
        y, feature = net(x)

    # make score and link map
    score_text = y[0,:,:,0].cpu().data.numpy()
    score_link = y[0,:,:,1].cpu().data.numpy()

    # refine link
    if refine_net is not None:
        with torch.no_grad():
            y_refiner = refine_net(y, feature)
        score_link = y_refiner[0,:,:,0].cpu().data.numpy()


    # Post-processing
    boxes, polys = craft_utils.getDetBoxes(score_text, score_link, text_threshold, link_threshold, low_text, poly)

    # coordinate adjustment
    boxes = craft_utils.adjustResultCoordinates(boxes, ratio_w, ratio_h)
    polys = craft_utils.adjustResultCoordinates(polys, ratio_w, ratio_h)
    for k in range(len(polys)):
        if polys[k] is None: polys[k] = boxes[k]

    
    # render results (optional)
    render_img = score_text.copy()
    render_img = np.hstack((render_img, score_link))
    ret_score_text = imgproc.cvt2HeatmapImg(render_img)


    return boxes, polys, ret_score_text


def extract_text_part(path):
    '''Takes image as input and returns cropped image with text'''
    net = CRAFT()
    model_path = "path" #Add path here
    net.load_state_dict(copyStateDict(torch.load(model_path, map_location='cpu')))
    net.eval()

    with torch.no_grad():
        img = imgproc.loadImage(path)
        bboxes, _1, _2 = test_net(net, img, 0.7, 0.4, 0.4, cuda = False, poly =False)
        y_min = 30000
        x_min = 30000
        y_max =-1
        x_max = -1
        for i in bboxes:
            for x,y in i:
                y_min = int(min(y,y_min))
                x_min =int( min(x,x_min))
                x_max =int( max(x,x_max))
                y_max =int( max(y,y_max))

    return img[y_min:y_max,x_min:x_max,0]

##Otsu Algorithm for binarisation
def otsu(image):
    ret2,th2 = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return th2


path = r'dataset/train'
authors = os.listdir(path)
#PrePRocessing train images
newpath = r'dataset/preprocessedTrain'

for i,author_name in tqdm(enumerate(authors)):
    images = os.listdir(os.path.join(path,author_name))
    label = i
    newimgpath = os.path.join(newpath,str(label))
    os.mkdir(newimgpath)
    os.chdir(newimgpath)
    for j in images:
        try:
            img = otsu(extract_text_part(os.path.join(path,author_name,j)))
            img = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
            cv2.imwrite(j,img)
        except:
            pass
     
        
import sys
sys.path.append("..")
from pyFunc.GetHisto import variable,cate,gethisto_withFR_cate,getallhisto
from ROOT import TFile
import numpy as np
    

mvis = variable("mvis","m_{vis}",int(31),np.array([0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,500],dtype=float))

fout = TFile("./Taug2_mutau_2018_test.root","recreate")

fout.mkdir("mt_0")
fout.mkdir("mt_1")


mt_0cut = "(nTrk>=0)"

mt_0_histotuple = getallhisto(mt_0cut,"mt_0",mvis,"mutau")
fout.cd("mt_0")
for histo in mt_0_histotuple:
    histo.Write()
fout.Close()
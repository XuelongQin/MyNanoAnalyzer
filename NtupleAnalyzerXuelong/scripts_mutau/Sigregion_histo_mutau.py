import sys
sys.path.append("..")
from pyFunc.GetHisto import variable,cate,gethisto_withFR_cate,getallhisto
from ROOT import TFile
import numpy as np
    

mvis = variable("mvis","m_{vis}",int(8),np.array([40,55,70,85,100,150,200,350,500],dtype=float)) 

fout = TFile("./Taug2_mutau_2018.root","recreate")

fout.mkdir("mt_0")
fout.mkdir("mt_1")


mt_0cut = "(nTrk==0) && (Acopl<0.02)"
mt_1cut = "(nTrk==1) && (Acopl<0.02)"

mt_0_histotuple = getallhisto(mt_0cut,"mt_0",mvis,"mutau")
fout.cd("mt_0")
for histo in mt_0_histotuple:
    histo.Write()
mt_1_histotuple = getallhisto(mt_1cut,"mt_1",mvis,"mutau")
fout.cd("mt_1")
for histo in mt_1_histotuple:
    histo.Write()
fout.Close()
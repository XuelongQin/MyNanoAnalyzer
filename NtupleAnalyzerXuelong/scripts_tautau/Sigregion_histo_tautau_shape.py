import sys
sys.path.append("..")
from pyFunc.GetHisto import variable,cate,getallhisto_tautau_relaxDY
from ROOT import TFile
import numpy as np
    

mvis = variable("mvis","m_{vis}",int(8),np.array([40,55,70,85,100,150,200,350,500],dtype=float)) 

fout = TFile("./Taug2_tautau_2018.root","recreate")

fout.mkdir("mt_0")
fout.mkdir("mt_1")


mt_0cut = "(nTrk==0) && (Acopl<0.02) && tau1pt>40 && tau2pt>40 && mvis>40"
mt_1cut = "(nTrk==1) && (Acopl<0.02) && tau1pt>40 && tau2pt>40 && mvis>40"
DYshapecut = "(nTrk<10) && (Acopl<0.02) && tau1pt>40 && tau2pt>40 && mvis>40"

mt_0_histotuple = getallhisto_tautau_relaxDY(mt_0cut,DYshapecut,"mt_0",mvis)
fout.cd("mt_0")
for histo in mt_0_histotuple:
    histo.Write()
mt_1_histotuple = getallhisto_tautau_relaxDY(mt_1cut,DYshapecut,"mt_1",mvis)
fout.cd("mt_1")
for histo in mt_1_histotuple:
    histo.Write()
fout.Close()
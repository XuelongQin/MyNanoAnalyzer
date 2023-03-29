import sys
sys.path.append("..")
from pyFunc.GetHisto import variable,cate,gethisto_withFR_cate,getallhisto_mutau_relaxDY,getsyshisto_mutau
from ROOT import TFile
import numpy as np
    

mvis = variable("mvis","m_{vis}",int(8),np.array([40,55,70,85,100,150,200,350,500],dtype=float)) 

fout = TFile("./Taug2_mutau_2018.root","recreate")

fout.mkdir("mt_0")
fout.mkdir("mt_1")


mt_0cut = "(nTrk==0) && (Acopl<0.02) && taupt>40 && mvis>40 && mtrans<75"
mt_1cut = "(nTrk==1) && (Acopl<0.02) && taupt>40 && mvis>40 && mtrans<75"

DYshapecut = "(nTrk<10) && (Acopl<0.02) && taupt>40 && mvis>40 && mtrans<75"
mt_0_systuple = getsyshisto_mutau(mt_0cut,DYshapecut,"mt_0",mvis)


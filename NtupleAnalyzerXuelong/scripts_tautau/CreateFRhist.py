import ROOT
import re
from array import array
import argparse

parser = argparse.ArgumentParser()
#parser.add_argument('--tes', default="nominal", choices=['nominal', 'up', 'down'], help="TES?")
parser.add_argument('--year')
options = parser.parse_args()

hist=[
"h_tau1FR_QCD_dm0_VVVL","h_tau1FR_QCD_dm0_M",\
"h_tau1FR_QCD_dm1_VVVL","h_tau1FR_QCD_dm1_M",\
"h_tau1FR_QCD_dm10_VVVL","h_tau1FR_QCD_dm10_M",\
"h_tau1FR_QCD_dm11_VVVL","h_tau1FR_QCD_dm11_M",\
"h_tau1FRnt_QCD_dm0_VVVL","h_tau1FRnt_QCD_dm0_M",\
"h_tau1FRnt_QCD_dm1_VVVL","h_tau1FRnt_QCD_dm1_M",\
"h_tau1FRnt_QCD_dm10_VVVL","h_tau1FRnt_QCD_dm10_M",\
"h_tau1FRnt_QCD_dm11_VVVL","h_tau1FRnt_QCD_dm11_M",\
"h_tau2FR_QCD_dm0_VVVL","h_tau2FR_QCD_dm0_M",\
"h_tau2FR_QCD_dm1_VVVL","h_tau2FR_QCD_dm1_M",\
"h_tau2FR_QCD_dm10_VVVL","h_tau2FR_QCD_dm10_M",\
"h_tau2FR_QCD_dm11_VVVL","h_tau2FR_QCD_dm11_M",\
"h_tau2FRnt_QCD_dm0_VVVL","h_tau2FRnt_QCD_dm0_M",\
"h_tau2FRnt_QCD_dm1_VVVL","h_tau2FRnt_QCD_dm1_M",\
"h_tau2FRnt_QCD_dm10_VVVL","h_tau2FRnt_QCD_dm10_M",\
"h_tau2FRnt_QCD_dm11_VVVL","h_tau2FRnt_QCD_dm11_M"\
]

fileData=ROOT.TFile("Histo/HistoforFR_"+options.year+"/Tau.root","r")
fileMC=ROOT.TFile("Histo/HistoforFR_"+options.year+"/MC.root","r")
fileDataSub=ROOT.TFile("Histo/HistoforFR_"+options.year+"/DataSub.root","recreate")

ncat=32

for i in range (0,ncat):
   Data=fileData.Get(hist[i])
   for j in range(1,Data.GetSize()-1):
       if Data.GetBinContent(j)<1: Data.SetBinError(j,1.8)
   Data.Add(fileMC.Get(hist[i]),-1)
   for j in range(1,Data.GetSize()-1):
       if Data.GetBinContent(j)<0: Data.SetBinContent(j,0.0)
   Data.SetName(hist[i])
   fileDataSub.cd()
   Data.Write()

import ROOT
import re
from array import array
import argparse

parser = argparse.ArgumentParser()
#parser.add_argument('--tes', default="nominal", choices=['nominal', 'up', 'down'], help="TES?")
parser.add_argument('--year', default="2016", choices=['2016', '2017', '2018'], help="Year?")
options = parser.parse_args()

hist=[
"h_tauFR_QCD_dm0_VVVL","h_tauFR_QCD_dm0_M",
"h_tauFR_QCD_dm1_VVVL","h_tauFR_QCD_dm1_M",
"h_tauFR_QCD_dm10_VVVL","h_tauFR_QCD_dm10_M",
"h_tauFR_QCD_dm11_VVVL","h_tauFR_QCD_dm11_M",
"h_tauFRnt_QCD_dm0_VVVL","h_tauFRnt_QCD_dm0_M",
"h_tauFRnt_QCD_dm1_VVVL","h_tauFRnt_QCD_dm1_M",
"h_tauFRnt_QCD_dm10_VVVL","h_tauFRnt_QCD_dm10_M",
"h_tauFRnt_QCD_dm11_VVVL","h_tauFRnt_QCD_dm11_M",
"h_tau1FR_QCD_dm0_VVVL","h_tau1FR_QCD_dm0_M",
"h_tau1FR_QCD_dm1_VVVL","h_tau1FR_QCD_dm1_M",
"h_tau1FR_QCD_dm10_VVVL","h_tau1FR_QCD_dm10_M",
"h_tau1FR_QCD_dm11_VVVL","h_tau1FR_QCD_dm11_M",
"h_tau1FRnt_QCD_dm0_VVVL","h_tau1FRnt_QCD_dm0_M",
"h_tau1FRnt_QCD_dm1_VVVL","h_tau1FRnt_QCD_dm1_M",
"h_tau1FRnt_QCD_dm10_VVVL","h_tau1FRnt_QCD_dm10_M",
"h_tau1FRnt_QCD_dm11_VVVL","h_tau1FRnt_QCD_dm11_M",
"h_tau2FR_QCD_dm0_VVVL","h_tau2FR_QCD_dm0_M",
"h_tau2FR_QCD_dm1_VVVL","h_tau2FR_QCD_dm1_M",
"h_tau2FR_QCD_dm10_VVVL","h_tau2FR_QCD_dm10_M",
"h_tau2FR_QCD_dm11_VVVL","h_tau2FR_QCD_dm11_M",
"h_tau2FRnt_QCD_dm0_VVVL","h_tau2FRnt_QCD_dm0_M",
"h_tau2FRnt_QCD_dm1_VVVL","h_tau2FRnt_QCD_dm1_M",
"h_tau2FRnt_QCD_dm10_VVVL","h_tau2FRnt_QCD_dm10_M",
"h_tau2FRnt_QCD_dm11_VVVL","h_tau2FRnt_QCD_dm11_M"
]

fileData=ROOT.TFile("output_tautau_2018/Tau.root","r")
fileMC=ROOT.TFile("output_tautau_2018/DY.root","r")
fileDataSub=ROOT.TFile("output_tautau_2018/DataSub.root","recreate")

ncat=16*3

for i in range (0,ncat):
   print hist[i]
   Data=fileData.Get(hist[i])
   Data.Add(fileMC.Get(hist[i]),-1)
   Data.SetName(hist[i])
   fileDataSub.cd()
   Data.Write()


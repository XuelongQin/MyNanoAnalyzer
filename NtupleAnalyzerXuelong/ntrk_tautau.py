from ROOT import RDataFrame, TFile, TChain, TTree, TFile, TH1D, TLorentzVector,TCanvas
import numpy as np
import sys
from math import cos,sin,sqrt,pi
import ROOT
import time as timer
time_start=timer.time()
ROOT.gSystem.Load('./lib/RDFfunc.so')
ROOT.gInterpreter.Declare('#include "./lib/basic_sel.h"')
ROOT.gInterpreter.Declare('#include "./lib/GetPFtrk.h"')
ROOT.gInterpreter.Declare('#include "./lib/Correction.h"')


year = sys.argv[1]
sample = sys.argv[2]


isdata = True

if (sample!="dataA" and sample!="dataB" and sample!="dataC" and sample!="dataD"):
    isdata=False

arbre = TChain("Events")
arbre.Add("/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/tautau/RDF/{}.root".format(sample))

df = RDataFrame(arbre)


##Acoplanarity weights only for DY samples
if (isdata):
    df = df.Define("genAco","-99.0").Define("Acoweight","1.0").Define("npvsweight","1.0")
else: 
    if sample=="DYJetsToLL_M-50":
        df = df.Define("genAco","GetGenAco(nZGenCand,ZGenCand_phi,Acopl)").Define("Acoweight","Get_Aweight(genAco)").Define("npvsweight","Get_npvsweight(PV_npvs)")
    else:
        df = df.Define("genAco","-99.0").Define("Acoweight","1.0").Define("npvsweight","Get_npvsweight(PV_npvs)")

##make new  mutrack and tautrack collection, choose highest pt muon track as mutrack, choose same dz as tautrack 
print ("Choose all tautrk")

print ("Choose tautrk")
df =df.Define("tautrkcut","(ChargedPFCandidates_dz==LepCand_trk1dz[tau1index] && ChargedPFCandidates_pt==LepCand_trk1pt[tau1index] && ChargedPFCandidates_eta==LepCand_trk1eta[tau1index] && ChargedPFCandidates_phi==LepCand_trk1phi[tau1index])\
    || (ChargedPFCandidates_dz==LepCand_trk2dz[tau1index] && ChargedPFCandidates_pt==LepCand_trk2pt[tau1index] && ChargedPFCandidates_eta==LepCand_trk2eta[tau1index] && ChargedPFCandidates_phi==LepCand_trk2phi[tau1index])\
    || (ChargedPFCandidates_dz==LepCand_trk3dz[tau1index] && ChargedPFCandidates_pt==LepCand_trk3pt[tau1index] && ChargedPFCandidates_eta==LepCand_trk3eta[tau1index] && ChargedPFCandidates_phi==LepCand_trk3phi[tau1index])\
    || (ChargedPFCandidates_dz==LepCand_trk1dz[tau2index] && ChargedPFCandidates_pt==LepCand_trk1pt[tau2index] && ChargedPFCandidates_eta==LepCand_trk1eta[tau2index] && ChargedPFCandidates_phi==LepCand_trk1phi[tau2index])\
    || (ChargedPFCandidates_dz==LepCand_trk2dz[tau2index] && ChargedPFCandidates_pt==LepCand_trk2pt[tau2index] && ChargedPFCandidates_eta==LepCand_trk2eta[tau2index] && ChargedPFCandidates_phi==LepCand_trk2phi[tau2index])\
    || (ChargedPFCandidates_dz==LepCand_trk3dz[tau2index] && ChargedPFCandidates_pt==LepCand_trk3pt[tau2index] && ChargedPFCandidates_eta==LepCand_trk3eta[tau2index] && ChargedPFCandidates_phi==LepCand_trk3phi[tau2index])")\
    .Define("nFinalTautrk","Sum(tautrkcut)")\
    .Define("FinalTautrk_pt","ChargedPFCandidates_pt[tautrkcut]")\
    .Define("FinalTautrk_eta","ChargedPFCandidates_eta[tautrkcut]")\
    .Define("FinalTautrk_phi","ChargedPFCandidates_phi[tautrkcut]")\
    .Define("FinalTautrk_dz","ChargedPFCandidates_dz[tautrkcut]")\
    .Define("FinalTautrk_pdgId","ChargedPFCandidates_pdgId[tautrkcut]")\
    .Define("FinalTautrk_mass","ChargedPFCandidates_mass[tautrkcut]")\
    .Define("FinalTautrk_isMatchedToGenHS","ChargedPFCandidates_isMatchedToGenHS[tautrkcut]")\
    .Define("FinalTautrk_ditaudz","Compute_ditaudz(FinalTautrk_dz,PV_z,zvtxll1)")

###Remove tautau trk
print ("Remove tautau trk from PFCandidates")
df = df.Define("PFtrkcut", "Getntrkcut_tautau(ChargedPFCandidates_pt, ChargedPFCandidates_eta, ChargedPFCandidates_phi, ChargedPFCandidates_dz,\
     FinalTautrk_pt,  FinalTautrk_eta,  FinalTautrk_phi,  FinalTautrk_dz)")\
    .Define("nPFtrk", "Sum(PFtrkcut)")\
    .Define("PFtrk_pt","ChargedPFCandidates_pt[PFtrkcut]")\
    .Define("PFtrk_eta","ChargedPFCandidates_eta[PFtrkcut]")\
    .Define("PFtrk_phi","ChargedPFCandidates_phi[PFtrkcut]")\
    .Define("PFtrk_dz","ChargedPFCandidates_dz[PFtrkcut]")\
    .Define("PFtrk_pdgId","ChargedPFCandidates_pdgId[PFtrkcut]")\
    .Define("PFtrk_mass","ChargedPFCandidates_mass[PFtrkcut]")\
    .Define("PFtrk_isMatchedToGenHS","ChargedPFCandidates_isMatchedToGenHS[PFtrkcut]")
    

###Get ditaudz (putrk need to add BS correction)
print ("Calculate ditaudz")
if (isdata):
    df = df.Define("PFtrk_ditaudz","Compute_ditaudz(PFtrk_dz,PV_z,zvtxll1)")
else: 
    df = df.Define("PFtrk_ditaudz","Get_BScor_ditaudz(PFtrk_dz,PFtrk_isMatchedToGenHS,PV_z,zvtxll1)")
    
df = df.Define("Trkcut","PFtrk_ditaudz<0.05")\
    .Define("nTrk", "Sum(Trkcut)")\
    .Define("Trk_pt","PFtrk_pt[Trkcut]")\
    .Define("Trk_eta","PFtrk_eta[Trkcut]")\
    .Define("Trk_phi","PFtrk_phi[Trkcut]")\
    .Define("Trk_dz","PFtrk_dz[Trkcut]")\
    .Define("Trk_pdgId","PFtrk_pdgId[Trkcut]")\
    .Define("Trk_mass","PFtrk_mass[Trkcut]")\
    .Define("Trk_isMatchedToGenHS","PFtrk_isMatchedToGenHS[Trkcut]")\
    .Define("Trk_ditaudz","PFtrk_ditaudz[Trkcut]")

###Apply nputrack correction
print ("Apply nputrack correctionz")
if (isdata):
    df = df.Define("nPUtrk", "0")\
    .Define("nPUtrkweight","1.0")
else: 
    df = df.Define("PUtrkcut","Trk_isMatchedToGenHS==0")\
    .Define("nPUtrk", "Sum(PUtrkcut)")\
    .Define("nPUtrkweight","Get_ntpuweight(nPUtrk,zvtxll1)")\


###Apply nHStrk correction(only for DY)
print ("Apply nHStrack correctionz")
if (isdata):
    df = df.Define("nHStrk","0")\
        .Define("nHStrkweight","1.0")
else:
    if (sample=="DYJetsToLL_M-50"):
        df = df.Define("HStrkcut","Trk_isMatchedToGenHS==1")\
            .Define("nHStrk","Sum(HStrkcut)")\
            .Define("nHStrkweight","Get_ntHSweight(nHStrk,genAco)")
    else:
        df = df.Define("HStrkcut","Trk_isMatchedToGenHS==1")\
            .Define("nHStrk","Sum(HStrkcut)")\
            .Define("nHStrkweight","1.0") 
    
columns = ROOT.std.vector("string")()
for c in ("run","luminosityBlock","event",\
    "nFinalTautrk","FinalTautrk_pt","FinalTautrk_eta","FinalTautrk_phi","FinalTautrk_mass","FinalTautrk_pdgId","FinalTautrk_dz","FinalTautrk_isMatchedToGenHS","FinalTautrk_ditaudz",\
    "nTrk","Trk_pt","Trk_eta","Trk_phi","Trk_mass","Trk_pdgId","Trk_dz","Trk_isMatchedToGenHS","Trk_ditaudz",\
    "nPUtrk","nHStrk","Acoweight","npvsweight","nPUtrkweight","nHStrkweight","genAco"):
    columns.push_back(c)
    
df.Snapshot("ntrktuple","/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/tautau/RDF/{}_friend.root".format(sample),columns)
time_end=timer.time()
print('totally cost',time_end-time_start)    


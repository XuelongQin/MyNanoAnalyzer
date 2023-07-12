from ROOT import RDataFrame, TFile, TChain, TTree, TFile, TH1D, TLorentzVector,TCanvas,TH1, TH2, TH1F
import numpy as np
from ROOT.RDF import TH1DModel, TH2DModel
import sys
from math import cos,sin,sqrt,pi
sys.path.append("..")
from pyFunc.gethisto import variable
import ROOT
import time as timer
time_start=timer.time()
ROOT.gInterpreter.AddIncludePath('/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/lib')
ROOT.gInterpreter.Declare('#include "basic_sel.h"')
ROOT.gInterpreter.Declare('#include "GetPFtrk.h"')
ROOT.gInterpreter.Declare('#include "Correction.h"')
ROOT.gInterpreter.Declare('#include "ApplyFR.h"')
ROOT.gSystem.Load('/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/lib/RDFfunc.so')
ROOT.EnableImplicitMT()

TH1.SetDefaultSumw2(True)
TH2.SetDefaultSumw2(True)

def gethisto(cut,cutname,variable,df):
    histo=0
    hmodel = TH1DModel("h_{}_{}".format(variable.name,cutname),"",variable.nbins,variable.binning)
    if cutname=="anti":
        histo = df.Filter(cut).Define("qcdFR","GetFR_mutau_qcd(LepCand_DecayMode[tauindex],taupt,nTrk, isMuonTauTrigger,\"{}\")".format(year))\
        .Define("wFR","GetFR_mutau_w(LepCand_DecayMode[tauindex],taupt,nTrk, isMuonTauTrigger,\"{}\")".format(year)).Define("wfraction", "Getwfraction(mvis, mtrans,\"{}\")".format(year))\
        .Define("FR", "GetFR_mutau(qcdFR,wFR,wfraction)").Define("plotweight","totalweight*FR").Histo1D(hmodel,variable.name,"plotweight").GetPtr()
    else:
        histo = df.Filter(cut).Histo1D(hmodel,variable.name,"totalweight").GetPtr()
    return histo
        
mvis = variable("mvis","m_{vis}",int(32),np.array([0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,400,500],dtype=float))
taupt = variable("taupt","#tau p_{T}",int(34),np.array([30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,84,88,92,96,100,105,110,115,120],dtype=float))
mupt = variable("mupt","#mu p_{T}",int(39),np.array([20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,84,88,92,96,100,105,110,115,120],dtype=float))
Aco = variable("Acopl","acoplanarity",int(40),np.arange(0,1.025,0.025,dtype=float))
mtranse = variable("mtrans","m_{T}(#mu,MET)",int(36),np.arange(0,185,5,dtype=float))
nTrk = variable("nTrk","N_{tracks}",int(50),np.arange(0,102,2,dtype=float))
MET = variable("MET_pt","MET",int(19),np.array([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,80,90,100,110,120],dtype=float))
taueta = variable("taueta","#tau #eta", int(25), np.arange(-2.5,2.7,0.2,dtype=float))
mueta = variable("mueta","#mu #eta", int(25), np.arange(-2.5,2.7,0.2,dtype=float))
#variablelist = [mvis,taupt,mupt,Aco,mtranse]
variablelist = [mvis,taupt,mupt,Aco,mtranse,nTrk,MET,taueta,mueta]

year = sys.argv[1]
sample = sys.argv[2]
name = sys.argv[3]
realcut = " && LepCand_gen[tauindex]!=0"
if "SingleMuon" in sample:
    realcut = ""

weight = "xsweight*SFweight*Acoweight*npvs_weight*nPUtrkweight*nHStrkweight*eeSF"


print ("year is ", year , " sample is ", sample, " weight is ", weight)
df= RDataFrame("Events","/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuples_mutau_{}_basicsel/{}.root".format(year,sample))
df = df.Define("totalweight",weight)
fout=0
if sample == "DY":
    fout = TFile("Histo/HistoInclu_{}/{}.root".format(year,name),"recreate")
else:
    fout = TFile("Histo/HistoInclu_{}/{}.root".format(year,sample),"recreate")
for var in variablelist:
    cut = "nTrk>=0 && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex] )||(taupt>32 && isMuonTauTrigger && LepCand_trgmatch[muindex])) && mvis>40"
    if year=="2016pre" or year=="2016post":
        cut = "nTrk>=0 && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>30 && isMuonTauTrigger && LepCand_trgmatch[muindex])) && mvis>40"
    if year=="2017":
        cut = "nTrk>=0 && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>32 && isMuonTauTrigger && LepCand_trgmatch[muindex] && LepCand_trgmatch[tauindex])) && mvis>40"
    print ("cut is ", cut)
    if var.name!="mtrans":
        cut = cut + " && mtrans<75"
    if name=="ZLL":
        cut = cut + " && LepCand_gen[tauindex]!=5"
    if name=="ZTT":
        cut = cut + " && LepCand_gen[tauindex]==5"
    cutiso = cut+" && isOS && is_isolated" + realcut
    cutnoniso = cut + " && isOS && !is_isolated" + realcut
    
    
    histoantiiso = gethisto(cutnoniso,"anti",var,df)
    histoiso = gethisto(cutiso,"",var,df)
    vardir = fout.mkdir(var.name)
    vardir.cd()
    histoantiiso.SetName("{}_anti".format(name))
    histoiso.SetName("{}".format(name))
    histoantiiso.Write()
    histoiso.Write()
fout.Close()
    
    
    
    
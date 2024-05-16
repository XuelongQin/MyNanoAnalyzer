from ROOT import RDataFrame, TFile, TChain, TTree, TFile, TH1D, TLorentzVector,TCanvas,TH1, TH2, TH1F
import numpy as np
from ROOT.RDF import TH1DModel, TH2DModel
import sys
from math import cos,sin,sqrt,pi
import ROOT
import time as timer
import ctypes
sys.path.append("..")
from pyFunc.gethisto_CR_mutau import df_withFR_anti, gethisto, df_withFR_anti_sys, gethisto_anti,DY_rescale
time_start=timer.time()
ROOT.gInterpreter.AddIncludePath('/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/lib')
ROOT.gInterpreter.Declare('#include "basic_sel.h"')
ROOT.gInterpreter.Declare('#include "GetPFtrk.h"')
ROOT.gInterpreter.Declare('#include "Correction.h"')
ROOT.gInterpreter.Declare('#include "ApplyFR.h"')
ROOT.gSystem.Load('/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/lib/RDFfunc.so')


TH1.SetDefaultSumw2(True)
TH2.SetDefaultSumw2(True)


nbins = int(10)
binning = np.array([0,1,2,3,4,5,6,7,8,9,10],dtype=float)


year = sys.argv[1]
sample = sys.argv[2]
name = sys.argv[3]

def DYscale(histo):
    error = ctypes.c_double(1.0)
    total = histo.IntegralAndError(0, histo.GetNbinsX() + 1, error)
    error = error.value
    histo.SetBinContent(1,0.0248*total)
    histo.SetBinError(1,0.0248*error) 
    histo.SetBinContent(2,0.0512*total)
    histo.SetBinError(2,0.0512*error) 
    histo.SetBinContent(3,0.072*total)
    histo.SetBinError(3,0.072*error)
    histo.SetBinContent(4,0.091*total)
    histo.SetBinError(4,0.091*error)
    histo.SetBinContent(5,0.101*total)
    histo.SetBinError(5,0.101*error)
    histo.SetBinContent(6,0.120*total)
    histo.SetBinError(6,0.120*error)
    histo.SetBinContent(7,0.130*total)
    histo.SetBinError(7,0.130*error)
    histo.SetBinContent(8,0.133*total)
    histo.SetBinError(8,0.133*error)
    histo.SetBinContent(9,0.140*total)
    histo.SetBinError(9,0.140*error)
    histo.SetBinContent(10,0.141*total)
    histo.SetBinError(10,0.141*error)

realcut = " && LepCand_gen[tauindex]!=0"
if "SingleMuon" in sample:
    realcut = ""

weight = "xsweight*SFweight*Acoweight*nPUtrkweight*nHStrkweight*eeSF*tausfcor"

fake_uncertainty = ["CMS_jetfake_tauptextrap_qcd_mt_dm0_yearDown", "CMS_jetfake_tauptextrap_qcd_mt_dm0_yearUp", \
    "CMS_jetfake_tauptextrap_qcd_mt_dm1_yearDown", "CMS_jetfake_tauptextrap_qcd_mt_dm1_yearUp", \
    "CMS_jetfake_tauptextrap_qcd_mt_dm10_yearDown", "CMS_jetfake_tauptextrap_qcd_mt_dm10_yearUp", \
    "CMS_jetfake_tauptextrap_qcd_mt_dm11_yearDown", "CMS_jetfake_tauptextrap_qcd_mt_dm11_yearUp", \
    "CMS_jetfake_ntracksextrap_qcd_mt_dm0Down", "CMS_jetfake_ntracksextrap_qcd_mt_dm0Up", \
    "CMS_jetfake_ntracksextrap_qcd_mt_dm1Down", "CMS_jetfake_ntracksextrap_qcd_mt_dm1Up", \
    "CMS_jetfake_ntracksextrap_qcd_mt_dm10Down", "CMS_jetfake_ntracksextrap_qcd_mt_dm10Up", \
    "CMS_jetfake_ntracksextrap_qcd_mt_dm11Down", "CMS_jetfake_ntracksextrap_qcd_mt_dm11Up", \
    "CMS_jetfake_tauptextrap_w_mt_dm0_yearDown", "CMS_jetfake_tauptextrap_w_mt_dm0_yearUp", \
    "CMS_jetfake_tauptextrap_w_mt_dm1_yearDown", "CMS_jetfake_tauptextrap_w_mt_dm1_yearUp", \
    "CMS_jetfake_tauptextrap_w_mt_dm10_yearDown", "CMS_jetfake_tauptextrap_w_mt_dm10_yearUp", \
    "CMS_jetfake_tauptextrap_w_mt_dm11_yearDown", "CMS_jetfake_tauptextrap_w_mt_dm11_yearUp", \
    "CMS_jetfake_ntracksextrap_w_mt_dm0Down", "CMS_jetfake_ntracksextrap_w_mt_dm0Up", \
    "CMS_jetfake_ntracksextrap_w_mt_dm1Down", "CMS_jetfake_ntracksextrap_w_mt_dm1Up", \
    "CMS_jetfake_ntracksextrap_w_mt_dm10Down", "CMS_jetfake_ntracksextrap_w_mt_dm10Up", \
    "CMS_jetfake_ntracksextrap_w_mt_dm11Down", "CMS_jetfake_ntracksextrap_w_mt_dm11Up", \
    ]


fake_func = ["GetFR_mutau_qcd_sys_taupt(qcdFR,taupt,0,LepCand_DecayMode[tauindex],true)",\
    "GetFR_mutau_qcd_sys_taupt(qcdFR,taupt,0,LepCand_DecayMode[tauindex],false)",\
    "GetFR_mutau_qcd_sys_taupt(qcdFR,taupt,1,LepCand_DecayMode[tauindex],true)",\
    "GetFR_mutau_qcd_sys_taupt(qcdFR,taupt,1,LepCand_DecayMode[tauindex],false)",\
    "GetFR_mutau_qcd_sys_taupt(qcdFR,taupt,10,LepCand_DecayMode[tauindex],true)",\
    "GetFR_mutau_qcd_sys_taupt(qcdFR,taupt,10,LepCand_DecayMode[tauindex],false)",\
    "GetFR_mutau_qcd_sys_taupt(qcdFR,taupt,11,LepCand_DecayMode[tauindex],true)",\
    "GetFR_mutau_qcd_sys_taupt(qcdFR,taupt,11,LepCand_DecayMode[tauindex],false)",\
    "GetFR_mutau_qcd_sys_ntrk_dm(qcdFR,0,LepCand_DecayMode[tauindex],true,\"{}\")".format(year),\
    "GetFR_mutau_qcd_sys_ntrk_dm(qcdFR,0,LepCand_DecayMode[tauindex],false,\"{}\")".format(year),\
    "GetFR_mutau_qcd_sys_ntrk_dm(qcdFR,1,LepCand_DecayMode[tauindex],true,\"{}\")".format(year),\
    "GetFR_mutau_qcd_sys_ntrk_dm(qcdFR,1,LepCand_DecayMode[tauindex],false,\"{}\")".format(year),\
    "GetFR_mutau_qcd_sys_ntrk_dm(qcdFR,10,LepCand_DecayMode[tauindex],true,\"{}\")".format(year),\
    "GetFR_mutau_qcd_sys_ntrk_dm(qcdFR,10,LepCand_DecayMode[tauindex],false,\"{}\")".format(year),\
    "GetFR_mutau_qcd_sys_ntrk_dm(qcdFR,11,LepCand_DecayMode[tauindex],true,\"{}\")".format(year),\
    "GetFR_mutau_qcd_sys_ntrk_dm(qcdFR,11,LepCand_DecayMode[tauindex],false,\"{}\")".format(year),\
    "GetFR_mutau_w_sys_taupt(wFR,taupt,0,LepCand_DecayMode[tauindex],true)",\
    "GetFR_mutau_w_sys_taupt(wFR,taupt,0,LepCand_DecayMode[tauindex],false)",\
    "GetFR_mutau_w_sys_taupt(wFR,taupt,1,LepCand_DecayMode[tauindex],true)",\
    "GetFR_mutau_w_sys_taupt(wFR,taupt,1,LepCand_DecayMode[tauindex],false)",\
    "GetFR_mutau_w_sys_taupt(wFR,taupt,10,LepCand_DecayMode[tauindex],true)",\
    "GetFR_mutau_w_sys_taupt(wFR,taupt,10,LepCand_DecayMode[tauindex],false)",\
    "GetFR_mutau_w_sys_taupt(wFR,taupt,11,LepCand_DecayMode[tauindex],true)",\
    "GetFR_mutau_w_sys_taupt(wFR,taupt,11,LepCand_DecayMode[tauindex],false)",\
    "GetFR_mutau_w_sys_ntrk_dm(wFR,0,LepCand_DecayMode[tauindex],true,\"{}\")".format(year),\
    "GetFR_mutau_w_sys_ntrk_dm(wFR,0,LepCand_DecayMode[tauindex],false,\"{}\")".format(year),\
    "GetFR_mutau_w_sys_ntrk_dm(wFR,1,LepCand_DecayMode[tauindex],true,\"{}\")".format(year),\
    "GetFR_mutau_w_sys_ntrk_dm(wFR,1,LepCand_DecayMode[tauindex],false,\"{}\")".format(year),\
    "GetFR_mutau_w_sys_ntrk_dm(wFR,10,LepCand_DecayMode[tauindex],true,\"{}\")".format(year),\
    "GetFR_mutau_w_sys_ntrk_dm(wFR,10,LepCand_DecayMode[tauindex],false,\"{}\")".format(year),\
    "GetFR_mutau_w_sys_ntrk_dm(wFR,11,LepCand_DecayMode[tauindex],true,\"{}\")".format(year),\
    "GetFR_mutau_w_sys_ntrk_dm(wFR,11,LepCand_DecayMode[tauindex],false,\"{}\")".format(year),\
    ]

print ("year is ", year , " sample is ", sample, " name is ", name)
df= RDataFrame("Events","/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuples_mutau_{}_basicsel/{}.root".format(year,sample))
df = df.Define("totalweight",weight)
fout=0
year4 = year

if year=="2016pre": year4="2016preVFP"
if year=="2016post": year4="2016postVFP"

print(" year is ", year, " year4 is ", year4)

if sample == "DY":
    fout = TFile("Histo/HistoCR45_anti_{}/{}.root".format(year,name),"recreate")
else:
    fout = TFile("Histo/HistoCR45_anti_{}/{}.root".format(year,sample),"recreate")
    
mt_4cut = "(nTrk<10) && (Acopl<0.015) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex] )||(taupt>32 && isMuonTauTrigger )) && mvis>40 && mvis<100  && mtrans<75"
#DYshapecut = "(nTrk<10) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex] )||(taupt>32 && isMuonTauTrigger )) && mvis>40 && mvis<100  && mtrans<75"

if year=="2016pre" or year=="2016post":
    mt_4cut = "(nTrk<10) && (Acopl<0.015) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>30 && isMuonTauTrigger )) && mvis>40 && mvis<100  && mtrans<75 "
    #DYshapecut = "(nTrk<10)  && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>30 && isMuonTauTrigger )) && mvis>40 && mvis<100  && mtrans<75"

if year=="2017":
    mt_4cut = "(nTrk<10) && (Acopl<0.015)  && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex] )||(taupt>32 && isMuonTauTrigger )) && mvis>40 && mvis<100  && mtrans<75 "
    #DYshapecut = "(nTrk<10)  && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>32 && isMuonTauTrigger )) && mvis>40 && mvis<100  && mtrans<75"

mt_5cut = "(nTrk<10) && (Acopl<0.015) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex] )||(taupt>32 && isMuonTauTrigger )) && mvis>40 && mvis>=100  && mtrans<75"
#DYshapecut = "(nTrk<10) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex] )||(taupt>32 && isMuonTauTrigger )) && mvis>40 && mvis<100  && mtrans<75"

if year=="2016pre" or year=="2016post":
    mt_5cut = "(nTrk<10) && (Acopl<0.015) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>30 && isMuonTauTrigger )) && mvis>40 && mvis>=100  && mtrans<75 "
    #DYshapecut = "(nTrk<10)  && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>30 && isMuonTauTrigger )) && mvis>40 && mvis<100  && mtrans<75"

if year=="2017":
    mt_5cut = "(nTrk<10) && (Acopl<0.015)  && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex] )||(taupt>32 && isMuonTauTrigger )) && mvis>40 && mvis>=100  && mtrans<75 "
    #DYshapecut = "(nTrk<10)  && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>32 && isMuonTauTrigger )) && mvis>40 && mvis<100  && mtrans<75"


isocut = "&& isOS && is_isolated"
anticut = "&& isOS && !is_isolated"

cutZTT = " && LepCand_gen[tauindex]==5"
cutZLL = " && LepCand_gen[tauindex]!=5"
dir4 = fout.mkdir("mt_4")
dir5 = fout.mkdir("mt_5")

mt_4cut = mt_4cut + realcut
mt_5cut = mt_5cut + realcut
#DYshapecut = DYshapecut + realcut

if (name=="ZTT"):
    #DYshapecut = DYshapecut+cutZTT
    mt_4cut = mt_4cut + cutZTT
    mt_5cut = mt_5cut + cutZTT
if (name=="ZLL"):
    #DYshapecut = DYshapecut+cutZLL
    mt_4cut = mt_4cut + cutZLL 
    mt_5cut = mt_5cut + cutZLL

histo_mt4_anti=0
histo_mt5_anti=0

if sample == "DY":
    #df_DYhigh_anti = df_withFR_anti(df.Filter(DYshapecut+anticut),year)
    df_mt4_anti = df_withFR_anti(df.Filter(mt_4cut+anticut),year)
    df_mt5_anti = df_withFR_anti(df.Filter(mt_5cut+anticut),year)
    
    #histoDYhigh_anti = gethisto_anti(df_DYhigh_anti,"DYhigh_anti", nbins, binning)
    histoDY_mt4_anti = gethisto_anti(df_mt4_anti,"mt4_anti","nTrk", nbins, binning)
    histoDY_mt5_anti = gethisto_anti(df_mt5_anti,"mt5_anti","nTrk", nbins, binning)
    DYscale(histoDY_mt4_anti)
    DYscale(histoDY_mt5_anti)
    #histo_mt4_anti = DY_rescale(histoDYhigh_anti,histoDY_mt4_anti,0.194)

    print ("mt_4 basic ", histoDY_mt4_anti.Integral())
    print ("mt_5 basic ", histoDY_mt5_anti.Integral())

    dir4.cd()
    histoDY_mt4_anti.SetName("{}_anti".format(name))
    histoDY_mt4_anti.Write()
    dir5.cd()
    histoDY_mt5_anti.SetName("{}_anti".format(name))
    histoDY_mt5_anti.Write()
    
    ### now systematic part
    for i in range(len(fake_uncertainty)):
        uncertainty_name = str.replace(fake_uncertainty[i],"year",year4)
        if ("qcd" in uncertainty_name):
            sysflag = 0
        elif ("wfraction" in uncertainty_name):
            sysflag = 2
        else:
            sysflag = 1
        #df_DYhigh_anti_sys = df_withFR_anti_sys(df_DYhigh_anti, sysflag, fake_func[i])
        df_mt4_anti_sys = df_withFR_anti_sys(df_mt4_anti, sysflag, fake_func[i])
        df_mt5_anti_sys = df_withFR_anti_sys(df_mt5_anti, sysflag, fake_func[i])
        #histoDYhigh_anti_sys = gethisto_anti(df_DYhigh_anti_sys,"DYhigh_anti_{}".format(uncertainty_name), nbins, binning)
        histoDY_mt4_anti_sys = gethisto_anti(df_mt4_anti_sys,"mt4_anti_{}".format(uncertainty_name),"nTrk", nbins, binning)
        histoDY_mt5_anti_sys = gethisto_anti(df_mt5_anti_sys,"mt5_anti_{}".format(uncertainty_name),"nTrk", nbins, binning)
        DYscale(histoDY_mt4_anti_sys)
        DYscale(histoDY_mt5_anti_sys)
        #histo_mt4_anti_sys = DY_rescale(histoDYhigh_anti_sys,histoDY_mt4_anti_sys,0.194)
        print ("mt_4 ", uncertainty_name, " ", histoDY_mt4_anti_sys.Integral())
        print ("mt_5 ", uncertainty_name, " ", histoDY_mt5_anti_sys.Integral())
        dir4.cd()
        histoDY_mt4_anti_sys.SetName("{}_anti_{}".format(name,uncertainty_name))
        histoDY_mt4_anti_sys.Write()
        dir5.cd()
        histoDY_mt5_anti_sys.SetName("{}_anti_{}".format(name,uncertainty_name))
        histoDY_mt5_anti_sys.Write()

else:
    df_mt4_anti = df_withFR_anti(df.Filter(mt_4cut+anticut),year)
    histo_mt4_anti = gethisto_anti(df_mt4_anti,"mt4_anti","nTrk", nbins, binning)
    print ("mt_4 basic ", histo_mt4_anti.Integral())
    dir4.cd()
    histo_mt4_anti.SetName("{}_anti".format(name))
    histo_mt4_anti.Write()

    df_mt5_anti = df_withFR_anti(df.Filter(mt_5cut+anticut),year)
    histo_mt5_anti = gethisto_anti(df_mt5_anti,"mt5_anti","nTrk", nbins, binning)
    print ("mt_5 basic ", histo_mt5_anti.Integral())
    dir5.cd()
    histo_mt5_anti.SetName("{}_anti".format(name))
    histo_mt5_anti.Write()

    ### now systematic part
    for i in range(len(fake_uncertainty)):
        uncertainty_name = str.replace(fake_uncertainty[i],"year",year4)
        if ("qcd" in uncertainty_name):
            sysflag = 0
        elif ("wfraction" in uncertainty_name):
            sysflag = 2
        else:
            sysflag = 1
        df_mt4_anti_sys = df_withFR_anti_sys(df_mt4_anti, sysflag, fake_func[i])
        histo_mt4_anti_sys = gethisto_anti(df_mt4_anti_sys,"mt4_anti_{}".format(uncertainty_name),"nTrk", nbins, binning)
        print ("mt_4 ", uncertainty_name, " ", histo_mt4_anti_sys.Integral())
        dir4.cd()
        histo_mt4_anti_sys.SetName("{}_anti_{}".format(name,uncertainty_name))
        histo_mt4_anti_sys.Write()
        df_mt5_anti_sys = df_withFR_anti_sys(df_mt5_anti, sysflag, fake_func[i])
        histo_mt5_anti_sys = gethisto_anti(df_mt5_anti_sys,"mt5_anti_{}".format(uncertainty_name),"nTrk", nbins, binning)
        print ("mt_5 ", uncertainty_name, " ", histo_mt5_anti_sys.Integral())
        dir5.cd()
        histo_mt5_anti_sys.SetName("{}_anti_{}".format(name,uncertainty_name))
        histo_mt5_anti_sys.Write()
fout.Close()

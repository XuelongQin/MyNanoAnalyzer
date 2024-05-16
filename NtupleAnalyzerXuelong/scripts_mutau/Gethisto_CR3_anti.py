from ROOT import RDataFrame, TFile, TChain, TTree, TFile, TH1D, TLorentzVector,TCanvas,TH1, TH2, TH1F
import numpy as np
from ROOT.RDF import TH1DModel, TH2DModel
import sys
from math import cos,sin,sqrt,pi
import ROOT
import time as timer
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


nbins = int(8)
binning = np.array([0.0,0.015,0.03,0.045,0.06,0.1,0.20,0.50,1.0],dtype=float)


year = sys.argv[1]
sample = sys.argv[2]
name = sys.argv[3]

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
    fout = TFile("Histo/HistoCR3_anti_{}/{}.root".format(year,name),"recreate")
else:
    fout = TFile("Histo/HistoCR3_anti_{}/{}.root".format(year,sample),"recreate")
    
mt_3cut = "((nTrk==0)||(nTrk==1)) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex] )||(taupt>32 && isMuonTauTrigger)) && mvis>40 && mvis<100  && mtrans<75 "
DYshapecut = "(nTrk<10) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex] )||(taupt>32 && isMuonTauTrigger )) && mvis>40 && mvis<100  && mtrans<75"

if year=="2016pre" or year=="2016post":
    mt_3cut = "((nTrk==0)||(nTrk==1))  && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>30 && isMuonTauTrigger )) && mvis>40 && mvis<100  && mtrans<75 "
    DYshapecut = "(nTrk<10)  && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>30 && isMuonTauTrigger )) && mvis>40 && mvis<100  && mtrans<75"

if year=="2017":
    mt_3cut = "((nTrk==0)||(nTrk==1))  && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex] )||(taupt>32 && isMuonTauTrigger )) && mvis>40 && mvis<100  && mtrans<75 "
    DYshapecut = "(nTrk<10)  && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>32 && isMuonTauTrigger )) && mvis>40 && mvis<100  && mtrans<75"


isocut = "&& isOS && is_isolated"
anticut = "&& isOS && !is_isolated"

cutZTT = " && LepCand_gen[tauindex]==5"
cutZLL = " && LepCand_gen[tauindex]!=5"
dir3 = fout.mkdir("mt_3")

mt_3cut = mt_3cut + realcut
DYshapecut = DYshapecut + realcut

if (name=="ZTT"):
    DYshapecut = DYshapecut+cutZTT
    mt_3cut = mt_3cut + cutZTT
if (name=="ZLL"):
    DYshapecut = DYshapecut+cutZLL
    mt_3cut = mt_3cut + cutZLL 

histo_mt3_anti=0

'''if sample == "DY":
    df_DYhigh_anti = df_withFR_anti(df.Filter(DYshapecut+anticut),year)
    df_mt3_anti = df_withFR_anti(df.Filter(mt_3cut+anticut),year)
    
    histoDYhigh_anti = gethisto_anti(df_DYhigh_anti,"DYhigh_anti","Acopl", nbins, binning)
    histoDY_mt3_anti = gethisto_anti(df_mt3_anti,"mt3_anti","Acopl", nbins, binning)

    histo_mt3_anti = DY_rescale(histoDYhigh_anti,histoDY_mt3_anti,0.194)

    print ("mt_3 basic ", histo_mt3_anti.Integral())

    dir3.cd()
    histo_mt3_anti.SetName("{}_anti".format(name))
    histo_mt3_anti.Write()
    
    ### now systematic part
    for i in range(len(fake_uncertainty)):
        uncertainty_name = str.replace(fake_uncertainty[i],"year",year4)
        if ("qcd" in uncertainty_name):
            sysflag = 0
        elif ("wfraction" in uncertainty_name):
            sysflag = 2
        else:
            sysflag = 1
        df_DYhigh_anti_sys = df_withFR_anti_sys(df_DYhigh_anti, sysflag, fake_func[i])
        df_mt3_anti_sys = df_withFR_anti_sys(df_mt3_anti, sysflag, fake_func[i])
        histoDYhigh_anti_sys = gethisto_anti(df_DYhigh_anti_sys,"DYhigh_anti_{}".format(uncertainty_name),"Acopl", nbins, binning)
        histoDY_mt3_anti_sys = gethisto_anti(df_mt3_anti_sys,"mt3_anti_{}".format(uncertainty_name),"Acopl", nbins, binning)
        histo_mt3_anti_sys = DY_rescale(histoDYhigh_anti_sys,histoDY_mt3_anti_sys,0.194)
        print ("mt_3 ", uncertainty_name, " ", histo_mt3_anti_sys.Integral())
        dir3.cd()
        histo_mt3_anti_sys.SetName("{}_anti_{}".format(name,uncertainty_name))
        histo_mt3_anti_sys.Write()

else:
    '''
df_mt3_anti = df_withFR_anti(df.Filter(mt_3cut+anticut),year)
histo_mt3_anti = gethisto_anti(df_mt3_anti,"mt3_anti","Acopl", nbins, binning)
print ("mt_3 basic ", histo_mt3_anti.Integral())
dir3.cd()
histo_mt3_anti.SetName("{}_anti".format(name))
histo_mt3_anti.Write()

### now systematic part
for i in range(len(fake_uncertainty)):
    uncertainty_name = str.replace(fake_uncertainty[i],"year",year4)
    if ("qcd" in uncertainty_name):
        sysflag = 0
    elif ("wfraction" in uncertainty_name):
        sysflag = 2
    else:
        sysflag = 1
    df_mt3_anti_sys = df_withFR_anti_sys(df_mt3_anti, sysflag, fake_func[i])
    histo_mt3_anti_sys = gethisto_anti(df_mt3_anti_sys,"mt3_anti_{}".format(uncertainty_name),"Acopl", nbins, binning)
    print ("mt_3 ", uncertainty_name, " ", histo_mt3_anti_sys.Integral())
    dir3.cd()
    histo_mt3_anti_sys.SetName("{}_anti_{}".format(name,uncertainty_name))
    histo_mt3_anti_sys.Write()
fout.Close()

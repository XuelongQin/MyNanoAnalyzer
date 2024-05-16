from ROOT import RDataFrame, TFile, TChain, TTree, TFile, TH1D, TLorentzVector,TCanvas,TH1, TH2, TH1F
import numpy as np
from ROOT.RDF import TH1DModel, TH2DModel
import sys
from math import cos,sin,sqrt,pi
import ROOT
import time as timer
sys.path.append("..")
from pyFunc.gethisto_SR_tautau import df_withFR_anti, gethisto, df_withFR_anti_sys, gethisto_anti,DY_rescale
time_start=timer.time()
ROOT.gInterpreter.AddIncludePath('/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/lib')
ROOT.gInterpreter.Declare('#include "basic_sel.h"')
ROOT.gInterpreter.Declare('#include "GetPFtrk.h"')
ROOT.gInterpreter.Declare('#include "Correction.h"')
ROOT.gInterpreter.Declare('#include "ApplyFR.h"')
ROOT.gSystem.Load('/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/lib/RDFfunc.so')


TH1.SetDefaultSumw2(True)
TH2.SetDefaultSumw2(True)


nbins = int(5)
binning = np.array([70,85,100,150,200,250],dtype=float)

year = sys.argv[1]
sample = sys.argv[2]
name = sys.argv[3]

realcutleading = " && LepCand_gen[tau1index]!=0"
realcutsubleading = " && LepCand_gen[tau2index]!=0"
realcutdouble = "&& (LepCand_gen[tau1index]!=0 || LepCand_gen[tau2index]!=0)"
if "Tau" in sample:
    realcutleading = ""
    realcutsubleading = ""
    realcutdouble = ""
    

weight = "xsweight*SFweight*Acoweight*nPUtrkweight*nHStrkweight*eeSF*tausfcor"

fake_uncertainty = ["CMS_jetfake_tauptextrap_qcd_tt_dm0_yearDown", "CMS_jetfake_tauptextrap_qcd_tt_dm0_yearUp", \
    "CMS_jetfake_tauptextrap_qcd_tt_dm1_yearDown", "CMS_jetfake_tauptextrap_qcd_tt_dm1_yearUp", \
    "CMS_jetfake_tauptextrap_qcd_tt_dm10_yearDown", "CMS_jetfake_tauptextrap_qcd_tt_dm10_yearUp", \
    "CMS_jetfake_tauptextrap_qcd_tt_dm11_yearDown", "CMS_jetfake_tauptextrap_qcd_tt_dm11_yearUp", \
    "CMS_jetfake_ntracksextrap_qcd_tt_dm0Down", "CMS_jetfake_ntracksextrap_qcd_tt_dm0Up", \
    "CMS_jetfake_ntracksextrap_qcd_tt_dm1Down", "CMS_jetfake_ntracksextrap_qcd_tt_dm1Up", \
    "CMS_jetfake_ntracksextrap_qcd_tt_dm10Down", "CMS_jetfake_ntracksextrap_qcd_tt_dm10Up", \
    "CMS_jetfake_ntracksextrap_qcd_tt_dm11Down", "CMS_jetfake_ntracksextrap_qcd_tt_dm11Up", \
    ]

fake_func = ["GetFR_tautau_qcd_sys_taupt(qcdFR,taukpt,0,LepCand_DecayMode[tauindex],true)",\
    "GetFR_tautau_qcd_sys_taupt(qcdFR,taukpt,0,LepCand_DecayMode[tauindex],false)",\
    "GetFR_tautau_qcd_sys_taupt(qcdFR,taukpt,1,LepCand_DecayMode[tauindex],true)",\
    "GetFR_tautau_qcd_sys_taupt(qcdFR,taukpt,1,LepCand_DecayMode[tauindex],false)",\
    "GetFR_tautau_qcd_sys_taupt(qcdFR,taukpt,10,LepCand_DecayMode[tauindex],true)",\
    "GetFR_tautau_qcd_sys_taupt(qcdFR,taukpt,10,LepCand_DecayMode[tauindex],false)",\
    "GetFR_tautau_qcd_sys_taupt(qcdFR,taukpt,11,LepCand_DecayMode[tauindex],true)",\
    "GetFR_tautau_qcd_sys_taupt(qcdFR,taukpt,11,LepCand_DecayMode[tauindex],false)",\
    "GetFR_tautau_qcd_sys_ntrk_dm(qcdFR,0,LepCand_DecayMode[tauindex],true,leading,nTrk,\"{}\")".format(year),\
    "GetFR_tautau_qcd_sys_ntrk_dm(qcdFR,0,LepCand_DecayMode[tauindex],false,leading,nTrk,\"{}\")".format(year),\
    "GetFR_tautau_qcd_sys_ntrk_dm(qcdFR,1,LepCand_DecayMode[tauindex],true,leading,nTrk,\"{}\")".format(year),\
    "GetFR_tautau_qcd_sys_ntrk_dm(qcdFR,1,LepCand_DecayMode[tauindex],false,leading,nTrk,\"{}\")".format(year),\
    "GetFR_tautau_qcd_sys_ntrk_dm(qcdFR,10,LepCand_DecayMode[tauindex],true,leading,nTrk,\"{}\")".format(year),\
    "GetFR_tautau_qcd_sys_ntrk_dm(qcdFR,10,LepCand_DecayMode[tauindex],false,leading,nTrk,\"{}\")".format(year),\
    "GetFR_tautau_qcd_sys_ntrk_dm(qcdFR,11,LepCand_DecayMode[tauindex],true,leading,nTrk,\"{}\")".format(year),\
    "GetFR_tautau_qcd_sys_ntrk_dm(qcdFR,11,LepCand_DecayMode[tauindex],false,leading,nTrk,\"{}\")".format(year),\
]

print ("year is ", year , " sample is ", sample, " name is ", name)
df= RDataFrame("Events","/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuples_tautau_{}_basicsel/{}.root".format(year,sample))
df = df.Define("totalweight",weight)
fout=0
year4 = year

if year=="2016pre": year4="2016preVFP"
if year=="2016post": year4="2016postVFP"

if sample == "DY":
    fout = TFile("Histo/HistoCR_anti_{}/{}.root".format(year,name),"recreate")
else:
    fout = TFile("Histo/HistoCR_anti_{}/{}.root".format(year,sample),"recreate")
    
tt_2cut = "((nTrk==3)||(nTrk==4)) && (Acopl<0.015) && tau1pt>40 && tau2pt>40 && mvis>40 && mvis<500 "
DYshapecut = "(nTrk<10) && (Acopl<0.015) && tau1pt>40 && tau2pt>40 && mvis>40 && mvis<500 "

#if year == "2017":
#    tt_0cut = "(nTrk==0) && (Acopl<0.015) && tau1pt>40 && tau2pt>40 && mvis>40 && LepCand_trgmatch[tau1index] && LepCand_trgmatch[tau2index]"
#    tt_1cut = "(nTrk==1) && (Acopl<0.015) && tau1pt>40 && tau2pt>40 && mvis>40 && LepCand_trgmatch[tau1index] && LepCand_trgmatch[tau2index]"
#    DYshapecut = "(nTrk<10) && (Acopl<0.015) && tau1pt>40 && tau2pt>40 && mvis>40 && LepCand_trgmatch[tau1index] && LepCand_trgmatch[tau2index]"
    

anticutleading = "&& isOS && !leading_isolated && subleading_isolated "
anticutsubleading = "&& isOS && leading_isolated && !subleading_isolated "
anticutdouble = "&& isOS && !leading_isolated && !subleading_isolated "

cutZTT = " "
dir2 = fout.mkdir("tt_2")

anticutleading  = anticutleading  + realcutleading
anticutsubleading  = anticutsubleading + realcutsubleading
anticutdouble = anticutdouble  + realcutdouble

if (name=="ZTT"):
    DYshapecut = DYshapecut+cutZTT
    
if sample == "DY":
    df_DYhigh_antileading = df_withFR_anti(df.Filter(DYshapecut+anticutleading),1,year)
    df_DYhigh_antisubleading = df_withFR_anti(df.Filter(DYshapecut+anticutsubleading),2,year)
    df_DYhigh_antidouble = df_withFR_anti(df.Filter(DYshapecut+anticutdouble),0,year)
    
    df_tt2_antileading = df_withFR_anti(df.Filter(tt_2cut+anticutleading),1,year)
    df_tt2_antisubleading = df_withFR_anti(df.Filter(tt_2cut+anticutsubleading),2,year)
    df_tt2_antidouble= df_withFR_anti(df.Filter(tt_2cut+anticutdouble),0,year)
    

    histoDYhigh_antileading = gethisto_anti(df_DYhigh_antileading,"DYhigh_antileading", nbins, binning)
    histoDYhigh_antisubleading = gethisto_anti(df_DYhigh_antisubleading,"DYhigh_antisubleading", nbins, binning)
    histoDYhigh_antidouble = gethisto_anti(df_DYhigh_antidouble,"DYhigh_antidouble", nbins, binning)
    
    histoDY_tt2_antileading = gethisto_anti(df_tt2_antileading,"tt2_antileading", nbins, binning)
    histoDY_tt2_antisubleading = gethisto_anti(df_tt2_antisubleading,"tt2_antisubleading", nbins, binning)
    histoDY_tt2_antidouble = gethisto_anti(df_tt2_antidouble,"tt2_antidouble", nbins, binning)
    
    histo_tt2_antileading = DY_rescale(histoDYhigh_antileading,histoDY_tt2_antileading,0.194)
    histo_tt2_antisubleading = DY_rescale(histoDYhigh_antisubleading,histoDY_tt2_antisubleading,0.194)
    histo_tt2_antidouble= DY_rescale(histoDYhigh_antidouble,histoDY_tt2_antidouble,0.194)
    
    print ("tt_2 basic antileading ", histo_tt2_antileading.Integral(), " antisubleading ", histo_tt2_antisubleading.Integral()," antidouble ", histo_tt2_antidouble.Integral() )
    dir2.cd()
    histo_tt2_antileading.SetName("{}_antileading".format(name))
    histo_tt2_antisubleading.SetName("{}_antisubleading".format(name))
    histo_tt2_antidouble.SetName("{}_antidouble".format(name))
    histo_tt2_antileading.Write()
    histo_tt2_antisubleading.Write()
    histo_tt2_antidouble.Write()
    
    ### now systematic part
    for i in range(len(fake_uncertainty)):
        uncertainty_name = str.replace(fake_uncertainty[i],"year",year4)
        df_DYhigh_antileading_sys = df_withFR_anti_sys(df_DYhigh_antileading, 1, fake_func[i])
        df_DYhigh_antisubleading_sys = df_withFR_anti_sys(df_DYhigh_antisubleading, 2, fake_func[i])
        df_DYhigh_antidouble_sys = df_withFR_anti_sys(df_DYhigh_antidouble, 0, fake_func[i])
        
        df_tt2_antileading_sys = df_withFR_anti_sys(df_tt2_antileading, 1, fake_func[i])
        df_tt2_antisubleading_sys = df_withFR_anti_sys(df_tt2_antisubleading, 2, fake_func[i])
        df_tt2_antidouble_sys = df_withFR_anti_sys(df_tt2_antidouble, 0, fake_func[i])
        
        histoDYhigh_antileading_sys = gethisto_anti(df_DYhigh_antileading_sys,"DYhigh_antileading_{}".format(uncertainty_name), nbins, binning)
        histoDYhigh_antisubleading_sys = gethisto_anti(df_DYhigh_antisubleading_sys,"DYhigh_antisubleading_{}".format(uncertainty_name), nbins, binning)
        histoDYhigh_antidouble_sys = gethisto_anti(df_DYhigh_antidouble_sys,"DYhigh_antidouble_{}".format(uncertainty_name), nbins, binning)
        
        histoDY_tt2_antileading_sys = gethisto_anti(df_tt2_antileading_sys,"tt2_antileading_{}".format(uncertainty_name), nbins, binning)
        histoDY_tt2_antisubleading_sys = gethisto_anti(df_tt2_antisubleading_sys,"tt2_antisubleading_{}".format(uncertainty_name), nbins, binning)
        histoDY_tt2_antidouble_sys = gethisto_anti(df_tt2_antidouble_sys,"tt2_antidouble_{}".format(uncertainty_name), nbins, binning)
        
        histo_tt2_antileading_sys = DY_rescale(histoDYhigh_antileading_sys,histoDY_tt2_antileading_sys,0.194)
        histo_tt2_antisubleading_sys = DY_rescale(histoDYhigh_antisubleading_sys,histoDY_tt2_antisubleading_sys,0.194)
        histo_tt2_antidouble_sys = DY_rescale(histoDYhigh_antidouble_sys,histoDY_tt2_antidouble_sys,0.194)
        
        print ("tt_2 ", uncertainty_name, " antileading ", histo_tt2_antileading_sys.Integral()," antisubleading ", histo_tt2_antisubleading_sys.Integral()," antidouble ", histo_tt2_antidouble_sys.Integral())
        
        dir2.cd()
        histo_tt2_antileading_sys.SetName("{}_antileading_{}".format(name,uncertainty_name))
        histo_tt2_antisubleading_sys.SetName("{}_antisubleading_{}".format(name,uncertainty_name))
        histo_tt2_antidouble_sys.SetName("{}_antidouble_{}".format(name,uncertainty_name))
        histo_tt2_antileading_sys.Write()
        histo_tt2_antisubleading_sys.Write()
        histo_tt2_antidouble_sys.Write()
        
else:
    
    df_tt2_antileading = df_withFR_anti(df.Filter(tt_2cut+anticutleading),1,year)
    df_tt2_antisubleading = df_withFR_anti(df.Filter(tt_2cut+anticutsubleading),2,year)
    df_tt2_antidouble= df_withFR_anti(df.Filter(tt_2cut+anticutdouble),0,year)
    #columns0 = ROOT.std.vector("string")()
    #columns1 = ROOT.std.vector("string")()
    #for c in ( "tau1pt", "tau2pt", "totalweight", "FR"):
    #    columns0.push_back(c)
    #    columns1.push_back(c)
    #columns1.push_back("FR1")
    #columns1.push_back("FR2")
    
    '''df_tt0_antileading.Snapshot("Events","./test/{}test_antileading_tt0.root".format(sample),columns0)
    df_tt0_antisubleading.Snapshot("Events","./test/{}test_antisubleading_tt0.root".format(sample),columns0)
    df_tt0_antidouble.Snapshot("Events","./test/{}test_antidouble_tt0.root".format(sample),columns1)
    
    df_tt1_antileading.Snapshot("Events","./test/{}test_antileading_tt1.root".format(sample),columns0)
    df_tt1_antisubleading.Snapshot("Events","./test/{}test_antisubleading_tt1.root".format(sample),columns0)
    df_tt1_antidouble.Snapshot("Events","./test/{}test_antidouble_tt1.root".format(sample),columns1)'''
    
    histo_tt2_antileading = gethisto_anti(df_tt2_antileading,"tt2_antileading", nbins, binning)
    histo_tt2_antisubleading = gethisto_anti(df_tt2_antisubleading,"tt2_antisubleading", nbins, binning)
    histo_tt2_antidouble = gethisto_anti(df_tt2_antidouble,"tt2_antidouble", nbins, binning)

    print ("tt_2 basic antileading ", histo_tt2_antileading.Integral(), " antisubleading ", histo_tt2_antisubleading.Integral()," antidouble ", histo_tt2_antidouble.Integral() )
    
    dir2.cd()
    histo_tt2_antileading.SetName("{}_antileading".format(name))
    histo_tt2_antisubleading.SetName("{}_antisubleading".format(name))
    histo_tt2_antidouble.SetName("{}_antidouble".format(name))
    histo_tt2_antileading.Write()
    histo_tt2_antisubleading.Write()
    histo_tt2_antidouble.Write()

    ### now systematic part
    for i in range(len(fake_uncertainty)):
        #continue
        uncertainty_name = str.replace(fake_uncertainty[i],"year",year4)
        
        df_tt2_antileading_sys = df_withFR_anti_sys(df_tt2_antileading, 1, fake_func[i])
        df_tt2_antisubleading_sys = df_withFR_anti_sys(df_tt2_antisubleading, 2, fake_func[i])
        df_tt2_antidouble_sys = df_withFR_anti_sys(df_tt2_antidouble, 0, fake_func[i])
        
        
        histo_tt2_antileading_sys = gethisto_anti(df_tt2_antileading_sys,"tt2_antileading_{}".format(uncertainty_name), nbins, binning)
        histo_tt2_antisubleading_sys = gethisto_anti(df_tt2_antisubleading_sys,"tt2_antisubleading_{}".format(uncertainty_name), nbins, binning)
        histo_tt2_antidouble_sys = gethisto_anti(df_tt2_antidouble_sys,"tt2_antidouble_{}".format(uncertainty_name), nbins, binning)
        
        print ("tt_2 ", uncertainty_name, " antileading ", histo_tt2_antileading_sys.Integral()," antisubleading ", histo_tt2_antisubleading_sys.Integral()," antidouble ", histo_tt2_antidouble_sys.Integral())
        
        dir2.cd()
        histo_tt2_antileading_sys.SetName("{}_antileading_{}".format(name,uncertainty_name))
        histo_tt2_antisubleading_sys.SetName("{}_antisubleading_{}".format(name,uncertainty_name))
        histo_tt2_antidouble_sys.SetName("{}_antidouble_{}".format(name,uncertainty_name))
        histo_tt2_antileading_sys.Write()
        histo_tt2_antisubleading_sys.Write()
        histo_tt2_antidouble_sys.Write()
        
fout.Close()


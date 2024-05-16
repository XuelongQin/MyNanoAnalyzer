from ROOT import RDataFrame, TFile, TChain, TTree, TFile, TH1D, TLorentzVector,TCanvas,TH1, TH2, TH1F
import numpy as np
from ROOT.RDF import TH1DModel, TH2DModel
import sys
from math import cos,sin,sqrt,pi
import ROOT
import time as timer
import ctypes
sys.path.append("..")
from pyFunc.gethisto_CR_tautau import df_sys,gethisto,DY_rescale
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


nbins = int(8)
binning = np.array([0.0,0.015,0.03,0.045,0.06,0.1,0.20,0.50,1.0],dtype=float)


year = sys.argv[1]
sample = sys.argv[2]
name = sys.argv[3]

realcut = " && LepCand_gen[tau1index]!=0 && LepCand_gen[tau2index]!=0 "
if "Tau" in sample:
    realcut = ""
    
weight = "xsweight*SFweight*Acoweight*nPUtrkweight*nHStrkweight*eeSF*tausfcor"
if "GGTT" in name:
    if name == "GGTT":
        weight = "xsweight*SFweight*Acoweight*nPUtrkweight*nHStrkweight*eeSF*tausfcor*TauG2Weights_ceBRe_0p0"
    elif "Im" in name:
        weight = "xsweight*SFweight*Acoweight*nPUtrkweight*nHStrkweight*eeSF*tausfcor*TauG2Weights_ceBIm"+name[7:]
    else:
        weight = "xsweight*SFweight*Acoweight*nPUtrkweight*nHStrkweight*eeSF*tausfcor*TauG2Weights_ceBRe"+name[4:]
    print ("name is ", name, " weight is ", weight)

uncertainty = ["_CMS_tauid_stat1_dm0_yearDown","_CMS_tauid_stat1_dm0_yearUp","_CMS_tauid_stat1_dm1_yearDown","_CMS_tauid_stat1_dm1_yearUp","_CMS_tauid_stat1_dm10_yearDown","_CMS_tauid_stat1_dm10_yearUp","_CMS_tauid_stat1_dm11_yearDown","_CMS_tauid_stat1_dm11_yearUp",\
    "_CMS_tauid_stat2_dm0_yearDown","_CMS_tauid_stat2_dm0_yearUp","_CMS_tauid_stat2_dm1_yearDown","_CMS_tauid_stat2_dm1_yearUp","_CMS_tauid_stat2_dm10_yearDown","_CMS_tauid_stat2_dm10_yearUp","_CMS_tauid_stat2_dm11_yearDown","_CMS_tauid_stat2_dm11_yearUp", \
    "_CMS_tauid_syst_allerasDown", "_CMS_tauid_syst_allerasUp","_CMS_tauid_syst_yearDown", "_CMS_tauid_syst_yearUp", \
    "_CMS_tauid_syst_dm0_yearDown","_CMS_tauid_syst_dm0_yearUp","_CMS_tauid_syst_dm1_yearDown","_CMS_tauid_syst_dm1_yearUp","_CMS_tauid_syst_dm10_yearDown","_CMS_tauid_syst_dm10_yearUp","_CMS_tauid_syst_dm11_yearDown","_CMS_tauid_syst_dm11_yearUp",\
    "_CMS_ditautrg_dm0_yearDown","_CMS_ditautrg_dm0_yearUp", "_CMS_ditautrg_dm1_yearDown","_CMS_ditautrg_dm1_yearUp","_CMS_ditautrg_3prong_yearDown","_CMS_ditautrg_3prong_yearUp",\
    "_CMS_pileup_yearDown","_CMS_pileup_yearUp","_CMS_taues_dm0_yearDown","_CMS_taues_dm0_yearUp","_CMS_taues_dm1_yearDown","_CMS_taues_dm1_yearUp","_CMS_taues_3prong_yearDown","_CMS_taues_3prong_yearUp"]

uncertainty_func = ["Gettauidsysweight_dm(0,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert0_down[tauindex])",\
    "Gettauidsysweight_dm(0,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert0_up[tauindex])",\
    "Gettauidsysweight_dm(1,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert0_down[tauindex])",\
    "Gettauidsysweight_dm(1,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert0_up[tauindex])",\
    "Gettauidsysweight_dm(10,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert0_down[tauindex])",\
    "Gettauidsysweight_dm(10,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert0_up[tauindex])",\
    "Gettauidsysweight_dm(11,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert0_down[tauindex])",\
    "Gettauidsysweight_dm(11,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert0_up[tauindex])",\
    "Gettauidsysweight_dm(0,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert1_down[tauindex])",\
    "Gettauidsysweight_dm(0,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert1_up[tauindex])",\
    "Gettauidsysweight_dm(1,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert1_down[tauindex])",\
    "Gettauidsysweight_dm(1,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert1_up[tauindex])",\
    "Gettauidsysweight_dm(10,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert1_down[tauindex])",\
    "Gettauidsysweight_dm(10,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert1_up[tauindex])",\
    "Gettauidsysweight_dm(11,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert1_down[tauindex])",\
    "Gettauidsysweight_dm(11,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_uncert1_up[tauindex])",\
    "Gettauidsysweight(LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_syst_alleras_down[tauindex])",\
    "Gettauidsysweight(LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_syst_alleras_up[tauindex])",\
    "Gettauidsysweight(LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_syst_era_down[tauindex])",\
    "Gettauidsysweight(LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_syst_era_up[tauindex])",\
    "Gettauidsysweight_dm(0,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_syst_dm_era_down[tauindex])",\
    "Gettauidsysweight_dm(0,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_syst_dm_era_up[tauindex])",\
    "Gettauidsysweight_dm(1,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_syst_dm_era_down[tauindex])",\
    "Gettauidsysweight_dm(1,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_syst_dm_era_up[tauindex])",\
    "Gettauidsysweight_dm(10,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_syst_dm_era_down[tauindex])",\
    "Gettauidsysweight_dm(10,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_syst_dm_era_up[tauindex])",\
    "Gettauidsysweight_dm(11,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_syst_dm_era_down[tauindex])",\
    "Gettauidsysweight_dm(11,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_tauidMsf[tauindex],LepCand_tauidMsf_syst_dm_era_up[tauindex])",\
    "Getditautrigweight(0,LepCand_DecayMode[tauindex],LepCand_tautriggersf[tauindex],LepCand_tautriggersf_down[tauindex])",\
    "Getditautrigweight(0,LepCand_DecayMode[tauindex],LepCand_tautriggersf[tauindex],LepCand_tautriggersf_up[tauindex])",\
    "Getditautrigweight(1,LepCand_DecayMode[tauindex],LepCand_tautriggersf[tauindex],LepCand_tautriggersf_down[tauindex])",\
    "Getditautrigweight(1,LepCand_DecayMode[tauindex],LepCand_tautriggersf[tauindex],LepCand_tautriggersf_up[tauindex])",\
    "Getditautrigweight(1011,LepCand_DecayMode[tauindex],LepCand_tautriggersf[tauindex],LepCand_tautriggersf_down[tauindex])",\
    "Getditautrigweight(1011,LepCand_DecayMode[tauindex],LepCand_tautriggersf[tauindex],LepCand_tautriggersf_up[tauindex])",\
    "Getpusysweight(puWeight,puWeightDown,1.0,1.0)",\
    "Getpusysweight(puWeight,puWeightUp,1.0,1.0)",\
    "Gettauessys(0,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_taues[tauindex],LepCand_taues_down[tauindex],my_tau)",\
    "Gettauessys(0,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_taues[tauindex],LepCand_taues_up[tauindex],my_tau)",\
    "Gettauessys(1,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_taues[tauindex],LepCand_taues_down[tauindex],my_tau)",\
    "Gettauessys(1,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_taues[tauindex],LepCand_taues_up[tauindex],my_tau)",\
    "Gettauessys(1011,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_taues[tauindex],LepCand_taues_down[tauindex],my_tau)",\
    "Gettauessys(1011,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_taues[tauindex],LepCand_taues_up[tauindex],my_tau)",\
    ]

uncertainty.append("_CMS_L1PrefiringDown")
uncertainty.append("_CMS_L1PrefiringUp")
uncertainty_func.append("GetL1PrefiringWeight(L1PreFiringWeight_Nom, L1PreFiringWeight_Dn)")
uncertainty_func.append("GetL1PrefiringWeight(L1PreFiringWeight_Nom, L1PreFiringWeight_Up)")

if "GGTT" in name or name=="GGWW" or name=="GGMM" or name=="GGEE":
    uncertainty.append("_CMS_elasticRescalingDown")
    uncertainty.append("_CMS_elasticRescalingUp")
    uncertainty_func.append("GeteeSFsysweight(eeSF,nTrk,true)")
    uncertainty_func.append("GeteeSFsysweight(eeSF,nTrk,false)")
if name=="ZTT" or name=="ZLL":
    uncertainty.append("_CMS_ISRDown")
    uncertainty.append("_CMS_ISRUp")
    uncertainty.append("_CMS_FSRDown")
    uncertainty.append("_CMS_FSRUp")
    uncertainty.append("_CMS_PDFDown")
    uncertainty.append("_CMS_PDFUp")
    uncertainty.append("_CMS_muR0p5_muF0p5")
    uncertainty.append("_CMS_muRDown")
    uncertainty.append("_CMS_muFDown")
    uncertainty.append("_CMS_muFUp")
    uncertainty.append("_CMS_muRUp")
    uncertainty.append("_CMS_muR2p0_muF2p0")
    uncertainty_func.append("GetPSsysweight(PSWeight[2],Acoweight_ps3,Acoweight)")
    uncertainty_func.append("GetPSsysweight(PSWeight[0],Acoweight_ps1,Acoweight)")
    uncertainty_func.append("GetPSsysweight(PSWeight[3],Acoweight_ps4,Acoweight)")
    uncertainty_func.append("GetPSsysweight(PSWeight[1],Acoweight_ps2,Acoweight)")
    uncertainty_func.append("GetPDFsysweight(LHEPdfWeight,true)")
    uncertainty_func.append("GetPDFsysweight(LHEPdfWeight,false)")
    uncertainty_func.append("GetScalesysweight(LHEScaleWeight[0],0.983,Acoweight_scale1,Acoweight)")
    uncertainty_func.append("GetScalesysweight(LHEScaleWeight[1],1.015,Acoweight_scale2,Acoweight)")
    uncertainty_func.append("GetScalesysweight(LHEScaleWeight[3],0.960,Acoweight_scale3,Acoweight)")
    uncertainty_func.append("GetScalesysweight(LHEScaleWeight[5],1.025,Acoweight_scale4,Acoweight)")
    uncertainty_func.append("GetScalesysweight(LHEScaleWeight[7],0.986,Acoweight_scale5,Acoweight)")
    uncertainty_func.append("GetScalesysweight(LHEScaleWeight[8],1.018,Acoweight_scale6,Acoweight)")
print ("year is ", year , " sample is ", sample, " name is ", name)
df= RDataFrame("Events","/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuples_tautau_{}_basicsel/{}.root".format(year,sample))
df = df.Define("totalweight",weight)
fout=0
year4 = year

if year=="2016pre": year4="2016preVFP"
if year=="2016post": year4="2016postVFP"

if sample == "DY":
    fout = TFile("Histo/HistoCR3_{}/{}.root".format(year,name),"recreate")
elif "GGToTauTau" in sample:
    if name == "GGTT":
        fout = TFile("Histo/HistoCR3_{}/{}.root".format(year,sample),"recreate")
    else: 
        fout = TFile("Histo/HistoCR3_{}/BSM/{}.root".format(year,name),"recreate")
else:
    fout = TFile("Histo/HistoCR3_{}/{}.root".format(year,sample),"recreate")
    
tt_3cut = "((nTrk==0)||(nTrk==1)) && tau1pt>40 && tau2pt>40 && mvis>40 && mvis<100 "
DYshapecut = "(nTrk<10) && tau1pt>40 && tau2pt>40 && mvis>40 && mvis<100 "

#if year=="2017":
#    tt_0cut = "(nTrk==0) && (Acopl<0.015) && tau1pt>40 && tau2pt>40 && mvis>40 && LepCand_trgmatch[tau1index] && LepCand_trgmatch[tau2index]"
#    tt_1cut = "(nTrk==1) && (Acopl<0.015) && tau1pt>40 && tau2pt>40 && mvis>40 && LepCand_trgmatch[tau1index] && LepCand_trgmatch[tau2index]"
#    DYshapecut = "(nTrk<10) && (Acopl<0.015) && tau1pt>40 && tau2pt>40 && mvis>40 && LepCand_trgmatch[tau1index] && LepCand_trgmatch[tau2index]"
    

isocut = "&& isOS && leading_isolated && subleading_isolated "

dir3 = fout.mkdir("tt_3")

tt_3cut = tt_3cut + realcut
DYshapecut = DYshapecut + realcut

'''if sample == "DY":
    df_DYhigh = df.Filter(DYshapecut+isocut)
    df_tt3 = df.Filter(tt_3cut+isocut)
    
    histoDYhigh = gethisto(df_DYhigh,"DYhigh","Acopl", nbins, binning)
    histoDY_tt3 = gethisto(df_tt3,"tt3","Acopl", nbins, binning)
    histo_tt3 = DY_rescale(histoDYhigh,histoDY_tt3,0.0501+0.0242)
    
    print ("tt_3 basic ", histo_tt3.Integral())
    
    dir3.cd()
    histo_tt3.SetName("{}".format(name))
    histo_tt3.Write()
    
    ### now systematic part
    for i in range(len(uncertainty)):
        uncertainty_name = str.replace(uncertainty[i],"year",year4)
        if ("taues" in uncertainty_name):
            sysflag = 2
        elif ("pileup" in uncertainty_name or "elasticRescaling" in uncertainty_name or "FSR" in uncertainty_name or "ISR" in uncertainty_name or "PDF" in uncertainty_name or "muF" in uncertainty_name or "muR" in uncertainty_name):
            sysflag = 1
        else:
            sysflag = 0
        df_DYhigh_sys = df_sys(df,DYshapecut+isocut, sysflag, uncertainty_func[i])
        df_tt3_sys = df_sys(df,tt_3cut+isocut, sysflag, uncertainty_func[i])
        histoDYhigh_sys = gethisto(df_DYhigh_sys,"DYhigh_{}".format(uncertainty_name),"Acopl", nbins, binning)
        histoDY_tt3_sys = gethisto(df_tt3_sys,"tt3_{}".format(uncertainty_name),"Acopl", nbins, binning)
        histo_tt3_sys = DY_rescale(histoDYhigh_sys,histoDY_tt3_sys,0.194)
        print ("tt_3 ", uncertainty_name, " ", histo_tt3_sys.Integral())
        dir3.cd()
        histo_tt3_sys.SetName("{}{}".format(name,uncertainty_name))
        histo_tt3_sys.Write()


else:'''
df_tt3 = df.Filter(tt_3cut+isocut)
histo_tt3 = gethisto(df_tt3,"tt3","Acopl", nbins, binning)
print ("tt_3 basic ", histo_tt3.Integral())
dir3.cd()
histo_tt3.SetName("{}".format(name))
histo_tt3.Write()

### now systematic part
if (name != "data_obs"):
    for i in range(len(uncertainty)):
        uncertainty_name = str.replace(uncertainty[i],"year",year4)
        if ("taues" in uncertainty_name):
            sysflag = 2
        elif ("pileup" in uncertainty_name or "elasticRescaling" in uncertainty_name or "FSR" in uncertainty_name or "ISR" in uncertainty_name or "PDF" in uncertainty_name or "muF" in uncertainty_name or "muR" in uncertainty_name):
            sysflag = 1
        else:
            sysflag = 0
        df_tt3_sys = df_sys(df,tt_3cut+isocut, sysflag, uncertainty_func[i])
        histo_tt3_sys = gethisto(df_tt3_sys,"tt3_{}".format(uncertainty_name),"Acopl", nbins, binning)
        print ("tt_3 ", uncertainty_name, " ", histo_tt3_sys.Integral())
        dir3.cd()
        histo_tt3_sys.SetName("{}{}".format(name,uncertainty_name))
        histo_tt3_sys.Write()
fout.Close()
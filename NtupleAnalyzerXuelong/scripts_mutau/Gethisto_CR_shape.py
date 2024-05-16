from ROOT import RDataFrame, TFile, TChain, TTree, TFile, TH1D, TLorentzVector,TCanvas,TH1, TH2, TH1F
import numpy as np
from ROOT.RDF import TH1DModel, TH2DModel
import sys
from math import cos,sin,sqrt,pi
import ROOT
import time as timer
import ctypes
sys.path.append("..")
from pyFunc.gethisto_SR_mutau import df_sys,gethisto,DY_rescale
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


nbins = int(5)
binning = np.array([55,70,85,100,150,200],dtype=float)

year = sys.argv[1]
sample = sys.argv[2]
name = sys.argv[3]

realcut = " && LepCand_gen[tauindex]!=0"
if "SingleMuon" in sample or "GGToTauTau" in sample:
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
        "_CMS_tauid_syst_allerasDown", "_CMS_tauid_syst_allerasUp","_CMS_tauid_syst_yearDown", "_CMS_tauid_syst_yearUp", 
        "_CMS_tauid_syst_dm0_yearDown","_CMS_tauid_syst_dm0_yearUp","_CMS_tauid_syst_dm1_yearDown","_CMS_tauid_syst_dm1_yearUp","_CMS_tauid_syst_dm10_yearDown","_CMS_tauid_syst_dm10_yearUp","_CMS_tauid_syst_dm11_yearDown","_CMS_tauid_syst_dm11_yearUp",\
        "_CMS_mutauFR_barrel_yearDown","_CMS_mutauFR_barrel_yearUp","_CMS_mutauFR_endcap_yearDown","_CMS_mutauFR_endcap_yearUp",\
        "_CMS_pileup_yearDown","_CMS_pileup_yearUp",\
        "_CMS_mutautrg_yearDown","_CMS_mutautrg_yearUp",\
        "_CMS_mutrg_systDown","_CMS_mutrg_systUp","_CMS_mutrg_stat_yearDown","_CMS_mutrg_stat_yearUp",\
        "_CMS_taues_dm0_yearDown","_CMS_taues_dm0_yearUp","_CMS_taues_dm1_yearDown","_CMS_taues_dm1_yearUp","_CMS_taues_3prong_yearDown","_CMS_taues_3prong_yearUp",\
        "_CMS_muId_systDown","_CMS_muId_systUp","_CMS_muId_stat_yearDown","_CMS_muId_stat_yearUp","_CMS_muIso_systDown","_CMS_muIso_systUp","_CMS_muIso_stat_yearDown","_CMS_muIso_stat_yearUp"]



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
        "Gettauantimusysweight(true,LepCand_gen[tauindex],LepCand_antimusf[tauindex], LepCand_antimusf_down[tauindex],taueta)",\
        "Gettauantimusysweight(true,LepCand_gen[tauindex],LepCand_antimusf[tauindex], LepCand_antimusf_up[tauindex],taueta)",\
        "Gettauantimusysweight(false,LepCand_gen[tauindex],LepCand_antimusf[tauindex], LepCand_antimusf_down[tauindex],taueta)",\
        "Gettauantimusysweight(false,LepCand_gen[tauindex],LepCand_antimusf[tauindex], LepCand_antimusf_up[tauindex],taueta)",\
        "Getpusysweight(puWeight,puWeightDown,1.0,1.0)",\
        "Getpusysweight(puWeight,puWeightUp,1.0,1.0)", \
        "Getmutautrgweight(isMuonTauTrigger,LepCand_tautriggersf[tauindex],0.98*LepCand_tautriggersf_down[tauindex])",\
        "Getmutautrgweight(isMuonTauTrigger,LepCand_tautriggersf[tauindex],1.02*LepCand_tautriggersf_up[tauindex])",\
        "Getsinglemutrgweight(isSingleMuonTrigger,mutrgsf,mutrgsf-mutrgsf_syst)",\
        "Getsinglemutrgweight(isSingleMuonTrigger,mutrgsf,mutrgsf+mutrgsf_syst)",\
        "Getsinglemutrgweight(isSingleMuonTrigger,mutrgsf,mutrgsf-mutrgsf_stat)",\
        "Getsinglemutrgweight(isSingleMuonTrigger,mutrgsf,mutrgsf+mutrgsf_stat)",\
        "Gettauessys(0,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_taues[tauindex],LepCand_taues_down[tauindex],my_tau)",\
        "Gettauessys(0,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_taues[tauindex],LepCand_taues_up[tauindex],my_tau)",\
        "Gettauessys(1,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_taues[tauindex],LepCand_taues_down[tauindex],my_tau)",\
        "Gettauessys(1,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_taues[tauindex],LepCand_taues_up[tauindex],my_tau)",\
        "Gettauessys(1011,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_taues[tauindex],LepCand_taues_down[tauindex],my_tau)",\
        "Gettauessys(1011,LepCand_DecayMode[tauindex],LepCand_gen[tauindex],LepCand_taues[tauindex],LepCand_taues_up[tauindex],my_tau)",\
        "Getmusysweight(muidsf,muidsf-muidsf_syst)",\
        "Getmusysweight(muidsf,muidsf+muidsf_syst)",\
        "Getmusysweight(muidsf,muidsf-muidsf_stat)",\
        "Getmusysweight(muidsf,muidsf+muidsf_stat)",\
        "Getmusysweight(muisosf,muisosf-muisosf_syst)",\
        "Getmusysweight(muisosf,muisosf+muisosf_syst)",\
        "Getmusysweight(muisosf,muisosf-muisosf_stat)",\
        "Getmusysweight(muisosf,muisosf+muisosf_stat)",\
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

year4 = year
if year=="2016pre": year4="2016preVFP"
if year=="2016post": year4="2016postVFP"

print ("year is ", year , " year4 is ", year4, " sample is ", sample, " name is ", name)
df= RDataFrame("Events","/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuples_mutau_{}_basicsel/{}.root".format(year,sample))
df = df.Define("totalweight",weight)
fout=0

if sample == "DY":
    fout = TFile("Histo/HistoCR_{}/{}.root".format(year,name),"recreate")
elif "GGToTauTau" in sample:
    if name == "GGTT":
        fout = TFile("Histo/HistoCR_{}/{}.root".format(year,sample),"recreate")
    else: 
        fout = TFile("Histo/HistoCR_{}/BSM/{}.root".format(year,name),"recreate")
else:
    fout = TFile("Histo/HistoCR_{}/{}.root".format(year,sample),"recreate")
    
mt_2cut = "((nTrk==3)||(nTrk==4)) && (Acopl<0.015) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex] )||(taupt>32 && isMuonTauTrigger)) && mvis>40 && mvis<500  && mtrans<75 "
DYshapecut = "(nTrk<10) && (Acopl<0.015) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex] )||(taupt>32 && isMuonTauTrigger )) && mvis>40 && mvis<500  && mtrans<75"

if year=="2016pre" or year=="2016post":
    mt_2cut = "((nTrk==3)||(nTrk==4)) && (Acopl<0.015) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>30 && isMuonTauTrigger )) && mvis>40 && mvis<500  && mtrans<75 "
    DYshapecut = "(nTrk<10) && (Acopl<0.015) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>30 && isMuonTauTrigger )) && mvis>40 && mvis<500  && mtrans<75"

if year=="2017":
    mt_2cut = "((nTrk==3)||(nTrk==4)) && (Acopl<0.015) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex] )||(taupt>32 && isMuonTauTrigger )) && mvis>40 && mvis<500  && mtrans<75 "
    DYshapecut = "(nTrk<10) && (Acopl<0.015) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>32 && isMuonTauTrigger )) && mvis>40 && mvis<500  && mtrans<75"


isocut = "&& isOS && is_isolated"
anticut = "&& isOS && !is_isolated"

cutZTT = " && LepCand_gen[tauindex]==5"
cutZLL = " && LepCand_gen[tauindex]!=5"
dir2 = fout.mkdir("mt_2")

mt_2cut = mt_2cut + realcut
DYshapecut = DYshapecut + realcut

if (name=="ZTT"):
    DYshapecut = DYshapecut+cutZTT
    mt_2cut = mt_2cut + cutZTT
if (name=="ZLL"):
    DYshapecut = DYshapecut+cutZLL
    mt_2cut = mt_2cut + cutZLL 

histo_mt2=0

if sample == "DY":
    df_DYhigh = df.Filter(DYshapecut+isocut)
    df_mt2 = df.Filter(mt_2cut+isocut)
    
    histoDYhigh = gethisto(df_DYhigh,"DYhigh", nbins, binning)
    histoDY_mt2 = gethisto(df_mt2,"mt2", nbins, binning)

    histo_mt2 = DY_rescale(histoDYhigh,histoDY_mt2,0.194)

    
    print ("mt_2 basic ", histo_mt2.Integral())
    dir2.cd()
    histo_mt2.SetName("{}".format(name))
    histo_mt2.Write()
    ### now systematic part
    for i in range(len(uncertainty)):
        uncertainty_name = str.replace(uncertainty[i],"year",year4)
        if ("taues" in uncertainty_name):
            sysflag = 1
        else:
            sysflag = 0
        df_DYhigh_sys = df_sys(df,DYshapecut+isocut, sysflag, uncertainty_func[i])
        df_mt2_sys = df_sys(df,mt_2cut+isocut, sysflag, uncertainty_func[i])
        histoDYhigh_sys = gethisto(df_DYhigh_sys,"DYhigh_{}".format(uncertainty_name), nbins, binning)
        histoDY_mt2_sys = gethisto(df_mt2_sys,"mt2_{}".format(uncertainty_name), nbins, binning)
        histo_mt2_sys = DY_rescale(histoDYhigh_sys,histoDY_mt2_sys,0.194)
        print ("mt_2 ", uncertainty_name, " ", uncertainty_func[i]," ", histo_mt2_sys.Integral())
        dir2.cd()
        histo_mt2_sys.SetName("{}{}".format(name,uncertainty_name))
        histo_mt2_sys.Write()

else:
    df_mt2 = df.Filter(mt_2cut+isocut)
    histo_mt2 = gethisto(df_mt2,"mt2", nbins, binning)
    print ("mt_2 basic ", histo_mt2.Integral())
    dir2.cd()
    histo_mt2.SetName("{}".format(name))
    histo_mt2.Write()
    
    
    ### now systematic part
    if (name != "data_obs"):
        for i in range(len(uncertainty)):
            uncertainty_name = str.replace(uncertainty[i],"year",year4)
            if ("taues" in uncertainty_name):
                sysflag = 1
            else:
                sysflag = 0
            df_mt2_sys = df_sys(df,mt_2cut+isocut, sysflag, uncertainty_func[i])
            histo_mt2_sys = gethisto(df_mt2_sys,"mt2_{}".format(uncertainty_name), nbins, binning)
            print ("mt_2 ", uncertainty_name, " ", uncertainty_func[i]," ", histo_mt2_sys.Integral())
            dir2.cd()
            histo_mt2_sys.SetName("{}{}".format(name,uncertainty_name))
            histo_mt2_sys.Write()
fout.Close()

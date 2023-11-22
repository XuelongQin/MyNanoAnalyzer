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
        weight = "xsweight*SFweight*Acoweight*nPUtrkweight*nHStrkweight*eeSF*tausfcor*TauG2Weights_ceBRe33_0p0"
    else:
        weight = "xsweight*SFweight*Acoweight*nPUtrkweight*nHStrkweight*eeSF*tausfcor*TauG2Weights_ceBRe33"+name[4:]
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

if "GGTT" in name or name=="GGWW":
    uncertainty.append("_CMS_elasticRescalingDown")
    uncertainty.append("_CMS_elasticRescalingUp")
    uncertainty_func.append("GeteeSFsysweight(eeSF,nTrk,true)")
    uncertainty_func.append("GeteeSFsysweight(eeSF,nTrk,false)")

year4 = year
if year=="2016pre": year4="2016preVFP"
if year=="2016post": year4="2016postVFP"

print ("year is ", year , " year4 is ", year4, " sample is ", sample, " name is ", name)
df= RDataFrame("Events","/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuples_mutau_{}_basicsel/{}.root".format(year,sample))
df = df.Define("totalweight",weight)
fout=0

if sample == "DY":
    fout = TFile("Histo/HistoSR_{}/{}.root".format(year,name),"recreate")
elif "GGToTauTau" in sample:
    if name == "GGTT":
        fout = TFile("Histo/HistoSR_{}/{}.root".format(year,sample),"recreate")
    else: 
        fout = TFile("Histo/HistoSR_{}/BSM/{}.root".format(year,name),"recreate")
else:
    fout = TFile("Histo/HistoSR_{}/{}.root".format(year,sample),"recreate")
    
mt_0cut = "(nTrk==0) && (Acopl<0.015) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex] )||(taupt>32 && isMuonTauTrigger && LepCand_trgmatch[muindex] )) && mvis>40 && mvis<500 && mtrans<75 "
mt_1cut = "(nTrk==1) && (Acopl<0.015) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex] )||(taupt>32 && isMuonTauTrigger && LepCand_trgmatch[muindex] )) && mvis>40 && mvis<500 && mtrans<75"
DYshapecut = "(nTrk<10) && (Acopl<0.015) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex] )||(taupt>32 && isMuonTauTrigger && LepCand_trgmatch[muindex] )) && mvis>40 && mvis<500 && mtrans<75"

if year=="2016pre" or year=="2016post":
    mt_0cut = "(nTrk==0) && (Acopl<0.015) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>30 && isMuonTauTrigger && LepCand_trgmatch[muindex])) && mvis>40 && mvis<500 && mtrans<75 "
    mt_1cut = "(nTrk==1) && (Acopl<0.015) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>30 && isMuonTauTrigger && LepCand_trgmatch[muindex])) && mvis>40 && mvis<500 && mtrans<75"
    DYshapecut = "(nTrk<10) && (Acopl<0.015) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>30 && isMuonTauTrigger && LepCand_trgmatch[muindex])) && mvis>40 && mvis<500 && mtrans<75"

if year=="2017":
    mt_0cut = "(nTrk==0) && (Acopl<0.015) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex] )||(taupt>32 && isMuonTauTrigger && LepCand_trgmatch[muindex] && LepCand_trgmatch[tauindex])) && mvis>40 && mvis<500 && mtrans<75 "
    mt_1cut = "(nTrk==1) && (Acopl<0.015) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>32 && isMuonTauTrigger && LepCand_trgmatch[muindex] && LepCand_trgmatch[tauindex])) && mvis>40 && mvis<500 && mtrans<75"
    DYshapecut = "(nTrk<10) && (Acopl<0.015) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>32 && isMuonTauTrigger && LepCand_trgmatch[muindex] && LepCand_trgmatch[tauindex])) && mvis>40 && mvis<500 && mtrans<75"


isocut = "&& isOS && is_isolated"
anticut = "&& isOS && !is_isolated"

cutZTT = " && LepCand_gen[tauindex]==5"
cutZLL = " && LepCand_gen[tauindex]!=5"
dir0 = fout.mkdir("mt_0")
dir1 = fout.mkdir("mt_1")

mt_0cut = mt_0cut + realcut
mt_1cut = mt_1cut + realcut
DYshapecut = DYshapecut + realcut

if (name=="ZTT"):
    DYshapecut = DYshapecut+cutZTT
    mt_0cut = mt_0cut + cutZTT
    mt_1cut = mt_1cut + cutZTT
if (name=="ZLL"):
    DYshapecut = DYshapecut+cutZLL
    mt_0cut = mt_0cut + cutZLL 
    mt_1cut = mt_1cut + cutZLL

histo_mt0=0
histo_mt1=0

if sample == "DY":
    df_DYhigh = df.Filter(DYshapecut+isocut)
    df_mt0 = df.Filter(mt_0cut+isocut)
    df_mt1 = df.Filter(mt_1cut+isocut)
    
    histoDYhigh = gethisto(df_DYhigh,"DYhigh", nbins, binning)
    histoDY_mt0 = gethisto(df_mt0,"mt0", nbins, binning)
    histoDY_mt1 = gethisto(df_mt1,"mt1", nbins, binning)

    '''err = ctypes.c_double(1.0)
    highvalue = histoDYhigh.IntegralAndError(1,10,err)
    print (name ," high ", highvalue, " +- ", err.value )
    mt_0value = histoDY_mt0.IntegralAndError(1,10,err)
    print (name ," mt_0 ", mt_0value, " +- ", err.value  )
    mt_1value = histoDY_mt1.IntegralAndError(1,10,err)
    print (name ," mt_1 ", mt_1value, " +- ", err.value  )
    
    '''

    histo_mt0 = DY_rescale(histoDYhigh,histoDY_mt0,0.0242)
    histo_mt1 = DY_rescale(histoDYhigh,histoDY_mt1,0.0501)

    
    print ("mt_0 basic ", histo_mt0.Integral())
    print ("mt_1 basic ", histo_mt1.Integral())
    dir0.cd()
    histo_mt0.SetName("{}".format(name))
    histo_mt0.Write()
    dir1.cd()
    histo_mt1.SetName("{}".format(name))
    histo_mt1.Write()
    ### now systematic part
    for i in range(len(uncertainty)):
        uncertainty_name = str.replace(uncertainty[i],"year",year4)
        if ("taues" in uncertainty_name):
            sysflag = 1
        else:
            sysflag = 0
        df_DYhigh_sys = df_sys(df,DYshapecut+isocut, sysflag, uncertainty_func[i])
        df_mt0_sys = df_sys(df,mt_0cut+isocut, sysflag, uncertainty_func[i])
        df_mt1_sys = df_sys(df,mt_1cut+isocut, sysflag, uncertainty_func[i])
        histoDYhigh_sys = gethisto(df_DYhigh_sys,"DYhigh_{}".format(uncertainty_name), nbins, binning)
        histoDY_mt0_sys = gethisto(df_mt0_sys,"mt0_{}".format(uncertainty_name), nbins, binning)
        histoDY_mt1_sys = gethisto(df_mt1_sys,"mt1_{}".format(uncertainty_name), nbins, binning)
        histo_mt0_sys = DY_rescale(histoDYhigh_sys,histoDY_mt0_sys,0.0242)
        histo_mt1_sys = DY_rescale(histoDYhigh_sys,histoDY_mt1_sys,0.0501)
        print ("mt_0 ", uncertainty_name, " ", uncertainty_func[i]," ", histo_mt0_sys.Integral())
        print ("mt_1 ", uncertainty_name, " ", uncertainty_func[i]," ", histo_mt1_sys.Integral())
        dir0.cd()
        histo_mt0_sys.SetName("{}{}".format(name,uncertainty_name))
        histo_mt0_sys.Write()
        dir1.cd()
        histo_mt1_sys.SetName("{}{}".format(name,uncertainty_name))
        histo_mt1_sys.Write()

else:
    df_mt0 = df.Filter(mt_0cut+isocut)
    df_mt1 = df.Filter(mt_1cut+isocut)
    histo_mt0 = gethisto(df_mt0,"mt0", nbins, binning)
    histo_mt1 = gethisto(df_mt1,"mt1", nbins, binning)
    print ("mt_0 basic ", histo_mt0.Integral())
    print ("mt_1 basic ", histo_mt1.Integral())
    dir0.cd()
    histo_mt0.SetName("{}".format(name))
    histo_mt0.Write()
    dir1.cd()
    histo_mt1.SetName("{}".format(name))
    histo_mt1.Write()
    
    
    ### now systematic part
    if (name != "data_obs"):
        for i in range(len(uncertainty)):
            uncertainty_name = str.replace(uncertainty[i],"year",year4)
            if ("taues" in uncertainty_name):
                sysflag = 1
            else:
                sysflag = 0
            df_mt0_sys = df_sys(df,mt_0cut+isocut, sysflag, uncertainty_func[i])
            df_mt1_sys = df_sys(df,mt_1cut+isocut, sysflag, uncertainty_func[i])
            histo_mt0_sys = gethisto(df_mt0_sys,"mt0_{}".format(uncertainty_name), nbins, binning)
            histo_mt1_sys = gethisto(df_mt1_sys,"mt1_{}".format(uncertainty_name), nbins, binning)
            print ("mt_0 ", uncertainty_name, " ", uncertainty_func[i]," ", histo_mt0_sys.Integral())
            print ("mt_1 ", uncertainty_name, " ", uncertainty_func[i]," ", histo_mt1_sys.Integral())
            dir0.cd()
            histo_mt0_sys.SetName("{}{}".format(name,uncertainty_name))
            histo_mt0_sys.Write()
            dir1.cd()
            histo_mt1_sys.SetName("{}{}".format(name,uncertainty_name))
            histo_mt1_sys.Write()
fout.Close()

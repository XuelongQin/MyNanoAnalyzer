from ROOT import RDataFrame, TFile, TChain, TTree, TFile, TH1D, TLorentzVector,TCanvas,TH1, TH2, TH1F
import numpy as np
from ROOT.RDF import TH1DModel, TH2DModel
import sys
from math import cos,sin,sqrt,pi
import ROOT
import time as timer
sys.path.append("..")
from pyFunc.gethisto_SR_mutau import df_sys,gethisto,DY_rescale,gethisto_BSM
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
binning = np.array([40,55,70,85,100,150,200,350,500],dtype=float)


year = sys.argv[1]
sample = "GGToTauTau_Ctb20"


def getBSMhisto(df, channel, name ):
    hisGGTTlist = []
    integer = 0
    decimals = 0
    ceBRname = ""
    TauG2weightsname = "TauG2Weights_ceBRe33_0p0"
    histo_normal = gethisto_BSM(df,channel,TauG2weightsname,nbins,binning)
    histo_normal.SetName("GGTT{}".format(name))
    print ("SM basic ", histo_normal.Integral())
    hisGGTTlist.append(histo_normal)
    for i in np.arange(-40.0,40.8,0.8):
        if (i<-0.4):
            integer = int(i-0.1)
        else:
            integer = int(i+0.1)
        decimals = int(round(abs(i-integer)*10,0))
        print ("i = ", i , " integer ", integer, " decimals ", decimals)
        if (i<-0.4):
            ceBRname = "_m{}p{}".format(abs(integer),decimals)
        else:
            ceBRname = "_{}p{}".format(integer,decimals)
        TauG2weightsname = "TauG2Weights_ceBRe33"+ceBRname
        histo = gethisto_BSM(df,channel,TauG2weightsname,nbins,binning)
        histo.SetName("GGTT{}{}".format(ceBRname,name))
        print ("BSM ", ceBRname , " " ,histo.Integral())
        hisGGTTlist.append(histo)
    return hisGGTTlist

realcut = " && LepCand_gen[tauindex]!=0"
if "SingleMuon" in sample or "GGToTauTau" in sample:
    realcut = ""

weight = "xsweight*SFweight*Acoweight*npvs_weight*nPUtrkweight*nHStrkweight*eeSF"

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
        "Getpusysweight(puWeight,puWeightDown,npvs_weight,npvsDown_weight)",\
        "Getpusysweight(puWeight,puWeightUp,npvs_weight,npvsUp_weight)", \
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

if year!="2018":
    uncertainty.append("_CMS_L1PrefiringDown")
    uncertainty.append("_CMS_L1PrefiringUp")
    uncertainty_func.append("GetL1PrefiringWeight(L1PreFiringWeight_Nom, L1PreFiringWeight_Dn)")
    uncertainty_func.append("GetL1PrefiringWeight(L1PreFiringWeight_Nom, L1PreFiringWeight_Up)")


uncertainty.append("_CMS_elasticRescalingDown")
uncertainty.append("_CMS_elasticRescalingUp")
uncertainty_func.append("GeteeSFsysweight(eeSF,nTrk,true)")
uncertainty_func.append("GeteeSFsysweight(eeSF,nTrk,false)")
    
print ("year is ", year , " sample is ", sample)
df= RDataFrame("Events","/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuples_mutau_{}_basicsel/{}.root".format(year,sample))
df = df.Define("totalweight",weight)
fout=0

fout = TFile("Histo/HistoSR_{}/Taug2_mutau_{}_BSM.root".format(year,year),"recreate")
    
mt_0cut = "(nTrk==0) && (Acopl<0.015) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex] )||(taupt>32 && isMuonTauTrigger && LepCand_trgmatch[muindex] )) && mvis>40 && mtrans<75 "
mt_1cut = "(nTrk==1) && (Acopl<0.015) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex] )||(taupt>32 && isMuonTauTrigger && LepCand_trgmatch[muindex] )) && mvis>40 && mtrans<75"

if year=="2016pre" or year=="2016post":
    mt_0cut = "(nTrk==0) && (Acopl<0.015) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>30 && isMuonTauTrigger && LepCand_trgmatch[muindex])) && mvis>40 && mtrans<75 "
    mt_1cut = "(nTrk==1) && (Acopl<0.015) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>30 && isMuonTauTrigger && LepCand_trgmatch[muindex])) && mvis>40 && mtrans<75"

if year=="2017":
    mt_0cut = "(nTrk==0) && (Acopl<0.015) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex] )||(taupt>32 && isMuonTauTrigger && LepCand_trgmatch[muindex] && LepCand_trgmatch[tauindex])) && mvis>40 && mtrans<75 "
    mt_1cut = "(nTrk==1) && (Acopl<0.015) && ((taupt>30 && isSingleMuonTrigger && LepCand_trgmatch[muindex])||(taupt>32 && isMuonTauTrigger && LepCand_trgmatch[muindex] && LepCand_trgmatch[tauindex])) && mvis>40 && mtrans<75"

isocut = "&& isOS && is_isolated"
anticut = "&& isOS && !is_isolated"

dir0 = fout.mkdir("mt_0")
dir1 = fout.mkdir("mt_1")

mt_0cut = mt_0cut + realcut
mt_1cut = mt_1cut + realcut

histo_mt0=0
histo_mt1=0


df_mt0 = df.Filter(mt_0cut+isocut)
df_mt1 = df.Filter(mt_1cut+isocut)
print ("mt_0 basic ")
histo_mt0_list = getBSMhisto(df_mt0,"mt0","")
print ("mt_1 basic ")
histo_mt1_list = getBSMhisto(df_mt1,"mt1","")
dir0.cd()
for histo_mt0 in histo_mt0_list:
    histo_mt0.Write()
dir1.cd()
for histo_mt1 in histo_mt1_list:
    histo_mt1.Write()

for i in range(len(uncertainty)):
    uncertainty_name = str.replace(uncertainty[i],"year",year)
    if ("taues" in uncertainty_name):
        sysflag = 1
    else:
        sysflag = 0
    df_mt0_sys = df_sys(df,mt_0cut+isocut, sysflag, uncertainty_func[i])
    df_mt1_sys = df_sys(df,mt_1cut+isocut, sysflag, uncertainty_func[i])
    print ("mt_0 ", uncertainty_name, " " , uncertainty_func[i], " sysflag ", sysflag)
    histo_mt0_sys_list = getBSMhisto(df_mt0_sys,"mt0_{}".format(uncertainty_name),uncertainty_name)
    print ("mt_1 ", uncertainty_name, " " , uncertainty_func[i], " sysflag ", sysflag)
    histo_mt1_sys_list = getBSMhisto(df_mt1_sys,"mt1_{}".format(uncertainty_name),uncertainty_name)
    
    dir0.cd()
    for histo_mt0_sys in histo_mt0_sys_list:
        histo_mt0_sys.Write()
    dir1.cd()
    for histo_mt1_sys in histo_mt1_sys_list:
        histo_mt1_sys.Write()
fout.Close()

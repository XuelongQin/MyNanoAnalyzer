from ROOT import RDataFrame, TFile, TChain, TTree, TFile, TH1D, TLorentzVector,TCanvas
import numpy as np
import sys
from math import cos,sin,sqrt,pi
import ROOT
import time as timer
time_start=timer.time()
#ROOT.gInterpreter.AddIncludePath('./lib/Myfunc.h')
ROOT.gSystem.Load('./lib/RDFfunc.so')
ROOT.gInterpreter.Declare('#include "./lib/basic_sel.h"')
ROOT.gInterpreter.Declare('#include "./lib/GetPFtrk.h"')
ROOT.gInterpreter.Declare('#include "./lib/Correction.h"')




### this code is used to perform basic selection on ntuples after nanoaod analyzer
### year: 2016, 2017, 2018
### name: name of ntuple after analyzer
### sample: output root file name
year = sys.argv[1]
sample = sys.argv[2]
name = sys.argv[3]

print ("year is ", year , " sample is ", sample, " name is ", name)

#fout = TFile("/eos/cms/store/user/xuqin/taug-2/ntuple_after_basicsel/{}.root".format(sample),"recreate")
#fout = TFile("/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/{}.root".format(sample),"recreate")
arbre = TChain("Events")
arbre2 = TChain("Runs")
arbre.Add("/eos/cms/store/group/cmst3/group/taug2/AnalysisXuelong/ntuple_after_analyzer/tautau/{}/*.root".format(name))
arbre2.Add("/eos/cms/store/group/cmst3/group/taug2/AnalysisXuelong/ntuple_after_analyzer/tautau/{}/*.root".format(name))

ngen = 0.
isdata = True

if (sample!="dataA" and sample!="dataB" and sample!="dataC" and sample!="dataD"):
    isdata=False
    rdf2 = RDataFrame(arbre2)
    #ngen = rdf2.Sum("genEventCount").GetValue()
    ngen = rdf2.Sum("genEventSumw").GetValue()
 
print ("isdata ", isdata)
print ("ngen is ", ngen)
xs = 1.0
weight = 1.0
eff=1.0
luminosity = 59830.0
if (year=="2017"): luminosity=41480.0
if (year=="2016pre"): luminosity=19520.0
if (year=="2016post"): luminosity=16810.0

if (isdata):
    weight = 1.0
    
if (sample=="DYJetsToLL_M-50"): 
    xs=6077.22 
    eff=0.318004188
    weight=luminosity*xs/ngen*eff
    
elif (sample=="WJets"): 
    xs=61526.7
    eff=1.0
    weight=1.0
    
elif (sample=="TTTo2L2Nu"): 
    xs=831.76*0.1061
    eff=0.6571875
    weight=luminosity*xs/ngen*eff
    
elif (sample=="TTToSemiLeptonic"): 
    xs=831.76*0.4392
    eff=0.401486111
    weight=luminosity*xs/ngen*eff
    
elif (sample=="TTToHadronic"):
    xs=831.76*0.4544
    eff=0.169864583
    weight=luminosity*xs/ngen*eff
    
elif (sample=="ZZ2L2Nu"): 
    xs=0.564
    eff=0.3018125
    weight=luminosity*xs/ngen*eff
    
elif (sample=="ZZ4L"): 
    xs=1.212 
    eff=0.304
    weight=luminosity*xs/ngen*eff
    
elif (sample=="ZZ2L2Q"): 
    xs=3.22 
    eff=0.372686157
    weight=luminosity*xs/ngen*eff
    
elif (sample=="ZZ2Q2L"): 
    xs=3.22 
    eff=0.372686157
    weight=luminosity*xs/ngen*eff
    
elif (sample=="WZ2L2Q"): 
    xs=5.595 
    eff=0.340629667
    weight=luminosity*xs/ngen*eff

elif (sample=="WZ2Q2L"): 
    xs=5.595 
    eff=0.340629667
    weight=luminosity*xs/ngen*eff
    
elif (sample=="WW2L2Nu"): 
    xs=12.178
    eff=0.396603175
    weight=luminosity*xs/ngen*eff
    
elif (sample=="WZ3LNu"): 
    xs=5.052
    eff=0.340808684
    weight=luminosity*xs/ngen*eff
    
elif (sample=="ST_tW_top"): 
    xs=35.6 
    eff=0.272813333
    weight=luminosity*xs/ngen*eff
    
elif (sample=="ST_tW_antitop"): 
    xs=35.6 
    eff=0.272407407
    weight=luminosity*xs/ngen*eff
    
elif (sample=="ST_t_top"): 
    xs=136.02
    eff=0.118160784
    weight=luminosity*xs/ngen*eff
    
elif (sample=="ST_t_antitop"):
    xs=80.95 
    eff=0.122142268
    weight=luminosity*xs/ngen*eff
    
elif (sample=="GGToTauTau"):
    xs = 0.669 
    eff=0.017169697
    weight=luminosity*xs/ngen*eff
    
print ("cross section is ", xs, " eff is ", eff, " xsweight is ", weight)


#nentries = arbre.GetEntries()
#print ("Before selection total entries", nentries)
df = RDataFrame(arbre)
nentries = df.Count().GetValue()

print ("Before selection total entries", nentries)


###define useful variable: tau index/pt/eta/phi/dz, isOS(tautau is opposite sign), is_isolated(tau pass mediumvsjet)
df_var = df.Define("tautauindex", "Gettautauindex(nLepCand,LepCand_dz)").Define("tau1index","tautauindex[0]").Define("tau2index","tautauindex[1]")
if (isdata):
    df_var = df_var.Define("my_tau1","GetLepVector(tau1index,LepCand_pt,LepCand_eta,LepCand_phi)").Define("my_tau2","GetLepVector(tau2index,LepCand_pt,LepCand_eta,LepCand_phi)")
else: 
    df_var = df_var.Define("my_tau1","GetLepVector(tau1index,LepCand_pt,LepCand_eta,LepCand_phi,LepCand_gen,LepCand_taues,LepCand_fes)").Define("my_tau2","GetLepVector(tau2index,LepCand_pt,LepCand_eta,LepCand_phi,LepCand_gen,LepCand_taues,LepCand_fes)")
    
    
df_var = df_var.Define("tau1pt","LepCand_pt[tau1index]").Define("tau1eta","LepCand_eta[tau1index]").Define("tau1phi","LepCand_phi[tau1index]").Define("tau1dz","LepCand_dz[tau1index]")\
                .Define("tau2pt","LepCand_pt[tau2index]").Define("tau2eta","LepCand_eta[tau2index]").Define("tau2phi","LepCand_phi[tau2index]").Define("tau2dz","LepCand_dz[tau2index]")\
                .Define("isOS","GetisOS(LepCand_charge,tau1index,tau2index)").Define("is_isolated","Getis_isolated(LepCand_vsjet,tau2index)")
                
###Add some basic selection: tau eta, leading tauvsjet, trigger, deltaR(The selection on taupt has been done in nanoaod processor)
df_sel = df_var.Filter("abs(tau1eta)<2.1&& abs(tau2eta)<2.1").Filter("LepCand_vsjet[tau1index]>=31").Filter("my_tau1.DeltaR(my_tau2)>0.5")\
    .Filter("tau1pt>40").Filter("tau2pt>40")

#trigger
if (isdata):
    '''df_sel = df_sel.Filter("(run>=317509 && HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg)\
        || (run<317509 && (HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg \
        || HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg \
        || HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg))")'''
    df_sel = df_sel

else:
    df_sel = df_sel.Filter("HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg")

###Add xsweight and SFweight
if (not isdata):
    df_sel = df_sel.Define("xsweight","{}*genWeight".format(weight)).Define("SFweight","GetSFweight_tautau(pu_weight,tau1index, tau2index, LepCand_gen,LepCand_tauidMsfDM,LepCand_antielesf,LepCand_antimusf,LepCand_tautriggersf)")
else:
    df_sel = df_sel.Define("xsweight","1.0").Define("SFweight","1.0")

###Add information of mass (mvis>40, transverse mass, collinear mass), acoplanarity
df_sel = df_sel.Define("mvis","(my_tau1+my_tau2).M()").Filter("mvis>40")\
    .Define("mcol","GetCollMass(my_tau1,my_tau2,MET_pt,MET_phi)").Define("Acopl","GetAcopl(my_tau1,my_tau2)")

###Define vtxtautau with 3 definition(simple average, theta-average, pt-average)
df_addvtx = df_sel.Define("zvtxll1","recovtxz1(LepCand_dz[tau1index],LepCand_dz[tau2index],PV_z)")\
    .Define("zvtxll2","recovtxz2(my_tau1,my_tau2,LepCand_dz[tau1index],LepCand_dz[tau2index],PV_z)")\
        .Define("zvtxll3","recovtxz3(LepCand_pt[tau1index],LepCand_pt[tau2index],LepCand_dz[tau1index],LepCand_dz[tau2index],PV_z)")\
            .Filter("fabs(LepCand_dz[tau1index]-LepCand_dz[tau2index])<0.1")

columns = ROOT.std.vector("string")()
for c in ("run", "luminosityBlock", "event", "nChargedPFCandidates", "ChargedPFCandidates_dxy", "ChargedPFCandidates_dz", "ChargedPFCandidates_dzError", "ChargedPFCandidates_eta",\
    "ChargedPFCandidates_mass","ChargedPFCandidates_phi","ChargedPFCandidates_pt","ChargedPFCandidates_charge","ChargedPFCandidates_fromPV",\
    "ChargedPFCandidates_lostInnerHits","ChargedPFCandidates_pdgId","ChargedPFCandidates_trackHighPurity","ChargedPFCandidates_isMatchedToGenHS",\
    "MET_phi","MET_pt","PV_ndof","PV_x","PV_y","PV_z","PV_chi2","PV_score","PV_npvs","PV_npvsGood",\
    "nLepCand","LepCand_id","LepCand_pt","LepCand_eta","LepCand_phi","LepCand_charge","LepCand_dxy","LepCand_dz","LepCand_gen",\
    "LepCand_vse","LepCand_vsmu","LepCand_vsjet","LepCand_muonMediumId","LepCand_muonIso","LepCand_tauidMsf","LepCand_taues",\
    "LepCand_fes","LepCand_antimusf","LepCand_antielesf","LepCand_DecayMode","LepCand_tauidMsfDM","LepCand_tautriggersf",\
    "LepCand_trk1pt","LepCand_trk2pt","LepCand_trk3pt","LepCand_trk1eta","LepCand_trk2eta","LepCand_trk3eta",\
    "LepCand_trk1phi","LepCand_trk2phi","LepCand_trk3phi","LepCand_trk1dz","LepCand_trk2dz","LepCand_trk3dz",\
    "nZGenCand","ZGenCand_id","ZGenCand_pt","ZGenCand_eta","ZGenCand_phi",\
    "nJets","nElectrons","nMuons","nTaus","JetCand_pt","JetCand_eta","JetCand_phi","JetCand_m","JetCand_puid","JetCand_jetid","JetCand_deepflavB",\
    "V_genpt","pu_weight","tau1index","tau2index","my_tau1","my_tau2","tau1pt","tau1eta","tau1phi","tau1dz","tau2pt","tau2eta","tau2phi",\
    "tau2dz","isOS","is_isolated","xsweight","SFweight","mvis","mcol","Acopl","zvtxll1","zvtxll2","zvtxll3"):
    columns.push_back(c)

    


df_addvtx.Snapshot("Events","/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/tautau/RDF/{}.root".format(sample),columns)

nentries = df_addvtx.Count().GetValue()
print ("After selection entries", nentries)

time_end=timer.time()
print('totally cost',time_end-time_start)




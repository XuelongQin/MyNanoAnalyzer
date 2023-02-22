from ROOT import RDataFrame, TFile, TChain, TTree, TFile, TH1D, TLorentzVector,TCanvas
import numpy as np
import sys
from math import cos,sin,sqrt,pi
import ROOT
import time as timer
time_start=timer.time()
ROOT.gInterpreter.AddIncludePath('./lib/')
ROOT.gInterpreter.Declare('#include "./lib/basic_sel.h"')
ROOT.gInterpreter.Declare('#include "./lib/GetPFtrk.h"')
ROOT.gInterpreter.Declare('#include "./lib/Correction.h"')
ROOT.gSystem.Load('./lib/RDFfunc.so')




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
arbre.Add("/eos/cms/store/group/cmst3/group/taug2/AnalysisXuelong/ntuple_after_analyzer/mutau/{}/*.root".format(name))
arbre2.Add("/eos/cms/store/group/cmst3/group/taug2/AnalysisXuelong/ntuple_after_analyzer/mutau/{}/*.root".format(name))

ngen = 0.
isdata = True
isW = False

#For W sample, we use genEventCount and don't consider genweight
#For others, we use genEventsSumw and consider genweight
if (sample=="WJets" or sample=="W1Jets" or sample=="W2Jets" or sample=="W3Jets" or sample=="W4Jets"):
    isW=True

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
    
'''elif (sample=="WJets"): 
    xs=61526.7
    eff=1.0
    weight=luminosity*xs/ngen*eff'''
print ("cross section is ", xs, " eff is ", eff, " xsweight is ", weight)


#nentries = arbre.GetEntries()
#print ("Before selection total entries", nentries)
df = RDataFrame(arbre)
nentries = df.Count().GetValue()

print ("Before selection total entries", nentries)

###define useful variable: mu/tau index/pt/eta/phi/dz, isOS(taumu is opposite sign), is_isolated(tau pass mediumvsjet)
df_var = df.Define("mutauindex", "Getmutauindex(nLepCand,LepCand_id ,LepCand_dz)").Define("muindex","mutauindex[0]").Define("tauindex","mutauindex[1]")
if (isdata):
    df_var = df_var.Define("my_tau","GetLepVector(tauindex,LepCand_pt,LepCand_eta,LepCand_phi)")
else: 
    df_var = df_var.Define("my_tau","GetLepVector(tauindex,LepCand_pt,LepCand_eta,LepCand_phi,LepCand_gen,LepCand_taues,LepCand_fes)")
    
df_var = df_var.Define("my_mu","GetLepVector(muindex,LepCand_pt,LepCand_eta,LepCand_phi)")\
            .Define("taupt","LepCand_pt[tauindex]").Define("taueta","LepCand_eta[tauindex]").Define("tauphi","LepCand_phi[tauindex]").Define("taudz","LepCand_dz[tauindex]")\
                .Define("mupt","LepCand_pt[muindex]").Define("mueta","LepCand_eta[muindex]").Define("muphi","LepCand_phi[muindex]").Define("mudz","LepCand_dz[muindex]")\
                    .Define("isOS","GetisOS(LepCand_charge,tauindex,muindex)").Define("is_isolated","Getis_isolated(LepCand_vsjet,tauindex)")

###Add some basic selection: mu/tau eta, muid/iso, trigger, deltaR(The selection on tauid and taupt has been done in nanoaod processor)
df_sel = df_var.Filter("abs(mueta)<2.4 && abs(taueta)<2.3").Filter("LepCand_muonMediumId[muindex]==1 && LepCand_muonIso[muindex]<0.15")\
    .Filter("HLT_IsoMu24").Filter("mupt>26").Filter("my_mu.DeltaR(my_tau)>0.5")
    
###Add xsweight and SFweight
if (not isdata):
    if (not isW):
        df_sel = df_sel.Define("xsweight","{}*genWeight".format(weight)).Define("SFweight","GetSFweight_mutau(my_mu, pu_weight,tauindex,LepCand_gen,LepCand_tauidMsf,LepCand_antielesf,LepCand_antimusf)")
    else:
        df_sel = df_sel.Define("xsweight","Getxsweight_W(LHE_Njets)").Define("SFweight","GetSFweight_mutau(my_mu, pu_weight,tauindex,LepCand_gen,LepCand_tauidMsf,LepCand_antielesf,LepCand_antimusf)")
else:
    df_sel = df_sel.Define("xsweight","1.0").Define("SFweight","1.0")
###Add information of mass (mvis>40, transverse mass, collinear mass), acoplanarity
df_sel = df_sel.Define("mvis","(my_mu+my_tau).M()").Filter("mvis>40").Define("mtrans","GetTransmass(my_mu, MET_pt, MET_phi)")\
    .Define("mcol","GetCollMass(my_mu,my_tau,MET_pt,MET_phi)").Define("Acopl","GetAcopl(my_mu,my_tau)")

###Define vtxtautau with 3 definition(simple average, theta-average, pt-average)
df_addvtx = df_sel.Define("zvtxll1","recovtxz1(LepCand_dz[muindex],LepCand_dz[tauindex],PV_z)")\
    .Define("zvtxll2","recovtxz2(my_mu,my_tau,LepCand_dz[muindex],LepCand_dz[tauindex],PV_z)")\
        .Define("zvtxll3","recovtxz3(LepCand_pt[muindex],LepCand_pt[tauindex],LepCand_dz[muindex],LepCand_dz[tauindex],PV_z)")\
            .Filter("fabs(LepCand_dz[muindex]-LepCand_dz[tauindex])<0.1")

columns = ROOT.std.vector("string")()
for c in ("run", "luminosityBlock", "event", "nChargedPFCandidates", "ChargedPFCandidates_dxy", "ChargedPFCandidates_dz", "ChargedPFCandidates_dzError", "ChargedPFCandidates_eta",\
    "ChargedPFCandidates_mass","ChargedPFCandidates_phi","ChargedPFCandidates_pt","ChargedPFCandidates_charge","ChargedPFCandidates_fromPV",\
    "ChargedPFCandidates_lostInnerHits","ChargedPFCandidates_pdgId","ChargedPFCandidates_trackHighPurity","ChargedPFCandidates_isMatchedToGenHS",\
    "MET_phi","MET_pt","PV_ndof","PV_x","PV_y","PV_z","PV_chi2","PV_score","PV_npvs","PV_npvsGood","HLT_IsoMu24",\
    "nLepCand","LepCand_id","LepCand_pt","LepCand_eta","LepCand_phi","LepCand_charge","LepCand_dxy","LepCand_dz","LepCand_gen",\
    "LepCand_vse","LepCand_vsmu","LepCand_vsjet","LepCand_muonMediumId","LepCand_muonIso","LepCand_tauidMsf","LepCand_taues",\
    "LepCand_fes","LepCand_antimusf","LepCand_antielesf","LepCand_DecayMode","LepCand_tauidMsfDM","LepCand_tautriggersf",\
    "LepCand_trk1pt","LepCand_trk2pt","LepCand_trk3pt","LepCand_trk1eta","LepCand_trk2eta","LepCand_trk3eta",\
    "LepCand_trk1phi","LepCand_trk2phi","LepCand_trk3phi","LepCand_trk1dz","LepCand_trk2dz","LepCand_trk3dz",\
    "nZGenCand","ZGenCand_id","ZGenCand_pt","ZGenCand_eta","ZGenCand_phi",\
    "nJets","nElectrons","nMuons","nTaus","JetCand_pt","JetCand_eta","JetCand_phi","JetCand_m","JetCand_puid","JetCand_jetid","JetCand_deepflavB",\
    "V_genpt","pu_weight","tauindex","muindex","my_tau","my_mu","taupt","taueta","tauphi","taudz","mupt","mueta","muphi",\
    "mudz","isOS","is_isolated","xsweight","SFweight","mvis","mtrans","mcol","Acopl","zvtxll1","zvtxll2","zvtxll3"):
    columns.push_back(c)

df_addvtx.Snapshot("Events","/eos/cms/store/cmst3/group/taug2/AnalysisXuelong/ntuple_after_basicsel/mutau/RDF/{}.root".format(sample),columns)

nentries = df_addvtx.Count().GetValue()
print ("After selection entries", nentries)

time_end=timer.time()
print('totally cost',time_end-time_start)


import sys
sys.path.append("..")
from pyFunc.GetHisto import variable,cate,gethisto2D_cate,gethisto2D
from ROOT import TFile
import numpy as np




def getWFRhisto(cut,cutname,variable1,variable2):
    ST = cate("ST",["ST_t_top","ST_t_antitop","ST_tW_top","ST_tW_antitop"])
    VV = cate("VV",["WW2L2Nu","WZ2Q2L","WZ3LNu","ZZ2Q2L","ZZ2L2Nu","ZZ4L"])
    TT = cate("TT",["TTTo2L2Nu","TTToHadronic","TTToSemiLeptonic"])
    ZTT = cate("ZTT",["DYJetsToLL_M-50"])
    W = cate("W",["WJets","W1Jets","W2Jets","W3Jets","W4Jets"])
    data_obs = cate("data_obs",["dataA","dataB","dataC","dataD"])
    weight = "xsweight*SFweight*Acoweight*npvsweight*nPUtrkweight*nHStrkweight"
    
    cutOS = cut + "&& isOS && is_isolated"
    cutSS = cut + "&& (!isOS) && is_isolated"
    cutOSname = cutname +"OS_iso"
    cutSSname = cutname + "SS_iso"
    channel = "mutau"
    histoSTSS = gethisto2D_cate(ST,cutSS,cutSSname,weight,variable1,variable2,channel)
    histoVVSS = gethisto2D_cate(VV,cutSS,cutSSname,weight,variable1,variable2,channel)
    histoTTSS = gethisto2D_cate(TT,cutSS,cutSSname,weight,variable1,variable2,channel)
    histoZTTSS = gethisto2D_cate(ZTT,cutSS,cutSSname,weight,variable1,variable2,channel)
    histoWSS = gethisto2D_cate(W,cutSS,cutSSname,weight,variable1,variable2,channel)
    histodataSS = gethisto2D_cate(data_obs,cutSS,cutSSname,"1",variable1,variable2,channel)
    histoSS= histodataSS.Clone("h_{}_{}_{}_{}".format(variable1.name,variable2.name,cutSSname,"QCD"))
    histoSS.Add(histoSTSS,-1)
    histoSS.Add(histoVVSS,-1)
    histoSS.Add(histoTTSS,-1)
    histoSS.Add(histoZTTSS,-1)
    histoSS.Add(histoWSS,-1)
    
    histoWOS = gethisto2D_cate(W,cutOS,cutOSname,weight,variable1,variable2,channel)
    

    hFR = histoWOS.Clone("hWFR_{}_{}_{}".format(variable1.name,variable2.name,cutname))
    #hFR.Divide(histononiso)
    deno = histoSS.Clone("hWQCD_{}_{}_{}".format(variable1.name,variable2.name,cutname))
    deno.Add(histoWOS)
    hFR.Divide(deno)
    
    return histoSTSS,histoVVSS,histoTTSS,histoZTTSS,histoWSS,histodataSS,histoSS,histoWOS,hFR

mvis = variable("mvis","mvis",int(5),np.array([50,100,150,200,250,300],dtype=float))
mtranse = variable("mtrans","mtrans",int(3),np.array([0,25,50,75],dtype=float))


fout = TFile("./FRW_mutau.root","recreate")
for DM in [0,1,10,11]:
    cut = "LepCand_DecayMode[tauindex]=={} && taupt>30 && mvis>40".format(DM)
    cutname = "DM{}".format(DM)
    histotuple = getWFRhisto(cut,cutname,mtranse,mvis)
    fout.cd()
    for histo in histotuple:
        histo.Write()
cut = "(LepCand_DecayMode[tauindex]==0 || LepCand_DecayMode[tauindex]==1 || LepCand_DecayMode[tauindex]==10 || LepCand_DecayMode[tauindex]==11) && taupt>30 && mvis>40"
cutname = "allDM"
histotuple = getWFRhisto(cut,cutname,mtranse,mvis)
fout.cd()
for histo in histotuple:
    histo.Write()

fout.Close()
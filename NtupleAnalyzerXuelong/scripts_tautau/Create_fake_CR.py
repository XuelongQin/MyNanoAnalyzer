if __name__ == "__main__":

    import ROOT
    import argparse
    import numpy as np

    parser = argparse.ArgumentParser()
    parser.add_argument('--year')

    options = parser.parse_args()
    postfixName=[ "",\
    "_CMS_jetfake_tauptextrap_qcd_tt_dm0_yearDown", "_CMS_jetfake_tauptextrap_qcd_tt_dm0_yearUp", \
    "_CMS_jetfake_tauptextrap_qcd_tt_dm1_yearDown", "_CMS_jetfake_tauptextrap_qcd_tt_dm1_yearUp", \
    "_CMS_jetfake_tauptextrap_qcd_tt_dm10_yearDown", "_CMS_jetfake_tauptextrap_qcd_tt_dm10_yearUp", \
    "_CMS_jetfake_tauptextrap_qcd_tt_dm11_yearDown", "_CMS_jetfake_tauptextrap_qcd_tt_dm11_yearUp", \
    "_CMS_jetfake_ntracksextrap_qcd_tt_dm0Down", "_CMS_jetfake_ntracksextrap_qcd_tt_dm0Up", \
    "_CMS_jetfake_ntracksextrap_qcd_tt_dm1Down", "_CMS_jetfake_ntracksextrap_qcd_tt_dm1Up", \
    "_CMS_jetfake_ntracksextrap_qcd_tt_dm10Down", "_CMS_jetfake_ntracksextrap_qcd_tt_dm10Up", \
    "_CMS_jetfake_ntracksextrap_qcd_tt_dm11Down", "_CMS_jetfake_ntracksextrap_qcd_tt_dm11Up"]
    nbhist=17

    fVV=ROOT.TFile("Histo/HistoCR_anti_"+options.year+"/VV.root","r")
    fTT=ROOT.TFile("Histo/HistoCR_anti_"+options.year+"/TT.root","r")
    fST=ROOT.TFile("Histo/HistoCR_anti_"+options.year+"/ST.root","r")
    fZTT=ROOT.TFile("Histo/HistoCR_anti_"+options.year+"/ZTT.root","r")
    fData=ROOT.TFile("Histo/HistoCR_anti_"+options.year+"/Tau.root","r")
    fout=ROOT.TFile("Histo/HistoCR_"+options.year+"/Fake.root","recreate")
    ncat=1
    cate = ["tt_2"]
    year4=options.year
    if options.year=="2016pre": year4="2016preVFP"
    if options.year=="2016post": year4="2016postVFP"
    for j in range(0,ncat):
        dir0=fout.mkdir(cate[j])
        for k in range(0,nbhist):
            postfix = str.replace(postfixName[k],"year",year4)
            
            h0=fData.Get("{}/data_obs_antileading{}".format(cate[j], postfix))
            h0.Add(fVV.Get("{}/VV_antileading{}".format(cate[j], postfix)),-1)
            h0.Add(fZTT.Get("{}/ZTT_antileading{}".format(cate[j], postfix)),-1)
            h0.Add(fTT.Get("{}/TT_antileading{}".format(cate[j], postfix)),-1)
            h0.Add(fST.Get("{}/ST_antileading{}".format(cate[j], postfix)),-1)

            h1=fData.Get("{}/data_obs_antisubleading{}".format(cate[j], postfix))
            h1.Add(fVV.Get("{}/VV_antisubleading{}".format(cate[j], postfix)),-1)
            h1.Add(fZTT.Get("{}/ZTT_antisubleading{}".format(cate[j], postfix)),-1)
            h1.Add(fTT.Get("{}/TT_antisubleading{}".format(cate[j], postfix)),-1)
            h1.Add(fST.Get("{}/ST_antisubleading{}".format(cate[j], postfix)),-1)
            
            h2=fData.Get("{}/data_obs_antidouble{}".format(cate[j], postfix))
            h2.Add(fVV.Get("{}/VV_antidouble{}".format(cate[j], postfix)),-1)
            h2.Add(fZTT.Get("{}/ZTT_antidouble{}".format(cate[j], postfix)),-1)
            h2.Add(fTT.Get("{}/TT_antidouble{}".format(cate[j], postfix)),-1)
            h2.Add(fST.Get("{}/ST_antidouble{}".format(cate[j], postfix)),-1)
            h0.SetName("Fake_leading{}".format(postfix))
            h1.SetName("Fake_subleading{}".format(postfix))
            h2.SetName("Fake_double{}".format(postfix))
            h3 = h0.Clone("Fake_subtraction{}".format(postfix))
            h3.Add(h1,1)
            h3.Add(h2,-1)
            for i in range(0,h0.GetSize()-2):
                if h0.GetBinContent(i)<0:
                    h0.SetBinError(i,max(0,h0.GetBinError(i)+h0.GetBinError(i)))
                    h0.SetBinContent(i,0)
                if h1.GetBinContent(i)<0:
                    h1.SetBinError(i,max(0,h1.GetBinError(i)+h1.GetBinError(i)))
                    h1.SetBinContent(i,0)
                if h2.GetBinContent(i)<0:
                    h2.SetBinError(i,max(0,h2.GetBinError(i)+h2.GetBinError(i)))
                    h2.SetBinContent(i,0)
                if h3.GetBinContent(i)<0:
                    h3.SetBinError(i,max(0,h3.GetBinError(i)+h3.GetBinError(i)))
                    h3.SetBinContent(i,0)
            h4 = h3.Clone("Fake{}".format(postfix))
            
            for i in range(0,h0.GetSize()-1):
                if h0.GetBinContent(i)>h4.GetBinContent(i):
                    h4.SetBinContent(i, h0.GetBinContent(i))
                    h4.SetBinError(i, h0.GetBinError(i))
                if h1.GetBinContent(i)>h4.GetBinContent(i):
                    h4.SetBinContent(i, h1.GetBinContent(i))
                    h4.SetBinError(i, h1.GetBinError(i))
                if h2.GetBinContent(i)>h4.GetBinContent(i):
                    h4.SetBinContent(i, h2.GetBinContent(i))
                    h4.SetBinError(i, h2.GetBinError(i))
            fout.cd()
            dir0.cd()
            #h0.Write()
            #h1.Write()
            #h2.Write()
            #h3.Write()
            h4.Write()
    fout.Close()
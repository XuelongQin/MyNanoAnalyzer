if __name__ == "__main__":

    import ROOT
    import argparse
    import numpy as np

    parser = argparse.ArgumentParser()
    parser.add_argument('--year')

    options = parser.parse_args()
    postfixName=[ "",\
    "_CMS_jetfake_tauptextrap_qcd_mt_dm0_yearDown", "_CMS_jetfake_tauptextrap_qcd_mt_dm0_yearUp", \
    "_CMS_jetfake_tauptextrap_qcd_mt_dm1_yearDown", "_CMS_jetfake_tauptextrap_qcd_mt_dm1_yearUp", \
    "_CMS_jetfake_tauptextrap_qcd_mt_dm10_yearDown", "_CMS_jetfake_tauptextrap_qcd_mt_dm10_yearUp", \
    "_CMS_jetfake_tauptextrap_qcd_mt_dm11_yearDown", "_CMS_jetfake_tauptextrap_qcd_mt_dm11_yearUp", \
    "_CMS_jetfake_ntracksextrap_qcd_mt_dm0Down", "_CMS_jetfake_ntracksextrap_qcd_mt_dm0Up", \
    "_CMS_jetfake_ntracksextrap_qcd_mt_dm1Down", "_CMS_jetfake_ntracksextrap_qcd_mt_dm1Up", \
    "_CMS_jetfake_ntracksextrap_qcd_mt_dm10Down", "_CMS_jetfake_ntracksextrap_qcd_mt_dm10Up", \
    "_CMS_jetfake_ntracksextrap_qcd_mt_dm11Down", "_CMS_jetfake_ntracksextrap_qcd_mt_dm11Up", \
    "_CMS_jetfake_tauptextrap_w_mt_dm0_yearDown", "_CMS_jetfake_tauptextrap_w_mt_dm0_yearUp", \
    "_CMS_jetfake_tauptextrap_w_mt_dm1_yearDown", "_CMS_jetfake_tauptextrap_w_mt_dm1_yearUp", \
    "_CMS_jetfake_tauptextrap_w_mt_dm10_yearDown", "_CMS_jetfake_tauptextrap_w_mt_dm10_yearUp", \
    "_CMS_jetfake_tauptextrap_w_mt_dm11_yearDown", "_CMS_jetfake_tauptextrap_w_mt_dm11_yearUp", \
    "_CMS_jetfake_ntracksextrap_w_mt_dm0Down", "_CMS_jetfake_ntracksextrap_w_mt_dm0Up", \
    "_CMS_jetfake_ntracksextrap_w_mt_dm1Down", "_CMS_jetfake_ntracksextrap_w_mt_dm1Up", \
    "_CMS_jetfake_ntracksextrap_w_mt_dm10Down", "_CMS_jetfake_ntracksextrap_w_mt_dm10Up", \
    "_CMS_jetfake_ntracksextrap_w_mt_dm11Down", "_CMS_jetfake_ntracksextrap_w_mt_dm11Up"]

    nbhist=33

    fVV=ROOT.TFile("Histo/HistoCR_anti_"+options.year+"/VV.root","r")
    fTT=ROOT.TFile("Histo/HistoCR_anti_"+options.year+"/TT.root","r")
    fST=ROOT.TFile("Histo/HistoCR_anti_"+options.year+"/ST.root","r")
    fZLL=ROOT.TFile("Histo/HistoCR_anti_"+options.year+"/ZLL.root","r")
    fZTT=ROOT.TFile("Histo/HistoCR_anti_"+options.year+"/ZTT.root","r")
    fData=ROOT.TFile("Histo/HistoCR_anti_"+options.year+"/SingleMuon.root","r")
    fout=ROOT.TFile("Histo/HistoCR_"+options.year+"/Fake.root","recreate")
    ncat=1
    cate = ["mt_2"]
    year4=options.year
    if options.year=="2016pre": year4="2016preVFP"
    if options.year=="2016post": year4="2016postVFP"
    for j in range(0,ncat):
        

        dir0=fout.mkdir(cate[j])

        for k in range(0,nbhist):
            print ("k = ", k)
            postfix = str.replace(postfixName[k],"year",year4)
            h0=fData.Get("{}/data_obs_anti{}".format(cate[j], postfix))
            h0.Add(fVV.Get("{}/VV_anti{}".format(cate[j], postfix)),-1)
            h0.Add(fZLL.Get("{}/ZLL_anti{}".format(cate[j], postfix)),-1)
            h0.Add(fZTT.Get("{}/ZTT_anti{}".format(cate[j], postfix)),-1)
            h0.Add(fTT.Get("{}/TT_anti{}".format(cate[j], postfix)),-1)
            h0.Add(fST.Get("{}/ST_anti{}".format(cate[j], postfix)),-1)
            for i in range(0,h0.GetSize()-2):
                if h0.GetBinContent(i)<0:
                    #h0.SetBinError(i,max(0,h0.GetBinError(i)+h0.GetBinError(i)))
                    h0.SetBinContent(i,0)
            fout.cd()
            dir0.cd()
            h0.SetName("Fake{}".format(postfix))
            h0.Write()
    fout.Close()
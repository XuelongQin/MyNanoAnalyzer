if __name__ == "__main__":

    import ROOT
    import argparse
    import numpy as np

    parser = argparse.ArgumentParser()
    parser.add_argument('--year')

    options = parser.parse_args()
    postfixName=[""]

    nbhist=1 

    fVV=ROOT.TFile("Histo/HistoInclu_"+options.year+"/VV.root","r")
    fTT=ROOT.TFile("Histo/HistoInclu_"+options.year+"/TT.root","r")
    fST=ROOT.TFile("Histo/HistoInclu_"+options.year+"/ST.root","r")
    fZLL=ROOT.TFile("Histo/HistoInclu_"+options.year+"/ZLL.root","r")
    fZTT=ROOT.TFile("Histo/HistoInclu_"+options.year+"/ZTT.root","r")
    fData=ROOT.TFile("Histo/HistoInclu_"+options.year+"/SingleMuon.root","r")
    fout=ROOT.TFile("Histo/HistoInclu_"+options.year+"/Fake.root","recreate")

    ncat=9
    
    class variable:
        def __init__(self, name, title, nbins, binning):
            self.name=name
            self.title = title
            self.nbins=nbins
            self.binning = binning
    mvis = variable("mvis","m_{vis}",int(32),np.array([0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,400,500],dtype=float))
    taupt = variable("taupt","#tau p_{T}",int(34),np.array([30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,84,88,92,96,100,105,110,115,120],dtype=float))
    mupt = variable("mupt","#mu p_{T}",int(39),np.array([20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,84,88,92,96,100,105,110,115,120],dtype=float))
    Aco = variable("Acopl","acoplanarity",int(40),np.arange(0,1.025,0.025,dtype=float))
    mtranse = variable("mtrans","m_{T}(#mu,MET)",int(36),np.arange(0,185,5,dtype=float))
    nTrk = variable("nTrk","N_{tracks}",int(50),np.arange(0,102,2,dtype=float))
    MET = variable("MET_pt","MET",int(19),np.array([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,80,90,100,110,120],dtype=float))
    taueta = variable("taueta","#tau #eta", int(25), np.arange(-2.5,2.7,0.2,dtype=float))
    mueta = variable("mueta","#mu #eta", int(25), np.arange(-2.5,2.7,0.2,dtype=float))
    #variablelist = [mvis,taupt,mupt,Aco,mtranse]
    variablelist = [mvis,taupt,mupt,Aco,mtranse,nTrk,MET,taueta,mueta]
    for j in range(0,ncat):

        dir0=fout.mkdir(variablelist[j].name)

        for k in range(0,nbhist):
            postfix=postfixName[k]
            h0=fData.Get("{}/data_obs_anti".format(variablelist[j].name))
            h0.Add(fVV.Get("{}/VV_anti".format(variablelist[j].name)),-1)
            h0.Add(fZLL.Get("{}/ZLL_anti".format(variablelist[j].name)),-1)
            h0.Add(fZTT.Get("{}/ZTT_anti".format(variablelist[j].name)),-1)
            h0.Add(fTT.Get("{}/TT_anti".format(variablelist[j].name)),-1)
            h0.Add(fST.Get("{}/ST_anti".format(variablelist[j].name)),-1)
            for i in range(0,h0.GetSize()-2):
                if h0.GetBinContent(i)<0:
                    h0.SetBinError(i,max(0,h0.GetBinError(i)+h0.GetBinError(i)))
                    h0.SetBinContent(i,0)

            fout.cd()
            dir0.cd()
            h0.SetName("Fake")
            h0.Write()
    fout.Close()
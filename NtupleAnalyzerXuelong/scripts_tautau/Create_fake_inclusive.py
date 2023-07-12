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
    fZTT=ROOT.TFile("Histo/HistoInclu_"+options.year+"/ZTT.root","r")
    fData=ROOT.TFile("Histo/HistoInclu_"+options.year+"/Tau.root","r")
    fout=ROOT.TFile("Histo/HistoInclu_"+options.year+"/Fake.root","recreate")

    ncat=8
    
    class variable:
        def __init__(self, name, title, nbins, binning):
            self.name=name
            self.title = title
            self.nbins=nbins
            self.binning = binning
    mvis = variable("mvis","m_{vis}",int(32),np.array([0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,400,500],dtype=float))
    tau1pt = variable("tau1pt","leading #tau p_{T}",int(29),np.array([40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,84,88,92,96,100,105,110,115,120],dtype=float))
    tau2pt = variable("tau2pt","subleading #tau p_{T}",int(29),np.array([40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,84,88,92,96,100,105,110,115,120],dtype=float))
    Aco = variable("Acopl","acoplanarity",int(40),np.arange(0,1.025,0.025,dtype=float))
    #mtranse = variable("mtrans","m_{T}(#mu,MET)",int(36),np.arange(0,185,5,dtype=float))
    nTrk = variable("nTrk","N_{tracks}",int(50),np.arange(0,102,2,dtype=float))
    MET = variable("MET_pt","MET",int(19),np.array([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,80,90,100,110,120],dtype=float))
    tau1eta = variable("tau1eta","leading #tau #eta", int(25), np.arange(-2.5,2.7,0.2,dtype=float))
    tau2eta = variable("tau2eta","subleading #tau #eta", int(25), np.arange(-2.5,2.7,0.2,dtype=float))
    #variablelist = [mvis,taupt,mupt,Aco,mtranse]
    variablelist = [mvis,tau1pt,tau2pt,Aco,nTrk,MET,tau1eta,tau2eta]
    for j in range(0,ncat):

        dir0=fout.mkdir(variablelist[j].name)

        for k in range(0,nbhist):
            postfix=postfixName[k]
            h0=fData.Get("{}/data_obs_leadinganti".format(variablelist[j].name))
            h0.Add(fVV.Get("{}/VV_leadinganti".format(variablelist[j].name)),-1)
            h0.Add(fZTT.Get("{}/ZTT_leadinganti".format(variablelist[j].name)),-1)
            h0.Add(fTT.Get("{}/TT_leadinganti".format(variablelist[j].name)),-1)
            h0.Add(fST.Get("{}/ST_leadinganti".format(variablelist[j].name)),-1)

            h1=fData.Get("{}/data_obs_subleadinganti".format(variablelist[j].name))
            h1.Add(fVV.Get("{}/VV_subleadinganti".format(variablelist[j].name)),-1)
            h1.Add(fZTT.Get("{}/ZTT_subleadinganti".format(variablelist[j].name)),-1)
            h1.Add(fTT.Get("{}/TT_subleadinganti".format(variablelist[j].name)),-1)
            h1.Add(fST.Get("{}/ST_subleadinganti".format(variablelist[j].name)),-1)
            
            h2=fData.Get("{}/data_obs_doubleanti".format(variablelist[j].name))
            h2.Add(fVV.Get("{}/VV_doubleanti".format(variablelist[j].name)),-1)
            h2.Add(fZTT.Get("{}/ZTT_doubleanti".format(variablelist[j].name)),-1)
            h2.Add(fTT.Get("{}/TT_doubleanti".format(variablelist[j].name)),-1)
            h2.Add(fST.Get("{}/ST_doubleanti".format(variablelist[j].name)),-1)
            h0.SetName("Fake_leading")
            h1.SetName("Fake_subleading")
            h2.SetName("Fake_double")
            h3 = h0.Clone("Fake_subtraction")
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
            h4 = h3.Clone("Fake")
            for i in range(0,h0.GetSize()-2):
                if h0.GetBinContent(i)>h4.GetBinContent(i):
                    h4.SetBinContent(i, h0.GetBinContent(i))
                    h4.SetBinError(i, h0.GetBinError(i))
                if h1.GetBinContent(i)>h4.GetBinContent(i):
                    h4.SetBinContent(i, h1.GetBinContent(i))
                    h4.SetBinError(i, h1.GetBinError(i))
                if h2.GetBinContent(i)>h4.GetBinContent(i):
                    h4.SetBinContent(i, h2.GetBinContent(i))
                    h4.SetBinError(i, h2.GetBinError(i))
                if h3.GetBinContent(i)>h4.GetBinContent(i):
                    h4.SetBinContent(i, h3.GetBinContent(i))
                    h4.SetBinError(i, h3.GetBinError(i))
                    
            fout.cd()
            dir0.cd()
            h0.Write()
            h1.Write()
            h2.Write()
            h3.Write()
            h4.Write()
    fout.Close()
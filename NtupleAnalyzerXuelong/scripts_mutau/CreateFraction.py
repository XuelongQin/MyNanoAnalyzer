import ROOT
import re
from array import array
import argparse

def add_lumi(year):
    lowX=0.4
    lowY=0.835
    if (year=="2016pre" or year=="2016post"): lowX = 0.22
    lumi  = ROOT.TPaveText(lowX, lowY+0.06, lowX+0.30, lowY+0.16, "NDC")
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.SetTextSize(0.055)
    lumi.SetTextFont (   42 )
    
    if (year=="2018"): lumi.AddText("2018, 60 fb^{-1} (13 TeV)")
    if (year=="2016pre"): lumi.AddText("2016 preVFP, 19 fb^{-1} (13 TeV)")
    if (year=="2016post"): lumi.AddText("2016 postVFP, 16 fb^{-1} (13 TeV)")
    if (year=="2017"): lumi.AddText("2017, 41 fb^{-1} (13 TeV)")
    if (year=="2016"): lumi.AddText("2016, 36 fb^{-1} (13 TeV)")
    return lumi

def add_CMS(year):
    lowX=0.16
    lowY=0.835
    if (year=="2016pre" or year=="2016post"): lowX = 0.08
    lumi  = ROOT.TPaveText(lowX, lowY+0.06, lowX+0.15, lowY+0.16, "NDC")
    lumi.SetTextFont(61)
    lumi.SetTextSize(0.065)
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.AddText("CMS")
    return lumi


parser = argparse.ArgumentParser()
parser.add_argument('--year', default="2016pre", choices=['2016','2016pre','2016post', '2017', '2018'], help="Year?")
options = parser.parse_args()


fileData=ROOT.TFile("Histo/HistoforFR_{}/SingleMuon.root".format(options.year),"r")
fileMC=ROOT.TFile("Histo/HistoforFR_{}/MC.root".format(options.year),"r")
fileW=ROOT.TFile("Histo/HistoforFR_{}/Wall.root".format(options.year),"r")
#fileout=ROOT.TFile("Histo/HistoforFR_2018/fractions.root","recreate")
fileout=ROOT.TFile("Histo/HistoforFR_{}/Wfractions.root".format(options.year),"recreate")

W=fileW.Get("fractionOS").Clone()
QCD=fileData.Get("fractionSS").Clone()
QCD.Add(fileMC.Get("fractionSS"),-1)
QCD.Add(fileW.Get("fractionSS"),-1)

denom=W.Clone()
denom.Add(QCD)
W.Divide(denom)
W.SetName("frac_W")
fileout.cd()
W.Write()

#Wdown = W.Clone("frac_W_down")
#Wdown.Scale(0.5)


ROOT.gStyle.SetOptStat(0)
c=ROOT.TCanvas("canvas","",0,0,800,800)
c.cd()
c.SetRightMargin(0.2)
W.SetTitle("")
W.SetMarkerStyle(20)
W.SetMarkerColor(1)
W.SetLineColor(1)
W.GetXaxis().SetTitle("m_{T}(#mu,MET) (GeV)")
W.GetYaxis().SetTitle("m_{vis}(#mu,#tau_{h}) (GeV)")
W.GetZaxis().SetTitle("W fraction")
W.GetZaxis().SetTitleOffset(1.5)
W.Draw("colz")
lumi=add_lumi(options.year)
lumi.Draw("same")
cms=add_CMS(options.year)
cms.Draw("same")
c.cd()
c.Modified()
c.SaveAs("Plots_FR/"+options.year+"/fractions.pdf")
c.SaveAs("Plots_FR/"+options.year+"/fractions.png")
from ROOT import TFile, TFile, TH1D, TCanvas,TH1F,TPaveText,TF1,TMath,TGraphAsymmErrors,TLatex,TGraph,TVirtualFitter,kCyan,TLegend
import math
#from ROOT.RDF import TH1DModel
import numpy as np
from array import array
import sys
from math import cos,sin,sqrt,pi
import ROOT
import time as timer
time_start=timer.time()
import ROOT
ROOT.gROOT.SetBatch(1)

year = sys.argv[1]

def fitFlat(x,p):
    return p[0]

def fitLinear(x,p):
    return p[0] + p[1]*x[0]

def fitExp(x,p):
    return p[0] + p[1]*(TMath.Exp(-(p[2]*x[0]+p[3])))
                        
def fitLandau(x,p):
    return p[0] + p[1]*(TMath.Landau(x[0],p[2],p[3],0))

def fitPoly2(x,p):
    return p[0] + p[1]*x[0] + p[2]*x[0]*x[0]

if (year=="Run2paper"):
    f = TFile("Histo/HistoforFR_{}/DataSub.root".format("Run2"))
else:
    f = TFile("Histo/HistoforFR_{}/DataSub.root".format(year))
FR_H = TFile("Histo/HistoforFR_{}/FitHistograms_FR.root".format(year), "RECREATE")
def fit_histo(cut, decaymode, variablename , variabletitle):
    decaymode = str(decaymode)
    Numerator = f.Get("h_tauFR_{}_dm{}_M".format(cut,decaymode))
    Denumerator = f.Get("h_tauFR_{}_dm{}_VVVL".format(cut,decaymode))

    histogram_pass = Numerator
    
    histogram_fail = Denumerator

    histogram_FR = histogram_pass.Clone("h_tauFR_{}_dm{}_FR".format(cut,decaymode))
    histogram_FR.Divide(histogram_fail)

    print(Numerator.GetBinContent(1))
    print(Denumerator.GetBinContent(1))
    print(histogram_FR.GetBinContent(1))

    TGraph_FR = TGraphAsymmErrors(histogram_FR)
    
    fMin = 30
    fMax = 300
    nPar = 4 
    fitfunc = TF1("fitfunc", fitLandau, fMin, fMax, nPar)
    xAxisMax = 500.
    if (year=="2018"):
        if cut =="QCD":
            if decaymode=='0':
                fitfunc.SetParameter(0, 0.12)
                fitfunc.SetParameter(1, -0.18)
                fitfunc.SetParameter(2, 56.1)
                fitfunc.SetParameter(3, 10.8)
            if decaymode=='1':
                fitfunc.SetParameter(0, 0.15)
                fitfunc.SetParameter(1, -0.25)
                fitfunc.SetParameter(2, 52)
                fitfunc.SetParameter(3, 8.6)
            if decaymode=='10':
                fitfunc.SetParameter(0, 0.061)
                fitfunc.SetParameter(1, 0.056)
                fitfunc.SetParameter(2, 68.3)
                fitfunc.SetParameter(3, 17.4)
            if decaymode=='11':
                fitfunc.SetParameter(0, 0.022)
                fitfunc.SetParameter(1, 3.82)
                fitfunc.SetParameter(2, 1682)
                fitfunc.SetParLimits(2,1500,1800)
                fitfunc.SetParameter(3, 615)
        else:
            fitfunc.SetParameter(0, 1.8)
            fitfunc.SetParameter(1, -9)
            fitfunc.SetParameter(2, 130)
            fitfunc.SetParameter(3, 240)
            if decaymode=='0':
                fitfunc.SetParameter(0, 0.28)
                fitfunc.SetParameter(1, -1.03)
                fitfunc.SetParameter(2, 110)
                fitfunc.SetParameter(3, 100)
            if decaymode=='1':
                fitfunc.SetParameter(0, 0.15)
                fitfunc.SetParameter(1, -0.25)
                fitfunc.SetParameter(2, 148)
                fitfunc.SetParameter(3, 48.6)
            if decaymode=='10':
                fitfunc.SetParameter(0, 0.03)
                fitfunc.SetParameter(1, 0.3)
                fitfunc.SetParameter(2, 74)
                fitfunc.SetParameter(3, 144)
            if decaymode=='11':
                fitfunc.SetParameter(0, 0.046)
                fitfunc.SetParameter(1, 0.20)
                fitfunc.SetParameter(2, 300)
                fitfunc.SetParLimits(2,300,3000)
                fitfunc.SetParameter(3, 73)
                
    if (year=="2017"):
        if cut =="QCD":
            if decaymode=='0':
                fitfunc.SetParameter(0, 0.12)
                fitfunc.SetParameter(1, -0.18)
                fitfunc.SetParameter(2, 56.1)
                fitfunc.SetParLimits(2,56,80)
                fitfunc.SetParameter(3, 10.8)
            if decaymode=='1':
                fitfunc.SetParameter(0, 0.09)
                fitfunc.SetParameter(1, -1.47)
                fitfunc.SetParLimits(1,-2.0,-1.4)
                fitfunc.SetParameter(2, 32.5)
                fitfunc.SetParameter(3, 0.0003)
            if decaymode=='10':
                fitfunc.SetParameter(0, 0.061)
                fitfunc.SetParameter(1, 0.056)
                fitfunc.SetParameter(2, 68.3)
                fitfunc.SetParameter(3, 17.4)
            if decaymode=='11':
                fitfunc.SetParameter(0, 0.013)
                fitfunc.SetParameter(1, 0.043)
                fitfunc.SetParameter(2, 53)
                fitfunc.SetParameter(3, 8.1)
        else:
            fitfunc.SetParameter(0, 1.8)
            fitfunc.SetParameter(1, -9)
            fitfunc.SetParameter(2, 130)
            fitfunc.SetParameter(3, 240)
            if decaymode=='0':
                fitfunc.SetParameter(0, 0.28)
                fitfunc.SetParameter(1, -1.03)
                fitfunc.SetParameter(2, 110)
                fitfunc.SetParameter(3, 100)
            if decaymode=='1':
                fitfunc.SetParameter(0, 0.14)
                fitfunc.SetParameter(1, -0.33)
                fitfunc.SetParameter(2, 124)
                fitfunc.SetParameter(3, 39.6)
            if decaymode=='10':
                fitfunc.SetParameter(0, 0.03)
                fitfunc.SetParameter(1, 0.3)
                fitfunc.SetParameter(2, 74)
                fitfunc.SetParameter(3, 144)
            if decaymode=='11':
                fitfunc.SetParameter(0, 0.063)
                fitfunc.SetParameter(1, 0.043)
                fitfunc.SetParameter(2, 53)
                fitfunc.SetParameter(3, 8.1)
    if (year=="2016pre"):
        if cut =="QCD":
            if decaymode=='0':
                fitfunc.SetParameter(0, 0.18)
                fitfunc.SetParameter(1, -0.42)
                fitfunc.SetParameter(2, 56.1)
                fitfunc.SetParameter(3, 7.26)
                
            if decaymode=='1':
                fitfunc.SetParameter(0, 0.14)
                fitfunc.SetParameter(1, -0.33)
                fitfunc.SetParameter(2, 124)
                fitfunc.SetParameter(3, 39.6)
            if decaymode=='10':
                fitfunc.SetParameter(0, 0.061)
                fitfunc.SetParameter(1, 0.056)
                fitfunc.SetParameter(2, 68.3)
                fitfunc.SetParameter(3, 17.4)
            if decaymode=='11':
                fitfunc.SetParameter(0, 0.033)
                fitfunc.SetParameter(1, 1.19)
                fitfunc.SetParLimits(1,0.50,13.9)
                fitfunc.SetParameter(2, 392)
                fitfunc.SetParameter(3, 98)
                
        else:
            fitfunc.SetParameter(0, 1.8)
            fitfunc.SetParameter(1, -9)
            fitfunc.SetParameter(2, 130)
            fitfunc.SetParameter(3, 240)
            if decaymode=='0':
                fitfunc.SetParameter(0, 0.11)
                fitfunc.SetParameter(1, 116)
                fitfunc.SetParameter(2, -31)
                fitfunc.SetParLimits(2,-35,-30)
                fitfunc.SetParameter(3, 1.45)
            if decaymode=='1':
                fitfunc.SetParameter(0, 0.19)
                fitfunc.SetParameter(1, -0.9)
                fitfunc.SetParameter(2, 108)
                fitfunc.SetParameter(3, 52.2)
            if decaymode=='10':
                fitfunc.SetParameter(0, 0.044)
                fitfunc.SetParameter(1, 0.27)
                fitfunc.SetParameter(2, 65)
                fitfunc.SetParameter(3, 32)
            if decaymode=='11':
                fitfunc.SetParameter(0, 0.063)
                fitfunc.SetParameter(1, 0.043)
                fitfunc.SetParameter(2, 53)
                fitfunc.SetParameter(3, 8.1)

    if (year=="2016post"):
        if cut =="QCD":
            if decaymode=='0':
                fitfunc.SetParameter(0, 0.18)
                fitfunc.SetParameter(1, -0.42)
                fitfunc.SetParameter(2, 56.1)
                fitfunc.SetParameter(3, 7.26)
            if decaymode=='1':
                fitfunc.SetParameter(0, 0.084)
                fitfunc.SetParameter(1, 0.051)
                fitfunc.SetParameter(2, 37.2)
                fitfunc.SetParameter(3, 2.53)
            if decaymode=='10':
                fitfunc.SetParameter(0, 0.06)
                fitfunc.SetParameter(1, 0.05)
                fitfunc.SetParameter(2, 54.1)
                fitfunc.SetParameter(3, 10.4)
            if decaymode=='11':
                fitfunc.SetParameter(0, 0.019)
                fitfunc.SetParameter(1, 0.092)
                fitfunc.SetParameter(2, 96.7)
                fitfunc.SetParameter(3, 41.7)
        else:
            fitfunc.SetParameter(0, 1.8)
            fitfunc.SetParameter(1, -9)
            fitfunc.SetParameter(2, 130)
            fitfunc.SetParameter(3, 240)
            if decaymode=='0':
                fitfunc.SetParameter(0, 0.18)
                fitfunc.SetParameter(1, -0.22)
                fitfunc.SetParLimits(1,-0.32,-0.2)
                fitfunc.SetParameter(2, 56.14)
                fitfunc.SetParameter(3, 7.26)
            if decaymode=='1':
                fitfunc.SetParameter(0, 0.25)
                fitfunc.SetParLimits(0,0.24,0.26)
                fitfunc.SetParameter(1, -0.89)
                fitfunc.SetParameter(2, 145)
                fitfunc.SetParameter(3, 93.1)
            if decaymode=='10':
                fitfunc.SetParameter(0, 0.03)
                fitfunc.SetParameter(1, 0.3)
                fitfunc.SetParameter(2, 74)
                fitfunc.SetParameter(3, 144)
            if decaymode=='11':
                fitfunc.SetParameter(0, 1.44)
                fitfunc.SetParameter(1, -3.7)
                fitfunc.SetParLimits(1,-32,-0.2)
                fitfunc.SetParameter(2, 480)
                fitfunc.SetParameter(3, 63.5)
                fitfunc.SetParLimits(3,60,1000)
                
    TGraph_FR.Fit(fitfunc, "R0")

    canvas = TCanvas("canvas", "", 800, 600)
    canvas.SetTitle("")
    canvas.SetBottomMargin(0.12)
    #canvas.SetGrid()
    TGraph_FR.GetYaxis().SetRangeUser(0.00, 0.30)
    if (year == "2016pre" and cut== "QCD" and decaymode=='0'):
        TGraph_FR.GetYaxis().SetRangeUser(0.00, 0.50)
    if (year == "2016post" and cut== "QCD" and decaymode=='0'):
        TGraph_FR.GetYaxis().SetRangeUser(0.00, 0.50)
    if (year == "2016post" and cut== "QCD" and decaymode=='10'):
        TGraph_FR.GetYaxis().SetRangeUser(0.00, 0.70)
    if (year == "2017" and cut== "QCD" and decaymode=='0'):
        TGraph_FR.GetYaxis().SetRangeUser(0.00, 0.70)
    #if (decaymode==1) TGraph_FR.GetYaxis().SetRangeUser(0.00, 0.30)
        
    TGraph_FR.GetYaxis().SetTitle("f_{#tau}")
    TGraph_FR.GetXaxis().SetRangeUser(0, 330)
    TGraph_FR.GetXaxis().SetTitle("#tau_{h} p_{T} [GeV]")

    TGraph_FR.SetLineColor(1)
    TGraph_FR.SetTitle("")
    TGraph_FR.Draw("PAE0")
    TGraph_FR.SetLineWidth(1)
    TGraph_FR.SetMarkerStyle(20)
    TGraph_FR.GetXaxis().SetTitleSize(0.06)
    TGraph_FR.GetYaxis().SetTitleSize(0.06)
    TGraph_FR.GetXaxis().SetLabelSize(0.05)
    TGraph_FR.GetYaxis().SetLabelSize(0.05)
    TGraph_FR.GetXaxis().SetTitleOffset(0.85)
    TGraph_FR.GetYaxis().SetTitleOffset(0.8)

    t = TLatex()
    t.SetNDC()
    t.SetTextFont(42)
    t.SetTextAlign(12)
    t.SetTextSize(0.06)
    if (year=="2016"): t.DrawLatex(0.55, .95, "36 fb^{-1} (2016, 13 TeV)")
    if (year=="2016pre"): t.DrawLatex(0.5, .95, "19 fb^{-1} (2016 preVFP, 13 TeV)")
    if (year=="2016post"): t.DrawLatex(0.5, .95, "16 fb^{-1} (2016 postVFP, 13 TeV)")
    if (year=="2017"): t.DrawLatex(0.55, .95, "41 fb^{-1} (2017, 13 TeV)")
    if (year=="2018"): t.DrawLatex(0.55, .95, "60 fb^{-1} (2018, 13 TeV)")

    t2 = TLatex();
    t2.SetNDC();
    t2.SetTextFont(61);
    t2.SetTextAlign(12);
    t2.SetTextSize(0.08);
    t2.DrawLatex(0.15, .95, "CMS")

    outNaming = "Plots_FR/fit" + cut + "_" + "dm" + decaymode + variablename + ".pdf"
    if (year=="2016"): outNaming = "Plots_FR/2016/fit"  + cut + "_" + "dm" + decaymode + variablename + ".pdf"
    if (year=="2016pre"): outNaming = "Plots_FR/2016pre/fit"  + cut + "_" + "dm" + decaymode + variablename + ".pdf"
    if (year=="2016post"): outNaming = "Plots_FR/2016post/fit" + cut + "_" + "dm" + decaymode + variablename + ".pdf"
    if (year=="2017"): outNaming = "Plots_FR/2017/fit" + cut + "_" + "dm" + decaymode + variablename + ".pdf"
    if (year=="2018"): outNaming = "Plots_FR/2018/fit" + cut + "_" + "dm" + decaymode + variablename + ".pdf"
    outNamingPng = "Plots_FR/fit"+ cut + "_" + "dm" + decaymode + variablename + ".png"
    if (year=="2016"): outNamingPng = "Plots_FR/2016/fit" + cut + "_" + "dm" + decaymode + variablename + ".png"
    if (year=="2016pre"): outNamingPng = "Plots_FR/2016pre/fit" + cut + "_" + "dm" + decaymode + variablename + ".png"
    if (year=="2016post"): outNamingPng = "Plots_FR/2016post/fit" + cut + "_" + "dm" + decaymode + variablename + ".png"
    if (year=="2017"): outNamingPng = "Plots_FR/2017/fit" + cut + "_" + "dm" + decaymode + variablename + ".png"
    if (year=="2018"): outNamingPng = "Plots_FR/2018/fit" + cut + "_" + "dm" + decaymode + variablename + ".png"
    fitfunc.Draw("SAME")
    fitfunc.SetLineColor(2)
    
    x = np.zeros(100,dtype=float)
    yup = np.zeros(100,dtype=float)
    ydown = np.zeros(100,dtype=float)
    n = 100
    for i in range(0,n):
        x[i] = 30+i*2.7
        yup[i] = fitfunc.Eval(x[i])*(1.0+((x[i]-30)/540+0.00))
        ydown[i] = fitfunc.Eval(x[i])*(1.0-((x[i]-30)/540+0.00))
    gup = TGraph(n,x,yup)
    gup.SetLineColor(2)
    gup.Draw("CSAME")
    gdown = TGraph(n,x,ydown)
    gdown.SetLineColor(2)
    gdown.Draw("CSAME")
    canvas.SaveAs(outNaming)
    canvas.SaveAs(outNamingPng)
    
    FR_H.cd()
    TGraph_FR.SetName("FRhisto_{}_dm{}_{}".format(cut, decaymode, variablename))
    TGraph_FR.Write()
    return fitfunc
    
    
    
def fit_histo_ntrk(cut, decaymode, variablename , variabletitle):
    decaymode = str(decaymode)
    Numerator = f.Get("h_tauFRnt_{}_dm{}_M".format(cut,decaymode))
    Denumerator = f.Get("h_tauFRnt_{}_dm{}_VVVL".format(cut,decaymode))

    histogram_pass = Numerator
    histogram_fail = Denumerator
    
    histogram_FR = histogram_pass.Clone("h_tauFRnt_{}_dm{}_FR".format(cut,decaymode))
    histogram_FR.Divide(histogram_fail)
    ratio = Numerator.Integral()/Denumerator.Integral()
    for i in range(1,histogram_FR.GetNbinsX()+1):
        histogram_FR.SetBinContent(i,histogram_FR.GetBinContent(i)/ratio)
        histogram_FR.SetBinError(i,histogram_FR.GetBinError(i)/ratio)
        
    print(Numerator.GetBinContent(2))
    print(Denumerator.GetBinContent(2))
    print(histogram_FR.GetBinContent(2))

    TGraph_FR = TGraphAsymmErrors(histogram_FR)

    
    fitfunc1 = TF1("fitfunc1", fitExp, 0, 25, 4)
    fitfunc2 = TF1("fitfunc2", fitPoly2, 25, 100, 3)
    if year =="2018":
        fitfunc1.SetParameter(0, 0.56)
        fitfunc1.SetParameter(1, 1.2)
        fitfunc1.SetParameter(2, 0.04)
        fitfunc1.SetParameter(3, -0.16)
        if cut =='W':
            if decaymode=='11':
                fitfunc1 = TF1("fitfunc1", fitExp, 0, 25, 4)
                fitfunc2 = TF1("fitfunc2", fitPoly2, 25, 100, 3)
                fitfunc1.SetParameter(0, 0.86)
                fitfunc1.SetParLimits(0,0.8,0.9)
                fitfunc1.SetParameter(1, 1.03)
                fitfunc1.SetParameter(2, 0.059)
                fitfunc1.SetParameter(3, -0.06)
                
    if year =="2017":
        fitfunc1.SetParameter(0, 0.56)
        fitfunc1.SetParameter(1, 1.2)
        fitfunc1.SetParameter(2, 0.04)
        fitfunc1.SetParameter(3, -0.16)

    if year =="2016pre":
        fitfunc1.SetParameter(0, 0.56)
        fitfunc1.SetParameter(1, 1.2)
        fitfunc1.SetParameter(2, 0.04)
        fitfunc1.SetParameter(3, -0.16)
        if cut =='QCD':
            if decaymode=='1':
                fitfunc1 = TF1("fitfunc1", fitExp, 0, 25, 4)
                fitfunc2 = TF1("fitfunc2", fitPoly2, 25, 100, 3)
                fitfunc1.SetParameter(0, 0.87)
                fitfunc1.SetParLimits(0,0.6,1.0)
                fitfunc1.SetParameter(1, 0.76)
                fitfunc1.SetParameter(2, 0.077)
                fitfunc1.SetParameter(3, -0.58)
            if decaymode=='10':
                fitfunc1 = TF1("fitfunc1", fitExp, 0, 25, 4)
                fitfunc2 = TF1("fitfunc2", fitPoly2, 25, 100, 3)
                fitfunc1.SetParameter(0, 0.91)
                
                fitfunc1.SetParameter(1, 0.62)
                fitfunc1.SetParameter(2, 0.066)
                fitfunc1.SetParameter(3, -0.35)
            if decaymode=='11':
                fitfunc1 = TF1("fitfunc1", fitExp, 0, 25, 4)
                fitfunc2 = TF1("fitfunc2", fitPoly2, 25, 100, 3)
                fitfunc1.SetParameter(0, 0.74)
                fitfunc1.SetParLimits(0,0.6,0.8)
                fitfunc1.SetParameter(1, 0.63)

                fitfunc1.SetParameter(2, 0.039)
                fitfunc1.SetParameter(3, -0.37)
        if cut == 'W':
            if decaymode=='11':
                fitfunc1 = TF1("fitfunc1", fitExp, 0, 25, 4)
                fitfunc2 = TF1("fitfunc2", fitPoly2, 25, 100, 3)
                fitfunc1.SetParameter(0, 0.62)
                fitfunc1.SetParLimits(0,0.5,0.8)
                fitfunc1.SetParameter(1, 0.71)
                fitfunc1.SetParameter(2, 0.046)
                fitfunc1.SetParameter(3, -0.55)
            

            

    if year =="2016post":
        fitfunc1.SetParameter(0, 0.56)
        fitfunc1.SetParameter(1, 1.2)
        fitfunc1.SetParameter(2, 0.04)
        fitfunc1.SetParameter(3, -0.16)
        if cut == 'QCD':
            if decaymode=='10':
                fitfunc1 = TF1("fitfunc1", fitExp, 0, 30, 4)
                fitfunc2 = TF1("fitfunc2", fitPoly2, 30, 100, 3)
                fitfunc1.SetParameter(0, 0.41)
                fitfunc1.SetParLimits(0,0.3,0.6)
                fitfunc1.SetParameter(1, 0.74)
                fitfunc1.SetParameter(2, 0.030)
                fitfunc1.SetParameter(3, -0.6)
                
        if cut == 'W':
            if decaymode=='0':
                fitfunc1 = TF1("fitfunc1", fitExp, 0, 25, 4)
                fitfunc2 = TF1("fitfunc2", fitPoly2, 25, 100, 3)
                fitfunc1.SetParameter(0, 0.62)
                fitfunc1.SetParLimits(0,0.5,0.8)
                fitfunc1.SetParameter(1, 0.71)
                fitfunc1.SetParameter(2, 0.046)
                fitfunc1.SetParameter(3, -0.55)

    if year =="Run2" or year =="Run2paper":

        fitfunc1 = TF1("fitfunc1", fitExp, 0, 20, 4)
        fitfunc2 = TF1("fitfunc2", fitPoly2, 20, 100, 3)

        if cut=='QCD':
            if decaymode=='11':
                fitfunc1 = TF1("fitfunc1", fitExp, 0, 15, 4)
                fitfunc2 = TF1("fitfunc2", fitPoly2, 15, 100, 3)
            
        if cut=="W":
            fitfunc1 = TF1("fitfunc1", fitExp, 0, 10, 4)
            fitfunc2 = TF1("fitfunc2", fitPoly2, 10, 100, 3)
            if decaymode=='11':
                fitfunc1 = TF1("fitfunc1", fitExp, 0, 15, 4)
                fitfunc2 = TF1("fitfunc2", fitPoly2, 15, 100, 3)
            if decaymode=='1':
                fitfunc1 = TF1("fitfunc1", fitExp, 0, 10, 4)
                fitfunc2 = TF1("fitfunc2", fitPoly2, 10, 100, 3)
                fitfunc2.SetParLimits(0, 0., 5.)
                
            
        fitfunc1.SetParameter(0, 0.56)
        fitfunc1.SetParameter(1, 1.2)
        fitfunc1.SetParameter(2, 0.04)
        fitfunc1.SetParameter(3, -0.16)

    
    xAxisMax = 500.
    TGraph_FR.Fit(fitfunc2, "R0")
    TGraph_FR.Fit(fitfunc1, "R0")


    canvas = TCanvas("canvas", "", 800, 600)
    canvas.SetTitle("")
    #canvas.SetGrid()
    TGraph_FR.GetYaxis().SetRangeUser(0.00, 5.15)
    if cut=="W" and (year=="Run2" or year=="Run2paper"):
        if (decaymode=='0'): TGraph_FR.GetYaxis().SetRangeUser(0.00, 12.15)
        if (decaymode=='1'): TGraph_FR.GetYaxis().SetRangeUser(0.00, 8.15)
        if (decaymode=='10'): TGraph_FR.GetYaxis().SetRangeUser(0.00, 8.15)
        
    #if (decaymode==1) TGraph_FR.GetYaxis().SetRangeUser(0.00, 0.30)
        
    TGraph_FR.GetYaxis().SetTitle("MF correction factor")
    TGraph_FR.GetXaxis().SetRangeUser(0, 100)
    TGraph_FR.GetXaxis().SetTitle("N_{tracks}")
    
    TGraph_FR.SetTitle("")
    TGraph_FR.SetLineColor(1)
    TGraph_FR.Draw("PAE0")
    TGraph_FR.SetLineWidth(1)
    TGraph_FR.SetMarkerStyle(20)
    TGraph_FR.GetXaxis().SetTitleSize(0.06)
    TGraph_FR.GetYaxis().SetTitleSize(0.06)
    TGraph_FR.GetXaxis().SetLabelSize(0.05)
    TGraph_FR.GetYaxis().SetLabelSize(0.05)
    TGraph_FR.GetXaxis().SetTitleOffset(0.7)
    TGraph_FR.GetYaxis().SetTitleOffset(0.8)

    t = TLatex()
    t.SetNDC()
    t.SetTextFont(42)
    t.SetTextAlign(12)
    t.SetTextSize(0.06)
    if (year=="2016"): t.DrawLatex(0.55, .95, "36 fb^{-1} (2016, 13 TeV)")
    if (year=="2016pre"): t.DrawLatex(0.5, .95, "19 fb^{-1} (2016 preVFP, 13 TeV)")
    if (year=="2016post"): t.DrawLatex(0.5, .95, "16 fb^{-1} (2016 postVFP, 13 TeV)")
    if (year=="2017"): t.DrawLatex(0.55, .95, "41 fb^{-1} (2017, 13 TeV)")
    if (year=="2018"): t.DrawLatex(0.55, .95, "60 fb^{-1} (2018, 13 TeV)")
    if (year=="Run2" or "Run2paper"): t.DrawLatex(0.59, .95, "138 fb^{-1} (13 TeV)")
    
    t2 = TLatex();
    t2.SetNDC();
    t2.SetTextFont(61);
    t2.SetTextAlign(12);
    t2.SetTextSize(0.08);
    t2.DrawLatex(0.10, .95, "CMS")
    
    t4 = TLatex()
    t4.SetNDC()
    t4.SetTextFont(52)
    t4.SetTextAlign(12)
    t4.SetTextSize(0.06)
    if (year=="Run2paper"):
        t4.DrawLatex(0.24,0.94,"Supplementary")
    else:
        t4.DrawLatex(0.24,0.94,"Preliminary")


    t3 = TLatex();
    t3.SetNDC();
    t3.SetTextFont(42);
    t3.SetTextAlign(12);
    t3.SetTextSize(0.06);
    '''if (cut=="QCD"):
        if (decaymode=='0'): t3.DrawLatex(0.4, .55, "SS CR, #mu#tau_{h}, 1-prong")
        if (decaymode=='1'): t3.DrawLatex(0.4, .55, "SS CR, #mu#tau_{h}, 1-prong+#pi^{0}")
        if (decaymode=='10'): t3.DrawLatex(0.4, .55, "SS CR, #mu#tau_{h}, 3-prong")
        if (decaymode=='11'): t3.DrawLatex(0.4, .55, "SS CR, #mu#tau_{h}, 3-prong+#pi^{0}")
    if (cut=="W"):
        if (decaymode=='0'): t3.DrawLatex(0.4, .55, "High-m_{T} CR, #mu#tau_{h}, 1-prong")
        if (decaymode=='1'): t3.DrawLatex(0.4, .55, "High-m_{T} CR, #mu#tau_{h}, 1-prong+#pi^{0}")
        if (decaymode=='10'): t3.DrawLatex(0.4, .55, "High-m_{T} CR, #mu#tau_{h}, 3-prong")
        if (decaymode=='11'): t3.DrawLatex(0.4, .55, "High-m_{T} CR, #mu#tau_{h}, 3-prong+#pi^{0}")'''

    if (cut=="QCD"):
        if (decaymode=='0'): t3.DrawLatex(0.3, .55, "SS CR, #mu#tau_{h}, h^{#pm}")
        if (decaymode=='1'): t3.DrawLatex(0.3, .55, "SS CR, #mu#tau_{h}, h^{#pm}+#pi^{0}(s)")
        if (decaymode=='10'): t3.DrawLatex(0.3, .55, "SS CR, #mu#tau_{h}, h^{#pm}h^{#mp}h^{#pm}")
        if (decaymode=='11'): t3.DrawLatex(0.3, .55, "SS CR, #mu#tau_{h}, h^{#pm}h^{#mp}h^{#pm}+#pi^{0}(s)")
    if (cut=="W"):
        if (decaymode=='0'): t3.DrawLatex(0.3, .55, "High-m_{T} CR, #mu#tau_{h}, h^{#pm}")
        if (decaymode=='1'): t3.DrawLatex(0.3, .55, "High-m_{T} CR, #mu#tau_{h}, h^{#pm}+#pi^{0}(s)")
        if (decaymode=='10'): t3.DrawLatex(0.3, .55, "High-m_{T} CR, #mu#tau_{h}, h^{#pm}h^{#mp}h^{#pm}")
        if (decaymode=='11'): t3.DrawLatex(0.3, .55, "High-m_{T} CR, #mu#tau_{h}, h^{#pm}h^{#mp}h^{#pm}+#pi^{0}(s)")

    outNaming = "Plots_FR/fit" + cut + "_" + "dm" + decaymode + variablename + ".pdf"
    if (year=="2016"): outNaming = "Plots_FR/2016/fit"  + cut + "_" + "dm" + decaymode + variablename + ".pdf"
    if (year=="2016pre"): outNaming = "Plots_FR/2016pre/fit"  + cut + "_" + "dm" + decaymode + variablename + ".pdf"
    if (year=="2016post"): outNaming = "Plots_FR/2016post/fit" + cut + "_" + "dm" + decaymode + variablename + ".pdf"
    if (year=="2017"): outNaming = "Plots_FR/2017/fit" + cut + "_" + "dm" + decaymode + variablename + ".pdf"
    if (year=="2018"): outNaming = "Plots_FR/2018/fit" + cut + "_" + "dm" + decaymode + variablename + ".pdf"
    if (year=="Run2"): outNaming = "Plots_FR/Run2/fit" + cut + "_" + "dm" + decaymode + variablename + ".pdf"
    if (year=="Run2paper"): outNaming = "Plots_FR/Run2paper/fit" + cut + "_" + "dm" + decaymode + variablename + ".pdf"
    outNamingPng = "Plots_FR/fit"+ cut + "_" + "dm" + decaymode + variablename + ".png"
    if (year=="2016"): outNamingPng = "Plots_FR/2016/fit" + cut + "_" + "dm" + decaymode + variablename + ".png"
    if (year=="2016pre"): outNamingPng = "Plots_FR/2016pre/fit" + cut + "_" + "dm" + decaymode + variablename + ".png"
    if (year=="2016post"): outNamingPng = "Plots_FR/2016post/fit" + cut + "_" + "dm" + decaymode + variablename + ".png"
    if (year=="2017"): outNamingPng = "Plots_FR/2017/fit" + cut + "_" + "dm" + decaymode + variablename + ".png"
    if (year=="2018"): outNamingPng = "Plots_FR/2018/fit" + cut + "_" + "dm" + decaymode + variablename + ".png"
    if (year=="Run2"): outNamingPng = "Plots_FR/Run2/fit" + cut + "_" + "dm" + decaymode + variablename + ".png"
    if (year=="Run2paper"): outNamingPng = "Plots_FR/Run2paper/fit" + cut + "_" + "dm" + decaymode + variablename + ".png"
    outNamingRoot = "Plots_FR/fit"+ cut + "_" + "dm" + decaymode + variablename + ".root"
    if (year=="2016"): outNamingRoot = "Plots_FR/2016/fit" + cut + "_" + "dm" + decaymode + variablename + ".root"
    if (year=="2016pre"): outNamingRoot = "Plots_FR/2016pre/fit" + cut + "_" + "dm" + decaymode + variablename + ".root"
    if (year=="2016post"): outNamingRoot = "Plots_FR/2016post/fit" + cut + "_" + "dm" + decaymode + variablename + ".root"
    if (year=="2017"): outNamingRoot = "Plots_FR/2017/fit" + cut + "_" + "dm" + decaymode + variablename + ".root"
    if (year=="2018"): outNamingRoot = "Plots_FR/2018/fit" + cut + "_" + "dm" + decaymode + variablename + ".root"
    if (year=="Run2"): outNamingRoot = "Plots_FR/Run2/fit" + cut + "_" + "dm" + decaymode + variablename + ".root"
    if (year=="Run2paper"): outNamingRoot = "Plots_FR/Run2paper/fit" + cut + "_" + "dm" + decaymode + variablename + ".root"
    #fitfunc2.Draw("SAME")
    fitfunc2.SetLineColor(3)

    fitfunc1.SetLineColor(ROOT.kMagenta)
    fitfunc1.Draw("SAME")
     
    hint = TH1D("hint","Fitted Gaussian with .68 conf.band", 100, 0, 25)
    if (year == "Run2" or year=="Run2paper"):
        hint = TH1D("hint","Fitted Gaussian with .68 conf.band", 100, 0, 20)
        if cut == "QCD":
            if decaymode=='11':
                hint = TH1D("hint","Fitted Gaussian with .68 conf.band", 100, 0, 15)
        if cut == "W":
            hint = TH1D("hint","Fitted Gaussian with .68 conf.band", 100, 0, 10)
            if decaymode=='11':
                hint = TH1D("hint","Fitted Gaussian with .68 conf.band", 100, 0, 15)
    (TVirtualFitter.GetFitter()).GetConfidenceIntervals(hint,0.68)
    hint.SetStats(False)
    hint.SetFillColor(kCyan)
    hint.SetFillStyle(3001)
    hint.Draw("e3 same")
    print (hint.GetBinContent(1), " " , hint.GetBinError(1))
    err=hint.GetBinError(1)/hint.GetBinContent(1)
    print ("error ", err)
    #fitfunc2.Draw("SAME")
    fitfunc1.Draw("SAME")
    TGraph_FR.Draw("P")


    leg = TLegend(0.2,0.75,0.9,0.9,"","brNDC")
    leg.SetNColumns(2)
    leg.SetBorderSize(0)
    leg.SetLineWidth(0)
    leg.SetLineStyle(0)
    leg.SetFillStyle(0)
    leg.AddEntry(fitfunc1,"Exponential fit", "l")
    leg.AddEntry(hint,"Fit uncertainty","f")
    leg.Draw("SAME")

    canvas.SaveAs(outNaming)
    canvas.SaveAs(outNamingPng)
    canvas.SaveAs(outNamingRoot)
    
    FR_H.cd()
    TGraph_FR.SetName("FRhisto_{}_dm{}_{}".format(cut, decaymode, variablename))
    TGraph_FR.Write()
    return fitfunc1,fitfunc2,err

class variable:
    def __init__(self, name, title, nbins, binning):
        self.name=name
        self.title = title
        self.nbins=nbins
        self.binning = binning

taupt = variable("taupt","#tau_{h} p_{T}",int(11),np.array([30,35,40,45,50,60,80,100,150,200,250,300],dtype=float))
ntrk = variable("nTrk","N_{tracks}",int(24),np.array([-0.5,0.5,1.5,2.5,3.5,4.5,9.5,14.5,19.5,24.5,29.5,34.5,39.5,44.5,49.5,54.5,59.5,64.5,69.5,74.5,79.5,84.5,89.5,94.5,99.5],dtype=float))
Acopl = variable("Acopl","Acoplanarity",int(20),np.array([0,0.05,0.1,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50,0.55,0.60,0.65,0.70,0.75,0.80,0.85,0.90,0.95,1.00],dtype=float))
variablelist = [taupt,ntrk]
if (year == "Run2" or year=="Run2paper"):
    variablelist = [ntrk]
outfile = TFile("Histo/HistoforFR_{}/FRfit_mutau.root".format(year),"recreate")
err_nt0_ffW=TH1F("err_nt0_ffW","err_nt0_ffW",12,0,12)
err_nt0_ffQCD=TH1F("err_nt0_ffQCD","err_nt0_ffQCD",12,0,12)
errlist = []
for cut in ["QCD","W"]:
    for decaymode in [0,1,10,11]:
        for variable in variablelist:
            print ("Begin to fit cut_{} decaymode_{} variable_{}".format(cut,decaymode,variable.name))
            if (variable==ntrk):
                fitfunc1,fitfunc2,err = fit_histo_ntrk(cut,decaymode,variable.name,variable.title)
                fitfunc1.SetName("fitfunc_{}_DM{}_low{}".format(cut,decaymode,variable.name))
                fitfunc2.SetName("fitfunc_{}_DM{}_high{}".format(cut,decaymode,variable.name))
                errlist.append(err)
                outfile.cd()
                fitfunc1.Write()
                fitfunc2.Write()
            else:
                fitfunc = fit_histo(cut,decaymode,variable.name,variable.title)
                fitfunc.SetName("fitfunc_{}_DM{}_{}".format(cut,decaymode,variable.name))
                outfile.cd()
                fitfunc.Write()
err_nt0_ffQCD.SetBinContent(1,errlist[0])
err_nt0_ffQCD.SetBinContent(2,errlist[1])
err_nt0_ffQCD.SetBinContent(11,errlist[2])
err_nt0_ffQCD.SetBinContent(12,errlist[3])
err_nt0_ffW.SetBinContent(1,errlist[4])
err_nt0_ffW.SetBinContent(2,errlist[5])
err_nt0_ffW.SetBinContent(11,errlist[6])
err_nt0_ffW.SetBinContent(12,errlist[7])
outfile.cd()
err_nt0_ffQCD.Write()
err_nt0_ffW.Write()

hQCD_xtrg_VVVL = f.Get("h_tauFR_QCD_xtrg_VVVL")
hQCD_xtrg_M = f.Get("h_tauFR_QCD_xtrg_M")
hW_xtrg_VVVL = f.Get("h_tauFR_W_xtrg_VVVL")
hW_xtrg_M = f.Get("h_tauFR_W_xtrg_M")

hQCD_xtrg_M.Divide(hQCD_xtrg_VVVL)
hW_xtrg_M.Divide(hW_xtrg_VVVL)
hQCD_xtrg_M.SetName("h_tauFR_QCD_xtrg_SF")
hW_xtrg_M.SetName("h_tauFR_W_xtrg_SF")
outfile.cd()
hQCD_xtrg_M.Write()
hW_xtrg_M.Write()

outfile.Close()
    
    

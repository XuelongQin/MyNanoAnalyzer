from ROOT import TFile, TFile, TH1D, TCanvas,TH1F,TPaveText,TF1,TMath,TGraphAsymmErrors,TLatex,TGraph,TVirtualFitter,kCyan
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

f = TFile("Histo/HistoforFR_{}/DataSub.root".format(year))
FR_H = TFile("Histo/HistoforFR_{}/FitHistograms_FR.root".format(year), "RECREATE")

def fit_histo(cut, decaymode, variablename , variabletitle,leadingname,leading_str):
    decaymode = str(decaymode)
    Numerator = f.Get("h_tau{}FR_{}_dm{}_M".format(leadingname,cut,decaymode))
    Denumerator = f.Get("h_tau{}FR_{}_dm{}_VVVL".format(leadingname,cut,decaymode))

    histogram_pass = Numerator
    
    histogram_fail = Denumerator

    histogram_FR = histogram_pass.Clone("h_tau{}FR_{}_dm{}_FR".format(leadingname,cut,decaymode))
    histogram_FR.Divide(histogram_fail)

    print(Numerator.GetBinContent(1))
    print(Denumerator.GetBinContent(1))
    print(histogram_FR.GetBinContent(1))

    TGraph_FR = TGraphAsymmErrors(histogram_FR)
    
    fMin = 40
    fMax = 300
    nPar = 4 
    fitfunc = TF1("fitfunc", fitLandau, fMin, fMax, nPar)
    xAxisMax = 500.
    if (year=="2018"):
        if leadingname =="1":
            if decaymode=='0':
                fitfunc.SetParameter(0, 0.6)
                fitfunc.SetParameter(1, -0.9)
                fitfunc.SetParameter(2, 83)
                fitfunc.SetParameter(3, 75)
            if decaymode=='1':
                fitfunc.SetParameter(0, 0.39)
                fitfunc.SetParameter(1, -0.188)
                fitfunc.SetParameter(2, 170)
                fitfunc.SetParameter(3, 200)
            if decaymode=='10':
                fitfunc.SetParameter(0, 0.22)
                fitfunc.SetParameter(1, -42.5)
                fitfunc.SetParameter(2, 8)
                fitfunc.SetParLimits(2,0,10)
                fitfunc.SetParameter(3, 0.97)
            if decaymode=='11':
                fitfunc.SetParameter(0, 0.084)
                fitfunc.SetParameter(1, -0.10)
                fitfunc.SetParameter(2, 47.1)
                fitfunc.SetParameter(3, 4.74)
        else:
            fitfunc.SetParameter(0, 1.8)
            fitfunc.SetParameter(1, -9)
            fitfunc.SetParameter(2, 130)
            fitfunc.SetParameter(3, 240)
            if decaymode=='0':
                fitfunc.SetParameter(0, 1.3)
                fitfunc.SetParameter(1, -6.0)
                fitfunc.SetParameter(2, 89.6)
                fitfunc.SetParLimits(2,80,250)
                fitfunc.SetParameter(3, 56.2)
            if decaymode=='1':
                fitfunc.SetParameter(0,0.27)
                fitfunc.SetParameter(1, -0.87)
                fitfunc.SetParameter(2, 110)
                fitfunc.SetParLimits(2,100,150)
                fitfunc.SetParameter(3, 40)
            if decaymode=='10':
                fitfunc.SetParameter(0, 0.03)
                fitfunc.SetParameter(1, 0.3)
                fitfunc.SetParameter(2, 120)
                fitfunc.SetParameter(3, 344)
            if decaymode=='11':
                fitfunc.SetParameter(0, 0.084)
                fitfunc.SetParameter(1, -0.1)
                fitfunc.SetParameter(2, 47.1)
                fitfunc.SetParameter(3, 4.74)
                fitfunc.SetParLimits(3,1,150)

    if (year=="2017"):
        if leadingname =="1":
            if decaymode=='0':
                fitfunc.SetParameter(0, 0.6)
                fitfunc.SetParameter(1, -0.9)
                fitfunc.SetParameter(2, 83)
                fitfunc.SetParameter(3, 75)
            if decaymode=='1':
                fitfunc.SetParameter(0, 0.16)
                fitfunc.SetParameter(1, 2.65)
                #fitfunc.SetParLimits(1,0,10)
                fitfunc.SetParameter(2, 0.22)
                #fitfunc.SetParLimits(2,0,30)
                fitfunc.SetParameter(3, 11.2)
            if decaymode=='10':
                fitfunc.SetParameter(0, 0.25)
                fitfunc.SetParameter(1, -0.29)
                fitfunc.SetParameter(2, 41.3)
                fitfunc.SetParameter(3, 4.7)
            if decaymode=='11':
                fitfunc.SetParameter(0, 0.084)
                fitfunc.SetParameter(1, -0.10)
                fitfunc.SetParameter(2, 47.1)
                fitfunc.SetParameter(3, 4.74)
        else:
            fitfunc.SetParameter(0, 1.8)
            fitfunc.SetParameter(1, -9)
            fitfunc.SetParameter(2, 130)
            fitfunc.SetParameter(3, 240)
            if decaymode=='0':
                fitfunc.SetParameter(0, 0.51)
                fitfunc.SetParameter(1, -1.18)
                fitfunc.SetParameter(2, 100)
                fitfunc.SetParameter(3, 45.6)
            if decaymode=='1':
                fitfunc.SetParameter(0,0.44)
                fitfunc.SetParameter(1, -1.6)
                fitfunc.SetParameter(2, 142)
                #fitfunc.SetParLimits(2,100,150)
                fitfunc.SetParameter(3, 93)
            if decaymode=='10':
                fitfunc.SetParameter(0, 0.11)
                fitfunc.SetParameter(1, 0.23)
                fitfunc.SetParameter(2, 72.7)
                fitfunc.SetParameter(3, 13.8)
            if decaymode=='11':
                fitfunc.SetParameter(0, 0.084)
                fitfunc.SetParameter(1, -0.1)
                fitfunc.SetParameter(2, 47.1)
                fitfunc.SetParameter(3, 4.74)


    if (year=="2016pre"):
        if leadingname =="1":
            if decaymode=='0':
                fitfunc.SetParameter(0, 0.6)
                fitfunc.SetParameter(1, -0.9)
                fitfunc.SetParameter(2, 83)
                fitfunc.SetParameter(3, 75)
            if decaymode=='1':
                fitfunc.SetParameter(0, 1.18)
                fitfunc.SetParameter(1, -5.79)
                fitfunc.SetParameter(2, 181)
                fitfunc.SetParameter(3, 157)
            if decaymode=='10':
                fitfunc.SetParameter(0, 0.103)
                fitfunc.SetParameter(1, 0.47)
                fitfunc.SetParameter(2, 76.3)
                fitfunc.SetParameter(3, 29)
            if decaymode=='11':
                fitfunc.SetParameter(0, 0.073)
                fitfunc.SetParameter(1, -0.236)
                fitfunc.SetParameter(2, 23.4)
                fitfunc.SetParLimits(2,0,30)
                fitfunc.SetParameter(3, 0.43)
        else:
            fitfunc.SetParameter(0, 1.8)
            fitfunc.SetParameter(1, -9)
            fitfunc.SetParameter(2, 130)
            fitfunc.SetParameter(3, 240)
            if decaymode=='0':
                fitfunc.SetParameter(0, 0.51)
                fitfunc.SetParameter(1, -1.18)
                fitfunc.SetParameter(2, 100)
                fitfunc.SetParameter(3, 45.6)
            if decaymode=='1':
                fitfunc.SetParameter(0,0.44)
                fitfunc.SetParameter(1, -1.6)
                fitfunc.SetParameter(2, 142)
                #fitfunc.SetParLimits(2,100,150)
                fitfunc.SetParameter(3, 93)
            if decaymode=='10':
                fitfunc.SetParameter(0, 0.11)
                fitfunc.SetParameter(1, 0.23)
                fitfunc.SetParameter(2, 72.7)
                fitfunc.SetParameter(3, 13.8)
            if decaymode=='11':
                fitfunc.SetParameter(0, 0.084)
                fitfunc.SetParameter(1, -0.1)
                fitfunc.SetParameter(2, 47.1)
                fitfunc.SetParameter(3, 4.74)
                
    if (year=="2016post"):
        if leadingname =="1":
            if decaymode=='0':
                fitfunc.SetParameter(0, 0.6)
                fitfunc.SetParameter(1, -0.9)
                fitfunc.SetParameter(2, 83)
                fitfunc.SetParameter(3, 75)
            if decaymode=='1':
                fitfunc.SetParameter(0, 0.39)
                fitfunc.SetParameter(1, -0.188)
                fitfunc.SetParameter(2, 170)
                fitfunc.SetParameter(3, 200)
            if decaymode=='10':
                fitfunc.SetParameter(0, 0.103)
                fitfunc.SetParameter(1, 0.47)
                fitfunc.SetParameter(2, 76.3)
                fitfunc.SetParameter(3, 29)
            if decaymode=='11':
                fitfunc.SetParameter(0, 0.081)
                fitfunc.SetParameter(1, -0.088)
                fitfunc.SetParameter(2, 46.6)
                fitfunc.SetParameter(3, 4.69)
        else:
            fitfunc.SetParameter(0, 1.8)
            fitfunc.SetParameter(1, -9)
            fitfunc.SetParameter(2, 130)
            fitfunc.SetParameter(3, 240)
            if decaymode=='0':
                fitfunc.SetParameter(0, 1.3)
                fitfunc.SetParameter(1, -6.23)
                fitfunc.SetParameter(2, 133)
                fitfunc.SetParameter(3, 100)
            if decaymode=='1':
                fitfunc.SetParameter(0,0.27)
                fitfunc.SetParameter(1, -0.87)
                fitfunc.SetParameter(2, 110)
                fitfunc.SetParameter(3, 39.9)
            if decaymode=='10':
                fitfunc.SetParameter(0, 0.11)
                fitfunc.SetParameter(1, 0.23)
                fitfunc.SetParameter(2, 72.7)
                fitfunc.SetParameter(3, 13.8)
            if decaymode=='11':
                fitfunc.SetParameter(0, 0.056)
                fitfunc.SetParameter(1, -0.024)
                fitfunc.SetParameter(2, 42.5)
                fitfunc.SetParameter(3, 0.006)
                
    TGraph_FR.Fit(fitfunc, "R0")

    canvas = TCanvas("canvas", "", 800, 800)
    canvas.SetTitle("")
    canvas.SetGrid()
    TGraph_FR.GetYaxis().SetRangeUser(0.00, 1.0)
    if decaymode=='1' or decaymode=='10':
        TGraph_FR.GetYaxis().SetRangeUser(0.00, 0.5)
    if (year=="2016post"):
        if (leadingname == '1'):
            if decaymode == '10':
                TGraph_FR.GetYaxis().SetRangeUser(0.00, 0.8)
                
    if decaymode=='11':
        TGraph_FR.GetYaxis().SetRangeUser(0.00, 0.3)
    #if (decaymode==1) TGraph_FR.GetYaxis().SetRangeUser(0.00, 0.30)
        
    TGraph_FR.GetYaxis().SetTitle("f_{#tau}")
    TGraph_FR.GetXaxis().SetRangeUser(0, 330)
    TGraph_FR.GetXaxis().SetTitle("{} [GeV]".format(variabletitle))
    
    TGraph_FR.SetTitle("")
    TGraph_FR.Draw("PAE0")
    TGraph_FR.SetLineWidth(3)

    t = TLatex()
    t.SetNDC()
    t.SetTextFont(42)
    t.SetTextAlign(12)
    t.SetTextSize(0.04)
    if (year=="2016"): t.DrawLatex(0.55, .95, "36 fb^{-1} (2016, 13 TeV)")
    if (year=="2016pre"): t.DrawLatex(0.5, .95, "19 fb^{-1} (2016 preVFP, 13 TeV)")
    if (year=="2016post"): t.DrawLatex(0.5, .95, "16 fb^{-1} (2016 postVFP, 13 TeV)")
    if (year=="2017"): t.DrawLatex(0.55, .95, "41 fb^{-1} (2017, 13 TeV)")
    if (year=="2018"): t.DrawLatex(0.55, .95, "60 fb^{-1} (2018, 13 TeV)")
    

    outNaming = "Plots_FR/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".pdf"
    if (year=="2016"): outNaming = "Plots_FR/2016/fit"  + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".pdf"
    if (year=="2016pre"): outNaming = "Plots_FR/2016pre/fit"  + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".pdf"
    if (year=="2016post"): outNaming = "Plots_FR/2016post/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".pdf"
    if (year=="2017"): outNaming = "Plots_FR/2017/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".pdf"
    if (year=="2018"): outNaming = "Plots_FR/2018/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".pdf"
    outNamingPng = "Plots_FR/fit"+ cut + "_" + "dm" + decaymode + variablename + leading_str+ ".png"
    if (year=="2016"): outNamingPng = "Plots_FR/2016/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".png"
    if (year=="2016pre"): outNamingPng = "Plots_FR/2016pre/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".png"
    if (year=="2016post"): outNamingPng = "Plots_FR/2016post/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".png"
    if (year=="2017"): outNamingPng = "Plots_FR/2017/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".png"
    if (year=="2018"): outNamingPng = "Plots_FR/2018/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".png"
    fitfunc.Draw("SAME")
    fitfunc.SetLineColor(2)
    
    x = np.zeros(100,dtype=float)
    yup = np.zeros(100,dtype=float)
    ydown = np.zeros(100,dtype=float)
    n = 100
    for i in range(0,n):
        x[i] = 40+i*2.6
        yup[i] = fitfunc.Eval(x[i])*(1.0+((x[i]-40)/520+0.00))
        ydown[i] = fitfunc.Eval(x[i])*(1.0-((x[i]-40)/520+0.00))
    gup = TGraph(n,x,yup)
    gup.SetLineColor(2)
    gup.Draw("CSAME")
    gdown = TGraph(n,x,ydown)
    gdown.SetLineColor(2)
    gdown.Draw("CSAME")
    canvas.SaveAs(outNaming)
    canvas.SaveAs(outNamingPng)
    
    FR_H.cd()
    TGraph_FR.SetName("FRhisto_{}_dm{}_{}_tauh{}".format(cut, decaymode, variablename,leadingname))
    TGraph_FR.Write()
    return fitfunc
    
    
    
def fit_histo_ntrk(cut, decaymode, variablename , variabletitle,leadingname,leading_str):
    decaymode = str(decaymode)
    Numerator = f.Get("h_tau{}FRnt_{}_dm{}_M".format(leadingname,cut,decaymode))
    Denumerator = f.Get("h_tau{}FRnt_{}_dm{}_VVVL".format(leadingname,cut,decaymode))

    histogram_pass = Numerator
    histogram_fail = Denumerator
    
    histogram_FR = histogram_pass.Clone("h_tau{}FRnt_{}_dm{}_FR".format(leadingname,cut,decaymode))
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
        if leadingname =='1':
            if decaymode == '1':
                fitfunc1 = TF1("fitfunc1", fitExp, 0, 25, 4)
                
                fitfunc1.SetParameter(0, 1.3)
                #fitfunc1.SetParLimits(0,1.0,1.5)
                fitfunc1.SetParameter(1, 1.57)
                fitfunc1.SetParameter(2, 0.48)
                fitfunc1.SetParameter(3, -0.6)
                
                
        if leadingname =='2':
            if decaymode=='11':
                fitfunc1 = TF1("fitfunc1", fitExp, 0, 25, 4)
                fitfunc2 = TF1("fitfunc2", fitPoly2, 25, 100, 3)
                fitfunc1.SetParameter(0, 1.1)
                fitfunc1.SetParLimits(0,1.05,1.2)
                fitfunc1.SetParameter(1, 0.10)
                fitfunc1.SetParameter(2, 0.44)
                fitfunc1.SetParameter(3, -2.5)

    if year =="2017":
        fitfunc1.SetParameter(0, 0.56)
        fitfunc1.SetParameter(1, 1.2)
        fitfunc1.SetParameter(2, 0.04)
        fitfunc1.SetParameter(3, -0.16)
        if leadingname =='1':
            if decaymode == '11':
                fitfunc1 = TF1("fitfunc1", fitExp, 0, 25, 4)
                fitfunc1.SetParameter(0, 0.54)
                #fitfunc1.SetParLimits(0,0.4,1.2)
                fitfunc1.SetParameter(1, 0.95)
                fitfunc1.SetParameter(2, 0.02)
                fitfunc1.SetParameter(3, 0.085)
        if leadingname =='2':
            if decaymode == '10':
                fitfunc1 = TF1("fitfunc1", fitExp, 0, 25, 4)
                fitfunc1.SetParameter(0, 0.77)
                fitfunc1.SetParLimits(0,0.5,1.2)
                fitfunc1.SetParameter(1, 0.94)
                fitfunc1.SetParameter(2, 0.05)
                fitfunc1.SetParameter(3, 0.13)
            if decaymode == '11':
                fitfunc1 = TF1("fitfunc1", fitExp, 0, 25, 4)
                fitfunc1.SetParameter(0, 1.05)
                fitfunc1.SetParLimits(0,0.5,1.2)
                fitfunc1.SetParameter(1, 0.76)
                fitfunc1.SetParameter(2, 0.11)
                fitfunc1.SetParameter(3, 0.26)
        
    if year =="2016pre":
        fitfunc1.SetParameter(0, 0.56)
        fitfunc1.SetParameter(1, 1.2)
        fitfunc1.SetParameter(2, 0.04)
        fitfunc1.SetParameter(3, -0.16)
        if leadingname =='2':
            if decaymode == '11':
                fitfunc1 = TF1("fitfunc1", fitExp, 0, 25, 4)
                fitfunc1.SetParameter(0, 0.77)
                fitfunc1.SetParLimits(0,0,1.2)
                fitfunc1.SetParameter(1, 0.94)
                fitfunc1.SetParameter(2, 0.05)
                fitfunc1.SetParameter(3, 0.13)

    if year =="2016post":
        fitfunc1.SetParameter(0, 0.56)
        fitfunc1.SetParameter(1, 1.2)
        fitfunc1.SetParameter(2, 0.04)
        fitfunc1.SetParameter(3, -0.16)
        if leadingname =='1':
            if decaymode == '10':
                fitfunc1 = TF1("fitfunc1", fitExp, 0, 25, 4)
                fitfunc1.SetParameter(0, 0.66)
                fitfunc1.SetParLimits(0,0.5,1.2)
                fitfunc1.SetParameter(1, 0.92)
                fitfunc1.SetParameter(2, 0.03)
                fitfunc1.SetParameter(3, 0.16)
            if decaymode == '11':
                fitfunc1 = TF1("fitfunc1", fitExp, 0, 25, 4)
                fitfunc1.SetParameter(0, 0.66)
                fitfunc1.SetParLimits(0,0.5,1.2)
                fitfunc1.SetParameter(1, 0.92)
                fitfunc1.SetParameter(2, 0.03)
                fitfunc1.SetParameter(3, 0.15)
        if leadingname =='2':
            if decaymode == '10':
                fitfunc1 = TF1("fitfunc1", fitExp, 0, 25, 4)
                fitfunc1.SetParameter(0, 0.86)
                fitfunc1.SetParLimits(0,0.5,1.2)
                fitfunc1.SetParameter(1, 0.75)
                fitfunc1.SetParameter(2, 0.05)
                fitfunc1.SetParameter(3, 0.30)
            if decaymode == '11':
                fitfunc1 = TF1("fitfunc1", fitExp, 0, 25, 4)
                fitfunc1.SetParameter(0, 1.04)
                fitfunc1.SetParLimits(0,1.03,1.2)
                fitfunc1.SetParameter(1, 0.18)
                fitfunc1.SetParameter(2, 0.09)
                fitfunc1.SetParameter(3, 0.22)
    #if decaymode=='1':
    #    fitfunc1 = TF1("fitfunc1", fitPoly2, 0, 25, 3)

    
    xAxisMax = 500.
    TGraph_FR.Fit(fitfunc2, "R0")
    TGraph_FR.Fit(fitfunc1, "R0")


    canvas = TCanvas("canvas", "", 800, 800)
    canvas.SetTitle("")
    canvas.SetGrid()
    TGraph_FR.GetYaxis().SetRangeUser(0.00, 5.00)
                
    #if (decaymode==1) TGraph_FR.GetYaxis().SetRangeUser(0.00, 0.30)
        
    TGraph_FR.GetYaxis().SetTitle("f_{#tau}")
    TGraph_FR.GetXaxis().SetRangeUser(0, 120)
    TGraph_FR.GetXaxis().SetTitle("N_{tracks}")
    
    TGraph_FR.SetTitle("")
    TGraph_FR.Draw("PAE0")
    TGraph_FR.SetLineWidth(3)

    t = TLatex()
    t.SetNDC()
    t.SetTextFont(42)
    t.SetTextAlign(12)
    t.SetTextSize(0.04)
    if (year=="2016"): t.DrawLatex(0.55, .95, "36 fb^{-1} (2016, 13 TeV)")
    if (year=="2016pre"): t.DrawLatex(0.5, .95, "19 fb^{-1} (2016 preVFP, 13 TeV)")
    if (year=="2016post"): t.DrawLatex(0.5, .95, "16 fb^{-1} (2016 postVFP, 13 TeV)")
    if (year=="2017"): t.DrawLatex(0.55, .95, "41 fb^{-1} (2017, 13 TeV)")
    if (year=="2018"): t.DrawLatex(0.55, .95, "60 fb^{-1} (2018, 13 TeV)")
    

    outNaming = "Plots_FR/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".pdf"
    if (year=="2016"): outNaming = "Plots_FR/2016/fit"  + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".pdf"
    if (year=="2016pre"): outNaming = "Plots_FR/2016pre/fit"  + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".pdf"
    if (year=="2016post"): outNaming = "Plots_FR/2016post/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".pdf"
    if (year=="2017"): outNaming = "Plots_FR/2017/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".pdf"
    if (year=="2018"): outNaming = "Plots_FR/2018/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".pdf"
    outNamingPng = "Plots_FR/fit"+ cut + "_" + "dm" + decaymode + variablename + leading_str+ ".png"
    if (year=="2016"): outNamingPng = "Plots_FR/2016/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".png"
    if (year=="2016pre"): outNamingPng = "Plots_FR/2016pre/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".png"
    if (year=="2016post"): outNamingPng = "Plots_FR/2016post/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".png"
    if (year=="2017"): outNamingPng = "Plots_FR/2017/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".png"
    if (year=="2018"): outNamingPng = "Plots_FR/2018/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".png"
    fitfunc2.Draw("SAME")
    fitfunc2.SetLineColor(2)

    fitfunc1.SetLineColor(3)
    fitfunc1.Draw("SAME")
     
    hint = TH1D("hint","Fitted Gaussian with .68 conf.band", 100, 0, 25)
    (TVirtualFitter.GetFitter()).GetConfidenceIntervals(hint,0.68)
    hint.SetStats(False)
    hint.SetFillColor(kCyan)
    hint.SetFillStyle(3001)
    hint.Draw("e3 same")
    print (hint.GetBinContent(1), " " , hint.GetBinError(1))
    err=hint.GetBinError(1)/hint.GetBinContent(1)
    print ("error ", err)
    fitfunc2.Draw("SAME")
    fitfunc1.Draw("SAME")
    canvas.SaveAs(outNaming)
    canvas.SaveAs(outNamingPng)
    
    FR_H.cd()
    TGraph_FR.SetName("FRhisto_{}_dm{}_{}_tauh{}".format(cut, decaymode, variablename,leadingname))
    TGraph_FR.Write()
    return fitfunc1,fitfunc2,err

class variable:
    def __init__(self, name, title, nbins, binning):
        self.name=name
        self.title = title
        self.nbins=nbins
        self.binning = binning

taupt = variable("taupt","#tau_{h} p_{T}",int(11),np.array([30,35,40,45,50,60,80,100,150,200,250,300],dtype=float))
tau1pt = variable("tau1pt","leading #tau_{h} p_{T}",int(9),np.array([40,45,50,60,80,100,150,200,250,300],dtype=float))
tau2pt = variable("tau2pt","subleading #tau_{h} p_{T}",int(9),np.array([40,45,50,60,80,100,150,200,250,300],dtype=float))
ntrk = variable("nTrk","N_{tracks}",int(24),np.array([-0.5,0.5,1.5,2.5,3.5,4.5,9.5,14.5,19.5,24.5,29.5,34.5,39.5,44.5,49.5,54.5,59.5,64.5,69.5,74.5,79.5,84.5,89.5,94.5,99.5],dtype=float))
Acopl = variable("Acopl","Acoplanarity",int(20),np.array([0,0.05,0.1,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50,0.55,0.60,0.65,0.70,0.75,0.80,0.85,0.90,0.95,1.00],dtype=float))
variablelist = [taupt,ntrk]
outfile = TFile("Histo/HistoforFR_{}/FRfit_tautau.root".format(year),"recreate")
err_nt0_ffQCD_leading=TH1F("err_nt0_ffQCD_leading","err_nt0_ffQCD_leading",12,0,12)
err_nt0_ffQCD_subleading=TH1F("err_nt0_ffQCD_subleading","err_nt0_ffQCD_subleading",12,0,12)
errlist_leading = []
errlist_subleading = []
for leadingname in ["1","2"]:
    leading_str = ""
    if leadingname=="1":
        leading_str = "_leading"
    else:
        leading_str = "_subleading"
    for decaymode in [0,1,10,11]:
        for variable in variablelist:
            cut = "QCD"
            print ("Begin to fit cut_{} decaymode_{} variable_{} tauh_{}".format(cut,decaymode,variable.name, leading_str))
            if (variable==ntrk):
                fitfunc1,fitfunc2,err = fit_histo_ntrk(cut,decaymode,variable.name,variable.title,leadingname,leading_str)
                fitfunc1.SetName("fitfunc_{}_DM{}_low{}{}".format(cut,decaymode,variable.name,leading_str))
                fitfunc2.SetName("fitfunc_{}_DM{}_high{}{}".format(cut,decaymode,variable.name,leading_str))
                if leadingname=="1":
                    errlist_leading.append(err)
                else:
                    errlist_subleading.append(err)
                outfile.cd()
                fitfunc1.Write()
                fitfunc2.Write()
            else:
                if leadingname=="1":
                    variable=tau1pt
                else:
                    variable=tau2pt
                fitfunc = fit_histo(cut,decaymode,variable.name,variable.title,leadingname,leading_str)
                fitfunc.SetName("fitfunc_{}_DM{}_{}{}".format(cut,decaymode,variable.name,leading_str))
                outfile.cd()
                fitfunc.Write()
err_nt0_ffQCD_leading.SetBinContent(1,errlist_leading[0])
err_nt0_ffQCD_leading.SetBinContent(2,errlist_leading[1])
err_nt0_ffQCD_leading.SetBinContent(11,errlist_leading[2])
err_nt0_ffQCD_leading.SetBinContent(12,errlist_leading[3])
err_nt0_ffQCD_subleading.SetBinContent(1,errlist_subleading[0])
err_nt0_ffQCD_subleading.SetBinContent(2,errlist_subleading[1])
err_nt0_ffQCD_subleading.SetBinContent(11,errlist_subleading[2])
err_nt0_ffQCD_subleading.SetBinContent(12,errlist_subleading[3])
outfile.cd()
err_nt0_ffQCD_leading.Write()
err_nt0_ffQCD_subleading.Write()

outfile.Close()
    
    

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
                fitfunc.SetParameter(1, -0.13)
                fitfunc.SetParameter(2, 56)
                fitfunc.SetParameter(3, 5.75)
            if decaymode=='1':
                fitfunc.SetParameter(0, 7.0)
                fitfunc.SetParameter(1, -37)
                fitfunc.SetParameter(2, 150)
                fitfunc.SetParameter(3,180)
            if decaymode=='10':
                fitfunc.SetParameter(0, 0.061)
                fitfunc.SetParameter(1, 0.056)
                fitfunc.SetParameter(2, 68.3)
                fitfunc.SetParameter(3, 17.4)
            if decaymode=='11':
                fitfunc.SetParameter(0, 0.009)
                fitfunc.SetParameter(1, 1.82)
                fitfunc.SetParameter(2, 2383)
                fitfunc.SetParameter(3, 964)
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
                '''fitfunc = fitfunc = TF1("fitfunc", fitPoly2, fMin, fMax, 3)
                fitfunc.SetParameter(0, 0.4)
                fitfunc.SetParameter(1, 0.03)
                fitfunc.SetParameter(2, 0.02)'''
                fitfunc.SetParameter(0, 0.145)
                fitfunc.SetParameter(1, 114)
                fitfunc.SetParameter(2, 1901)
                fitfunc.SetParameter(3, 551)
                
    if (year=="2017"):
        if cut =="QCD":
            if decaymode=='0':
                #fitfunc = TF1("fitfunc", fitLandau, fMin, 200, nPar)
                fitfunc.SetParameter(0, 0.12)
                fitfunc.SetParameter(1, -0.18)
                #fitfunc.SetParLimits(1,-0.8,-0.22)
                fitfunc.SetParameter(2, 56.1)
                fitfunc.SetParLimits(2,56,80)
                fitfunc.SetParameter(3, 10.8)
                #fitfunc.SetParLimits(3,0.1,10)
            if decaymode=='1':
                fitfunc.SetParameter(0, 0.09)
                fitfunc.SetParameter(1, 0.17)
                fitfunc.SetParameter(2, 175)
                fitfunc.SetParameter(3, 601)
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
                '''fitfunc = fitfunc = TF1("fitfunc", fitPoly2, fMin, fMax, 3)
                fitfunc.SetParameter(0, 0.4)
                fitfunc.SetParameter(1, 0.03)
                fitfunc.SetParameter(2, 0.02)'''
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
                fitfunc.SetParameter(0, 7.0)
                fitfunc.SetParameter(1, -37)
                fitfunc.SetParameter(2, 150)
                fitfunc.SetParameter(3,180)
            if decaymode=='10':
                fitfunc.SetParameter(0, 0.061)
                fitfunc.SetParameter(1, 0.056)
                fitfunc.SetParameter(2, 68.3)
                fitfunc.SetParameter(3, 17.4)
            if decaymode=='11':
                fitfunc.SetParameter(0, 0.532)
                fitfunc.SetParameter(1, 2.82)
                fitfunc.SetParameter(2, 238)
                fitfunc.SetParameter(3, 96)
        else:
            fitfunc.SetParameter(0, 1.8)
            fitfunc.SetParameter(1, -9)
            fitfunc.SetParameter(2, 130)
            fitfunc.SetParameter(3, 240)
            if decaymode=='0':
                fitfunc.SetParameter(0, 0.11)
                fitfunc.SetParameter(1, 116)
                fitfunc.SetParameter(2, -11)
                fitfunc.SetParLimits(2,-20,-10)
                fitfunc.SetParameter(3, 1.45)
                #fitfunc.SetParLimits(3,0.1,1.0)
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
                fitfunc.SetParameter(0, 0.124)
                fitfunc.SetParameter(1, 1.70)
                fitfunc.SetParameter(2, 359)
                fitfunc.SetParameter(3, 88.9)
            if decaymode=='1':
                fitfunc.SetParameter(0, 0.086)
                fitfunc.SetParameter(1, 0.32)
                fitfunc.SetParameter(2, 38.6)
                fitfunc.SetParLimits(2,-20,20)
                fitfunc.SetParameter(3, 0.436)
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
                fitfunc.SetParameter(0, 0.19)
                fitfunc.SetParameter(1, -1.77)
                fitfunc.SetParameter(2, 152)
                fitfunc.SetParameter(3, 127)
            if decaymode=='10':
                fitfunc.SetParameter(0, 0.03)
                fitfunc.SetParameter(1, 0.3)
                fitfunc.SetParameter(2, 74)
                fitfunc.SetParameter(3, 144)
            if decaymode=='11':
                '''fitfunc = fitfunc = TF1("fitfunc", fitPoly2, fMin, fMax, 3)
                fitfunc.SetParameter(0, 0.4)
                fitfunc.SetParameter(1, 0.03)
                fitfunc.SetParameter(2, 0.02)'''
                fitfunc.SetParameter(0, 1.44)
                fitfunc.SetParameter(1, -3.7)
                fitfunc.SetParLimits(1,-32,-0.2)
                fitfunc.SetParameter(2, 480)
                fitfunc.SetParameter(3, 63.5)
                fitfunc.SetParLimits(3,60,1000)
                
    TGraph_FR.Fit(fitfunc, "R0")

    canvas = TCanvas("canvas", "", 800, 800)
    canvas.SetTitle("")
    canvas.SetGrid()
    TGraph_FR.GetYaxis().SetRangeUser(0.00, 0.30)
    if (year == "2016pre" and cut== "QCD" and decaymode=='0'):
        TGraph_FR.GetYaxis().SetRangeUser(0.00, 0.50)
    if (year == "2016post" and cut== "QCD" and decaymode=='0'):
        TGraph_FR.GetYaxis().SetRangeUser(0.00, 0.50)
    if (year == "2016post" and cut== "QCD" and decaymode=='10'):
        TGraph_FR.GetYaxis().SetRangeUser(0.00, 0.70)
    #if (decaymode==1) TGraph_FR.GetYaxis().SetRangeUser(0.00, 0.30)
        
    TGraph_FR.GetYaxis().SetTitle("f_{#tau}")
    TGraph_FR.GetXaxis().SetRangeUser(0, 330)
    TGraph_FR.GetXaxis().SetTitle("#tau_{h} p_{T} [GeV]")
    
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
                '''fitfunc1 = fitfunc = TF1("fitfunc", fitPoly2, 0, 25, 3)
                fitfunc1.SetParameter(0, 2.5)
                fitfunc1.SetParameter(1, -0.02)
                fitfunc1.SetParameter(2, 0.002)'''
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
                #fitfunc1.SetParLimits(0,0.6,1.0)
                
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
        if cut == 'W':
            if decaymode=='0':
                fitfunc1 = TF1("fitfunc1", fitExp, 0, 25, 4)
                fitfunc2 = TF1("fitfunc2", fitPoly2, 25, 100, 3)
                fitfunc1.SetParameter(0, 0.62)
                fitfunc1.SetParLimits(0,0.5,0.8)
                
                fitfunc1.SetParameter(1, 0.71)
                fitfunc1.SetParameter(2, 0.046)
                fitfunc1.SetParameter(3, -0.55)
        
        
                
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
    
    

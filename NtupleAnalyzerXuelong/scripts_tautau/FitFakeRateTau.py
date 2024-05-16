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

def fitPoly3(x,p):
    return p[0] + p[1]*x[0] + p[2]*x[0]*x[0] + p[3]*x[0]*x[0]*x[0]

if (year=="Run2paper"):
    f = TFile("Histo/HistoforFR_{}/DataSub.root".format("Run2"))
else:
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
                fitfunc.SetParameter(0, 0.54)
                fitfunc.SetParameter(1, -0.61)
                fitfunc.SetParameter(2, 52.7)
                fitfunc.SetParameter(3, 10.2)
            if decaymode=='1':
                fitfunc.SetParameter(0, 0.15)
                fitfunc.SetParameter(1, -0.05)
                fitfunc.SetParLimits(1,-10,10)
                fitfunc.SetParameter(2, 48.4)
                fitfunc.SetParLimits(2,45,50)
                fitfunc.SetParameter(3, 0.87)
                fitfunc.SetParLimits(3,0.8,10)
            if decaymode=='10':
                fitfunc.SetParameter(0, 0.22)
                fitfunc.SetParameter(1, -42.5)
                fitfunc.SetParameter(2, 6.0)
                fitfunc.SetParLimits(2,0,8)
                fitfunc.SetParameter(3, 0.97)
            if decaymode=='11':
                fitfunc.SetParameter(0, 0.064)
                fitfunc.SetParameter(1, -0.04)
                #fitfunc.SetParLimits(1,-0.07,0.9)
                fitfunc.SetParameter(2, 43.8)
                fitfunc.SetParameter(3, 5.0)
                fitfunc.SetParLimits(3,4.0,10)
        else:
            fitfunc.SetParameter(0, 1.8)
            fitfunc.SetParameter(1, -9)
            fitfunc.SetParameter(2, 130)
            fitfunc.SetParameter(3, 240)
            if decaymode=='0':
                fitfunc.SetParameter(0, 1.3)
                fitfunc.SetParameter(1, -6.0)
                fitfunc.SetParameter(2, 89.6)
                #fitfunc.SetParLimits(2,80,250)
                fitfunc.SetParameter(3, 56.2)
            if decaymode=='1':
                fitfunc.SetParameter(0,0.98)
                fitfunc.SetParameter(1, -4.49)
                fitfunc.SetParameter(2, 173)
                #fitfunc.SetParLimits(2,100,150)
                fitfunc.SetParameter(3, 191)
            if decaymode=='10':
                fitfunc.SetParameter(0, 0.03)
                fitfunc.SetParameter(1, 0.3)
                fitfunc.SetParameter(2, 120)
                fitfunc.SetParameter(3, 344)
            if decaymode=='11':
                fitfunc.SetParameter(0, 0.064)
                fitfunc.SetParameter(1, -0.04)
                fitfunc.SetParLimits(1,-0.07,0.9)
                fitfunc.SetParameter(2, 43.8)
                fitfunc.SetParameter(3, 5.0)
                fitfunc.SetParLimits(3,4.0,10)
                #fitfunc.SetParLimits(3,1,150)

    if (year=="2017"):
        if leadingname =="1":
            if decaymode=='0':
                fitfunc.SetParameter(0, 0.54)
                fitfunc.SetParameter(1, -0.61)
                fitfunc.SetParameter(2, 52.7)
                fitfunc.SetParameter(3, 10.2)
            if decaymode=='1':
                fitfunc.SetParameter(0, 0.16)
                fitfunc.SetParameter(1, 2.65)
                #fitfunc.SetParLimits(1,0,10)
                fitfunc.SetParameter(2, 0.22)
                #fitfunc.SetParLimits(2,0,30)
                fitfunc.SetParameter(3, 11.2)
            if decaymode=='10':
                fitfunc.SetParameter(0, 0.19)
                fitfunc.SetParameter(1, -0.59)
                fitfunc.SetParameter(2, 32.8)
                #fitfunc.SetParLimits(2,0,35)
                fitfunc.SetParameter(3, 8.95)
                fitfunc.SetParLimits(3,5.0,10)
            if decaymode=='11':
                fitfunc.SetParameter(0, 0.057)
                fitfunc.SetParameter(1, -0.013)
                #fitfunc.SetParLimits(1,-0.02,0)
                fitfunc.SetParameter(2, 43.0)
                fitfunc.SetParameter(3, 0.34)

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
                fitfunc.SetParameter(0, 0.14)
                fitfunc.SetParameter(1, 1.29)
                fitfunc.SetParLimits(1,0,10)
                fitfunc.SetParameter(2, 4.5)
                #fitfunc.SetParLimits(2,0,30)
                fitfunc.SetParameter(3, 2.4)
            if decaymode=='10':
                fitfunc.SetParameter(0, 0.11)
                fitfunc.SetParameter(1, 0.23)
                fitfunc.SetParameter(2, 72.7)
                fitfunc.SetParameter(3, 13.8)
            if decaymode=='11':
                fitfunc.SetParameter(0, 0.057)
                fitfunc.SetParameter(1, -0.013)
                fitfunc.SetParLimits(1,-0.02,0)
                fitfunc.SetParameter(2, 43.0)
                fitfunc.SetParameter(3, 0.34)


    if (year=="2016pre"):
        if leadingname =="1":
            if decaymode=='0':
                fitfunc.SetParameter(0, 0.41)
                fitfunc.SetParameter(1, -0.85)
                fitfunc.SetParameter(2, 105)
                fitfunc.SetParameter(3, 37.7)
            if decaymode=='1':
                fitfunc.SetParameter(0, 0.16)
                fitfunc.SetParameter(1, 2.65)
                #fitfunc.SetParLimits(1,0,10)
                fitfunc.SetParameter(2, 0.22)
                #fitfunc.SetParLimits(2,0,30)
                fitfunc.SetParameter(3, 11.2)
            if decaymode=='10':
                fitfunc.SetParameter(0, 0.103)
                fitfunc.SetParameter(1, 0.47)
                fitfunc.SetParameter(2, 76.3)
                fitfunc.SetParameter(3, 29)
            if decaymode=='11':
                fitfunc.SetParameter(0, 0.04)
                fitfunc.SetParameter(1, 13.9)
                fitfunc.SetParLimits(1,0.50,15.9)
                fitfunc.SetParameter(2, 1979)
                fitfunc.SetParameter(3, 677)
                #fitfunc = TF1("fitfunc", fitPoly2, 40, 300, 3)
                '''fitfunc.SetParameter(0, 1.78)
                #fitfunc.SetParLimits(0,0,2)
                fitfunc.SetParameter(1, -9.66)
                fitfunc.SetParLimits(1,-20,0)
                fitfunc.SetParameter(2, -8.5)
                fitfunc.SetParameter(3, 803)'''
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
                fitfunc.SetParameter(0, 0.02)
                fitfunc.SetParameter(1, 0.85)
                fitfunc.SetParLimits(1,0,10)
                fitfunc.SetParameter(2, -6.1)
                fitfunc.SetParameter(3, 1.06)
            if decaymode=='10':
                fitfunc.SetParameter(0, 0.11)
                fitfunc.SetParameter(1, 0.23)
                fitfunc.SetParameter(2, 72.7)
                fitfunc.SetParameter(3, 13.8)
            if decaymode=='11':
                fitfunc.SetParameter(0, 0.033)
                fitfunc.SetParameter(1, 1.19)
                fitfunc.SetParLimits(1,0.50,13.9)
                fitfunc.SetParameter(2, 392)
                fitfunc.SetParameter(3, 98)
                
    if (year=="2016post"):
        if leadingname =="1":
            if decaymode=='0':
                fitfunc.SetParameter(0, 0.51)
                fitfunc.SetParameter(1, -1.18)
                fitfunc.SetParameter(2, 100)
                fitfunc.SetParameter(3, 45.6)
            if decaymode=='1':
                fitfunc.SetParameter(0, 0.33)
                fitfunc.SetParameter(1, -1.02)
                fitfunc.SetParameter(2, 159)
                fitfunc.SetParameter(3, 79.5)
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
                fitfunc.SetParameter(0, 0.103)
                fitfunc.SetParameter(1, 0.47)
                fitfunc.SetParameter(2, 15.3)
                fitfunc.SetParLimits(2,0.50,16)
                fitfunc.SetParameter(3, 29)
            if decaymode=='1':
                fitfunc.SetParameter(0, 0.14)
                fitfunc.SetParameter(1, 1.29)
                fitfunc.SetParLimits(1,0,10)
                fitfunc.SetParameter(2, 4.5)
                #fitfunc.SetParLimits(2,0,30)
                fitfunc.SetParameter(3, 2.4)
            if decaymode=='10':
                fitfunc.SetParameter(0, 0.11)
                fitfunc.SetParameter(1, 0.23)
                fitfunc.SetParameter(2, 72.7)
                fitfunc.SetParameter(3, 13.8)
            if decaymode=='11':
                fitfunc.SetParameter(0, 0.057)
                fitfunc.SetParameter(1, -0.0339)
                fitfunc.SetParameter(2, 52.4)
                fitfunc.SetParameter(3, 5.78)
                
    TGraph_FR.Fit(fitfunc, "R0")

    canvas = TCanvas("canvas", "", 800, 600)
    canvas.SetTitle("")
    canvas.SetBottomMargin(0.12)
    #canvas.SetGrid()
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
    t.SetTextSize(0.04)
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
        
    #print(Numerator.GetBinContent(2))
    #print(Denumerator.GetBinContent(2))
    #print(histogram_FR.GetBinContent(2))
    FR_ntrk0 = histogram_FR.GetBinContent(2)
    FRe_ntrk0 = histogram_FR.GetBinError(2)
    FR_ntrk1 = histogram_FR.GetBinContent(3)
    FRe_ntrk1 = histogram_FR.GetBinError(3)
    print ("ntrk==0 ", " FR ", FR_ntrk0, " +- ", FRe_ntrk0)
    print ("ntrk==1 ", " FR ", FR_ntrk1, " +- ", FRe_ntrk1)
    TGraph_FR = TGraphAsymmErrors(histogram_FR)
    histogram_FR

    
    fitfunc1 = TF1("fitfunc1", fitExp, 2, 25, 4)
    fitfunc2 = TF1("fitfunc2", fitPoly2, 25, 100, 3)
    if year =="2018":
        fitfunc1.SetParameter(0, 0.56)
        fitfunc1.SetParameter(1, 1.2)
        fitfunc1.SetParameter(2, 0.04)
        fitfunc1.SetParameter(3, -0.16)
        if leadingname =='1':
            if decaymode == '1':
                fitfunc1 = TF1("fitfunc1", fitExp, 2, 25, 4)
                
                fitfunc1.SetParameter(0, 1.3)
                #fitfunc1.SetParLimits(0,1.0,1.5)
                fitfunc1.SetParameter(1, 1.57)
                fitfunc1.SetParameter(2, 0.48)
                fitfunc1.SetParameter(3, -0.6)
                
                
        if leadingname =='2':
            if decaymode=='11':
                fitfunc1 = TF1("fitfunc1", fitExp, 2, 25, 4)
                fitfunc2 = TF1("fitfunc2", fitPoly2, 25, 100, 3)
                fitfunc1.SetParameter(0, 1.1)
                #fitfunc1.SetParLimits(0,1.05,1.2)
                fitfunc1.SetParameter(1, 0.10)
                fitfunc1.SetParameter(2, 0.44)
                fitfunc1.SetParameter(3, -2.5)

    if year =="2017":
        fitfunc1.SetParameter(0, 0.56)
        fitfunc1.SetParameter(1, 1.2)
        fitfunc1.SetParameter(2, 0.04)
        fitfunc1.SetParameter(3, -0.16)
        if leadingname =='1':
            if decaymode == '0':
                fitfunc2 = TF1("fitfunc2", fitPoly2, 25, 100, 3)
                fitfunc2.SetParameter(0, 1.81)
                #fitfunc1.SetParLimits(0,1.05,1.2)
                fitfunc2.SetParameter(1, -0.027)
                fitfunc2.SetParameter(2, 0.00015)
            if decaymode == '1':
                fitfunc2 = TF1("fitfunc2", fitPoly2, 25, 100, 3)
                fitfunc2.SetParameter(0, 1.81)
                #fitfunc1.SetParLimits(0,1.05,1.2)
                fitfunc2.SetParameter(1, -0.027)
                fitfunc2.SetParameter(2, 0.00015)
                
                
                
                
                
            if decaymode == '11':
                fitfunc1 = TF1("fitfunc1", fitExp, 2, 25,4)
                fitfunc1.SetParameter(0, 0.54)
                #fitfunc1.SetParLimits(0,0.4,1.2)
                fitfunc1.SetParameter(1, 0.95)
                fitfunc1.SetParameter(2, 0.02)
                fitfunc1.SetParameter(3, 0.085)
        if leadingname =='2':
            if decaymode == '10':
                fitfunc1 = TF1("fitfunc1", fitExp, 2, 25, 4)
                fitfunc1.SetParameter(0, 0.77)
                #fitfunc1.SetParLimits(0,0.5,1.2)
                fitfunc1.SetParameter(1, 0.94)
                fitfunc1.SetParameter(2, 0.05)
                fitfunc1.SetParameter(3, 0.13)
            if decaymode == '11':
                fitfunc1 = TF1("fitfunc1", fitExp, 2, 25, 4)
                fitfunc1.SetParameter(0, 1.05)
                #fitfunc1.SetParLimits(0,0.5,1.2)
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
                fitfunc1 = TF1("fitfunc1", fitExp, 2, 25, 4)
                fitfunc1.SetParameter(0, 0.77)
                #fitfunc1.SetParLimits(0,0,1.2)
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
                fitfunc1 = TF1("fitfunc1", fitExp, 2, 25, 4)
                fitfunc1.SetParameter(0, 0.66)
                #fitfunc1.SetParLimits(0,0.5,1.2)
                fitfunc1.SetParameter(1, 0.92)
                fitfunc1.SetParameter(2, 0.03)
                fitfunc1.SetParameter(3, 0.16)
            if decaymode == '11':
                fitfunc1 = TF1("fitfunc1", fitExp, 2, 25, 4)
                fitfunc1.SetParameter(0, 0.66)
                #fitfunc1.SetParLimits(0,0.5,1.2)
                fitfunc1.SetParameter(1, 0.92)
                fitfunc1.SetParameter(2, 0.03)
                fitfunc1.SetParameter(3, 0.15)
        if leadingname =='2':
            if decaymode == '10':
                fitfunc1 = TF1("fitfunc1", fitExp, 2, 25, 4)
                fitfunc1.SetParameter(0, 0.86)
                #fitfunc1.SetParLimits(0,0.5,1.2)
                fitfunc1.SetParameter(1, 0.75)
                fitfunc1.SetParameter(2, 0.05)
                fitfunc1.SetParameter(3, 0.30)
            if decaymode == '11':
                fitfunc1 = TF1("fitfunc1", fitExp, 2, 25, 4)
                fitfunc1.SetParameter(0, 1.04)
                #fitfunc1.SetParLimits(0,1.03,1.2)
                fitfunc1.SetParameter(1, 0.18)
                fitfunc1.SetParameter(2, 0.09)
                fitfunc1.SetParameter(3, 0.22)
    #if decaymode=='1':
    #    fitfunc1 = TF1("fitfunc1", fitPoly2, 0, 25, 3)
    if year =="Run2" or year =="Run2paper":

        fitfunc1 = TF1("fitfunc1", fitExp, 2, 15, 4)
        fitfunc2 = TF1("fitfunc2", fitPoly2, 15, 100, 3)
        fitfunc1.SetParameter(0, 0.56)
        fitfunc1.SetParameter(1, 1.2)
        fitfunc1.SetParameter(2, 0.04)
        fitfunc1.SetParameter(3, -0.16)
        fitfunc2.SetParameter(0, 1.81)
        #fitfunc1.SetParLimits(0,1.05,1.2)
        fitfunc2.SetParameter(1, -0.027)
        fitfunc2.SetParameter(2, 0.00015)
        if leadingname =='1':
            if decaymode == '10':
                fitfunc1 = TF1("fitfunc1", fitExp, 2, 25, 4)
                fitfunc1.SetParameter(0, 0.66)
                #fitfunc1.SetParLimits(0,0.5,1.2)
                fitfunc1.SetParameter(1, 0.92)
                fitfunc1.SetParameter(2, 0.03)
                fitfunc1.SetParameter(3, 0.16)
        
        
    
    xAxisMax = 500.
    TGraph_FR.Fit(fitfunc2, "R0")
    TGraph_FR.Fit(fitfunc1, "R0")


    canvas = TCanvas("canvas", "", 800, 600)
    canvas.SetTitle("")
    #canvas.SetGrid()
    TGraph_FR.GetYaxis().SetRangeUser(0.00, 5.15)
                
    #if (decaymode==1) TGraph_FR.GetYaxis().SetRangeUser(0.00, 0.30)
        
    TGraph_FR.GetYaxis().SetTitle("MF correction factor")
    TGraph_FR.GetXaxis().SetRangeUser(0, 100)
    TGraph_FR.GetXaxis().SetTitle("N_{tracks}")
    TGraph_FR.SetLineColor(1)
    TGraph_FR.SetTitle("")
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

    '''if (leadingname =='1'):
        if (decaymode=='0'): t3.DrawLatex(0.3, .55, "leading #tau_{h} CR, #tau#tau_{h}, 1-prong")
        if (decaymode=='1'): t3.DrawLatex(0.3, .55, "leading #tau_{h} CR, #tau#tau_{h}, 1-prong+#pi^{0}")
        if (decaymode=='10'): t3.DrawLatex(0.3, .55, "leading #tau_{h} CR, #tau#tau_{h}, 3-prong")
        if (decaymode=='11'): t3.DrawLatex(0.3, .55, "leading #tau_{h} CR, #tau#tau_{h}, 3-prong+#pi^{0}")
    if (leadingname =='2'):
        if (decaymode=='0'): t3.DrawLatex(0.3, .55, "subleading #tau_{h} CR, #tau#tau_{h}, 1-prong")
        if (decaymode=='1'): t3.DrawLatex(0.3, .55, "subleading #tau_{h} CR, #tau#tau_{h}, 1-prong+#pi^{0}")
        if (decaymode=='10'): t3.DrawLatex(0.3, .55, "subleading #tau_{h} CR, #tau#tau_{h}, 3-prong")
        if (decaymode=='11'): t3.DrawLatex(0.3, .55, "subleading #tau_{h} CR, #tau#tau_{h}, 3-prong+#pi^{0}")'''

    if (leadingname =='1'):
        if (decaymode=='0'): t3.DrawLatex(0.3, .55, "leading #tau_{h} CR, #tau#tau_{h}, h^{#pm}")
        if (decaymode=='1'): t3.DrawLatex(0.3, .55, "leading #tau_{h} CR, #tau#tau_{h}, h^{#pm}+#pi^{0}(s)")
        if (decaymode=='10'): t3.DrawLatex(0.3, .55, "leading #tau_{h} CR, #tau#tau_{h}, h^{#pm}h^{#mp}h^{#pm}")
        if (decaymode=='11'): t3.DrawLatex(0.3, .55, "leading #tau_{h} CR, #tau#tau_{h}, h^{#pm}h^{#mp}h^{#pm}+#pi^{0}(s)")
    if (leadingname =='2'):
        if (decaymode=='0'): t3.DrawLatex(0.3, .55, "subleading #tau_{h} CR, #tau#tau_{h}, h^{#pm}")
        if (decaymode=='1'): t3.DrawLatex(0.3, .55, "subleading #tau_{h} CR, #tau#tau_{h}, h^{#pm}+#pi^{0}(s)")
        if (decaymode=='10'): t3.DrawLatex(0.25, .55, "subleading #tau_{h} CR, #tau#tau_{h}, h^{#pm}h^{#mp}h^{#pm}")
        if (decaymode=='11'): t3.DrawLatex(0.25, .55, "subleading #tau_{h} CR, #tau#tau_{h}, h^{#pm}h^{#mp}h^{#pm}+#pi^{0}(s)")

    outNaming = "Plots_FR/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".pdf"
    if (year=="2016"): outNaming = "Plots_FR/2016/fit"  + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".pdf"
    if (year=="2016pre"): outNaming = "Plots_FR/2016pre/fit"  + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".pdf"
    if (year=="2016post"): outNaming = "Plots_FR/2016post/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".pdf"
    if (year=="2017"): outNaming = "Plots_FR/2017/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".pdf"
    if (year=="2018"): outNaming = "Plots_FR/2018/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".pdf"
    if (year=="Run2"): outNaming = "Plots_FR/Run2/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+".pdf"
    if (year=="Run2paper"): outNaming = "Plots_FR/Run2paper/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+".pdf"
    outNamingPng = "Plots_FR/fit"+ cut + "_" + "dm" + decaymode + variablename + leading_str+ ".png"
    if (year=="2016"): outNamingPng = "Plots_FR/2016/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".png"
    if (year=="2016pre"): outNamingPng = "Plots_FR/2016pre/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".png"
    if (year=="2016post"): outNamingPng = "Plots_FR/2016post/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".png"
    if (year=="2017"): outNamingPng = "Plots_FR/2017/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".png"
    if (year=="2018"): outNamingPng = "Plots_FR/2018/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".png"
    if (year=="Run2"): outNamingPng = "Plots_FR/Run2/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".png"
    if (year=="Run2paper"): outNamingPng = "Plots_FR/Run2paper/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+".png"

    outNamingRoot = "Plots_FR/fit"+ cut + "_" + "dm" + decaymode + variablename + leading_str+ ".root"
    if (year=="2016"): outNamingRoot = "Plots_FR/2016/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".root"
    if (year=="2016pre"): outNamingRoot = "Plots_FR/2016pre/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".root"
    if (year=="2016post"): outNamingRoot = "Plots_FR/2016post/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".root"
    if (year=="2017"): outNamingRoot = "Plots_FR/2017/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".root"
    if (year=="2018"): outNamingRoot = "Plots_FR/2018/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".root"
    if (year=="Run2"): outNamingRoot = "Plots_FR/Run2/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+ ".root"
    if (year=="Run2paper"): outNamingRoot = "Plots_FR/Run2paper/fit" + cut + "_" + "dm" + decaymode + variablename + leading_str+".root"
    #fitfunc2.Draw("SAME")
    fitfunc2.SetLineColor(3)

    fitfunc1.SetLineColor(ROOT.kMagenta)
    fitfunc1.Draw("SAME")

    hint = TH1D("hint","Fitted Gaussian with .68 conf.band", 100, 2, 25)
    if (year == "Run2" or year=="Run2paper"):
        hint = TH1D("hint","Fitted Gaussian with .68 conf.band", 100, 2, 15)

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
     
    '''hint = TH1D("hint","Fitted Gauleading #tau_{h}ian with .68 conf.band", 100, 0, 25)
    (TVirtualFitter.GetFitter()).GetConfidenceIntervals(hint,0.68)
    hint.SetStats(False)
    hint.SetFillColor(kCyan)
    hint.SetFillStyle(3001)
    hint.Draw("e3 same")
    print (hint.GetBinContent(1), " " , hint.GetBinError(1))
    err=hint.GetBinError(1)/hint.GetBinContent(1)
    print ("error ", err)'''
    
    
    #fitfunc2.Draw("SAME")
    fitfunc1.Draw("SAME")
    canvas.SaveAs(outNaming)
    canvas.SaveAs(outNamingPng)
    canvas.SaveAs(outNamingRoot)
    
    FR_H.cd()
    TGraph_FR.SetName("FRhisto_{}_dm{}_{}_tauh{}".format(cut, decaymode, variablename,leadingname))
    TGraph_FR.Write()
    return fitfunc1,fitfunc2,FR_ntrk0,FRe_ntrk0,FR_ntrk1,FRe_ntrk1,err

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
if (year == "Run2" or year=="Run2paper"):
    variablelist = [ntrk]
outfile = TFile("Histo/HistoforFR_{}/FRfit_tautau.root".format(year),"recreate")
nt0_ffQCD_leading=TH1F("nt0_ffQCD_leading","nt0_ffQCD_leading",12,0,12)
nt0_ffQCD_subleading=TH1F("nt0_ffQCD_subleading","nt0_ffQCD_subleading",12,0,12)
nt1_ffQCD_leading=TH1F("nt1_ffQCD_leading","nt1_ffQCD_leading",12,0,12)
nt1_ffQCD_subleading=TH1F("nt1_ffQCD_subleading","nt1_ffQCD_subleading",12,0,12)
leading_FR_ntrk0 = []
leading_FR_ntrk1 = []
leading_FRe_ntrk0 = []
leading_FRe_ntrk1 = []
subleading_FR_ntrk0 = []
subleading_FR_ntrk1 = []
subleading_FRe_ntrk0 = []
subleading_FRe_ntrk1 = []
err_nt2_ff_tau1=TH1F("err_nt2_ff_tau1","err_nt2_ff_tau1",12,0,12)
err_nt2_ff_tau2=TH1F("err_nt2_ff_tau2","err_nt2_ff_tau2",12,0,12)
errlist = []
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
                fitfunc1,fitfunc2,FR_ntrk0,FRe_ntrk0,FR_ntrk1,FRe_ntrk1,err = fit_histo_ntrk(cut,decaymode,variable.name,variable.title,leadingname,leading_str)
                fitfunc1.SetName("fitfunc_{}_DM{}_low{}{}".format(cut,decaymode,variable.name,leading_str))
                fitfunc2.SetName("fitfunc_{}_DM{}_high{}{}".format(cut,decaymode,variable.name,leading_str))
                errlist.append(err)
                if leadingname=="1":
                    leading_FR_ntrk0.append(FR_ntrk0)
                    leading_FR_ntrk1.append(FR_ntrk1)
                    leading_FRe_ntrk0.append(FRe_ntrk0)
                    leading_FRe_ntrk1.append(FRe_ntrk1)
                else:
                    subleading_FR_ntrk0.append(FR_ntrk0)
                    subleading_FR_ntrk1.append(FR_ntrk1)
                    subleading_FRe_ntrk0.append(FRe_ntrk0)
                    subleading_FRe_ntrk1.append(FRe_ntrk1)
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
'''err_nt0_ff_tau1_leading.SetBinContent(1,errlist_leading[0])
err_nt0_ff_tau1_leading.SetBinContent(2,errlist_leading[1])
err_nt0_ff_tau1_leading.SetBinContent(11,errlist_leading[2])
err_nt0_ff_tau1_leading.SetBinContent(12,errlist_leading[3])
err_nt0_ff_tau1_subleading.SetBinContent(1,errlist_subleading[0])
err_nt0_ff_tau1_subleading.SetBinContent(2,errlist_subleading[1])
err_nt0_ff_tau1_subleading.SetBinContent(11,errlist_subleading[2])
err_nt0_ff_tau1_subleading.SetBinContent(12,errlist_subleading[3])'''
nt0_ffQCD_leading.SetBinContent(1,leading_FR_ntrk0[0])
nt0_ffQCD_leading.SetBinError(1,leading_FRe_ntrk0[0])
nt0_ffQCD_leading.SetBinContent(2,leading_FR_ntrk0[1])
nt0_ffQCD_leading.SetBinError(2,leading_FRe_ntrk0[1])
nt0_ffQCD_leading.SetBinContent(11,leading_FR_ntrk0[2])
nt0_ffQCD_leading.SetBinError(11,leading_FRe_ntrk0[2])
nt0_ffQCD_leading.SetBinContent(12,leading_FR_ntrk0[3])
nt0_ffQCD_leading.SetBinError(12,leading_FRe_ntrk0[3])

nt1_ffQCD_leading.SetBinContent(1,leading_FR_ntrk1[0])
nt1_ffQCD_leading.SetBinError(1,leading_FRe_ntrk1[0])
nt1_ffQCD_leading.SetBinContent(2,leading_FR_ntrk1[1])
nt1_ffQCD_leading.SetBinError(2,leading_FRe_ntrk1[1])
nt1_ffQCD_leading.SetBinContent(11,leading_FR_ntrk1[2])
nt1_ffQCD_leading.SetBinError(11,leading_FRe_ntrk1[2])
nt1_ffQCD_leading.SetBinContent(12,leading_FR_ntrk1[3])
nt1_ffQCD_leading.SetBinError(12,leading_FRe_ntrk1[3])

nt0_ffQCD_subleading.SetBinContent(1,subleading_FR_ntrk0[0])
nt0_ffQCD_subleading.SetBinError(1,subleading_FRe_ntrk0[0])
nt0_ffQCD_subleading.SetBinContent(2,subleading_FR_ntrk0[1])
nt0_ffQCD_subleading.SetBinError(2,subleading_FRe_ntrk0[1])
nt0_ffQCD_subleading.SetBinContent(11,subleading_FR_ntrk0[2])
nt0_ffQCD_subleading.SetBinError(11,subleading_FRe_ntrk0[2])
nt0_ffQCD_subleading.SetBinContent(12,subleading_FR_ntrk0[3])
nt0_ffQCD_subleading.SetBinError(12,subleading_FRe_ntrk0[3])

nt1_ffQCD_subleading.SetBinContent(1,subleading_FR_ntrk1[0])
nt1_ffQCD_subleading.SetBinError(1,subleading_FRe_ntrk1[0])
nt1_ffQCD_subleading.SetBinContent(2,subleading_FR_ntrk1[1])
nt1_ffQCD_subleading.SetBinError(2,subleading_FRe_ntrk1[1])
nt1_ffQCD_subleading.SetBinContent(11,subleading_FR_ntrk1[2])
nt1_ffQCD_subleading.SetBinError(11,subleading_FRe_ntrk1[2])
nt1_ffQCD_subleading.SetBinContent(12,subleading_FR_ntrk1[3])
nt1_ffQCD_subleading.SetBinError(12,subleading_FRe_ntrk1[3])

print ('errlist: ', errlist)
err_nt2_ff_tau1.SetBinContent(1,errlist[0])
err_nt2_ff_tau1.SetBinContent(2,errlist[1])
err_nt2_ff_tau1.SetBinContent(11,errlist[2])
err_nt2_ff_tau1.SetBinContent(12,errlist[3])
err_nt2_ff_tau2.SetBinContent(1,errlist[4])
err_nt2_ff_tau2.SetBinContent(2,errlist[5])
err_nt2_ff_tau2.SetBinContent(11,errlist[6])
err_nt2_ff_tau2.SetBinContent(12,errlist[7])


outfile.cd()
nt0_ffQCD_leading.Write()
nt1_ffQCD_leading.Write()
nt0_ffQCD_subleading.Write()
nt1_ffQCD_subleading.Write()
err_nt2_ff_tau1.Write()

err_nt2_ff_tau2.Write()
outfile.Close()
    
    

#include "ApplyFR.h"
using std::vector;

mutauFR::mutauFR(string year){
    yearconf = year;
    TFile *fFRw_mutau = new TFile(Form("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/scripts_mutau/Histo/HistoforFR_%s/Wfractions.root",year.c_str()),"read");
    TFile *fFR_mutau = new TFile(Form("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/scripts_mutau/Histo/HistoforFR_%s/FRfit_mutau.root",year.c_str()),"read");

    WFR_allDM = (TH2D*)fFRw_mutau->Get("frac_W");

    FRQCD_taupt_DM0 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM0_taupt");
    FRQCD_lownTrk_DM0 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM0_lownTrk");
    FRQCD_highnTrk_DM0 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM0_highnTrk");

    FRQCD_taupt_DM1 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM1_taupt");
    FRQCD_lownTrk_DM1 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM1_lownTrk");
    FRQCD_highnTrk_DM1 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM1_highnTrk");

    FRQCD_taupt_DM10 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM10_taupt");
    FRQCD_lownTrk_DM10 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM10_lownTrk");
    FRQCD_highnTrk_DM10 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM10_highnTrk");

    FRQCD_taupt_DM11 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM11_taupt");
    FRQCD_lownTrk_DM11 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM11_lownTrk");
    FRQCD_highnTrk_DM11 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM11_highnTrk");

    FRW_taupt_DM0 = (TF1*)fFR_mutau->Get("fitfunc_W_DM0_taupt");
    FRW_lownTrk_DM0 = (TF1*)fFR_mutau->Get("fitfunc_W_DM0_lownTrk");
    FRW_highnTrk_DM0 = (TF1*)fFR_mutau->Get("fitfunc_W_DM0_highnTrk");

    FRW_taupt_DM1 = (TF1*)fFR_mutau->Get("fitfunc_W_DM1_taupt");
    FRW_lownTrk_DM1 = (TF1*)fFR_mutau->Get("fitfunc_W_DM1_lownTrk");
    FRW_highnTrk_DM1 = (TF1*)fFR_mutau->Get("fitfunc_W_DM1_highnTrk");

    FRW_taupt_DM10 = (TF1*)fFR_mutau->Get("fitfunc_W_DM10_taupt");
    FRW_lownTrk_DM10 = (TF1*)fFR_mutau->Get("fitfunc_W_DM10_lownTrk");
    FRW_highnTrk_DM10 = (TF1*)fFR_mutau->Get("fitfunc_W_DM10_highnTrk");

    FRW_taupt_DM11 = (TF1*)fFR_mutau->Get("fitfunc_W_DM11_taupt");
    FRW_lownTrk_DM11 = (TF1*)fFR_mutau->Get("fitfunc_W_DM11_lownTrk");
    FRW_highnTrk_DM11 = (TF1*)fFR_mutau->Get("fitfunc_W_DM11_highnTrk");

    err_nt0_ffQCD = (TH1F*)fFR_mutau->Get("err_nt0_ffQCD");
    err_nt0_ffW = (TH1F*)fFR_mutau->Get("err_nt0_ffW");

    TH1F* h_tauFR_QCD_xtrg_SF = (TH1F*)fFR_mutau->Get("h_tauFR_QCD_xtrg_SF");
    TH1F* h_tauFR_W_xtrg_SF = (TH1F*)fFR_mutau->Get("h_tauFR_W_xtrg_SF");

    QCDxtrgSF = h_tauFR_QCD_xtrg_SF->GetBinContent(2)/h_tauFR_QCD_xtrg_SF->GetBinContent(3);
    WxtrgSF = h_tauFR_W_xtrg_SF->GetBinContent(2)/h_tauFR_W_xtrg_SF->GetBinContent(3);
    cout << year << " xtg SF " << " QCD: " << QCDxtrgSF << " W: " << WxtrgSF << endl;

}

mutauFR::mutauFR(){
    
}

mutauFR mutauFR2016pre("2016pre");
mutauFR mutauFR2016post("2016post");
mutauFR mutauFR2017("2017");
mutauFR mutauFR2018("2018");

map<string, mutauFR> mutauFRmap = {
    {"2016pre", mutauFR2016pre}, {"2016post", mutauFR2016post},{"2017", mutauFR2017},{"2018", mutauFR2018}
};


/*TFile *fFRw_mutau = new TFile("Histo/HistoforFR_2018/Wfractions.root","read");
TFile *fFR_mutau = new TFile("Histo/HistoforFR_2018/FRfit_mutau.root","read");


TH2D *WFR_allDM = (TH2D*)fFRw_mutau->Get("frac_W");

TF1 *FRQCD_taupt_DM0 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM0_taupt");
TF1 *FRQCD_lownTrk_DM0 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM0_lownTrk");
TF1 *FRQCD_highnTrk_DM0 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM0_highnTrk");

TF1 *FRQCD_taupt_DM1 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM1_taupt");
TF1 *FRQCD_lownTrk_DM1 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM1_lownTrk");
TF1 *FRQCD_highnTrk_DM1 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM1_highnTrk");

TF1 *FRQCD_taupt_DM10 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM10_taupt");
TF1 *FRQCD_lownTrk_DM10 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM10_lownTrk");
TF1 *FRQCD_highnTrk_DM10 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM10_highnTrk");

TF1 *FRQCD_taupt_DM11 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM11_taupt");
TF1 *FRQCD_lownTrk_DM11 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM11_lownTrk");
TF1 *FRQCD_highnTrk_DM11 = (TF1*)fFR_mutau->Get("fitfunc_QCD_DM11_highnTrk");

TF1 *FRW_taupt_DM0 = (TF1*)fFR_mutau->Get("fitfunc_W_DM0_taupt");
TF1 *FRW_lownTrk_DM0 = (TF1*)fFR_mutau->Get("fitfunc_W_DM0_lownTrk");
TF1 *FRW_highnTrk_DM0 = (TF1*)fFR_mutau->Get("fitfunc_W_DM0_highnTrk");

TF1 *FRW_taupt_DM1 = (TF1*)fFR_mutau->Get("fitfunc_W_DM1_taupt");
TF1 *FRW_lownTrk_DM1 = (TF1*)fFR_mutau->Get("fitfunc_W_DM1_lownTrk");
TF1 *FRW_highnTrk_DM1 = (TF1*)fFR_mutau->Get("fitfunc_W_DM1_highnTrk");

TF1 *FRW_taupt_DM10 = (TF1*)fFR_mutau->Get("fitfunc_W_DM10_taupt");
TF1 *FRW_lownTrk_DM10 = (TF1*)fFR_mutau->Get("fitfunc_W_DM10_lownTrk");
TF1 *FRW_highnTrk_DM10 = (TF1*)fFR_mutau->Get("fitfunc_W_DM10_highnTrk");

TF1 *FRW_taupt_DM11 = (TF1*)fFR_mutau->Get("fitfunc_W_DM11_taupt");
TF1 *FRW_lownTrk_DM11 = (TF1*)fFR_mutau->Get("fitfunc_W_DM11_lownTrk");
TF1 *FRW_highnTrk_DM11 = (TF1*)fFR_mutau->Get("fitfunc_W_DM11_highnTrk");

TH1F *err_nt0_ffQCD = (TH1F*)fFR_mutau->Get("err_nt0_ffQCD");
TH1F *err_nt0_ffW = (TH1F*)fFR_mutau->Get("err_nt0_ffW");

*/


float GetFR_mutau_qcd(int taudecaymode, float taupt, int nTrk, bool isMuonTauTrigger, string year){
    float mytaupt = taupt;
    if (taupt>300) mytaupt=299;
    int mynTrk=nTrk;
    if (nTrk>=100) mynTrk=99;
    float tfr_QCD=1.0;

    float ntrkcut = 25;
    if (taudecaymode==0 ){
        if (mynTrk<ntrkcut){
            tfr_QCD = TMath::Min(1.0,mutauFRmap[year].FRQCD_taupt_DM0->Eval(mytaupt)*mutauFRmap[year].FRQCD_lownTrk_DM0->Eval(mynTrk));
        }
        else{
            tfr_QCD = TMath::Min(1.0,mutauFRmap[year].FRQCD_taupt_DM0->Eval(mytaupt)*mutauFRmap[year].FRQCD_highnTrk_DM0->Eval(mynTrk));
        }

    }
    else if (taudecaymode==1){
        if (mynTrk<ntrkcut){
            tfr_QCD = TMath::Min(1.0,mutauFRmap[year].FRQCD_taupt_DM1->Eval(mytaupt)*mutauFRmap[year].FRQCD_lownTrk_DM1->Eval(mynTrk));
        }
        else{
            tfr_QCD = TMath::Min(1.0,mutauFRmap[year].FRQCD_taupt_DM1->Eval(mytaupt)*mutauFRmap[year].FRQCD_highnTrk_DM1->Eval(mynTrk));
        }
    }
    else if (taudecaymode==10){
        if (mynTrk<ntrkcut){
            tfr_QCD = TMath::Min(1.0,mutauFRmap[year].FRQCD_taupt_DM10->Eval(mytaupt)*mutauFRmap[year].FRQCD_lownTrk_DM10->Eval(mynTrk));
        }
        else{
            tfr_QCD = TMath::Min(1.0,mutauFRmap[year].FRQCD_taupt_DM10->Eval(mytaupt)*mutauFRmap[year].FRQCD_highnTrk_DM10->Eval(mynTrk));
        }

    }
    else if (taudecaymode==11){
        if (mynTrk<ntrkcut){
            tfr_QCD = TMath::Min(1.0,mutauFRmap[year].FRQCD_taupt_DM11->Eval(mytaupt)*mutauFRmap[year].FRQCD_lownTrk_DM11->Eval(mynTrk));
        }
        else{
            tfr_QCD = TMath::Min(1.0,mutauFRmap[year].FRQCD_taupt_DM11->Eval(mytaupt)*mutauFRmap[year].FRQCD_highnTrk_DM11->Eval(mynTrk));
        }
    }

    if (isMuonTauTrigger){
        tfr_QCD*=mutauFRmap[year].QCDxtrgSF;
    }
    return tfr_QCD;
}

float GetFR_mutau_w(int taudecaymode, float taupt, int nTrk, bool isMuonTauTrigger,string year){
    float mytaupt = taupt;
    if (taupt>300) mytaupt=299;
    int mynTrk=nTrk;
    if (nTrk>=100) mynTrk=99;
    float tfr_W=1.0;

    float ntrkcut = 25;
    if (taudecaymode==0){
        if (mynTrk<ntrkcut){
            tfr_W=TMath::Min(1.0,mutauFRmap[year].FRW_taupt_DM0->Eval(mytaupt)*mutauFRmap[year].FRW_lownTrk_DM0->Eval(mynTrk));
        }
        else{
            tfr_W=TMath::Min(1.0,mutauFRmap[year].FRW_taupt_DM0->Eval(mytaupt)*mutauFRmap[year].FRW_highnTrk_DM0->Eval(mynTrk));
        }

    }
    else if (taudecaymode==1){
        if (mynTrk<ntrkcut){
            tfr_W=TMath::Min(1.0,mutauFRmap[year].FRW_taupt_DM1->Eval(mytaupt)*mutauFRmap[year].FRW_lownTrk_DM1->Eval(mynTrk));
        }
        else{
            tfr_W=TMath::Min(1.0,mutauFRmap[year].FRW_taupt_DM1->Eval(mytaupt)*mutauFRmap[year].FRW_highnTrk_DM1->Eval(mynTrk));
        }
    }
    else if (taudecaymode==10){
        if (mynTrk<ntrkcut){
            tfr_W=TMath::Min(1.0,mutauFRmap[year].FRW_taupt_DM10->Eval(mytaupt)*mutauFRmap[year].FRW_lownTrk_DM10->Eval(mynTrk));
        }
        else{
            tfr_W=TMath::Min(1.0,mutauFRmap[year].FRW_taupt_DM10->Eval(mytaupt)*mutauFRmap[year].FRW_highnTrk_DM10->Eval(mynTrk));
        }

    }
    else if (taudecaymode==11){
        if (mynTrk<ntrkcut){
            tfr_W=TMath::Min(1.0,mutauFRmap[year].FRW_taupt_DM11->Eval(mytaupt)*mutauFRmap[year].FRW_lownTrk_DM11->Eval(mynTrk));
        }
        else{
            tfr_W=TMath::Min(1.0,mutauFRmap[year].FRW_taupt_DM11->Eval(mytaupt)*mutauFRmap[year].FRW_highnTrk_DM11->Eval(mynTrk));
        }
    }

    if (isMuonTauTrigger){
        tfr_W*=mutauFRmap[year].WxtrgSF;
    }
    return tfr_W;
}


float Getwfraction(float mvis, float mtrans,string year){
    float fracW= 0;

    float mymvis = mvis;
    float mymtrans = mtrans;
    if (mymvis>300) mymvis=299;
    if (mymvis<50) mymvis=51;
    if (mymtrans>75) {
        fracW=1.0;
    }
    else{
        fracW = mutauFRmap[year].WFR_allDM->GetBinContent(mutauFRmap[year].WFR_allDM->GetXaxis()->FindBin(mymtrans),mutauFRmap[year].WFR_allDM->GetYaxis()->FindBin(mymvis));
    }
    return fracW;
}


//Inversion of selection criteria to measure the fake rates
float GetFR_mutau_qcd_sys_invertOS(float qcdFR,float FRratio){
    return qcdFR*FRratio;
}

float GetFR_mutau_w_sys_invertmT(float wFR,float FRratio){
    return wFR*FRratio;
}

//Extrapolation of the fake rates with tauh pT
float GetFR_mutau_qcd_sys_taupt(float qcdFR, float taupt, int decaymode, int taudecaymode, bool down){
    float mytaupt = taupt;
    if (taupt>300) mytaupt=299;
    if (taudecaymode==decaymode){
        if (down){
            return qcdFR*(1-0.5*(mytaupt-30)/270);
        }
        else {
            return qcdFR*(1+0.5*(mytaupt-30)/270);
        }
    }
    else{
        return qcdFR;
    }
}

float GetFR_mutau_w_sys_taupt(float wFR, float taupt, int decaymode, int taudecaymode, bool down){
    float mytaupt = taupt;
    if (taupt>300) mytaupt=299;
    if (taudecaymode==decaymode){
        if (down){
            return wFR*(1-0.5*(mytaupt-30)/270);
        }
        else {
            return wFR*(1+0.5*(mytaupt-30)/270);
        }
    }
    else{
        return wFR;
    }
}
//Statistical uncertainty in the Ntracks extrapolation
float GetFR_mutau_qcd_sys_ntrk_dm(float qcdFR, int decaymode, int taudecaymode, bool down,string year){
    float err = mutauFRmap[year].err_nt0_ffQCD->GetBinContent(decaymode+1);
    if (taudecaymode==decaymode){
        if (down){
            return qcdFR*(1-err);
        }
        else {
            return qcdFR*(1+err);
        }
    }
    else{
        return qcdFR;
    }
}

float GetFR_mutau_w_sys_ntrk_dm(float wFR, int decaymode, int taudecaymode, bool down,string year){
    float err = mutauFRmap[year].err_nt0_ffW->GetBinContent(decaymode+1);
    if (taudecaymode==decaymode){
        if (down){
            return wFR*(1-err);
        }
        else {
            return wFR*(1+err);
        }
    }
    else{
        return wFR;
    }
}

//Systematic uncertainty in the Ntracks extrapolation
float GetFR_mutau_qcd_sys_ntrk(float qcdFR, float FRratio){
    return qcdFR*FRratio;
}

float GetFR_mutau_w_sys_ntrk(float wFR, float FRratio){
    return wFR*FRratio;
}


//Systematic uncertainty of Determination of theWand QCD fractions //fix me
float Getwfraction_sys(float wfraction, bool down){
    if (wfraction>=1.0){
        return 1.0;
    }
    else{
        if (down){
            return 0.8*wfraction;
        }
        else{
            if (1.2*wfraction>=1.0){
                return 1.0;
            }
            else{
                return 1.2*wfraction;
            }
        }
    }
}



float GetFR_mutau(float qcdFR, float wFR, float wfraction){
    float tfr=wfraction*wFR + (1-wfraction)*qcdFR;
    return tfr;
}


/*float GetFR_mutau(int taudecaymode, float mvis, float mtrans, float taupt, int nTrk, bool isMuonTauTrigger){
    float fracW= 0;
    float mymvis = mvis;
    float mymtrans = mtrans;
    if (mymvis>300) mymvis=299;
    if (mymvis<50) mymvis=51;
    if (mymtrans>75) {
        fracW=1.0;
    }
    else{
        fracW = WFR_allDM->GetBinContent(WFR_allDM->GetXaxis()->FindBin(mymtrans),WFR_allDM->GetYaxis()->FindBin(mymvis));
    }

    float mytaupt = taupt;
    if (taupt>300) mytaupt=299;
    int mynTrk=nTrk;
    if (nTrk>=100) mynTrk=99;
    float tfr_W=1.0;
    float tfr_QCD=1.0;

    float ntrkcut = 25;
    if (taudecaymode==0){
        if (mynTrk<ntrkcut){
            tfr_W=TMath::Min(1.0,FRW_taupt_DM0->Eval(mytaupt)*FRW_lownTrk_DM0->Eval(mynTrk));
            tfr_QCD = TMath::Min(1.0,FRQCD_taupt_DM0->Eval(mytaupt)*FRQCD_lownTrk_DM0->Eval(mynTrk));
        }
        else{
            tfr_W=TMath::Min(1.0,FRW_taupt_DM0->Eval(mytaupt)*FRW_highnTrk_DM0->Eval(mynTrk));
            tfr_QCD = TMath::Min(1.0,FRQCD_taupt_DM0->Eval(mytaupt)*FRQCD_highnTrk_DM0->Eval(mynTrk));
        }

    }
    else if (taudecaymode==1){
        if (mynTrk<ntrkcut){
            tfr_W=TMath::Min(1.0,FRW_taupt_DM1->Eval(mytaupt)*FRW_lownTrk_DM1->Eval(mynTrk));
            tfr_QCD = TMath::Min(1.0,FRQCD_taupt_DM1->Eval(mytaupt)*FRQCD_lownTrk_DM1->Eval(mynTrk));
        }
        else{
            tfr_W=TMath::Min(1.0,FRW_taupt_DM1->Eval(mytaupt)*FRW_highnTrk_DM1->Eval(mynTrk));
            tfr_QCD = TMath::Min(1.0,FRQCD_taupt_DM1->Eval(mytaupt)*FRQCD_highnTrk_DM1->Eval(mynTrk));
        }
    }
    else if (taudecaymode==10){
        if (mynTrk<ntrkcut){
            tfr_QCD = TMath::Min(1.0,FRQCD_taupt_DM10->Eval(mytaupt)*FRQCD_lownTrk_DM10->Eval(mynTrk));
            tfr_W=TMath::Min(1.0,FRW_taupt_DM10->Eval(mytaupt)*FRW_lownTrk_DM10->Eval(mynTrk));
        }
        else{
            tfr_QCD = TMath::Min(1.0,FRQCD_taupt_DM10->Eval(mytaupt)*FRQCD_highnTrk_DM10->Eval(mynTrk));
            tfr_W=TMath::Min(1.0,FRW_taupt_DM10->Eval(mytaupt)*FRW_highnTrk_DM10->Eval(mynTrk));
        }

    }
    else if (taudecaymode==11){
        if (mynTrk<ntrkcut){
            tfr_W=TMath::Min(1.0,FRW_taupt_DM11->Eval(mytaupt)*FRW_lownTrk_DM11->Eval(mynTrk));
            tfr_QCD = TMath::Min(1.0,FRQCD_taupt_DM11->Eval(mytaupt)*FRQCD_lownTrk_DM11->Eval(mynTrk));
        }
        else{
            tfr_W=TMath::Min(1.0,FRW_taupt_DM11->Eval(mytaupt)*FRW_highnTrk_DM11->Eval(mynTrk));
            tfr_QCD = TMath::Min(1.0,FRQCD_taupt_DM11->Eval(mytaupt)*FRQCD_highnTrk_DM11->Eval(mynTrk));
        }
    }

    if (isMuonTauTrigger){
        tfr_W*=1.7;
        tfr_QCD*=1.7;
    }
    float tfr=fracW*tfr_W + (1-fracW)*tfr_QCD;
    return tfr;
}

*/


tautauFR::tautauFR(string year){
    yearconf = year;
    TFile *fFR_tautau = new TFile(Form("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/scripts_tautau/Histo/HistoforFR_%s/FRfit_tautau.root",year.c_str()),"read");

    FRQCD_tau1pt_DM0_leading = (TF1*)fFR_tautau->Get("fitfunc_QCD_DM0_tau1pt_leading");
    FRQCD_lownTrk_DM0_leading = (TF1*)fFR_tautau->Get("fitfunc_QCD_DM0_lownTrk_leading");
    FRQCD_highnTrk_DM0_leading = (TF1*)fFR_tautau->Get("fitfunc_QCD_DM0_highnTrk_leading");

    FRQCD_tau1pt_DM1_leading = (TF1*)fFR_tautau->Get("fitfunc_QCD_DM1_tau1pt_leading");
    FRQCD_lownTrk_DM1_leading = (TF1*)fFR_tautau->Get("fitfunc_QCD_DM1_lownTrk_leading");
    FRQCD_highnTrk_DM1_leading = (TF1*)fFR_tautau->Get("fitfunc_QCD_DM1_highnTrk_leading");

    FRQCD_tau1pt_DM10_leading = (TF1*)fFR_tautau->Get("fitfunc_QCD_DM10_tau1pt_leading");
    FRQCD_lownTrk_DM10_leading = (TF1*)fFR_tautau->Get("fitfunc_QCD_DM10_lownTrk_leading");
    FRQCD_highnTrk_DM10_leading = (TF1*)fFR_tautau->Get("fitfunc_QCD_DM10_highnTrk_leading");

    FRQCD_tau1pt_DM11_leading = (TF1*)fFR_tautau->Get("fitfunc_QCD_DM11_tau1pt_leading");
    FRQCD_lownTrk_DM11_leading = (TF1*)fFR_tautau->Get("fitfunc_QCD_DM11_lownTrk_leading");
    FRQCD_highnTrk_DM11_leading = (TF1*)fFR_tautau->Get("fitfunc_QCD_DM11_highnTrk_leading");


    FRQCD_tau2pt_DM0_subleading = (TF1*)fFR_tautau->Get("fitfunc_QCD_DM0_tau2pt_subleading");
    FRQCD_lownTrk_DM0_subleading = (TF1*)fFR_tautau->Get("fitfunc_QCD_DM0_lownTrk_subleading");
    FRQCD_highnTrk_DM0_subleading = (TF1*)fFR_tautau->Get("fitfunc_QCD_DM0_highnTrk_subleading");

    FRQCD_tau2pt_DM1_subleading = (TF1*)fFR_tautau->Get("fitfunc_QCD_DM1_tau2pt_subleading");
    FRQCD_lownTrk_DM1_subleading = (TF1*)fFR_tautau->Get("fitfunc_QCD_DM1_lownTrk_subleading");
    FRQCD_highnTrk_DM1_subleading = (TF1*)fFR_tautau->Get("fitfunc_QCD_DM1_highnTrk_subleading");

    FRQCD_tau2pt_DM10_subleading = (TF1*)fFR_tautau->Get("fitfunc_QCD_DM10_tau2pt_subleading");
    FRQCD_lownTrk_DM10_subleading = (TF1*)fFR_tautau->Get("fitfunc_QCD_DM10_lownTrk_subleading");
    FRQCD_highnTrk_DM10_subleading = (TF1*)fFR_tautau->Get("fitfunc_QCD_DM10_highnTrk_subleading");

    FRQCD_tau2pt_DM11_subleading = (TF1*)fFR_tautau->Get("fitfunc_QCD_DM11_tau2pt_subleading");
    FRQCD_lownTrk_DM11_subleading = (TF1*)fFR_tautau->Get("fitfunc_QCD_DM11_lownTrk_subleading");
    FRQCD_highnTrk_DM11_subleading = (TF1*)fFR_tautau->Get("fitfunc_QCD_DM11_highnTrk_subleading");

    err_nt0_ffQCD_leading = (TH1F*)fFR_tautau->Get("err_nt0_ffQCD_leading");
    err_nt0_ffQCD_subleading = (TH1F*)fFR_tautau->Get("err_nt0_ffQCD_subleading");
}


tautauFR::tautauFR(){
    
}

tautauFR tautauFR2016pre("2016pre");
tautauFR tautauFR2016post("2016post");
tautauFR tautauFR2017("2017");
tautauFR tautauFR2018("2018");

map<string, tautauFR> tautauFRmap = {
    {"2016pre", tautauFR2016pre}, {"2016post", tautauFR2016post},{"2017", tautauFR2017},{"2018", tautauFR2018}
};


float GetFR_tautau(int taudecaymode,float taupt, int nTrk, int fake, string year){
    //fake 1: leading tau fake; fake 2: subleading tau fake

    float mytaupt = taupt;
    if (taupt>300) mytaupt=299;
    int mynTrk=nTrk;
    if (nTrk>=100) mynTrk=99;
    float tfr_QCD=1;
    float ntrkcut = 25;
    if (fake==1){
        if (taudecaymode==0){
            if (mynTrk<ntrkcut){
                tfr_QCD = TMath::Min(1.0,tautauFRmap[year].FRQCD_tau1pt_DM0_leading->Eval(mytaupt)*tautauFRmap[year].FRQCD_lownTrk_DM0_leading->Eval(mynTrk));
            }
            else{
                tfr_QCD = TMath::Min(1.0,tautauFRmap[year].FRQCD_tau1pt_DM0_leading->Eval(mytaupt)*tautauFRmap[year].FRQCD_highnTrk_DM0_leading->Eval(mynTrk));
            }
        }
        else if (taudecaymode==1){
            if (mynTrk<ntrkcut){
                tfr_QCD = TMath::Min(1.0,tautauFRmap[year].FRQCD_tau1pt_DM1_leading->Eval(mytaupt)*tautauFRmap[year].FRQCD_lownTrk_DM1_leading->Eval(mynTrk));
            }
            else{
                tfr_QCD = TMath::Min(1.0,tautauFRmap[year].FRQCD_tau1pt_DM1_leading->Eval(mytaupt)*tautauFRmap[year].FRQCD_highnTrk_DM1_leading->Eval(mynTrk));
            }
        }
        else if (taudecaymode==10){
            if (mynTrk<ntrkcut){
                tfr_QCD = TMath::Min(1.0,tautauFRmap[year].FRQCD_tau1pt_DM10_leading->Eval(mytaupt)*tautauFRmap[year].FRQCD_lownTrk_DM10_leading->Eval(mynTrk));
            }
            else{
                tfr_QCD = TMath::Min(1.0,tautauFRmap[year].FRQCD_tau1pt_DM10_leading->Eval(mytaupt)*tautauFRmap[year].FRQCD_highnTrk_DM10_leading->Eval(mynTrk));
            }
        }
        else if (taudecaymode==11){
            if (mynTrk<ntrkcut){
                tfr_QCD = TMath::Min(1.0,tautauFRmap[year].FRQCD_tau1pt_DM11_leading->Eval(mytaupt)*tautauFRmap[year].FRQCD_lownTrk_DM11_leading->Eval(mynTrk));
            }
            else{
                tfr_QCD = TMath::Min(1.0,tautauFRmap[year].FRQCD_tau1pt_DM11_leading->Eval(mytaupt)*tautauFRmap[year].FRQCD_highnTrk_DM11_leading->Eval(mynTrk));
            }
        }
    }

    else if (fake==2){
        if (taudecaymode==0){
            if (mynTrk<ntrkcut){
                tfr_QCD = TMath::Min(1.0,tautauFRmap[year].FRQCD_tau2pt_DM0_subleading->Eval(mytaupt)*tautauFRmap[year].FRQCD_lownTrk_DM0_subleading->Eval(mynTrk));
            }
            else{
                tfr_QCD = TMath::Min(1.0,tautauFRmap[year].FRQCD_tau2pt_DM0_subleading->Eval(mytaupt)*tautauFRmap[year].FRQCD_highnTrk_DM0_subleading->Eval(mynTrk));
            }
        }
        else if (taudecaymode==1){
            if (mynTrk<ntrkcut){
                tfr_QCD = TMath::Min(1.0,tautauFRmap[year].FRQCD_tau2pt_DM1_subleading->Eval(mytaupt)*tautauFRmap[year].FRQCD_lownTrk_DM1_subleading->Eval(mynTrk));
            }
            else{
                tfr_QCD = TMath::Min(1.0,tautauFRmap[year].FRQCD_tau2pt_DM1_subleading->Eval(mytaupt)*tautauFRmap[year].FRQCD_highnTrk_DM1_subleading->Eval(mynTrk));
            }
        }
        else if (taudecaymode==10){
            if (mynTrk<ntrkcut){
                tfr_QCD = TMath::Min(1.0,tautauFRmap[year].FRQCD_tau2pt_DM10_subleading->Eval(mytaupt)*tautauFRmap[year].FRQCD_lownTrk_DM10_subleading->Eval(mynTrk));
            }
            else{
                tfr_QCD = TMath::Min(1.0,tautauFRmap[year].FRQCD_tau2pt_DM10_subleading->Eval(mytaupt)*tautauFRmap[year].FRQCD_highnTrk_DM10_subleading->Eval(mynTrk));
            }
        }
        else if (taudecaymode==11){
            if (mynTrk<ntrkcut){
                tfr_QCD = TMath::Min(1.0,tautauFRmap[year].FRQCD_tau2pt_DM11_subleading->Eval(mytaupt)*tautauFRmap[year].FRQCD_lownTrk_DM11_subleading->Eval(mynTrk));
            }
            else{
                tfr_QCD = TMath::Min(1.0,tautauFRmap[year].FRQCD_tau2pt_DM11_subleading->Eval(mytaupt)*tautauFRmap[year].FRQCD_highnTrk_DM11_subleading->Eval(mynTrk));
            }
        }
    }
    else{
        tfr_QCD=1;
    }
    if (tfr_QCD<0){
        tfr_QCD=0;
    }
    float tfr=tfr_QCD;
    return tfr;
}

//Extrapolation of the fake rates with tauh pT
float GetFR_tautau_qcd_sys_taupt(float qcdFR, float taupt, int decaymode, int taudecaymode, bool down){
    float mytaupt = taupt;
    if (taupt>300) mytaupt=299;
    if (taudecaymode==decaymode){
        if (down){
            return qcdFR*(1-0.5*(mytaupt-40)/260);
        }
        else {
            return qcdFR*(1+0.5*(mytaupt-40)/260);
        }
    }
    else{
        return qcdFR;
    }
}


//Statistical uncertainty in the Ntracks extrapolation
float GetFR_tautau_qcd_sys_ntrk_dm(float qcdFR, int decaymode, int taudecaymode, bool down, int leading, string year){
    //leading 0: leading, 1 :subleading
    float err = 0;
    if (leading==0){
         err = tautauFRmap[year].err_nt0_ffQCD_leading->GetBinContent(decaymode+1);
    }
    else{
        err = tautauFRmap[year].err_nt0_ffQCD_subleading->GetBinContent(decaymode+1);
    }
    if (taudecaymode==decaymode){
        if (down){
            return qcdFR*(1-err);
        }
        else {
            return qcdFR*(1+err);
        }
    }
    else{
        return qcdFR;
    }
}








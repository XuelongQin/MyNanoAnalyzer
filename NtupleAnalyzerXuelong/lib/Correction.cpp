#include "Correction.h"

spe_cor::spe_cor(string year, string sys){
    yearconf = year;
    if (year == "2016pre"){
        TFile* f_aco_fine=new TFile("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/corrections/new_new_correction_acoplanarity_fine_2016pre.root","read");
        fit_aco_2030_2030 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_2030_2030%s",sys.c_str()));
        fit_aco_3040_2030 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_3040_2030%s",sys.c_str()));
        fit_aco_4050_2030 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_4050_2030%s",sys.c_str()));
        fit_aco_gt50_2030 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_gt50_2030%s",sys.c_str()));
        fit_aco_3040_3040 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_3040_3040%s",sys.c_str()));
        fit_aco_4050_3040 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_4050_3040%s",sys.c_str()));
        fit_aco_gt50_3040 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_gt50_3040%s",sys.c_str()));
        fit_aco_4050_4050 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_4050_4050%s",sys.c_str()));
        fit_aco_gt50_4050 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_gt50_4050%s",sys.c_str()));
        fit_aco_gt50_gt50 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_gt50_gt50%s",sys.c_str()));
        TFile* f_bs=new TFile("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/corrections/beamspot_UL2016_preVFP_Data.root","read");
        h_bs_sigma = (TH1F*) f_bs->Get("bs_sigma");
        h_bs_z = (TH1F*) f_bs->Get("bs_z");
        TFile* f_bs_mc=new TFile("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/corrections/beamspot_UL2016_preVFP_MC.root","read");
        h_bs_sigma_mc = (TH1F*) f_bs_mc->Get("bs_sigma");
        h_bs_z_mc = (TH1F*) f_bs_mc->Get("bs_z");
        bs_z_mc=h_bs_z_mc->GetMean();
        bs_zsigma_mc=h_bs_sigma_mc->GetMean();
        TFile *f_punt=new TFile("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/corrections/corrs_ntracks_pu_UL2016_preVFP.root");
        correction_map=(TH2F*) f_punt->Get("corr");
        TFile *f_hsnt=new TFile("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/corrections/corrs_ntracks_hs_UL2016_preVFP.root");
        correction_mapHS=(TH2F*) f_hsnt->Get("correction_map");
    }
    else if (year == "2016post"){
        TFile* f_aco_fine=new TFile("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/corrections/new_new_correction_acoplanarity_fine_2016post.root","read");
        fit_aco_2030_2030 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_2030_2030%s",sys.c_str()));
        fit_aco_3040_2030 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_3040_2030%s",sys.c_str()));
        fit_aco_4050_2030 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_4050_2030%s",sys.c_str()));
        fit_aco_gt50_2030 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_gt50_2030%s",sys.c_str()));
        fit_aco_3040_3040 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_3040_3040%s",sys.c_str()));
        fit_aco_4050_3040 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_4050_3040%s",sys.c_str()));
        fit_aco_gt50_3040 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_gt50_3040%s",sys.c_str()));
        fit_aco_4050_4050 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_4050_4050%s",sys.c_str()));
        fit_aco_gt50_4050 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_gt50_4050%s",sys.c_str()));
        fit_aco_gt50_gt50 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_gt50_gt50%s",sys.c_str()));
        TFile* f_bs=new TFile("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/corrections/beamspot_UL2016_postVFP_Data.root","read");
        h_bs_sigma = (TH1F*) f_bs->Get("bs_sigma");
        h_bs_z = (TH1F*) f_bs->Get("bs_z");
        TFile* f_bs_mc=new TFile("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/corrections/beamspot_UL2016_postVFP_MC.root","read");
        h_bs_sigma_mc = (TH1F*) f_bs_mc->Get("bs_sigma");
        h_bs_z_mc = (TH1F*) f_bs_mc->Get("bs_z");
        bs_z_mc=h_bs_z_mc->GetMean();
        bs_zsigma_mc=h_bs_sigma_mc->GetMean();
        TFile *f_punt=new TFile("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/corrections/corrs_ntracks_pu_UL2016_postVFP.root");
        correction_map=(TH2F*) f_punt->Get("corr");
        TFile *f_hsnt=new TFile("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/corrections/corrs_ntracks_hs_UL2016_postVFP.root");
        correction_mapHS=(TH2F*) f_hsnt->Get("correction_map");
    }
    else if (year == "2017"){
        TFile* f_aco_fine=new TFile("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/corrections/new_new_correction_acoplanarity_fine_2017.root","read");
        fit_aco_2030_2030 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_2030_2030%s",sys.c_str()));
        fit_aco_3040_2030 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_3040_2030%s",sys.c_str()));
        fit_aco_4050_2030 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_4050_2030%s",sys.c_str()));
        fit_aco_gt50_2030 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_gt50_2030%s",sys.c_str()));
        fit_aco_3040_3040 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_3040_3040%s",sys.c_str()));
        fit_aco_4050_3040 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_4050_3040%s",sys.c_str()));
        fit_aco_gt50_3040 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_gt50_3040%s",sys.c_str()));
        fit_aco_4050_4050 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_4050_4050%s",sys.c_str()));
        fit_aco_gt50_4050 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_gt50_4050%s",sys.c_str()));
        fit_aco_gt50_gt50 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_gt50_gt50%s",sys.c_str()));
        TFile* f_bs=new TFile("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/corrections/beamspot_UL2017_Data.root","read");
        h_bs_sigma = (TH1F*) f_bs->Get("bs_sigma");
        h_bs_z = (TH1F*) f_bs->Get("bs_z");
        TFile* f_bs_mc=new TFile("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/corrections/beamspot_UL2017_MC.root","read");
        h_bs_sigma_mc = (TH1F*) f_bs_mc->Get("bs_sigma");
        h_bs_z_mc = (TH1F*) f_bs_mc->Get("bs_z");
        bs_z_mc=h_bs_z_mc->GetMean();
        bs_zsigma_mc=h_bs_sigma_mc->GetMean();
        TFile *f_punt=new TFile("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/corrections/corrs_ntracks_pu_UL2017.root");
        correction_map=(TH2F*) f_punt->Get("corr");
        TFile *f_hsnt=new TFile("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/corrections/corrs_ntracks_hs_UL2017.root");
        correction_mapHS=(TH2F*) f_hsnt->Get("correction_map");
    }
    else if (year == "2018"){
        TFile* f_aco_fine=new TFile("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/corrections/new_new_correction_acoplanarity_fine_2018.root","read");
        fit_aco_2030_2030 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_2030_2030%s",sys.c_str()));
        fit_aco_3040_2030 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_3040_2030%s",sys.c_str()));
        fit_aco_4050_2030 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_4050_2030%s",sys.c_str()));
        fit_aco_gt50_2030 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_gt50_2030%s",sys.c_str()));
        fit_aco_3040_3040 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_3040_3040%s",sys.c_str()));
        fit_aco_4050_3040 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_4050_3040%s",sys.c_str()));
        fit_aco_gt50_3040 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_gt50_3040%s",sys.c_str()));
        fit_aco_4050_4050 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_4050_4050%s",sys.c_str()));
        fit_aco_gt50_4050 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_gt50_4050%s",sys.c_str()));
        fit_aco_gt50_gt50 = (TF1*) f_aco_fine->Get(Form("fit_acoplanarity_gt50_gt50%s",sys.c_str()));
        TFile* f_bs=new TFile("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/corrections/beamspot_UL2018_Data.root","read");
        h_bs_sigma = (TH1F*) f_bs->Get("bs_sigma");
        h_bs_z = (TH1F*) f_bs->Get("bs_z");
        TFile* f_bs_mc=new TFile("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/corrections/beamspot_UL2018_MC.root","read");
        h_bs_sigma_mc = (TH1F*) f_bs_mc->Get("bs_sigma");
        h_bs_z_mc = (TH1F*) f_bs_mc->Get("bs_z");
        bs_z_mc=h_bs_z_mc->GetMean();
        bs_zsigma_mc=h_bs_sigma_mc->GetMean();
        TFile *f_punt=new TFile("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/corrections/corrs_ntracks_pu_UL2018.root");
        correction_map=(TH2F*) f_punt->Get("corr");
        TFile *f_hsnt=new TFile("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/corrections/corrs_ntracks_hs_UL2018.root");
        correction_mapHS=(TH2F*) f_hsnt->Get("correction_map");
    }
    else {
        cout << "wrong year configuration" << endl;
    }
}

spe_cor::spe_cor(){
    
}
spe_cor spe_cor2016pre("2016pre","");
spe_cor spe_cor2016post("2016post","");
spe_cor spe_cor2017("2017","");
spe_cor spe_cor2018("2018","");


spe_cor spe_cor2016pre_scale1("2016pre","_scale1");
spe_cor spe_cor2016post_scale1("2016post","_scale1");
spe_cor spe_cor2017_scale1("2017","_scale1");
spe_cor spe_cor2018_scale1("2018","_scale1");


spe_cor spe_cor2016pre_scale2("2016pre","_scale2");
spe_cor spe_cor2016post_scale2("2016post","_scale2");
spe_cor spe_cor2017_scale2("2017","_scale2");
spe_cor spe_cor2018_scale2("2018","_scale2");


spe_cor spe_cor2016pre_scale3("2016pre","_scale3");
spe_cor spe_cor2016post_scale3("2016post","_scale3");
spe_cor spe_cor2017_scale3("2017","_scale3");
spe_cor spe_cor2018_scale3("2018","_scale3");


spe_cor spe_cor2016pre_scale4("2016pre","_scale4");
spe_cor spe_cor2016post_scale4("2016post","_scale4");
spe_cor spe_cor2017_scale4("2017","_scale4");
spe_cor spe_cor2018_scale4("2018","_scale4");


spe_cor spe_cor2016pre_scale5("2016pre","_scale5");
spe_cor spe_cor2016post_scale5("2016post","_scale5");
spe_cor spe_cor2017_scale5("2017","_scale5");
spe_cor spe_cor2018_scale5("2018","_scale5");


spe_cor spe_cor2016pre_scale6("2016pre","_scale6");
spe_cor spe_cor2016post_scale6("2016post","_scale6");
spe_cor spe_cor2017_scale6("2017","_scale6");
spe_cor spe_cor2018_scale6("2018","_scale6");


spe_cor spe_cor2016pre_ps1("2016pre","_ps1");
spe_cor spe_cor2016post_ps1("2016post","_ps1");
spe_cor spe_cor2017_ps1("2017","_ps1");
spe_cor spe_cor2018_ps1("2018","_ps1");


spe_cor spe_cor2016pre_ps2("2016pre","_ps2");
spe_cor spe_cor2016post_ps2("2016post","_ps2");
spe_cor spe_cor2017_ps2("2017","_ps2");
spe_cor spe_cor2018_ps2("2018","_ps2");


spe_cor spe_cor2016pre_ps3("2016pre","_ps3");
spe_cor spe_cor2016post_ps3("2016post","_ps3");
spe_cor spe_cor2017_ps3("2017","_ps3");
spe_cor spe_cor2018_ps3("2018","_ps3");


spe_cor spe_cor2016pre_ps4("2016pre","_ps4");
spe_cor spe_cor2016post_ps4("2016post","_ps4");
spe_cor spe_cor2017_ps4("2017","_ps4");
spe_cor spe_cor2018_ps4("2018","_ps4");


map<string, spe_cor> spe_cormap = {
    {"2016pre", spe_cor2016pre}, {"2016post", spe_cor2016post},{"2017", spe_cor2017},{"2018", spe_cor2018},
    {"2016pre_scale1", spe_cor2016pre_scale1}, {"2016post_scale1", spe_cor2016post_scale1},{"2017_scale1", spe_cor2017_scale1},{"2018_scale1", spe_cor2018_scale1},
    {"2016pre_scale2", spe_cor2016pre_scale2}, {"2016post_scale2", spe_cor2016post_scale2},{"2017_scale2", spe_cor2017_scale2},{"2018_scale2", spe_cor2018_scale2},
    {"2016pre_scale3", spe_cor2016pre_scale3}, {"2016post_scale3", spe_cor2016post_scale3},{"2017_scale3", spe_cor2017_scale3},{"2018_scale3", spe_cor2018_scale3},
    {"2016pre_scale4", spe_cor2016pre_scale4}, {"2016post_scale4", spe_cor2016post_scale4},{"2017_scale4", spe_cor2017_scale4},{"2018_scale4", spe_cor2018_scale4},
    {"2016pre_scale5", spe_cor2016pre_scale5}, {"2016post_scale5", spe_cor2016post_scale5},{"2017_scale5", spe_cor2017_scale5},{"2018_scale5", spe_cor2018_scale5},
    {"2016pre_scale6", spe_cor2016pre_scale6}, {"2016post_scale6", spe_cor2016post_scale6},{"2017_scale6", spe_cor2017_scale6},{"2018_scale6", spe_cor2018_scale6},
    {"2016pre_ps1", spe_cor2016pre_ps1}, {"2016post_ps1", spe_cor2016post_ps1},{"2017_ps1", spe_cor2017_ps1},{"2018_ps1", spe_cor2018_ps1},
    {"2016pre_ps2", spe_cor2016pre_ps2}, {"2016post_ps2", spe_cor2016post_ps2},{"2017_ps2", spe_cor2017_ps2},{"2018_ps2", spe_cor2018_ps2},
    {"2016pre_ps3", spe_cor2016pre_ps3}, {"2016post_ps3", spe_cor2016post_ps3},{"2017_ps3", spe_cor2017_ps3},{"2018_ps3", spe_cor2018_ps3},
    {"2016pre_ps4", spe_cor2016pre_ps4}, {"2016post_ps4", spe_cor2016post_ps4},{"2017_ps4", spe_cor2017_ps4},{"2018_ps4", spe_cor2018_ps4}
};



//Get Correction on Acopolanarity only for DY
/*TFile* f_aco_fine=new TFile("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/corrections/correction_acoplanarity_fine_2018.root","read");
TF1* fit_aco_2030_2030 = (TF1*) f_aco_fine->Get("fit_acoplanarity_2030_2030");
TF1* fit_aco_3040_2030 = (TF1*) f_aco_fine->Get("fit_acoplanarity_3040_2030");
TF1* fit_aco_4050_2030 = (TF1*) f_aco_fine->Get("fit_acoplanarity_4050_2030");
TF1* fit_aco_gt50_2030 = (TF1*) f_aco_fine->Get("fit_acoplanarity_gt50_2030");
TF1* fit_aco_3040_3040 = (TF1*) f_aco_fine->Get("fit_acoplanarity_3040_3040");
TF1* fit_aco_4050_3040 = (TF1*) f_aco_fine->Get("fit_acoplanarity_4050_3040");
TF1* fit_aco_gt50_3040 = (TF1*) f_aco_fine->Get("fit_acoplanarity_gt50_3040");
TF1* fit_aco_4050_4050 = (TF1*) f_aco_fine->Get("fit_acoplanarity_4050_4050");
TF1* fit_aco_gt50_4050 = (TF1*) f_aco_fine->Get("fit_acoplanarity_gt50_4050");
TF1* fit_aco_gt50_gt50 = (TF1*) f_aco_fine->Get("fit_acoplanarity_gt50_gt50");
*/
float GetGenAco(int nZGenCand, Vec_t &ZGenCand_pt, Vec_t &ZGenCand_eta,Vec_t &ZGenCand_phi ,float Acopl){
    float gen_aco = Acopl;
    if (nZGenCand==2){//if we have 2 ZGenCand, we use genaco
        TLorentzVector my_gen1;
        TLorentzVector my_gen2;
        my_gen1.SetPtEtaPhiM(ZGenCand_pt[0],ZGenCand_eta[0],ZGenCand_phi[0],0);
        my_gen2.SetPtEtaPhiM(ZGenCand_pt[1],ZGenCand_eta[1],ZGenCand_phi[1],0);
        //float DRmatch1 = my_lep1.DeltaR(my_gen1)+my_lep2.DeltaR(my_gen2);
        //float DRmatch2 = my_lep1.DeltaR(my_gen2)+my_lep2.DeltaR(my_gen1);
        //if (DRmatch1<0.2 || DRmatch2<0.2){
        float dphi = my_gen1.DeltaPhi(my_gen2);
        gen_aco = 1-fabs(dphi)/TMath::Pi();
        //}
        //else{
        //    gen_aco = Acopl;
        //}
        
    }
    //else{//else use recoaco
    //    gen_aco = Acopl;
    //}
    return gen_aco;
}


float Get_Aweight(int nZGenCand, Vec_t &ZGenCand_pt, Vec_t &ZGenCand_eta,Vec_t &ZGenCand_phi,float gen_aco, string year, string sys){
    float my_lep1pt = 0;
    float my_lep2pt = 0;
    year = year + sys;
    if (nZGenCand==2){
        TLorentzVector my_gen1;
        TLorentzVector my_gen2;
        my_gen1.SetPtEtaPhiM(ZGenCand_pt[0],ZGenCand_eta[0],ZGenCand_phi[0],0);
        my_gen2.SetPtEtaPhiM(ZGenCand_pt[1],ZGenCand_eta[1],ZGenCand_phi[1],0);
        my_lep1pt = TMath::Max(ZGenCand_pt[0],ZGenCand_pt[1]);
        my_lep2pt = TMath::Min(ZGenCand_pt[0],ZGenCand_pt[1]);
    }
/*    else{

    }
    if (nZGenCand==2){//if we have 2 ZGenCand, we use genpt
        my_lep1pt = TMath::Max(ZGenCand_pt[0],ZGenCand_pt[1]);
        my_lep2pt = TMath::Min(ZGenCand_pt[0],ZGenCand_pt[1]);
    }
    else{
        my_lep1pt = TMath::Max(lep1pt,lep2pt);
        my_lep2pt = TMath::Min(lep1pt,lep2pt);
    }
    */
    float Acocut = 0.35;
    float A_weight=1.0;
    if (my_lep1pt<30 && my_lep2pt<30){
        A_weight = spe_cormap[year].fit_aco_2030_2030->Eval(TMath::Min(Acocut,gen_aco));
    }
    else if (my_lep1pt>30 && my_lep1pt<40 && my_lep2pt<30){
        A_weight = spe_cormap[year].fit_aco_3040_2030->Eval(TMath::Min(Acocut,gen_aco));
    }
    else if (my_lep1pt>40 && my_lep1pt<50 && my_lep2pt<30){
        A_weight = spe_cormap[year].fit_aco_4050_2030->Eval(TMath::Min(Acocut,gen_aco));
    }
    else if (my_lep1pt>50 && my_lep2pt<30){
        A_weight = spe_cormap[year].fit_aco_gt50_2030->Eval(TMath::Min(Acocut,gen_aco));
    }
    else if (my_lep1pt>30 && my_lep1pt<40 && my_lep2pt>30 && my_lep2pt<40 ){
        A_weight = spe_cormap[year].fit_aco_3040_3040->Eval(TMath::Min(Acocut,gen_aco));
    }
    else if (my_lep1pt>40 && my_lep1pt<50 && my_lep2pt>30 && my_lep2pt<40 ){
        A_weight = spe_cormap[year].fit_aco_4050_3040->Eval(TMath::Min(Acocut,gen_aco));
    }
    else if (my_lep1pt>50 && my_lep2pt>30 && my_lep2pt<40 ){
        A_weight = spe_cormap[year].fit_aco_gt50_3040->Eval(TMath::Min(Acocut,gen_aco));
    }
    else if (my_lep1pt>40 && my_lep1pt<50 && my_lep2pt>40 && my_lep2pt<50 ){
        A_weight = spe_cormap[year].fit_aco_4050_4050->Eval(TMath::Min(Acocut,gen_aco));
    }
    else if (my_lep1pt>50 && my_lep2pt>40 && my_lep2pt<50 ){
        A_weight = spe_cormap[year].fit_aco_gt50_4050->Eval(TMath::Min(Acocut,gen_aco));
    }
    else if (my_lep1pt>50 && my_lep2pt>50 ){
        A_weight = spe_cormap[year].fit_aco_gt50_gt50->Eval(TMath::Min(Acocut,gen_aco));
    }
    return A_weight;
}

//Get Correction on N_PV for all simulation
/*TFile* f_npvs=new TFile("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/corrections/correction_npvs_2018.root","read");
TH1F* h_npvs_weight = (TH1F*) f_npvs->Get("correction_hist_npvs");
TH1F* h_npvsDown_weight = (TH1F*) f_npvs->Get("correction_hist_npvsDown");
TH1F* h_npvsUp_weight = (TH1F*) f_npvs->Get("correction_hist_npvsUp");
float Get_npvs_weight(int PV_npvs){
    float npvs_weight=h_npvs_weight->GetBinContent(h_npvs_weight->GetXaxis()->FindBin(PV_npvs));
    return npvs_weight;
}

float Get_npvsDown_weight(int PV_npvs){
    float npvs_weight=h_npvsDown_weight->GetBinContent(h_npvsDown_weight->GetXaxis()->FindBin(PV_npvs));
    return npvs_weight;
}

float Get_npvsUp_weight(int PV_npvs){
    float npvs_weight=h_npvsUp_weight->GetBinContent(h_npvsUp_weight->GetXaxis()->FindBin(PV_npvs));
    return npvs_weight;
}


//Get Correction on beamspot for all simulation only for isMatchedToGenHS=0

TFile* f_bsz=new TFile("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/corrections/beamspotz_2018.root","read");
TF1* f_beamspotz=(TF1*) f_bsz->Get("f_beamspotz");

TFile* f_bs=new TFile("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/corrections/beamspot_TF1_2018.root","read");
TF1* h_bs_width = (TF1*) f_bs->Get("f1");
*/

ROOT::RVec<float> Get_BScor_ditaudz( Vec_t &PF_dz, ROOT::RVec<int> &PF_isMatchedToGenHS,float PV_z, float zvtxll,string year ){
    float bs_zsigma_obs=spe_cormap[year].h_bs_sigma->GetRandom();
    float bs_z_obs=spe_cormap[year].h_bs_z->GetRandom();
    float corr_zsig= (bs_zsigma_obs / spe_cormap[year].bs_zsigma_mc);
    float corr_z= bs_z_obs - corr_zsig * spe_cormap[year].bs_z_mc;

    auto mod = [PV_z, zvtxll,corr_z,corr_zsig](float dz, int HS ){
        float BScorrected_dz;
        if (HS==1){
            BScorrected_dz = fabs(PV_z+dz-zvtxll);
        }
        else{
            float z_corr = corr_z + corr_zsig * (PV_z+dz);
            BScorrected_dz = fabs(z_corr - zvtxll);
        }
        return BScorrected_dz;
    };
    ROOT::RVec<float> BScordz_ditaudz = Map(PF_dz,PF_isMatchedToGenHS,mod);
    return BScordz_ditaudz;
}

//Get Correction on n_putracks, apply to all simulation samples
//TFile *f_punt=new TFile("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/corrections/npu_correction_2018.root");
//TH2F* correction_map=(TH2F*) f_punt->Get("correction_map");

float Get_ntpuweight(int ntpu, float zvtxll,string year){
    float zpos = zvtxll;
    if (zpos<-10) zpos=-9.99;
    else if (zpos>10) zpos=9.99;
    float ntpu_weight=spe_cormap[year].correction_map->GetBinContent(spe_cormap[year].correction_map->GetXaxis()->FindBin(TMath::Min(49,ntpu)),spe_cormap[year].correction_map->GetYaxis()->FindBin(zpos)); // where zvtxll is the ditau vertex z, and ntpu is the number of BS corrected PU tracks inside the window
    return ntpu_weight;
}

//Get Correction on NHS_tracks, apply only to DY sample
//TFile *f_hsnt=new TFile("/afs/cern.ch/user/x/xuqin/work/taug-2/taug-2wkdir/CMSSW_10_6_27/src/MyNanoAnalyzer/NtupleAnalyzerXuelong/corrections/nhs_correction_2018.root");
//TH2F* correction_mapHS=(TH2F*) f_hsnt->Get("correction_map");
float Get_ntHSweight(int ntracksHS, float gen_aco,string year){
    float nths_weight=spe_cormap[year].correction_mapHS->GetBinContent(spe_cormap[year].correction_mapHS->GetXaxis()->FindBin(TMath::Min(30,ntracksHS)),spe_cormap[year].correction_mapHS->GetYaxis()->FindBin(gen_aco)); // here ntracksHS is number of HS tracks in window not matched to the tautau decay products
    return nths_weight;
}









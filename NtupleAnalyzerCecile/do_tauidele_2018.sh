./Make.sh FinalSelection_tauidele.cc
./FinalSelection_tauidele.exe 2018 /eos/cms/store/group/cmst3/group/taug2/AnalysisCecile/ntuples_etau_2018/EGammaA.root output_tauidele_2018/EGammaA.root data_obs data_obs
./FinalSelection_tauidele.exe 2018 /eos/cms/store/group/cmst3/group/taug2/AnalysisCecile/ntuples_etau_2018/EGammaB.root output_tauidele_2018/EGammaB.root data_obs data_obs
./FinalSelection_tauidele.exe 2018 /eos/cms/store/group/cmst3/group/taug2/AnalysisCecile/ntuples_etau_2018/EGammaC.root output_tauidele_2018/EGammaC.root data_obs data_obs
./FinalSelection_tauidele.exe 2018 /eos/cms/store/group/cmst3/group/taug2/AnalysisCecile/ntuples_etau_2018/EGammaD.root output_tauidele_2018/EGammaD.root data_obs data_obs
hadd -f output_tauidele_2018/EGamma.root output_tauidele_2018/EGammaA.root output_tauidele_2018/EGammaB.root output_tauidele_2018/EGammaC.root output_tauidele_2018/EGammaD.root
./FinalSelection_tauidele.exe 2018 /eos/cms/store/group/cmst3/group/taug2/AnalysisCecile/ntuples_etau_2018/DY.root output_tauidele_2018/ZTT.root DY ZTT
./FinalSelection_tauidele.exe 2018 /eos/cms/store/group/cmst3/group/taug2/AnalysisCecile/ntuples_etau_2018/DY.root output_tauidele_2018/ZLL.root DY ZLL
./FinalSelection_tauidele.exe 2018 /eos/cms/store/group/cmst3/group/taug2/AnalysisCecile/ntuples_etau_2018/DY.root output_tauidele_2018/ZJ.root DY ZJ
./FinalSelection_tauidele.exe 2018 /eos/cms/store/group/cmst3/group/taug2/AnalysisCecile/ntuples_etau_2018/W.root output_tauidele_2018/Wincl.root W W 
./FinalSelection_tauidele.exe 2018 /eos/cms/store/group/cmst3/group/taug2/AnalysisCecile/ntuples_etau_2018/W1.root output_tauidele_2018/W1.root W1 W
./FinalSelection_tauidele.exe 2018 /eos/cms/store/group/cmst3/group/taug2/AnalysisCecile/ntuples_etau_2018/W2.root output_tauidele_2018/W2.root W2 W
./FinalSelection_tauidele.exe 2018 /eos/cms/store/group/cmst3/group/taug2/AnalysisCecile/ntuples_etau_2018/W3.root output_tauidele_2018/W3.root W3 W
./FinalSelection_tauidele.exe 2018 /eos/cms/store/group/cmst3/group/taug2/AnalysisCecile/ntuples_etau_2018/W4.root output_tauidele_2018/W4.root W4 W
hadd -f output_tauidele_2018/W.root output_tauidele_2018/Wincl.root output_tauidele_2018/W1.root output_tauidele_2018/W2.root output_tauidele_2018/W3.root output_tauidele_2018/W4.root
./FinalSelection_tauidele.exe 2018 /eos/cms/store/group/cmst3/group/taug2/AnalysisCecile/ntuples_etau_2018/ST_t_antitop.root output_tauidele_2018/ST_t_antitop.root ST_t_antitop ST
./FinalSelection_tauidele.exe 2018 /eos/cms/store/group/cmst3/group/taug2/AnalysisCecile/ntuples_etau_2018/ST_t_top.root output_tauidele_2018/ST_t_top.root ST_t_top ST
./FinalSelection_tauidele.exe 2018 /eos/cms/store/group/cmst3/group/taug2/AnalysisCecile/ntuples_etau_2018/ST_tW_antitop.root output_tauidele_2018/ST_tW_antitop.root ST_tW_antitop ST
./FinalSelection_tauidele.exe 2018 /eos/cms/store/group/cmst3/group/taug2/AnalysisCecile/ntuples_etau_2018/ST_tW_top.root output_tauidele_2018/ST_tW_top.root ST_tW_top ST
hadd -f output_tauidele_2018/ST.root output_tauidele_2018/ST_t_antitop.root output_tauidele_2018/ST_t_top.root output_tauidele_2018/ST_tW_antitop.root output_tauidele_2018/ST_tW_top.root 
./FinalSelection_tauidele.exe 2018 /eos/cms/store/group/cmst3/group/taug2/AnalysisCecile/ntuples_etau_2018/WW2L2Nu.root output_tauidele_2018/WW2L2Nu.root WW2L2Nu VV
./FinalSelection_tauidele.exe 2018 /eos/cms/store/group/cmst3/group/taug2/AnalysisCecile/ntuples_etau_2018/WZ2Q2L.root output_tauidele_2018/WZ2Q2L.root WZ2Q2L VV
./FinalSelection_tauidele.exe 2018 /eos/cms/store/group/cmst3/group/taug2/AnalysisCecile/ntuples_etau_2018/WZ3LNu.root output_tauidele_2018/WZ3LNu.root WZ3LNu VV
./FinalSelection_tauidele.exe 2018 /eos/cms/store/group/cmst3/group/taug2/AnalysisCecile/ntuples_etau_2018/ZZ2L2Nu.root output_tauidele_2018/ZZ2L2Nu.root ZZ2L2Nu VV
./FinalSelection_tauidele.exe 2018 /eos/cms/store/group/cmst3/group/taug2/AnalysisCecile/ntuples_etau_2018/ZZ4L.root output_tauidele_2018/ZZ4L.root ZZ4L VV
hadd -f output_tauidele_2018/VV.root output_tauidele_2018/WW2L2Nu.root output_tauidele_2018/WZ2Q2L.root output_tauidele_2018/WZ3LNu.root output_tauidele_2018/ZZ2L2Nu.root output_tauidele_2018/ZZ4L.root
./FinalSelection_tauidele.exe 2018 /eos/cms/store/group/cmst3/group/taug2/AnalysisCecile/ntuples_etau_2018/TTToHadronic.root output_tauidele_2018/TTToHadronic.root TTToHadronic TT
./FinalSelection_tauidele.exe 2018 /eos/cms/store/group/cmst3/group/taug2/AnalysisCecile/ntuples_etau_2018/TTToSemiLeptonic.root output_tauidele_2018/TTToSemiLeptonic.root TTToSemiLeptonic TT
./FinalSelection_tauidele.exe 2018 /eos/cms/store/group/cmst3/group/taug2/AnalysisCecile/ntuples_etau_2018/TTTo2L2Nu.root output_tauidele_2018/TTTo2L2Nu.root TTTo2L2Nu TT
hadd -f output_tauidele_2018/TT.root output_tauidele_2018/TTToHadronic.root output_tauidele_2018/TTToSemiLeptonic.root output_tauidele_2018/TTTo2L2Nu.root
hadd -f output_tauidele_2018/MC.root output_tauidele_2018/ZLL.root output_tauidele_2018/ZTT.root output_tauidele_2018/ZJ.root output_tauidele_2018/ST.root output_tauidele_2018/VV.root output_tauidele_2018/TT.root output_tauidele_2018/W.root

python Create_fake_tauidele.py --year=2018
python Scale_W_tauidele.py --year=2018
hadd -f datacard_tauidele_2018.root output_tauidele_2018/Wrescaled.root output_tauidele_2018/QCD.root output_tauidele_2018/MC.root  output_tauidele_2018/EGamma.root 

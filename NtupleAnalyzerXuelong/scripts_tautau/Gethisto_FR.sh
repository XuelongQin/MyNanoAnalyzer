python3 Gethisto_FR.py 2018 GGToTauTau_Ctb20
python3 Gethisto_FR.py 2018 GGToElEl
python3 Gethisto_FR.py 2018 GGToWW
python3 Gethisto_FR.py 2018 DY
python3 Gethisto_FR.py 2018 ST_t_top
python3 Gethisto_FR.py 2018 ST_t_antitop
python3 Gethisto_FR.py 2018 ST_tW_top
python3 Gethisto_FR.py 2018 ST_tW_antitop
hadd -f Histo/HistoforFR_2018/ST.root Histo/HistoforFR_2018/ST_t_top.root Histo/HistoforFR_2018/ST_t_antitop.root Histo/HistoforFR_2018/ST_tW_top.root Histo/HistoforFR_2018/ST_tW_antitop.root 
python3 Gethisto_FR.py 2018 WZ2Q2L
python3 Gethisto_FR.py 2018 WZ3LNu
python3 Gethisto_FR.py 2018 VV2L2Nu
python3 Gethisto_FR.py 2018 ZZ2Q2L
python3 Gethisto_FR.py 2018 ZZ4L
hadd -f Histo/HistoforFR_2018/VV.root Histo/HistoforFR_2018/WZ2Q2L.root Histo/HistoforFR_2018/WZ3LNu.root Histo/HistoforFR_2018/VV2L2Nu.root Histo/HistoforFR_2018/ZZ2Q2L.root Histo/HistoforFR_2018/ZZ4L.root
python3 Gethisto_FR.py 2018 TTTo2L2Nu
python3 Gethisto_FR.py 2018 TTToHadronic
python3 Gethisto_FR.py 2018 TTToSemiLeptonic
hadd -f Histo/HistoforFR_2018/TT.root Histo/HistoforFR_2018/TTToHadronic.root Histo/HistoforFR_2018/TTToSemiLeptonic.root Histo/HistoforFR_2018/TTTo2L2Nu.root
hadd -f Histo/HistoforFR_2018/MC.root Histo/HistoforFR_2018/DY.root Histo/HistoforFR_2018/ST.root Histo/HistoforFR_2018/VV.root Histo/HistoforFR_2018/TT.root Histo/HistoforFR_2018/GGToElEl.root Histo/HistoforFR_2018/GGToWW.root 
python3 Gethisto_FR.py 2018 TauA
python3 Gethisto_FR.py 2018 TauB
python3 Gethisto_FR.py 2018 TauC
python3 Gethisto_FR.py 2018 TauD
hadd -f Histo/HistoforFR_2018/Tau.root Histo/HistoforFR_2018/TauA.root Histo/HistoforFR_2018/TauB.root Histo/HistoforFR_2018/TauC.root Histo/HistoforFR_2018/TauD.root
python3 CreateFRhist.py --year 2018
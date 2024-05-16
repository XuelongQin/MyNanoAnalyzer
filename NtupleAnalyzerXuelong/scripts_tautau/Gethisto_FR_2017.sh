python3 Gethisto_FR.py 2017 GGToTauTau_Ctb20
python3 Gethisto_FR.py 2017 GGToElEl
python3 Gethisto_FR.py 2017 GGToWW
python3 Gethisto_FR.py 2017 DY
python3 Gethisto_FR.py 2017 ST_t_top
python3 Gethisto_FR.py 2017 ST_t_antitop
python3 Gethisto_FR.py 2017 ST_tW_top
python3 Gethisto_FR.py 2017 ST_tW_antitop
hadd -f Histo/HistoforFR_2017/ST.root Histo/HistoforFR_2017/ST_t_top.root Histo/HistoforFR_2017/ST_t_antitop.root Histo/HistoforFR_2017/ST_tW_top.root Histo/HistoforFR_2017/ST_tW_antitop.root 
python3 Gethisto_FR.py 2017 WZ2Q2L
python3 Gethisto_FR.py 2017 WZ3LNu
python3 Gethisto_FR.py 2017 VV2L2Nu
python3 Gethisto_FR.py 2017 ZZ2Q2L
python3 Gethisto_FR.py 2017 ZZ4L
hadd -f Histo/HistoforFR_2017/VV.root Histo/HistoforFR_2017/WZ2Q2L.root Histo/HistoforFR_2017/WZ3LNu.root Histo/HistoforFR_2017/VV2L2Nu.root Histo/HistoforFR_2017/ZZ2Q2L.root Histo/HistoforFR_2017/ZZ4L.root
python3 Gethisto_FR.py 2017 TTTo2L2Nu
python3 Gethisto_FR.py 2017 TTToHadronic
python3 Gethisto_FR.py 2017 TTToSemiLeptonic
hadd -f Histo/HistoforFR_2017/TT.root Histo/HistoforFR_2017/TTToHadronic.root Histo/HistoforFR_2017/TTToSemiLeptonic.root Histo/HistoforFR_2017/TTTo2L2Nu.root
hadd -f Histo/HistoforFR_2017/MC.root Histo/HistoforFR_2017/DY.root Histo/HistoforFR_2017/ST.root Histo/HistoforFR_2017/VV.root Histo/HistoforFR_2017/TT.root Histo/HistoforFR_2017/GGToElEl.root Histo/HistoforFR_2017/GGToWW.root 
python3 Gethisto_FR.py 2017 TauB
python3 Gethisto_FR.py 2017 TauC
python3 Gethisto_FR.py 2017 TauD
python3 Gethisto_FR.py 2017 TauE
python3 Gethisto_FR.py 2017 TauF
hadd -f Histo/HistoforFR_2017/Tau.root Histo/HistoforFR_2017/TauB.root Histo/HistoforFR_2017/TauC.root Histo/HistoforFR_2017/TauD.root Histo/HistoforFR_2017/TauE.root Histo/HistoforFR_2017/TauF.root
python3 CreateFRhist.py --year 2017
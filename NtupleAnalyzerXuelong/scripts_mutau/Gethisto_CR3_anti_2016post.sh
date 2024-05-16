python3 Gethisto_CR3_anti.py 2016post DY ZTT
python3 Gethisto_CR3_anti.py 2016post DY ZLL
python3 Gethisto_CR3_anti.py 2016post ST_t_top ST
python3 Gethisto_CR3_anti.py 2016post ST_t_antitop ST
python3 Gethisto_CR3_anti.py 2016post ST_tW_top ST
python3 Gethisto_CR3_anti.py 2016post ST_tW_antitop ST
hadd -f Histo/HistoCR3_anti_2016post/ST.root Histo/HistoCR3_anti_2016post/ST_t_top.root Histo/HistoCR3_anti_2016post/ST_t_antitop.root Histo/HistoCR3_anti_2016post/ST_tW_top.root Histo/HistoCR3_anti_2016post/ST_tW_antitop.root 
python3 Gethisto_CR3_anti.py 2016post WZ2Q2L VV
python3 Gethisto_CR3_anti.py 2016post WZ3LNu VV
python3 Gethisto_CR3_anti.py 2016post VV2L2Nu VV
python3 Gethisto_CR3_anti.py 2016post ZZ2Q2L VV
python3 Gethisto_CR3_anti.py 2016post ZZ4L VV
hadd -f Histo/HistoCR3_anti_2016post/VV.root Histo/HistoCR3_anti_2016post/WZ2Q2L.root Histo/HistoCR3_anti_2016post/WZ3LNu.root Histo/HistoCR3_anti_2016post/VV2L2Nu.root Histo/HistoCR3_anti_2016post/ZZ2Q2L.root Histo/HistoCR3_anti_2016post/ZZ4L.root
python3 Gethisto_CR3_anti.py 2016post TTTo2L2Nu TT
python3 Gethisto_CR3_anti.py 2016post TTToHadronic TT
python3 Gethisto_CR3_anti.py 2016post TTToSemiLeptonic TT
hadd -f Histo/HistoCR3_anti_2016post/TT.root Histo/HistoCR3_anti_2016post/TTToHadronic.root Histo/HistoCR3_anti_2016post/TTToSemiLeptonic.root Histo/HistoCR3_anti_2016post/TTTo2L2Nu.root
python3 Gethisto_CR3_anti.py 2016post SingleMuonF data_obs
python3 Gethisto_CR3_anti.py 2016post SingleMuonG data_obs
python3 Gethisto_CR3_anti.py 2016post SingleMuonH data_obs
hadd -f Histo/HistoCR3_anti_2016post/SingleMuon.root Histo/HistoCR3_anti_2016post/SingleMuonF.root Histo/HistoCR3_anti_2016post/SingleMuonG.root Histo/HistoCR3_anti_2016post/SingleMuonH.root
python3 Create_fake_CR3.py --year 2016post

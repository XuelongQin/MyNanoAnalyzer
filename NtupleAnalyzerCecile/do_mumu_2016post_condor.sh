condor_submit submission_mumu_SingleMuonF2016post.sub
condor_submit submission_mumu_SingleMuonG2016post.sub
condor_submit submission_mumu_SingleMuonH2016post.sub
condor_submit submission_mumu_DY2016post.sub
##condor_submit submission_mumu_TT.sub
##condor_submit submission_mumu_WW.sub

hadd -f output_mumu_2016post/SingleMuonF.root output_mumu_2016post/SingleMuonF0.root output_mumu_2016post/SingleMuonF1.root output_mumu_2016post/SingleMuonF2.root output_mumu_2016post/SingleMuonF3.root output_mumu_2016post/SingleMuonF4.root output_mumu_2016post/SingleMuonF5.root output_mumu_2016post/SingleMuonF6.root output_mumu_2016post/SingleMuonF7.root output_mumu_2016post/SingleMuonF8.root output_mumu_2016post/SingleMuonF9.root
hadd -f output_mumu_2016post/SingleMuonG.root output_mumu_2016post/SingleMuonG0.root output_mumu_2016post/SingleMuonG1.root output_mumu_2016post/SingleMuonG2.root output_mumu_2016post/SingleMuonG3.root output_mumu_2016post/SingleMuonG4.root output_mumu_2016post/SingleMuonG5.root output_mumu_2016post/SingleMuonG6.root output_mumu_2016post/SingleMuonG7.root output_mumu_2016post/SingleMuonG8.root output_mumu_2016post/SingleMuonG9.root
hadd -f output_mumu_2016post/SingleMuonH.root output_mumu_2016post/SingleMuonH0.root output_mumu_2016post/SingleMuonH1.root output_mumu_2016post/SingleMuonH2.root output_mumu_2016post/SingleMuonH3.root output_mumu_2016post/SingleMuonH4.root output_mumu_2016post/SingleMuonH5.root output_mumu_2016post/SingleMuonH6.root output_mumu_2016post/SingleMuonH7.root output_mumu_2016post/SingleMuonH8.root output_mumu_2016post/SingleMuonH9.root
hadd -f output_mumu_2016post/Data.root output_mumu_2016post/SingleMuonF.root output_mumu_2016post/SingleMuonG.root output_mumu_2016post/SingleMuonH.root
hadd -f output_mumu_2016post/DY.root output_mumu_2016post/DY0.root output_mumu_2016post/DY1.root output_mumu_2016post/DY2.root output_mumu_2016post/DY3.root output_mumu_2016post/DY4.root output_mumu_2016post/DY5.root output_mumu_2016post/DY6.root output_mumu_2016post/DY7.root output_mumu_2016post/DY8.root output_mumu_2016post/DY9.root
###python Create_fake_mumu.py --year=2016post
###hadd -f datacard_mumu_2016post.root output_mumu_2016post/Fake.root output_mumu_2016post/TTTo2L2Nu.root output_mumu_2016post/WW2L2Nu.root output_mumu_2016post/Data.root output_mumu_2016post/DY.root


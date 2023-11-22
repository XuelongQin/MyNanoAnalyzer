#!/usr/bin/env python
import os
import sys
import optparse
import shutil
import random
import glob
from MyNanoAnalyzer.TauG2.EraConfig_Xuelong import *


def buildCondorFile(opt,FarmDirectory):

    """ builds the condor file to submit the ntuplizer """

    cmssw=os.environ['CMSSW_BASE']
    rand='{:03d}'.format(random.randint(0,123456))

    datasets=open(opt.input).read().splitlines()

    #condor submission file
    condorFile='%s/condor_generator_%s.sub'%(FarmDirectory,rand)
    print('Writes: %s'%condorFile)
    with open (condorFile,'w') as condor:
        condor.write('executable = {0}/worker_{1}.sh\n'.format(FarmDirectory,rand))
        condor.write('output     = {0}/output{1}.out\n'.format(FarmDirectory,rand))
        condor.write('error      = {0}/output{1}.err\n'.format(FarmDirectory,rand))
        condor.write('log        = {0}/output{1}.log\n'.format(FarmDirectory,rand))
        condor.write('max_retries = 5\n')
        #condor.write('retry_until = 0')
        condor.write('+JobFlavour = "tomorrow"\n')
        condor.write('+AccountingGroup = "group_u_CMST3.all"\n')
        OpSysAndVer = str(os.system('cat /etc/redhat-release'))
        if 'SLC' in OpSysAndVer:
            OpSysAndVer = "SLCern6"
        else:
            OpSysAndVer = "CentOS7"
        condor.write('requirements = (OpSysAndVer =?= "{0}")\n\n'.format(OpSysAndVer))
        condor.write('should_transfer_files = YES\n')
        condor.write('transfer_input_files = %s\n\n'%os.environ['X509_USER_PROXY'])
        for dataset in datasets:
          if "#" in dataset or len(dataset)<2: continue
          print('INFO: Processing %s'%(dataset))
          sufix=''
          prefix=''
          year='2018'

          if 'Run20' in dataset:
            print ('haha')
            dataset_name = '_'.join(dataset.split('/')[1:3])
            dataset_name = dataset.split('/')[10]+"_"+dataset.split('/')[12]
            year=dataset.split('UL')[1][:4]
            if 'UL1' in dataset:
              year="20"+str(dataset.split('UL')[1][:2])
              print ('year = ', year)
            sufix='data'
            cmd='dasgoclient --query=\"file dataset={} status=*\"'.format(dataset)
            #file_list=os.popen(cmd).read().split()
            file_list=glob.glob(dataset+'/*.root')
            print dataset_name
            #prefix='root://cms-xrd-global.cern.ch/'
          elif 'eos' in dataset.split('/'):
            sufix='mc'
            #dataset_name = dataset.split('/')[-1]
            dataset_name = dataset.split('/')[9]+"_"+dataset.split('/')[12]
            #if "RunII" in dataset.split('/')[9]:
              #dataset_name = dataset.split('/')[10]+"_"+dataset.split('/')[12]
            print "name: ",dataset_name
            if 'UL1' in dataset:
              year="20"+str(dataset.split('UL')[1][:2])
              print ('year = ', year)
            if "TauTau" not in dataset.split('/') and ("SingleMuon" in dataset.split('/') or "EGamma" in dataset.split('/') or "MuonEG" in dataset.split('/') or "Tau" in dataset.split('/') or "SingleElectron" in dataset.split('/')): 
              dataset_name = dataset.split('/')[9]+"_"+dataset.split('/')[10]+"_"+dataset.split('/')[12]
            file_list=glob.glob(dataset+'/*.root')
            print dataset_name
          else:
            print('ERROR: found invalid dataset = ',dataset,'stop the code')
            sys.exit(1)
          if 'Tau' not in dataset and "SingleMuon" not in dataset and "EGamma" not in dataset and "MuonEG" not in dataset and "DoubleMuon" not in dataset and "SingleElectron" not in dataset:
            sufix='mc'
          elif 'TauTau' in dataset:
            sufix='mc'
          else:
            sufix='data'
          channels=['tautau'] #EDIT THIS (could be ee,emu,etau,mumu,mutau,tautau)
          print ('sufix = ', sufix)

          yearmodified=year
          
          #if "preVFP" in dataset and year=="2016" and sufix=="mc":
          #   yearmodified="2016pre"
          #if "preVFP" not in dataset and year=="2016" and sufix=="mc":
          #   yearmodified="2016post"
          if "2016pre" in opt.input and sufix=="mc":
            yearmodified="2016pre"
          if "2016post" in opt.input and sufix=="mc":
            yearmodified="2016post"
          
            
          #prepare output
          output=opt.output+'/'+dataset_name

          for channel in channels:
            output_full=output+"_"+channel
            # apply filter to data: trigger and GRL
            #filter=ANALYSISCUT[year][channel]
            filter = ""
            if sufix=='mc':
              filter = ANALYSISMCCUT[year][channel]
            else:
              filter = ANALYSISDATACUT[year][channel]
            print year
            print ("filter is ", filter)
            os.system('mkdir -p {}'.format(output_full))
            for file in file_list:

              outfile='%s/%s'%(output_full,os.path.basename(file).replace('.root','_Skim.root'))
              if os.path.isfile(outfile) and not opt.force: continue

              condor.write('arguments = %s %s %s %s\n'%(prefix+file,'analysis_'+channel+sufix+yearmodified,output_full,filter))
              condor.write('queue 1\n')


    workerFile='%s/worker_%s.sh'%(FarmDirectory,rand)
    with open(workerFile,'w') as worker:
        worker.write('#!/bin/bash\n')
        worker.write('startMsg="Job started on "`date`\n')
        worker.write('echo $startMsg\n')
        worker.write('export HOME=%s\n'%os.environ['HOME']) #otherwise, 'dasgoclient' won't work on condor
        worker.write('export X509_USER_PROXY=%s\n'%os.environ['X509_USER_PROXY'])
        worker.write('########### INPUT SETTINGS ###########\n')
        worker.write('input=${1}\n')
        worker.write('channel=${2}\n')
        worker.write('output=${3}\n')
        worker.write('filter=${@:4}\n')
        worker.write('filename=`echo ${1} | rev | cut -d"/" -f1 | rev | cut -d"." -f1`\n')
        worker.write('######################################\n')
        worker.write('echo "worker_%s.sh arguments:"\n'%(rand))
        worker.write('echo input="$input"\necho channel="$channel"\necho output="$output"\necho filter="$filter"\n')
        worker.write('######################################\n')
        worker.write('WORKDIR=/tmp/%s/${filename}; mkdir -pv $WORKDIR\n'%os.environ['USER'])
        worker.write('echo "Working directory is ${WORKDIR}"\n')
        worker.write('cd %s\n'%cmssw)
        worker.write('eval `scram r -sh`\n')
        worker.write('cd ${WORKDIR}\n')
        worker.write('echo "INFO: Run ntuplizer"\n')
        worker.write('echo "python $CMSSW_BASE/src/PhysicsTools/NanoAODTools/scripts/nano_postproc.py \\\\"\n')
        worker.write('echo "$filename ${input}  \\\\"\n')
        worker.write('echo "--bi $CMSSW_BASE/src/MyNanoAnalyzer/TauG2/scripts/keep_in.txt   \\\\"\n')
        if channels[0]=="mumu": worker.write('echo "--bo $CMSSW_BASE/src/MyNanoAnalyzer/TauG2/scripts/keep_out_mumu.txt  \\\\"\n')
        elif channels[0]=="etau": worker.write('echo "--bo $CMSSW_BASE/src/MyNanoAnalyzer/TauG2/scripts/keep_out_etau.txt  \\\\"\n')
        elif channels[0]=="mutau": worker.write('echo "--bo $CMSSW_BASE/src/MyNanoAnalyzer/TauG2/scripts/keep_out_mutau.txt  \\\\"\n')
        elif channels[0]=="emu": worker.write('echo "--bo $CMSSW_BASE/src/MyNanoAnalyzer/TauG2/scripts/keep_out_emu.txt  \\\\"\n')
        elif channels[0]=="tautau": worker.write('echo "--bo $CMSSW_BASE/src/MyNanoAnalyzer/TauG2/scripts/keep_out_tautau.txt  \\\\"\n')
        else: worker.write('echo "--bo $CMSSW_BASE/src/MyNanoAnalyzer/TauG2/scripts/keep_out.txt  \\\\"\n')
        worker.write('echo "${filter} -I MyNanoAnalyzer.TauG2.TauG2_analysis_Xuelong ${channel} "\n')
        worker.write('python $CMSSW_BASE/src/PhysicsTools/NanoAODTools/scripts/nano_postproc.py \\\n')
        worker.write('$filename ${input}  \\\n')
        worker.write('--bi $CMSSW_BASE/src/MyNanoAnalyzer/TauG2/scripts/keep_in.txt   \\\n')
        if channels[0]=="mumu": worker.write('--bo $CMSSW_BASE/src/MyNanoAnalyzer/TauG2/scripts/keep_out_mumu.txt  \\\n')
        elif channels[0]=="etau": worker.write('--bo $CMSSW_BASE/src/MyNanoAnalyzer/TauG2/scripts/keep_out_etau.txt  \\\n')
        elif channels[0]=="mutau": worker.write('--bo $CMSSW_BASE/src/MyNanoAnalyzer/TauG2/scripts/keep_out_mutau.txt  \\\n')
        elif channels[0]=="emu": worker.write('--bo $CMSSW_BASE/src/MyNanoAnalyzer/TauG2/scripts/keep_out_emu.txt  \\\n')
        elif channels[0]=="tautau": worker.write('--bo $CMSSW_BASE/src/MyNanoAnalyzer/TauG2/scripts/keep_out_tautau.txt  \\\n')
        else: worker.write('--bo $CMSSW_BASE/src/MyNanoAnalyzer/TauG2/scripts/keep_out.txt  \\\n')
        worker.write('${filter} -I MyNanoAnalyzer.TauG2.TauG2_analysis_Xuelong ${channel} \n')
        worker.write('echo cp ${filename}/${filename}_Skim.root ${output}/${filename}_Skim.root\n')
        worker.write('cp ${filename}/${filename}_Skim.root ${output}/\n')
        worker.write('\necho clean output\ncd ../\nrm -rf ${WORKDIR}\n')
        worker.write('echo ls; ls -l $PWD\n')
        worker.write('echo $startMsg\n')
        worker.write('echo job finished on `date`\n')
    os.system('chmod u+x %s'%(workerFile))

    return condorFile

def main():

    if not os.environ.get('CMSSW_BASE'):
      print('ERROR: CMSSW not set')
      sys.exit(0)
    
    cmssw=os.environ['CMSSW_BASE']

    #configuration
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    #parser.add_option('-i', '--in',     dest='input',  help='list of input datasets',    default='reNanoAODTau2016post.txt', type='string')
    parser.add_option('-i', '--in',     dest='input',  help='list of input datasets',    default='reNanoAODMC2016post_DY.txt', type='string')
    #parser.add_option('-o', '--out',      dest='output',   help='output directory',  default='/eos/cms/store/user/ccaillol/TauG2/ntuples_mumu_2018', type='string') #EDIT THIS
    parser.add_option('-o', '--out',      dest='output',   help='output directory',  default='/eos/cms/store/group/cmst3/group/taug2/AnalysisXuelong/ntuples_tautau_2016post', type='string') #EDIT THIS
    parser.add_option('-f', '--force',      dest='force',   help='force resubmission',  action='store_true')
    parser.add_option('-s', '--submit',   dest='submit',   help='submit jobs',       action='store_true')
    (opt, args) = parser.parse_args()
     
    if not os.path.isfile(opt.input): 
      print('ERROR: bad input file (%s)'%opt.input)
      sys.exit(1)

    #prepare directory with scripts
    FarmDirectory=os.environ['PWD']+'/FarmLocalNtuple'
    if not os.path.exists(FarmDirectory):  os.system('mkdir -vp '+FarmDirectory)
    print('\nINFO: IMPORTANT MESSAGE: RUN THE FOLLOWING SEQUENCE:')
    print('voms-proxy-init --voms cms --valid 72:00 --out %s/myproxy509\n'%FarmDirectory)
    os.environ['X509_USER_PROXY']='%s/myproxy509'%FarmDirectory

    #build condor submission script and launch jobs
    condor_script=buildCondorFile(opt,FarmDirectory)

    #submit to condor
    if opt.submit:
        os.system('condor_submit {}'.format(condor_script))
    else:
        print('condor_submit {}\n'.format(condor_script))
		

if __name__ == "__main__":
    sys.exit(main())

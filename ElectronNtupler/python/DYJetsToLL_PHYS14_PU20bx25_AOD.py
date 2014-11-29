import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/00CC714A-F86B-E411-B99A-0025904B5FB8.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/040D9AF7-FB6B-E411-8106-0025907DBA06.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/04442001-036C-E411-9C90-0025901D42C0.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/08501832-106C-E411-BCEE-0025904B1420.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/0AA8983B-046C-E411-B0D3-0025901D4C3E.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/0C924143-0D6C-E411-B48A-0025907BAF70.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/0CB30B20-186C-E411-A85E-002590AC4BF6.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/0CF38497-006C-E411-A713-0025907DCA0C.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/0E2BE86D-1E6C-E411-9FD4-003048D4DEAE.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/0E50D3F3-056C-E411-8DF6-0025907DCA7E.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/1018A829-046C-E411-B9CC-003048F0E1AC.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/106A192C-F36B-E411-A881-00266CFFA5C4.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/129CB285-EA6B-E411-9E8B-002481E7636A.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/12A2B90A-FE6B-E411-9815-003048F0E526.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/14C90B98-1D6C-E411-A7CC-00266CF1074C.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/183160F9-F66B-E411-B043-002590AC4B54.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/1869A139-E86B-E411-8676-003048D439C6.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/1ED08A31-176C-E411-9B49-00266CF327C4.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/1EF561A5-1F6C-E411-AE5E-002590DB9286.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/20498159-E76B-E411-98C3-002481E1070E.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/26523C4D-016C-E411-92D3-00215AD4D6C8.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/265C9EF8-706C-E411-B853-0025901D4940.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/2671AAB9-F36B-E411-82DA-00266CFFA3EC.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/2AA42B49-E36B-E411-AB0E-0025907DC9D0.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/300F8579-296C-E411-AFCC-0025907DC9D2.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/34693E6F-F96B-E411-940F-0025907DC9D6.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/34D157FE-066C-E411-8E1F-003048D3C7DC.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/36224C8F-E86B-E411-B2E0-00266CFFA780.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/364C6158-1C6C-E411-8437-002590AC5082.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/36C90B71-136C-E411-935B-002590DB92C4.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/38763351-166C-E411-A924-002481E10D3E.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/3A050F7A-086C-E411-8CEF-002590DB9298.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/3A3D73F2-0C6C-E411-8F5B-0025907DC9B0.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/3A3F41DE-E76B-E411-A2C6-0025907DCA9C.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/3AB930E2-296C-E411-8C2E-00266CFFA604.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/40F92A4D-E36B-E411-B925-00266CF327E0.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/44711C19-186C-E411-85C9-0025907DCA72.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/447DD69D-1D6C-E411-8719-00266CF3338C.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/4A3DA57E-FD6B-E411-BEE9-0025904B1026.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/4C4AC53B-3E6C-E411-A4DE-00237DE0BED6.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/4CB288A2-ED6B-E411-A147-003048F02CB2.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/4CB38FFE-156C-E411-8018-002590DB9286.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/4E1AD1B0-EB6B-E411-835E-003048D43958.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/4E1C8AAA-276C-E411-BB3F-002590DB040C.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/4EE59D95-E76B-E411-937C-002590AC5060.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/4EEC1EEC-FE6B-E411-822A-002590AC504A.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/4EFD08E5-E76B-E411-A92E-002590DB9358.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/5AD9F69F-F76B-E411-982F-0025901D4A58.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/5E347D12-096C-E411-995E-002590A8DC50.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/5E355D80-1E6C-E411-8FAD-002590DB9214.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/5E664C9F-116C-E411-92CF-0025901D4B4C.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/62AD1887-126C-E411-8810-002590DB921C.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/64FD45D6-EE6B-E411-B3E8-002590DB918A.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/6617C8E6-F96B-E411-8982-003048F0E828.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/68267244-F56B-E411-BCEC-002481E0D2E8.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/686F7B84-F46B-E411-8B8D-0025904B12E2.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/688D7D38-1B6C-E411-AA68-003048D437D2.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/6A177B98-276C-E411-95F9-002590DB9188.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/6A7EA970-EC6B-E411-A430-002590AC4C76.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/6E4A2394-ED6B-E411-921C-0025907FD2B2.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/6E69FE58-E36B-E411-B05E-002590AC4C66.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/7270BC46-276C-E411-8EB5-0025907DC9DC.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/72B7CA91-276C-E411-913B-00266CFFA120.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/7806F013-1C6C-E411-AB4C-002481E14F2A.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/7AFA3589-E36B-E411-A184-003048F02CB8.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/8834A861-146C-E411-8B9A-0025901D4B06.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/888BEB26-F16B-E411-AE01-003048F0E80C.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/88A13622-F96B-E411-A734-002481E1026A.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/8AA30AC3-1B6C-E411-9C6F-003048CF6336.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/8C5CEC13-FC6B-E411-8288-0025904B1370.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/946FC97C-F06B-E411-B5FE-00266CF2E2C8.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/985F434B-0E6C-E411-8A0D-002481E0D2E8.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/9CDC5A61-E76B-E411-83CE-0025901D4C32.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/A43CD519-F26B-E411-BDB9-00266CFFA6A8.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/A461813F-0A6C-E411-8F8F-002590DB0640.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/A4C01A3C-D46B-E411-B02B-002590DB9298.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/A4FFB8BD-106C-E411-B2A0-0025904B1424.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/A639575B-116C-E411-A0F8-0025907DCA0C.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/A89FEF05-1B6C-E411-B4B5-00266CF33340.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/A8DB4ABE-1B6C-E411-BE6F-00259081A2C8.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/AE5013A4-2E6C-E411-AF70-0025907DCA7E.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/B0FC8751-096C-E411-9A54-002590AC4C9E.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/B28B1790-276C-E411-98D7-002590DB9214.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/B290C4B4-146C-E411-B391-0025904B12A8.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/B60179D1-0A6C-E411-ADBF-0025901D493C.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/B850F23D-E36B-E411-8255-00266CFFA344.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/B8CEC9F7-F66B-E411-B592-002590AC4B5A.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/B8D6BF62-E36B-E411-8FA8-003048D43942.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/BA17EAD5-EE6B-E411-9235-002590AC4C76.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/BA349E8A-276C-E411-8BCE-00266CFFA750.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/BC96D1A4-076C-E411-8C00-00215AD4D6C8.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/BC9D6F72-EA6B-E411-86C9-002481E101DA.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/BCF4B414-E36B-E411-9620-003048F0E3AC.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/BE36EBF7-706C-E411-B674-0025901D4940.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/BEE5CB8E-276C-E411-A38C-00266CFFA148.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/C011054D-206C-E411-BFD5-00266CF2718C.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/C076C5D2-0B6C-E411-972E-00266CFFA1AC.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/C2D93175-156C-E411-8A87-002590DB9252.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/C60ED61B-FB6B-E411-9537-0025901D481E.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/C641D9B9-EF6B-E411-83EE-00266CF2AACC.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/C69E3498-2B6C-E411-BF78-003048D4DEA6.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/C89D578C-276C-E411-BC8E-00266CF32EB8.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/CE539C36-276C-E411-BD66-0025901D493E.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/CE543A2D-F16B-E411-BCA6-002590AC4FC8.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/D05DE651-016C-E411-AB9D-00266CFFA044.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/D2420C68-F26B-E411-8948-0025907DCAA6.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/D24EF49C-286C-E411-B96B-00266CF32F00.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/D29A24FC-FC6B-E411-80F5-003048D4397E.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/D2D935B9-F46B-E411-86A0-0025904B5FB8.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/D4049C56-E76B-E411-A858-0025907FD2D8.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/DAC98E2A-FB6B-E411-B3F2-00266CFFA678.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/DC927F5A-056C-E411-8443-002590DB9172.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/DCA282B4-E36B-E411-9A0C-0025904B1452.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/DEAEB786-416C-E411-9551-0025901D4940.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/E0B1D1A5-1C6C-E411-92B0-0025904B1372.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/E6840B4F-1F6C-E411-BB40-002590DB9196.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/EA877196-0B6C-E411-A6B6-0025907DCA0C.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/EAF37145-EB6B-E411-91FB-00266CFFA048.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/EC90CCF6-FE6B-E411-9EFF-0025907FD34C.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/EE34D409-436C-E411-BA53-0025901D4940.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/F07BB817-036C-E411-A449-00266CF32930.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/F2A6DA89-0F6C-E411-9069-002481E0D69C.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/F2FD3813-216C-E411-BFFD-0025901D4D54.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/F4CB1AE0-E86B-E411-9098-002590AC5076.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/F4F94750-0E6C-E411-B17B-002590DB9278.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/FA22903C-006C-E411-BD1C-002590A2CDA8.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/FC25FF33-176C-E411-A48F-0025901D4938.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/FE96B422-F66B-E411-BF01-00266CFFA3EC.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/02AF500F-1A6C-E411-9C69-002590AC4B5C.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/02E9CF6A-1E6C-E411-9F98-0025907DCA9C.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/0498C39E-E66B-E411-B0A4-00266CF326A8.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/06200CFA-1C6C-E411-AC23-002481E94C56.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/08266DC0-106C-E411-8D10-00259074B2BE.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/0C176FCB-186C-E411-8481-00266CF33054.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/128ECE3B-F96B-E411-8F56-002590AC5062.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/14DC18A1-086C-E411-B561-00266CFFA5C4.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/168268D7-DA6B-E411-A400-002590DB041E.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/182181F5-0C6C-E411-A54E-002590DB9166.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/1C31F7AA-316C-E411-968F-0025908325DC.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/1EB80493-1C6C-E411-86EB-00266CF422D8.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/1EFA864F-056C-E411-9BF8-002590AC5012.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/22D7F875-FA6B-E411-ADAE-00266CFFA038.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/24865249-E06B-E411-AA58-002590DB918C.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/24F89207-016C-E411-BF43-003048D439A8.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/26DE8703-0F6C-E411-9EA3-0025901D4B04.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/28B7EB66-EA6B-E411-824C-0025904B12FC.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/2A908DEF-DA6B-E411-8EF2-003048D43656.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/2C12EF8E-006C-E411-BDC6-003048D438EA.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/2E7735C1-1B6C-E411-BD08-0025907FD2DA.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/30436754-ED6B-E411-B3C7-00266CFFA630.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/32081CCB-226C-E411-A960-003048F0E82C.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/32B624ED-FE6B-E411-ACE3-00266CF327C4.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/3605EB78-FA6B-E411-BE4F-00266CFFB1F4.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/389FB2F3-FD6B-E411-950D-003048D438EA.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/3A1AAA7D-E66B-E411-B112-00266CFFA1AC.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/3A618A31-0B6C-E411-BD1F-003048F0E3AC.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/3A63C8E9-216C-E411-A39B-00266CF32EB8.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/3CB88818-FF6B-E411-8562-002590DB9152.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/4006F21C-F46B-E411-9793-003048F0E780.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/400A3DD3-DA6B-E411-B0F5-0025907BAD4A.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/42C97857-186C-E411-850B-002590DB9262.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/464A6A36-F06B-E411-B931-002590DB91E0.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/4655A4C5-076C-E411-93C8-0025907DC9F8.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/46F0C5D5-266C-E411-A1C4-00266CFFA7A8.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/481A0845-126C-E411-9C49-002590AC5074.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/4AFA763F-F96B-E411-A45F-002590DB92BE.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/5237DB96-0C6C-E411-B494-002481E0D6A6.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/52479658-FD6B-E411-B009-002590DB9358.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/52B95BBF-E66B-E411-BDCA-003048F0E3B4.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/541CAAEC-E76B-E411-8324-002590DB9166.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/5809AC99-516C-E411-BDA7-0025901D4940.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/5A66F1F7-F46B-E411-B1FE-002590DB928E.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/5EC14B5B-FB6B-E411-9C59-002590A7A2E0.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/60E54AA9-0A6C-E411-B41B-003048D3C7BC.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/621D6DB9-1B6C-E411-97CF-002590DB9152.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/669CBDDE-276C-E411-ACB9-003048F30422.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/6A066E61-E66B-E411-9231-003048F0E55A.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/6A78806B-FD6B-E411-8136-003048D462FE.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/6C10AC43-056C-E411-9D38-003048D4363C.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/6C318212-F46B-E411-83F7-00266CFFA2EC.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/6E66207A-F86B-E411-8304-0025901D4124.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/701EDDF5-F66B-E411-950D-002590DB91F0.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/76039513-046C-E411-B656-002481E14D72.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/76B9C078-176C-E411-809E-0025904B130E.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/76C27B55-266C-E411-BD85-0025907FD2B6.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/78688849-146C-E411-BF99-00266CF32CD0.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/78CCF28A-E66B-E411-B76B-002481E0EA06.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/78D652FD-096C-E411-A6EF-00266CFFA704.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/7A2D1E06-0F6C-E411-85A1-00266CF422D8.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/7A300C94-FE6B-E411-A0FC-0025901D4A0E.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/7A33D2D0-116C-E411-983D-002590AC4C9E.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/7CA47AAD-FB6B-E411-B40D-002590DB9152.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/7CDFEE1F-F86B-E411-858A-002590DB91CE.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/7E6EB077-206C-E411-991D-002590AC4C3E.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/804292C5-066C-E411-A61B-003048D4364C.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/80C0103D-016C-E411-97E0-003048D436EA.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/80EB083C-EE6B-E411-8F89-002590AC5082.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/848EB395-1F6C-E411-9D3C-00266CFFA204.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/849AA784-036C-E411-885B-00266CF270A8.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/849B463A-E06B-E411-B0DD-003048D43656.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/86004EEE-216C-E411-B791-002590494CB2.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/885FE11D-EF6B-E411-8582-0025907DC9BA.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/88EDF5CC-F26B-E411-8424-002590DB92BC.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/8C414F02-166C-E411-9561-002590AC4E28.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/8CEA6C84-EB6B-E411-9FB5-0025901D4B20.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/8CEBBADF-1D6C-E411-9AAB-00266CFFA68C.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/8E9C6686-EB6B-E411-8ADC-002590AC5082.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/90DD775E-F16B-E411-9698-002590AC4C3E.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/92140433-256C-E411-A74B-0025907FD4A0.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/967593F2-026C-E411-ABA6-002590DB9196.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/9A1721A8-F66B-E411-8909-002481E15176.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/9C5F8384-F06B-E411-A8C1-003048D373CC.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/9CD35893-1F6C-E411-9FBB-003048CEFFE4.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/A271DB33-126C-E411-9AC3-0025901D4D64.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/A2E739E9-236C-E411-8517-0025907DC9C4.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/A2F52941-146C-E411-AC18-00266CF327C4.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/A2F97678-136C-E411-A214-00266CFFA7C0.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/A4DC553A-F26B-E411-B9ED-003048D437EC.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/A6003E54-ED6B-E411-AB3E-002590AC4B54.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/ACA199CB-226C-E411-A24D-00266CFFA120.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/ACF270FF-206C-E411-914E-003048D4610C.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/B2B81C33-1B6C-E411-8C0C-002590DB9262.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/B2F98568-E66B-E411-9798-002590DB92C4.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/B4BB1E7F-1D6C-E411-A246-00266CFFA418.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/B89AAB3A-FC6B-E411-BB84-0025907DCA72.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/BCFF9F35-176C-E411-A367-002590DB041A.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/BE95A5BB-166C-E411-B886-00266CFFA6A8.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/C0118027-1B6C-E411-9B47-0025904B130E.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/C029E0A6-E76B-E411-914D-002590AC4C6C.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/C0E16C56-2A6C-E411-8C22-003048D437A0.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/C0E98332-256C-E411-9B60-00266CFFA5CC.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/C21ED44A-E06B-E411-8A04-00266CFB8D74.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/C4357A97-516C-E411-B146-0025901D4940.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/C8529BF5-FC6B-E411-81FE-002481E94BCA.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/CA693F53-236C-E411-A32D-002590DB91D2.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/CC13DFC6-186C-E411-85B2-003048D4397E.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/CC145F97-1C6C-E411-9D9B-002590DB91D2.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/CC495811-1A6C-E411-B6EC-0025907DC9C8.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/D2ADE031-026C-E411-AABE-003048D4DFB8.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/D4010F83-E66B-E411-AF74-00266CFF9FFC.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/D4834DB2-F16B-E411-81C9-002590A7A2E0.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/D62421C8-EC6B-E411-BFF2-002481E102C6.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/D6CEDCD9-336C-E411-A72B-002590DB91CE.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/D8B2567D-2B6C-E411-9A83-00266CF32920.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/DA2A76CB-E96B-E411-880D-002590AC5082.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/E0A8398F-066C-E411-8DF5-00266CF32BC4.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/E0FFAC67-E66B-E411-90B5-0025904B1426.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/E22C8279-F36B-E411-9081-00266CF32EAC.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/E2DD81CB-F56B-E411-A882-00266CF32BC4.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/E8BDAF82-E96B-E411-A863-0025901D4926.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/EA3DDAC7-106C-E411-B8E5-0025907DC9C6.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/EA8DE7FF-206C-E411-9F89-002481E0D708.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/ECE59075-206C-E411-B558-002590AC4CA6.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/EE4DFCF5-E86B-E411-8ED7-002590DB9216.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/F0B206D3-EA6B-E411-B974-002590DB92A8.root' ] );
readFiles.extend( [

       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/F2E0DC67-0E6C-E411-B13C-002590AC5074.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/F40E1F64-E66B-E411-A0DA-0025907BAF70.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/F4C96EE3-F76B-E411-B697-002590494C92.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/F6C7F514-EF6B-E411-A3DD-0025907FD2B6.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/F8ACAA0D-F16B-E411-8990-0025901D4124.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/FC35A3EC-F56B-E411-8A3B-002590DB9232.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/FCE844C7-116C-E411-A2FE-0025904B130E.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/FE1E5050-0E6C-E411-AE08-0025904B1420.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/FE70F174-1E6C-E411-A2CD-002590A52B4A.root',
       '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/10000/FEF640DD-086C-E411-A742-00266CF32EAC.root' ] );


secFiles.extend( [
               ] )


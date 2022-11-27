# BioradReport

python version 3.8

- jupyter notebook kernel

  ```
  $ python -m ipykernel install --user --name=myenv
  ```

## 功能說明：

1. PrintOut_StatReportForExport.xml 匯出成 ALL.XLXS 檔
1. 檢查 QC 結果 `check_qc()`
1. 匯出 IH-500 QC 結果 (排除 QC 失敗) 為 IH500.HTML 及 QC.XLXS 檔
1. 匯出 IH-500 DC-screening II QC 結果 (排除 QC 失敗) 為 DC_SCREENING.HTML 檔
1. 統計全部、每日 LIQ rate 


## 使用方式

1. IH-COM/Report 掛載
1. 至 IH-COM 匯出資料： Print > statistics > ReportForExport
1. 執行本腳本
1. 在印表機資料夾產生三個檔：
    - LIQ： 統計每日 LIQ rate
    - QC： 所有 QC 結果 (排除 QC 失敗)
    - ALL：PrintOut_StatReportForExport.xml 資料
1. 在本腳本之資料夾產生兩個檔：列印以下檔案，組長簽閱後歸檔
    - IH500.HTML: IH-500 QC 結果
    - DC_SCREENING.HTML: IH-500 DC-screening II QC 結果
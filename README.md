# 資安產業研究入門 LLM Wiki

**主題：資安公司到底在保護什麼？從企業風險認識 CRWD、OKTA 與 PANW。**

本專案延續資安產業研究入門百科，以初學者為對象，從釣魚郵件情境出發，介紹端點防護、身分管理、網路安全與零信任，再認識公司的代表性產品視角及營收、ARR、自由現金流等指標。先閱讀並 ingest 八篇官方資料，整理摘要、日期、段落定位與使用限制，形成六篇 Wiki，再製作十八頁教學 HTML 簡報。

## 作業成果入口

- [LLM Wiki：六篇概念條目](wiki/README.md)
- [八篇資料來源與 ingest 筆記](intake/sources.json)
- [教學 HTML 簡報](index.html)：下載後用瀏覽器開啟；包含 Wiki 搜尋、測驗、講者備註與來源回查。
- [Loop / graph 流程說明](workflow.md)
- [初版實際執行紀錄](runs/baseline.json)／[修正版實際執行紀錄](runs/improved.json)
- [結構檢查紀錄](runs/validation.json)
- [實際執行反思](reflection.md)
- [專案與每季財務更新規則](AGENTS.md)

作者：江驊恩。資料檢查日：2026-11-24。

## 資料取得、整理與生成

先討論主題與受眾，再取得資料並生成。來源包括 NIST、CISA、CrowdStrike、Okta 與 Palo Alto Networks 的官方資料。原文已在本次研究對話中開啟閱讀，公開專案只保留自行整理的簡短摘要，不轉載完整原文。

LLM 在研究對話中負責摘要、整合、語意核對與教學編排；Python 負責索引、規則檢索、結構檢查與 HTML 生成。程式沒有自動呼叫 LLM API，也沒有向量資料庫。

## 實際執行與反思

同一份 Wiki、固定六題中文自然語言問題：初版只以空白切詞，六題皆未命中；改版加入概念標籤與同義詞後，六題第一筆結果皆符合人工指定的預期條目，無結果降為零。預期條目是測試設計時指定，不代表本次有獨立人工專家審核。

最常觀察到的問題在檢索節點，因此新增「問題正規化」，把「證據命中檢查」放在教學編排之前。未命中先補 Wiki 或來源，不直接生成缺少證據的段落。小樣本結果不能代表一般語意能力，也沒有量測 LLM 幻覺率。

已做引用、來源欄位、HTML 結構與 JavaScript 語法檢查；未做真實瀏覽器測試。財務資料不會自動更新。

## 瀏覽簡報與 GitHub Pages

下載 [index.html](index.html) 後即可離線使用，無須安裝套件或提供 API key。左右方向鍵換頁、Home／End 跳首尾；上方可切換 Wiki、工作流程與反思。「列印簡報」可透過瀏覽器輸出 PDF；原始資料外連需要網路。

本儲存庫已提供根目錄 index.html 與 .nojekyll，適合 GitHub Pages 的 branch 部署。若尚未啟用，可在 Settings → Pages 選擇 Deploy from a branch、main、/ (root)。設定完成後，預期網址為 https://howardchiang0129.github.io/LLMWiki/ 。此網址僅為預期路徑，README 不代表已驗證部署。

## 重現

需要 Python 3.9+，無額外 Python 依賴：

```sh
python3 scripts/seed.py
python3 scripts/workflow.py --mode baseline
python3 scripts/workflow.py --mode improved
python3 scripts/build.py
python3 scripts/check.py
node --check dist/deck.js
```

seed.py 是本次 LLM 閱讀整理後的輸入快照，不會重新下載來源。重跑會覆寫示範 runs；正式更新前請另存歷史紀錄。根目錄 index.html 與 dist/index.html 應維持一致。

## 前期專案

- [資安產業研究入門百科](https://howardchiang0129.github.io/cybersecurity-research-wiki/)
- [前期 GitHub repository](https://github.com/howardchiang0129/cybersecurity-research-wiki)

本專案為獨立延伸，保留前期網站。

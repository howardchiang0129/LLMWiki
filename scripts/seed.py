"""Curated LLM research output. Run once to reproduce the reviewed input notes."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sources=[
('S01','NIST Cybersecurity Framework 2.0 發布說明','NIST','2024-02-26','https://www.nist.gov/news-events/news/2024/02/nist-releases-version-20-landmark-cybersecurity-framework','六項核心功能','政府概念指引','CSF 2.0 適用於各種規模與產業的組織。Govern、Identify、Protect、Detect、Respond、Recover 六項功能，提供管理資安風險的共同語言。','六項功能可以並行；不能當成依序完成就能保證安全的清單。',['治理','風險','框架','CSF']),
('S02','Zero Trust Architecture，SP 800-207','NIST','2020-08-10','https://www.nist.gov/publications/zero-trust-architecture','Abstract','政府技術指引','零信任不因網路位置或設備所有權而給予隱含信任。存取資源前應驗證與授權，保護重點包括使用者、資產與資源。','零信任是架構原則，不是單一產品；不代表拒絕所有存取。',['零信任','信任','存取','授權','Zero Trust']),
('S03','Implementing Phishing-Resistant MFA','CISA','2022-10','https://www.cisa.gov/sites/default/files/publications/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf','第 1–3 頁，MFA 與 FIDO/WebAuthn','政府實務指引','MFA 結合不同類型的驗證因素，例如知道的秘密與持有的裝置。並非所有 MFA 都同樣能抵抗釣魚；CISA 建議採用抗釣魚的驗證方式。','MFA 降低帳密風險，不能取代裝置、權限與事件應變措施。',['MFA','驗證','釣魚','帳密']),
('S04','What is EDR? Endpoint Detection & Response Defined','CrowdStrike',None,'https://www.crowdstrike.com/en-us/cybersecurity-101/endpoint-security/endpoint-detection-and-response-edr/','EDR 定義與核心功能','供應商概念說明','EDR 透過蒐集端點活動、偵測可疑行為與支援調查及回應，協助處理電腦等裝置上的威脅。','供應商教學文件不構成獨立產品評測；偵測與回應不等於保證阻擋所有攻擊。',['端點','電腦','裝置','EDR','Endpoint']),
('S05','Identity and Access Management overview','Okta Developer',None,'https://developer.okta.com/docs/concepts/iam-overview/','IAM overview，Workforce 與 Customer Identity','供應商技術文件','IAM 管理身分與資源存取；員工身分與顧客身分有不同使用情境。身分驗證確認使用者身分，授權決定允許的行動；MFA 可強化登入。','登入成功不代表擁有所有權限；企業授權設計仍須依角色與資源需求決定。',['身分','帳號','IAM','SSO','授權','登入']),
('S06','App-ID Overview','Palo Alto Networks',None,'https://docs.paloaltonetworks.com/ngfw/administration/app-id/app-id-overview','App-ID 運作與加密流量條件','供應商技術文件','App-ID 使用簽章、協定解碼及啟發式方法辨識應用程式流量，協助依應用程式執行政策。文件說明 SSL／SSH 解密取決於是否配置相應解密政策。','不能宣稱能無條件解開所有加密流量；技術能力與實際部署政策須分開。',['網路','流量','防火牆','NGFW','App-ID']),
('S07','Palo Alto Networks Fiscal Q1 2027 Financial Results','Palo Alto Networks IR','2026-11-18','https://investors.paloaltonetworks.com/news-releases/news-release-details/palo-alto-networks-reports-fiscal-first-quarter-2027-financial','財務摘要與 Next-Generation Security ARR 定義','公司公布數據','FY2027 Q1 截至 2026-10-31，營收為 34.4 億美元，NGS ARR 為 97.3 億美元。NGS ARR 以期末有效合約的年化分配收入為基礎，排除硬體、舊有附加訂閱及支援與專業服務等項目。','NGS ARR 的產品涵蓋範圍不同於其他公司的 ARR；不能直接視為相同口徑。',['財報','營收','PANW','ARR','NGS ARR']),
('S08','CrowdStrike Second Quarter Fiscal 2027 Financial Results','CrowdStrike IR','2026-08-26','https://ir.crowdstrike.com/news-releases/news-release-details/crowdstrike-reports-second-quarter-fiscal-year-2027-financial','財務摘要、ARR、現金流','公司公布數據','FY2027 Q2 截至 2026-07-31，營收為 14.7 億美元，期末 ARR 為 58.4 億美元；營運現金流為 5.303 億美元，自由現金流為 3.774 億美元。','ARR 為期末年化經常性指標，營收與自由現金流是期間數值；不同公司計算方式須另行核對。',['財報','營收','CRWD','ARR','現金流'])
]
out=[]
for sid,title,pub,date,url,section,kind,note,caveat,tags in sources:
    d=dict(id=sid,title=title,publisher=pub,published=date,url=url,locator=section,kind=kind,summary=note,caveat=caveat,tags=tags,retrieved='2026-11-24',method='本次對話開啟官方原始來源，由 LLM 摘要並由 LLM 依規則檢查；不重製全文。')
    out.append(d)
    (ROOT/'intake'/f'{sid}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
(ROOT/'intake'/'sources.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')

entries=[
('risk','企業風險與 CSF','企業資安從要保護的資產與營運風險出發。治理、識別、保護、偵測、回應與復原是相互支援的功能。',['S01'],['風險','治理','框架','CSF','企業']),
('endpoint','端點與 EDR','端點是工作用電腦等裝置。EDR 觀察活動、偵測異常，支援調查與處置；偵測能力與實際處置效果須分別評估。',['S04'],['端點','電腦','裝置','EDR','Endpoint']),
('identity','身分、IAM 與 MFA','身分驗證問「你是誰」，授權問「你能做什麼」。MFA 結合不同因素；抗釣魚驗證能降低特定攻擊風險，但不等於完整資安。',['S05','S03'],['身分','帳號','登入','驗證','授權','IAM','MFA','釣魚']),
('network','網路防護與應用辨識','網路防護關注連線與應用流量是否符合政策。App-ID 是辨識應用的技術範例；檢視加密內容還取決於解密政策等部署條件。',['S06'],['網路','連線','流量','防火牆','App-ID','NGFW']),
('zero-trust','零信任與多層防護','網路內部不自動等於可信。存取決策應考慮身分、資源與情境。端點、身分與網路是理解防護的三個切入點，並不是完整分類，也不是互斥市場。',['S02','S04','S05','S06'],['零信任','多層','存取','信任','架構']),
('metrics','從公司產品到財報指標','營收觀察期間認列的業務規模；ARR 觀察期末年化經常性業務，但依公司定義。自由現金流觀察營運產生現金扣除特定資本支出後的情況，仍須查原始定義。PANW 的 NGS ARR 與 CRWD 的 ARR 不宜直接當作同口徑規模排名。',['S07','S08'],['財報','公司','營收','ARR','季度','現金流','PANW','CRWD'])
]
wiki=[]
for slug,title,body,refs,tags in entries:
    d=dict(id=slug,title=title,body=body,sources=refs,tags=tags)
    wiki.append(d)
    (ROOT/'wiki'/f'{slug}.md').write_text('# '+title+'\n\n'+body+'\n\n來源：'+', '.join(refs)+'\n')
(ROOT/'wiki'/'entries.json').write_text(json.dumps(wiki,ensure_ascii=False,indent=2)+'\n')
print('已寫入 8 篇來源筆記與 6 篇 Wiki 條目。')

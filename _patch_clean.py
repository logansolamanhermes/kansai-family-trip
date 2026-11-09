# Clean the plan: drop audit panels/history/courier, add packing links
import re, sys
p='index.html'; h=open(p,encoding='utf-8').read()
q='booking-templates.html'; t=open(q,encoding='utf-8').read()
S=re.S

def kill(buf, pattern, label, count=1, flags=0):
    out,n=re.subn(pattern, '\n', buf, count=count, flags=flags)
    if n!=count: print('FAILED:',label,'matches',n); sys.exit(1)
    print('ok:',label)
    return out

def exact(buf, old, new, label, minc=1):
    n=buf.count(old)
    if n<minc: print('FAILED:',label,'count',n); sys.exit(1)
    print('ok:',label,'(',n,')')
    return buf.replace(old,new)

# 1. remove the three named audit panels
for pid in ['carTitle','v5Title','day5Title']:
    h = kill(h, r'\s*<section class="panel"[^>]*aria-labelledby="'+pid+r'"[^>]*>.*?</section>\s*\n', 'remove panel '+pid, flags=S)

# 2. remove the version changelog details
h = kill(h, r'\s*<details class="diff">.*?</details>', 'remove changelog', flags=S)

# 3. version links -> packing link, no archives
h = exact(h, '''        <div class="versionlinks">
          <a class="cta" href="booking-templates.html">日文／英文白紙黑字預約範本</a>
          <a href="v5/">v5 鋼鐵執行版（GranAce）</a>
          <a href="v4/">v4 最終校正版</a>
          <a href="v3/">v3 10/10 極致執行版</a>
          <a href="v2/">v2 誠實版預算行程</a>
          <a href="v1/">v1 初版（5 人）</a>
        </div>''',
    '''        <div class="versionlinks">
          <a class="cta" href="booking-templates.html">日文／英文白紙黑字預約範本</a>
          <a class="cta" href="packing-list.html">→ 出發打包清單（可列印）</a>
        </div>''', 'version links')

# 4. add packing links in topbar + first CTA row + rail
h = exact(h, '<button id="printBtn" class="ctl primary" type="button">列印</button>',
    '<a class="ctl" href="packing-list.html">打包清單 ☑</a>\n        <button id="printBtn" class="ctl primary" type="button">列印</button>', 'topbar packing link')
h = exact(h, '<a class="cta" href="booking-templates.html">→ 打開日文／英文白紙黑字預約範本（可直接複製貼上）</a>',
    '<a class="cta" href="booking-templates.html">→ 打開日文／英文白紙黑字預約範本（可直接複製貼上）</a>\n          <a class="cta" href="packing-list.html">→ 出發打包清單（3大箱・3軟包・6人）</a>', 'due panel packing link')
h = exact(h, '      勾選、訂位、實付、備註、Day 7 方案皆存於此瀏覽器；用「匯出 JSON」帶走。',
    '      <strong>打包</strong> <a href="packing-list.html" style="color:var(--accent)">3大箱・3軟包・6人 檢查表 ↗</a><br><br>\n      勾選、訂位、實付、備註、Day 7 方案皆存於此瀏覽器；用「匯出 JSON」帶走。', 'rail packing link')

# 5. compact packing panel in the plan itself
PACK_PANEL = '''    <section class="panel" aria-labelledby="packTitle">
      <div class="panel-head"><h2 id="packTitle">出發打包鐵律（3大箱・3軟包・6人）</h2><span class="hint">3 男 3 女，按酒店同房配對</span></div>
      <div class="panel-body">
        <div class="audit">
          <ul>
            <li><b>總量上限：</b>3 個 24 吋硬殼箱（每箱 ≤ 65×45×25cm、≤ 20kg）＋ 3 個 40L 軟質手提袋 ＋ 6 個隨身一日背包。<b>每 2 人共用 1 箱，按同房配對分配，不是按性別或情侶分。</b>3 個硬殼箱全程隨車，不寄送。</li>
            <li><b>去程規條：</b>軟包出發當日接近完全清空，留作回程冬日大褸與 Day 10 臨空城採購；嚴禁第 4 個硬殼箱。羽絨／防風大褸與防水防滑步行鞋直接穿上機，不佔箱內空間。</li>
            <li><b>個人鐵律：</b>3 件 Heattech（2 件 Ultra Warm＋1 件普通/極暖，<b>嚴禁 3 件超極暖</b>）、5 套內衣褲、5 雙 Merino 襪、冷帽／圍巾／觸控手套；禁高跟鞋與正式皮鞋（榻榻米需脫鞋）。4 天份量、Day 2 必清洗。</li>
            <li><b>司機：</b>香港身份證＋正式駕照實體卡＋運輸署 IDP 實體紙本（1949 公約、簽發 1 年內），並書面確認全部登記司機已列入保險許可範圍。</li>
          </ul>
          <p style="margin:8px 0 0"><a href="packing-list.html" style="color:var(--accent);font-weight:700;border:1px solid var(--accent);padding:4px 10px;border-radius:2px;text-decoration:none">→ 打開完整可列印打包檢查表（含手寫房間分配欄與逐項勾選）</a></p>
        </div>
      </div>
    </section>

'''
# insert before the budget panel (which is now the first main panel after dueTitle)
h = kill(h, r'(?=<section class="panel" aria-labelledby="budgetTitle">)', 'anchor check', count=0) if False else h
h2,n = re.subn(r'(?=<section class="panel" aria-labelledby="budgetTitle">)', lambda m: PACK_PANEL, h, count=1, flags=S)
if n!=1: print('FAILED: insert packing panel'); sys.exit(1)
h=h2; print('ok: insert packing panel')

# 6. remove both courier items and the courier budget label
h = exact(h, "    {t:'10:30', kind:'luggage', title:'機場黑貓櫃檯寄 2 大箱 → 京都 MIMARU', desc:'Day 2 寄達，每箱約 ¥3,500。車上只留 1 大箱 + 3 軟包。運費歸交通預算，請保留單號。'},\n", '', 'remove Day1 courier')
h = exact(h, "    {t:'上午', kind:'luggage', title:'黑貓逆向寄 2 大箱 → 臨空城 Star Gate', desc:'Day 9 寄達；減輕當日長途車的行李。'},\n", '', 'remove Day8 courier')
h = exact(h, '交通（租金・雪胎・油錢・路費・泊車・黑貓）', '交通（租金・雪胎・油錢・路費・泊車）', 'budget courier label')

# 7. scrub remaining version/history references from visible copy
SCRUB = [
 ('比 v4 的 19:00 提早 45 分鐘；「40 分鐘黃金緩衝」是舊標題。', '較原定 19:00 提早 45 分鐘。'),
 ('（配合 v5 Day 10）', '（配合 Day 10）'),
 ('寫法比前一版安全', '寫法安全'),
 ('比上一版再多抓 30 分鐘緩衝', '再多抓 30 分鐘緩衝'),
 ('10/10 時間修正：比前一版提早收手。', '10/10 時間修正：提早收手。'),
 ('準時發車離開臨空城（比 v4 提早 30 分鐘）', '準時發車離開臨空城（提早 30 分鐘）'),
 ('查核：18:15 到 T2 → 21:05 起飛 = 2 小時 50 分，比 v4 的 19:00 提早 45 分鐘；「40 分鐘黃金緩衝」是舊標題。', '18:15 到 T2 → 21:05 起飛 = 2 小時 50 分，較原定 19:00 提早 45 分鐘。'),
 ('（已非原始標題的 19:00 到櫃檯）', '（較原定 19:00 到櫃檯提早）'),
 ('上一版查到', '查核'),
 ('這版因此徹底放棄太閤の湯，方向正確。', '因此徹底放棄太閤の湯。'),
 ('刺青令已被這版採納，但換湯不換藥：', '刺青令：'),
 ('kansai-family-trip-v6-state.json', 'kansai-family-trip-state.json'),
]
for old,new in SCRUB:
    if old in h: h = exact(h, old, new, 'scrub '+old[:24])
    else: print('skip (not present):', old[:24])

# 8. rewrite footer to a neutral source line (no version labels)
h2,n = re.subn(r'<div class="foot">.*?</div>', '''<div class="foot">
  行程來源：你提供的「10/10 關西冬日海陸盛宴」系列文件（2026/11/9）。價格、定休、路況、房況與刺青規定仍須向店家最終確認；本頁不代為訂位，地圖為 Google Maps 搜尋連結而非導航保證。
  參考資料：<a href="https://eco.mtk.nao.ac.jp/koyomi/dni/2026/s2812.html" target="_blank" rel="noopener">國立天文台 2026/12 大阪日の出入り</a>、<a href="https://www.hinotabi.com/mie/ise-shi/sun_events/12" target="_blank" rel="noopener">伊勢市 2026/12 日の入り</a>、<a href="https://www.pref.osaka.lg.jp/o120130/suisan/tab/asa.html" target="_blank" rel="noopener">田尻漁港日曜朝市</a>、<a href="https://ja.kyoto.travel/tourism/single01.php?category_id=4&tourism_id=2943" target="_blank" rel="noopener">三嶋亭（京都市觀光 Navi）</a>、<a href="https://www.taikounoyu.com/howto" target="_blank" rel="noopener">太閤の湯 ご利用案内</a>、<a href="https://travel.yahoo.co.jp/00030106/info/" target="_blank" rel="noopener">月光園 游月山荘 風呂資訊</a>、<a href="https://www.yukoyuko.net/2828/bath" target="_blank" rel="noopener">有馬御苑 風呂資訊</a>、<a href="https://www.driveplaza.com/dp/SearchQuick?startPlaceKana=%E5%92%8C%E6%AD%8C%E5%B1%B1&arrivePlaceKana=%E4%BC%8A%E5%8B%A2" target="_blank" rel="noopener">ドラぷら 和歌山→伊勢</a>、<a href="https://www.kansai-airport.or.jp/access/from-airport/rental-car" target="_blank" rel="noopener">KIX 租車櫃檯營業時間</a>。
  即時查核建議：<a href="https://www.jma.go.jp/" target="_blank" rel="noopener">氣象廳 JMA</a>、<a href="https://www.w-nexco.co.jp/" target="_blank" rel="noopener">NEXCO 西日本</a>。
  狀態存於各自瀏覽器，家人之間不會同步；用匯出／匯入 JSON 傳遞。<a href="packing-list.html">出發打包檢查表（可列印）</a>。
</div>''', h, count=1, flags=S)
if n!=1: print('FAILED: footer'); sys.exit(1)
h=h2; print('ok: footer rewrite')

# 9. templates: neutralise the only version label
t = exact(t, '  v5 補充：', '  補充資料：', 'templates footer label')

open(p,'w',encoding='utf-8').write(h)
open(q,'w',encoding='utf-8').write(t)
print('index.html',len(h.encode()),'bytes | templates',len(t.encode()),'bytes')
for k in ['carTitle','v5Title','day5Title','v1/','v2/','v3/','v4/','v5/','黑貓','GranAce','packing-list.html']:
    print(' ',k,'=',h.count(k))

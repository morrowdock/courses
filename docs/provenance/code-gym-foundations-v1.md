# Code Gym foundations v1 provenance audit

Status: verified export inventory; proposed public draft; human rights and teaching review pending.
Checked: 2026-11-14 UTC.
Source baseline: `cc40e0a6315a9f86d21496f268b34aa8547786d3` (owner-authorized private course repository).
Source scope: `content/code-gym/foundations-v1` and `native-study/scripts/export_courses.py` at that baseline. No private repository URL or source-only prose is republished.

## Origin and permission

Every included item below is classified **original by the owner's AI agents**. Creator and rights attestation: Collin Craig; owner direction dated 2026-11-14 authorizes these original course materials under CC-BY-SA-4.0. This records the owner's grant and source evidence, not independent legal verification or a claim that AI output is necessarily copyrightable. AI-written content needs human review; status stays `draft`. No third-party licensed works, images or attributed external quotations were identified. Quoted misconceptions and sample strings are original instructional text, covered by their containing item. Any newly discovered unknown origin or incompatible third-party material must be excluded before promotion.

Evidence: each of the six source lesson `provenance.author` fields explicitly identifies original AI-authored programs and copy, dated 2026-11-03. These author-only fields are withheld by the exporter. Source introduction commits range from `82898d5bc6b525bc6faeffd3397ff95256afd52b` to `b8508f800f539d6dd63c04aa7331e8d8c3ecb0dd`.

## Inclusion and exclusion counts

Included: **6 lessons; 96 activities; 163 inventory units; 289 embedded code/command sample locations**. Units contain all their descendant prose, hints, rubrics, choices, examples and recorded data; sample locations overlap those units and are not additional activities. Images: 0. Third-party attributed quotes: 0. Third-party licensed items: 0.

Excluded whole learning items: **0**. No unknown-origin or incompatible third-party learning item was identified in the authorized scope. Author metadata and private cross-course roadmap are withheld.

Withheld source subtrees listed below: **7** (separate from whole-item counts). Source README, tools and tests are excluded in full; they are author/integration material, not learner content. Source course-map metadata not admitted by the exporter is excluded.

## Privacy and answer boundary

Names such as Ada, Sam, Mo, Ana, Bo and Cy occur only as fictional string literals and teaching examples; they do not identify people or learners. Numeric ages and scores are synthetic examples. No learner records are present. Recorded trace frames, checkpoint answers, fix outcomes, accepted Parsons orders and self-check models are deliberately admitted by the private runtime-free export contract, so they remain included. Nothing runs learner Python or asserts mastery.

Scan scope: every source JSON in these two course directories and every resulting public course asset; review URLs, names, paths, credential patterns and embedded samples. No class/instructor sources, real-person data, private-service URLs or credentials were identified in included material. Automated pattern and gitleaks results are recorded in the PR; they do not prove rights or factual accuracy. Owner approval required before status in-review/reviewed and before any announcement.

## Included item ledger

All rows: origin `original by owner AI agents`; disposition `included`; licence `CC-BY-SA-4.0`; creator `Collin Craig`. Pointers address attachment JSON under `courses/cg-foundations-v1/1.0.0-draft/attachments/`. Hashes include the public input-guidance and feedback revisions. Hashes use the exporter’s sorted compact UTF-8 JSON encoding with trailing newline. Course/lesson metadata rows cover the indicated metadata subset, not the full subtree. Bridge titles and all non-inventoried structural fields inherit their containing lesson provenance.

| Attachment | JSON pointer | Item kind | Stable ID | SHA-256 |
| --- | --- | --- | --- | --- |
| cg-foundations-01-names-values.json | `/` | lesson metadata | cg-found-names-values-v1 | `0cb5e2259cd2c144f56bcad72901187ec4ae1f8a93f14c864a182261d5e372ed` |
| cg-foundations-01-names-values.json | `/teach/0` | teach | nv-t1 | `95279ff0c8fed4f2db94b077cb1ce68f6ea2ceee098b29fbc86f9794ac6d89f5` |
| cg-foundations-01-names-values.json | `/teach/1` | teach | nv-t2 | `2ee9ffca1ca85cc3c2ce07022607c8ba0766321e5fd75d0236c3d57995d84a6f` |
| cg-foundations-01-names-values.json | `/teach/2` | teach | nv-t3 | `e539266f144e0efc7d48dd50602a40a9ed4aa7b22db9ab56d96394e3fa7164d2` |
| cg-foundations-01-names-values.json | `/activities/0` | activities | nv-l-watch | `df3983e8fcf86c8f59d167a4950029d6aa9f222334ee5203076de4f4d052f63a` |
| cg-foundations-01-names-values.json | `/activities/1` | activities | nv-l-plus | `4fe471e32f566c75e332e8d28685b61c464b90c01c42e66215fa2786debf4e33` |
| cg-foundations-01-names-values.json | `/activities/2` | activities | nv-g-copy | `98fa88e930d24776f1481090c4ba5e4feee14032371a7a170698b9fa58d66967` |
| cg-foundations-01-names-values.json | `/activities/3` | activities | nv-g-trace | `3588c8d723b9aff38afa5e65e485f1394f3baadb3cdaa72f39847bb7d82ec842` |
| cg-foundations-01-names-values.json | `/activities/4` | activities | nv-g-fix | `0625be065db2da46ee56892367dc7b232faf8d8a1db4803e865fec3d30952bc5` |
| cg-foundations-01-names-values.json | `/activities/5` | activities | nv-g-parsons | `7397c61a129586bd375fe6a6375062c4e8ccc78a635169192b7046a271c0c800` |
| cg-foundations-01-names-values.json | `/activities/6` | activities | nv-g-explain | `c614b842b25e5b9ca6750316e1a13fd2399935d6b91a15a6bca4c21e3a3d9d69` |
| cg-foundations-01-names-values.json | `/activities/7` | activities | nv-i-predict | `809e46d516ed7053ca693fe915dad3527d5c6b5a557c2253c1a8f95735344c3d` |
| cg-foundations-01-names-values.json | `/activities/8` | activities | nv-i-predict-cb | `23456af8061cf55b931bcc72c1a5b86348ef357a01bd89170e6afbaf9d3e2925` |
| cg-foundations-01-names-values.json | `/activities/9` | activities | nv-i-trace | `7c349c6b377674cdb84ca6b89849e024f57069d94b699455d834110be54c9846` |
| cg-foundations-01-names-values.json | `/activities/10` | activities | nv-i-trace-cb | `0cec6d37f1f63762d0056e6f8f2982b1a831111ae72722602abc0fafd986a69a` |
| cg-foundations-01-names-values.json | `/activities/11` | activities | nv-i-fix | `d7705f1211658c429382eec51ec4b537b8d888c0a180de3e3199dee159bc3b65` |
| cg-foundations-01-names-values.json | `/activities/12` | activities | nv-i-fix-cb | `8724aec8129de6f59fd1b12bd3589fbe329cbeb21553d433fa139257b3897100` |
| cg-foundations-01-names-values.json | `/activities/13` | activities | nv-i-parsons | `c8443872887fe3bbf7f138bc54280c2269bcec63a5ca8fa12a3d4a8ed409f2dc` |
| cg-foundations-01-names-values.json | `/activities/14` | activities | nv-i-parsons-cb | `20d3953ee9a408f3c892f6ba38379d68ac504fafc1d40ecc4703d89e29944e37` |
| cg-foundations-01-names-values.json | `/activities/15` | activities | nv-i-explain | `2396bbb54f759619c52610c19a79c2cc6474152b0ac812128feb31ceda0bb1fd` |
| cg-foundations-01-names-values.json | `/bridge/rows/0` | bridge example | — | `978021978c4ebee088349a0a791998fd797d4c5d0a1f6e83cee5d6da739b6ee6` |
| cg-foundations-01-names-values.json | `/bridge/rows/1` | bridge example | — | `bc2fd8d80a52230d198f641d2253630b22aa5832b97f55631d3f8226c13b3206` |
| cg-foundations-01-names-values.json | `/bridge/rows/2` | bridge example | — | `5efe9ec599daafd3df80c0b998382964790d31d93d4001f786c02d229bf721e4` |
| cg-foundations-01-names-values.json | `/bridge/rows/3` | bridge example | — | `d5a7d8e43a4e61690404f41937eb4576ecf6b8a782c5a368e44b59d7c8228d0a` |
| cg-foundations-01-names-values.json | `/bridge/rows/4` | bridge example | — | `5e4a7fe3b1988e003141d8965b71d53a041e8dc6d09b575b36ea4ac3b17636c8` |
| cg-foundations-01-names-values.json | `/bridge/rows/5` | bridge example | — | `3e2f54b926ba52559c64ee13725a4db06497495a4cac12458a5524a635b1a082` |
| cg-foundations-01-names-values.json | `/referenceCard` | reference card | — | `4642166e2d98550ae1916da4898d0dbe9c37348a0ebcb2b0d18e322b61123375` |
| cg-foundations-02-conditionals.json | `/` | lesson metadata | cg-found-conditionals-v1 | `f5966f7089e550e7db67bd7f080fe06e40bbf8c06d8af4357575e3a44dc3653b` |
| cg-foundations-02-conditionals.json | `/teach/0` | teach | cd-t1 | `f21080a8e52cb149867008d35482e5d440b3252a469dd5fe74530b7e0d9dba69` |
| cg-foundations-02-conditionals.json | `/teach/1` | teach | cd-t2 | `6a0b0ba3bf8751362d45e7cc81912bafbeda7d0c9109a0470b546dc096151ab6` |
| cg-foundations-02-conditionals.json | `/teach/2` | teach | cd-t3 | `58b90dc8db99f0c197831e7422a78a1c20882e2baded07c92c0386b202f22efe` |
| cg-foundations-02-conditionals.json | `/activities/0` | activities | cd-l-watch | `4c8517d20bcd49a4bade1a8db5bee1cc8cc870c3e9f8dc1fcd35f71f252912ac` |
| cg-foundations-02-conditionals.json | `/activities/1` | activities | cd-l-order | `4005655c9816aef92fb07a860b020f7324bb8efb32d0d220e04a4a87588a6db2` |
| cg-foundations-02-conditionals.json | `/activities/2` | activities | cd-g-teen | `40cd8ed168cf5ccc6ab601a019cabc875e226e620443f7ab492ab4755cf01ec6` |
| cg-foundations-02-conditionals.json | `/activities/3` | activities | cd-g-trace | `7c7b20fa3a2775adc0b12c827474a221f9a1d1811bfeea49dd73e584db5e3c6e` |
| cg-foundations-02-conditionals.json | `/activities/4` | activities | cd-g-fix | `5bd825cdecca5a02997ca46ba2d5376588229778fb271f58b4c4400ef52183b9` |
| cg-foundations-02-conditionals.json | `/activities/5` | activities | cd-g-parsons | `39568c35dbc93d0c5f9046df0ec6bfb4223689e3543268159e839a4eb94c8c44` |
| cg-foundations-02-conditionals.json | `/activities/6` | activities | cd-g-explain | `4499135a9a4a700b8dd491f6531641ebffed4fb9dda16d9549fdeb7ba870fc9b` |
| cg-foundations-02-conditionals.json | `/activities/7` | activities | cd-i-grade | `83f934d13beb44b3ccac35b797e94c6af38d66feb4af5234007e92fc350cdb32` |
| cg-foundations-02-conditionals.json | `/activities/8` | activities | cd-i-grade-cb | `39b3b9a302d8d4ca13b71986046ba5a0a991d85cdc96ac365192d5ef6b4935ee` |
| cg-foundations-02-conditionals.json | `/activities/9` | activities | cd-i-trace | `e6723835a547d02c877aec3f53b82c7889fc3eb6509858fedf2c5eed05d84203` |
| cg-foundations-02-conditionals.json | `/activities/10` | activities | cd-i-trace-cb | `063ecf22c601b28db8edac60f64c854a7dc16f3777c9589e533eef555c49b53f` |
| cg-foundations-02-conditionals.json | `/activities/11` | activities | cd-i-fix | `431afeac9486148243326d7471045bfa68f530f157d1636709f6022d35a159fe` |
| cg-foundations-02-conditionals.json | `/activities/12` | activities | cd-i-fix-cb | `ff024e89d931d4ad284a9e7c191ee4364232deea5566f7d8bf2bf445efdf1c11` |
| cg-foundations-02-conditionals.json | `/activities/13` | activities | cd-i-parsons | `d85a2b94bed7ff626e85de1c958086700e04b8af3b0f7016cfbb4bea807ff446` |
| cg-foundations-02-conditionals.json | `/activities/14` | activities | cd-i-parsons-cb | `bf085dc7db3931b2522ccf67be29e8a398d69e124bb5cf09c8ab307f4f20629f` |
| cg-foundations-02-conditionals.json | `/activities/15` | activities | cd-i-explain | `10fb7a57288e9c0a24991f07f23b8c0361a38e42cd08ba2016b1fab952575401` |
| cg-foundations-02-conditionals.json | `/bridge/rows/0` | bridge example | — | `742d3dbab27d987a356fd437833b21bff2fdb1be8d0f43e2db5bfcc283015e89` |
| cg-foundations-02-conditionals.json | `/bridge/rows/1` | bridge example | — | `ef799e9db89fa141f67b1e1d6ab684811953d388df195f82171865bb9af89175` |
| cg-foundations-02-conditionals.json | `/bridge/rows/2` | bridge example | — | `c61c2ea5eeaaf8171664fb828d4eb75a6b1f7bd8c933bf0729ede289b7c9d8f6` |
| cg-foundations-02-conditionals.json | `/bridge/rows/3` | bridge example | — | `08e11b1924cd26db2cae52ff91cc9906d66a3c54a1c754e861154e2ca5f0e9c6` |
| cg-foundations-02-conditionals.json | `/bridge/rows/4` | bridge example | — | `4d4192dcdeae825daeb689780e7d8f68d1d559190b973fd66ded227cf42c73fe` |
| cg-foundations-02-conditionals.json | `/referenceCard` | reference card | — | `7080e97549050470f02b4d8798f494adf4398a6f1cd09343817b8b8ccc20ce76` |
| cg-foundations-03-loops.json | `/` | lesson metadata | cg-found-loops-v1 | `d88255f7b71f1b2c9d7b5620e1ef02fe4fe2114f6306b573e9579ee1d7a8d866` |
| cg-foundations-03-loops.json | `/teach/0` | teach | lp-t1 | `da278aa953cee7aab32fc8a9a6f1865d15d054d149fee5aadd16204061d667a1` |
| cg-foundations-03-loops.json | `/teach/1` | teach | lp-t2 | `3e396e44a228b8f8648e2aede5be3249e0cc892b88c87170646b6deaa65caff4` |
| cg-foundations-03-loops.json | `/teach/2` | teach | lp-t3 | `71ca586be90f617ad2e36be822cb8adb7c71a68bf3d77e77a4c1fd24350f5342` |
| cg-foundations-03-loops.json | `/activities/0` | activities | lp-l-watch | `ba908372582725d391835d54a5a124a3e380b6b5c2b68b3930f730202cfaedb0` |
| cg-foundations-03-loops.json | `/activities/1` | activities | lp-l-range | `b860b380e30cc8047ec5782039359e1bdc955d8ac513c09fcc3649364302f780` |
| cg-foundations-03-loops.json | `/activities/2` | activities | lp-g-countdown | `da784e26329378cfea46aac2594dbbada8ca10a40c1ce67715c61c6d5b79b646` |
| cg-foundations-03-loops.json | `/activities/3` | activities | lp-g-trace | `37cf49dec277acb82e7e02ae97d86465e75d93123b0aba90efe18dfb90f06051` |
| cg-foundations-03-loops.json | `/activities/4` | activities | lp-g-fix | `660b55ccff08a81537b24e113c3cf878bb2e2eacddceb4adc201e55cf7ad641d` |
| cg-foundations-03-loops.json | `/activities/5` | activities | lp-g-parsons | `65390391ed0cd34b4a8ed9099649bfba783cbce75b9fbb8979177f7e5e59d5dd` |
| cg-foundations-03-loops.json | `/activities/6` | activities | lp-g-explain | `5b6d075a5e17b17ed5f6815c6e86fbf43ac31caf070525321f9faae4dc4e9118` |
| cg-foundations-03-loops.json | `/activities/7` | activities | lp-i-triple | `e190512fae600dbf8911b18116f858a193faadcd1ab9c14e8fe11ba1efa348e0` |
| cg-foundations-03-loops.json | `/activities/8` | activities | lp-i-triple-cb | `2ba5d93f450886d22884a1d65f78d54bef6b1323a608f0ad92eff1f89900fe0c` |
| cg-foundations-03-loops.json | `/activities/9` | activities | lp-i-trace | `91d428591adf4dcb90bc1702da0d8f64f8b485d6f02ca22f3658c0eb721cb145` |
| cg-foundations-03-loops.json | `/activities/10` | activities | lp-i-trace-cb | `04fba628985d0a26cc1cdda89565efe71b63b7cfe1de5de00dbaf2e68870ed35` |
| cg-foundations-03-loops.json | `/activities/11` | activities | lp-i-fix | `f91959140527719329984139afedeea31e57fedba3762f3b31984a338d8a2b9e` |
| cg-foundations-03-loops.json | `/activities/12` | activities | lp-i-fix-cb | `7af7c0bd7a7127a093e2a0d0241aa661c295262063ad76cf5e0d4be16899683c` |
| cg-foundations-03-loops.json | `/activities/13` | activities | lp-i-parsons | `4f6d94c33faad7ce1d2c98fac582d5c2d1f7a4e94a1c8fa761b2d41b45e3c5e6` |
| cg-foundations-03-loops.json | `/activities/14` | activities | lp-i-parsons-cb | `e3138498103d85e949a1080b2562d78d1646cb3b80960c97a6d55a85b77b1828` |
| cg-foundations-03-loops.json | `/activities/15` | activities | lp-i-explain | `9aa9519b9a48f607d85a64778544c798773d91f470180723dc15249c3bb44d59` |
| cg-foundations-03-loops.json | `/bridge/rows/0` | bridge example | — | `f5df41f8d9c5b8c80ffb995da66f71fa4c3b2d2d4c68170a59f73f4c55fdf1d4` |
| cg-foundations-03-loops.json | `/bridge/rows/1` | bridge example | — | `e13de5ea74ee484e4986aabe8c4faea3b7c977b1623f95e05331a72abb50b080` |
| cg-foundations-03-loops.json | `/bridge/rows/2` | bridge example | — | `709997610941d8caaaa12fb1e7cf9c130bd65ab767ac5100dd63a7095773a8d8` |
| cg-foundations-03-loops.json | `/bridge/rows/3` | bridge example | — | `5b085b52db09cdef05cabf8170ab198a75945e2c411d5f24d07ad5e5d23361cc` |
| cg-foundations-03-loops.json | `/bridge/rows/4` | bridge example | — | `14df839fe9b9748c342ffb52f2d38bc49238b055b1b0781d665f7e556318fa51` |
| cg-foundations-03-loops.json | `/bridge/rows/5` | bridge example | — | `270ba79378438bbf8aa79e12488077dda9d64039feb429c921e48cae8522ee61` |
| cg-foundations-03-loops.json | `/bridge/rows/6` | bridge example | — | `0f6c8439b60205f211e4d128f890c31ca3badf82ccb11870db56efd1425bdb3e` |
| cg-foundations-03-loops.json | `/referenceCard` | reference card | — | `04f7a11f2145d9a71753923ef1e8ed51ed84c42454ceefd1bcbce836e333bc73` |
| cg-foundations-04-functions.json | `/` | lesson metadata | cg-found-functions-v1 | `7a862fca9b7506603c08381c858c33babe5ddb5b6ff3300a4a2c2c0231f21eee` |
| cg-foundations-04-functions.json | `/teach/0` | teach | fn-t1 | `6ec616d814143e810dac15e8ef607cd28ecc46c528cce7e8823867ef62b39c5e` |
| cg-foundations-04-functions.json | `/teach/1` | teach | fn-t2 | `889c87f65c5a3b489c43f4c7482120750e79ab460d3939e2fe015c3730517a3c` |
| cg-foundations-04-functions.json | `/teach/2` | teach | fn-t3 | `6954b7235a2ba5c3360695d7acbc66f07188f13cc1ce00eb60aee4552f84bc26` |
| cg-foundations-04-functions.json | `/activities/0` | activities | fn-l-watch | `b9e6069e95db35f385400105a1a1c61f2211dc0007d3222c8345a2a93ecd7de2` |
| cg-foundations-04-functions.json | `/activities/1` | activities | fn-l-print-return | `ddca78cf667619374783dd2ef8280bae76fa2e6adc52da55d7da95db42d119dc` |
| cg-foundations-04-functions.json | `/activities/2` | activities | fn-g-area | `45303b2179c180c819b8797701c6f2451f31ada4dd3b3272af2098dfeb908cfd` |
| cg-foundations-04-functions.json | `/activities/3` | activities | fn-g-trace | `7313c84d184c16338963a2fa62124600617b087e89a2fe0f1ee43b41c404111c` |
| cg-foundations-04-functions.json | `/activities/4` | activities | fn-g-fix | `a15526aa29c6dd1ecb3293733a0449f0d68c8c6fe0e731f5808251fb6641f17a` |
| cg-foundations-04-functions.json | `/activities/5` | activities | fn-g-parsons | `f2da621a9ff64967430a0d9f9a524ac136194f73f5f48125b61b44ac05c37921` |
| cg-foundations-04-functions.json | `/activities/6` | activities | fn-g-explain | `51b1ca0b7e333d2c7f7b1ce512bbb2b071aef3f1c03b3ff0199d639988f8538b` |
| cg-foundations-04-functions.json | `/activities/7` | activities | fn-i-scope | `28d6daa47960e43a98ddb79cfa9e9c6fed2f26cbb3f397e204ecce08ea2933f3` |
| cg-foundations-04-functions.json | `/activities/8` | activities | fn-i-scope-cb | `837b1af7cff4538aaf3cc13a75f710b6854d77edc007257d103912ed05eb70c9` |
| cg-foundations-04-functions.json | `/activities/9` | activities | fn-i-trace | `14b899fd11ff19fd871560c57556c23a3343b45af07bd7cd4f55240fa05d51c8` |
| cg-foundations-04-functions.json | `/activities/10` | activities | fn-i-trace-cb | `559fc698228cc6ae0467ecb0dec045688f9c31d11a1c80636a5145dd466c06d5` |
| cg-foundations-04-functions.json | `/activities/11` | activities | fn-i-fix | `a68c1e0aeaf9d3f9c767ef4b20108f0843390d6929317e6ed36525042b7a1191` |
| cg-foundations-04-functions.json | `/activities/12` | activities | fn-i-fix-cb | `4c76bdff7c6f7a7a935888113e4f057d7bb184c7ed9c37bdc05829afd440f40b` |
| cg-foundations-04-functions.json | `/activities/13` | activities | fn-i-parsons | `e074f0fc033610a824b3813baeed98452a85fe3705e3a908b16441be4397c337` |
| cg-foundations-04-functions.json | `/activities/14` | activities | fn-i-parsons-cb | `297840116f5ab466a85f4545577a9f7dd35d346fe6367b5969dbff77bde52485` |
| cg-foundations-04-functions.json | `/activities/15` | activities | fn-i-explain | `135ba42de9a5278b18203631558662c60b03a54a68ec03aac20f39ed10b275b5` |
| cg-foundations-04-functions.json | `/bridge/rows/0` | bridge example | — | `e69f829133999e1492ed5f9898651e7e921b6d62c2360c71b24656918cc4bdc4` |
| cg-foundations-04-functions.json | `/bridge/rows/1` | bridge example | — | `0921696963d9188fb524b7b91fdab242de6305858001450d9e3ad0809e1a640d` |
| cg-foundations-04-functions.json | `/bridge/rows/2` | bridge example | — | `efa67b758da5ea8e855391b2501b67be12b5a9ba235a27639a77c126ca356320` |
| cg-foundations-04-functions.json | `/bridge/rows/3` | bridge example | — | `8988ef296a6ddf87e0f31e32762bb6e2c400974850a1ccb700b58ff3e1440632` |
| cg-foundations-04-functions.json | `/bridge/rows/4` | bridge example | — | `ee5cf339fd0ea432ed55f6255573ffe96ed7c3e9a9e91992ba4865bebd118df6` |
| cg-foundations-04-functions.json | `/referenceCard` | reference card | — | `ef0264ba37aa40145f021b1f4a9306da97e1bf30bb7b5e12eddf571c2038c008` |
| cg-foundations-05-lists-dicts.json | `/` | lesson metadata | cg-found-lists-dicts-v1 | `568097a918c4119313225df4a6d1aa331b234c9ea6edf3f2b41423f21c33b466` |
| cg-foundations-05-lists-dicts.json | `/teach/0` | teach | ld-t1 | `58545d4fd3d47caf7c15c4d64d7120f9fa6dc0b3ea25e71e29f6d934f309bc38` |
| cg-foundations-05-lists-dicts.json | `/teach/1` | teach | ld-t2 | `faab366c00173f31e182d4a6aac16a2b9465ac7260b9fb01c10aff04ab45060e` |
| cg-foundations-05-lists-dicts.json | `/teach/2` | teach | ld-t3 | `72d368389041e0a52146cf9cf44c52bbeb470d0de3e18ee4c458a56fd65d6e99` |
| cg-foundations-05-lists-dicts.json | `/activities/0` | activities | ld-l-watch | `451ff95851ddc408c126f5f88172bdd0e3f2233518c224dc0f26d521991f7c93` |
| cg-foundations-05-lists-dicts.json | `/activities/1` | activities | ld-l-alias | `3bae1c67053d21861ce72de3b8f3d2bb24eba08e8932b3dc1dc3cb5e5a36eedb` |
| cg-foundations-05-lists-dicts.json | `/activities/2` | activities | ld-g-index | `fe6c64d7206569ff7d4610fec4a23c12a6e6e3cf9ebff1381915f26c579c027f` |
| cg-foundations-05-lists-dicts.json | `/activities/3` | activities | ld-g-trace | `e6415788bcdc9c333ba04ead19cf4589b97875b739b78bad1c1043715e3c6951` |
| cg-foundations-05-lists-dicts.json | `/activities/4` | activities | ld-g-fix | `c603d0f8431fbdc32246ef6bcfd76fbad7d9ce7df131f6d346bab3a4e933ed1e` |
| cg-foundations-05-lists-dicts.json | `/activities/5` | activities | ld-g-parsons | `fc6e9560bb5d46c1ee13ae54dfd61cb705c667467fc40a3c41736daa12fb60a6` |
| cg-foundations-05-lists-dicts.json | `/activities/6` | activities | ld-g-explain | `07909af728baf45e5d0a55e46eed30d15a36fa74fc51a6ed8557dd96eaa2346b` |
| cg-foundations-05-lists-dicts.json | `/activities/7` | activities | ld-i-index | `9fd768de85600ccd508a9d49bc2f17adc56c07ae42a198c3267f6e3a854b5b42` |
| cg-foundations-05-lists-dicts.json | `/activities/8` | activities | ld-i-index-cb | `ac1bc08b36224dcc5c0af573fe338c32a3c89844627c8e120b0d8c375574f9f6` |
| cg-foundations-05-lists-dicts.json | `/activities/9` | activities | ld-i-trace | `6509f805e77e4f1a46a727ad600b8fba44471411199b0a495436e74e334c39d3` |
| cg-foundations-05-lists-dicts.json | `/activities/10` | activities | ld-i-trace-cb | `c45db31e9443f9440321a0cf735a7eb0ed6ddc4dedd9e6943225ff007929be8b` |
| cg-foundations-05-lists-dicts.json | `/activities/11` | activities | ld-i-fix | `4b74b1458fa5655b11d4e44fdee261c98d06da9782fb7e07e3a6e0e1ba5c4108` |
| cg-foundations-05-lists-dicts.json | `/activities/12` | activities | ld-i-fix-cb | `37f62cf9e81db2ad1dc74de5e009a326339c567144c1361ca8ae70af3007178e` |
| cg-foundations-05-lists-dicts.json | `/activities/13` | activities | ld-i-parsons | `58d304d44fcb880e66b315d8b61fcc8ff0b18b7ea786bdd5475bde7b2af160c4` |
| cg-foundations-05-lists-dicts.json | `/activities/14` | activities | ld-i-parsons-cb | `308f256ac5dd1df88a851d6879f31ff9428d68cbc7114864761abe342881a05f` |
| cg-foundations-05-lists-dicts.json | `/activities/15` | activities | ld-i-explain | `728dca28853225464b1f4bae79b3ec3bd091d8ed30a0e270a6db21cd111b2174` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/0` | bridge example | — | `64e8a90da17cc59e5e846c6a87c1ac9e01032e0b187a1f81c840380ae9c56a52` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/1` | bridge example | — | `ccf6a01262065dd3e46741d0677a7fab872c24a6f2c9939787ded811dc8dbd28` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/2` | bridge example | — | `3f1b5237dee4708396b84d155b75d201ef5121e859c2698d4bceb0461303b810` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/3` | bridge example | — | `934d90c44fadd0e3ac968077132c8c318eb41f9fdc5f21882ea78a99f3c01ac0` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/4` | bridge example | — | `a364f0f8505891bb317b973e510b5096e38ad58d6de759056d602c2216aed3e6` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/5` | bridge example | — | `4bf82bb389283f3ac7b6b56bd57ad31a77c32e99ee9927ff4ae762d5d42a9ece` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/6` | bridge example | — | `80bf6a33d787993e8f1f4de00f3b2624f7d12d5d7a1566bf26925fe7b77ad268` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/7` | bridge example | — | `cbe8914ca95154200ee9c8c3fc6c79adc881256b01e6eb12c951842af94bda23` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/8` | bridge example | — | `5216abc683be0cfda804c8736e694389bf265a422505f1039a802e40c572dca1` |
| cg-foundations-05-lists-dicts.json | `/referenceCard` | reference card | — | `5cd5c071ffa7a49bd62a16cf7b97fd6c4aaa58e7dfdb54066de3da47a0236856` |
| cg-foundations-06-recursion.json | `/` | lesson metadata | cg-found-recursion-v1 | `c277cb1ab6cf6010b7b59910679556f40942ff2a46bde6bf760309599791579f` |
| cg-foundations-06-recursion.json | `/teach/0` | teach | rc-t1 | `20f319750d784fd0439b0c6775c139ac365ad84feb79bf9ce0d4c2cdcb8d1909` |
| cg-foundations-06-recursion.json | `/teach/1` | teach | rc-t2 | `abc613fb031736dca46dfb26dd52c10ca2ba3b425c25adeb7470f118cc00f560` |
| cg-foundations-06-recursion.json | `/teach/2` | teach | rc-t3 | `e5ace40d0b8bcbf96fb0332a1b1620c45eb3777ea14f75b3fcff344f38ec74ad` |
| cg-foundations-06-recursion.json | `/activities/0` | activities | rc-l-watch | `7fbd3b35e7eec3394a86aca1ee844162a26c551a9b69827d51fb9b0ddfe8f099` |
| cg-foundations-06-recursion.json | `/activities/1` | activities | rc-l-order | `927a8af131f0e5658c23917f26871f1df201c0afb002c98e4f5b2dfe2237aa1d` |
| cg-foundations-06-recursion.json | `/activities/2` | activities | rc-g-total | `503ac170796d0342fb15a33e75316532c460b9c8cba549f6d1571a450bbab8d5` |
| cg-foundations-06-recursion.json | `/activities/3` | activities | rc-g-trace | `9567a74a02a239174c786f05d949eeb4cb991cda5ad00607359694d0c3787161` |
| cg-foundations-06-recursion.json | `/activities/4` | activities | rc-g-fix | `2821e50fd336c501c914e9fb456ee55f9557e1a586b95519e914054526ec489b` |
| cg-foundations-06-recursion.json | `/activities/5` | activities | rc-g-parsons | `b402e4cb1c83217efbb946118fe273c5dd4ba84cf4faa317c3c2f2a80a1a58c2` |
| cg-foundations-06-recursion.json | `/activities/6` | activities | rc-g-explain | `e6bfc1fb057691a2ca9e3f22984a616141bda8ee84eda105ab4479e8c79acd37` |
| cg-foundations-06-recursion.json | `/activities/7` | activities | rc-i-digits | `469b951d98b261a77722d0cae5de24bb08b25969d863151de3e44316c47305c4` |
| cg-foundations-06-recursion.json | `/activities/8` | activities | rc-i-digits-cb | `7fc8920539d0ae6a9d10022cb18ff527f27d5ba15515dfe897b0cb1a9e6e46b2` |
| cg-foundations-06-recursion.json | `/activities/9` | activities | rc-i-trace | `9b991020b33ff024e9c88ce6e6a7d633adf35543eecb8c6a42d2bac4e2aecef3` |
| cg-foundations-06-recursion.json | `/activities/10` | activities | rc-i-trace-cb | `c3eed00526d5e8becd91e75c5bcee3b82c3d8fb6975a0ec6390e24d298cb6841` |
| cg-foundations-06-recursion.json | `/activities/11` | activities | rc-i-fix | `dc3367bc292fd2e431b61e36a0dc2c4c5d7a8094b93228c9f85d2cc1b477eb60` |
| cg-foundations-06-recursion.json | `/activities/12` | activities | rc-i-fix-cb | `cef36916727f29b86d4bdc985f4714282bb335ac29b1621e3b23291fdd2e923e` |
| cg-foundations-06-recursion.json | `/activities/13` | activities | rc-i-parsons | `549e0a3da5184890d41b0424a5700fbe235ca3a641baa5e3631d0208d5b79242` |
| cg-foundations-06-recursion.json | `/activities/14` | activities | rc-i-parsons-cb | `04607d33ec9856452e254f979b3c5a6b7c715446496941ac4293aa25667707dc` |
| cg-foundations-06-recursion.json | `/activities/15` | activities | rc-i-explain | `4a81c7b87757b49fd63d0f58ae88d9c1fe063bdb9bcd9023c94082897b471871` |
| cg-foundations-06-recursion.json | `/bridge/rows/0` | bridge example | — | `51790ee65266b14e9ab202fc5b3f25052bb85dc5053c4965f3e6d0441d9723dc` |
| cg-foundations-06-recursion.json | `/bridge/rows/1` | bridge example | — | `24db096893b060e819a153508e955ac0f0a51391c4e5880c45ea4b7984c89aa8` |
| cg-foundations-06-recursion.json | `/bridge/rows/2` | bridge example | — | `6918be29a7aee6a30db652b4bab65b2a4831e1a190668d20f17554a9126f4ce3` |
| cg-foundations-06-recursion.json | `/bridge/rows/3` | bridge example | — | `ae3d9b9ed1cbcb186fe72f66aebb39cd645566674f70649fa0b7e201ea46bb99` |
| cg-foundations-06-recursion.json | `/referenceCard` | reference card | — | `95e10e50afbb0f47e20a779028e81c0d53f7be9c163433f7a237bd1e13b0fba2` |
| authored-code-gym-foundations-v1.json | `/` | course metadata | cg-foundations-v1 | `303cdaa4d0c955eba35c0ca25c7d8ea7b1c896a184008eddf655d2386ac79aef` |

## Embedded samples

Each code/command location inherits the original origin, licence and included disposition above. Inline snippets and quoted strings embedded in prose are covered by their complete parent unit. No external images or quotations are linked.

| Attachment | JSON pointer | SHA-256 |
| --- | --- | --- |
| cg-foundations-01-names-values.json | `/activities/0/code` | `7e644804e000d1869d60029c94c9c8469b4dd060821a2171c6070bdac61a067d` |
| cg-foundations-01-names-values.json | `/activities/1/code` | `e8a1395ca503afc46946170ddadde43b39fe329b22115c007b5df2355fb1d1a1` |
| cg-foundations-01-names-values.json | `/activities/2/code` | `88c4a144cad89fe0e378670243b285fb1ab0b6515772e61f69f824e768523c0b` |
| cg-foundations-01-names-values.json | `/activities/3/code` | `b16f4597317e7546d77a9300cc935bbb5e33d952fbac0544f011c3359ea1fc45` |
| cg-foundations-01-names-values.json | `/activities/4/code` | `18387ed24b82a6d1fad53623e03bcaa1437e9865d3ae8d33126f64995c7f60c6` |
| cg-foundations-01-names-values.json | `/activities/4/fixes/0/fixLine` | `79111d34db0822875fad6124ac8b655c592cbcb3ed62c667b2f9dfd8664fced1` |
| cg-foundations-01-names-values.json | `/activities/4/fixes/1/fixLine` | `df66e58ad7104fd5cab4a639629fe87815366e78afd8c3764d7d4b4705701ef8` |
| cg-foundations-01-names-values.json | `/activities/4/fixes/2/fixLine` | `f8194f260658beab32a16defce9af44218a74d75f1e8c96e2583953254b77cc6` |
| cg-foundations-01-names-values.json | `/activities/5/distractors/0/line` | `1e0a2d5285415b4ede8fd4218d519aef9e003a8a138de634467c9362f8aade87` |
| cg-foundations-01-names-values.json | `/activities/5/lines/0/line` | `9d02f34323b184a48f4c04be8247b098a184342bee0ae1013d42fada63500919` |
| cg-foundations-01-names-values.json | `/activities/5/lines/1/line` | `f6bfc15db247d65902348da8b5d9d11f49ef611fef479af0e4aea2ac17c48ab9` |
| cg-foundations-01-names-values.json | `/activities/5/lines/2/line` | `f28dd0d0e8f48209deb3a0bbb5398e9f5c2c3f01039b1f8cace4e39d6599482a` |
| cg-foundations-01-names-values.json | `/activities/7/code` | `8754499cd4e63d75517f227906a5a34654fea1f50441440a965fa806378e8ad4` |
| cg-foundations-01-names-values.json | `/activities/8/code` | `1c93fdf930958441329b970f12aee46a0ebc1cffe3d85970f2b89c593f68e33c` |
| cg-foundations-01-names-values.json | `/activities/9/code` | `a8ee9b2c6336f00ace4d014e5a2db1aac927293e0153743876f312cc77e88e8b` |
| cg-foundations-01-names-values.json | `/activities/10/code` | `03ed78447834bad9cb488b6d17eb242b80939367c60af48ad091d63468eb42be` |
| cg-foundations-01-names-values.json | `/activities/11/code` | `fa224ee36a45c4f5b0d41d1828701737657178ea671a0d135c5befa5b49b1ec0` |
| cg-foundations-01-names-values.json | `/activities/11/fixes/0/fixLine` | `0d09642a05b6f0cebc01d429e6e64efc681cd7fe8ec2392244fb9152871a805d` |
| cg-foundations-01-names-values.json | `/activities/11/fixes/1/fixLine` | `ee5eb5e26b3d1744d5c269ef8d9b8d9c0b711490e4b047cd106b8242fef1a07a` |
| cg-foundations-01-names-values.json | `/activities/11/fixes/2/fixLine` | `05aa1b6ad010173109e765ad3c4061d7156a7373d203bbca81f2910c6d477c3e` |
| cg-foundations-01-names-values.json | `/activities/12/code` | `1fa39df375c5c8149b6f37e78d4dbe7367d5043274fee95834e5b3e4f543ada6` |
| cg-foundations-01-names-values.json | `/activities/12/fixes/0/fixLine` | `00a768d48f01de60bcef4c1a7538e6b6aafabdb6a25789f819a80e1bf55ee886` |
| cg-foundations-01-names-values.json | `/activities/12/fixes/1/fixLine` | `80ab8c40e18bc0400cb20f7dbdfb6de8236e97e7412f7343d5acae040f4a8c69` |
| cg-foundations-01-names-values.json | `/activities/12/fixes/2/fixLine` | `69123c5e5bc959dfc3721279735920845a5a5ac269eaa6975738cddb2006afd3` |
| cg-foundations-01-names-values.json | `/activities/13/distractors/0/line` | `eb81af570cf547552dfa0fd175e715f45e888518994df3b344c1b3622c51a727` |
| cg-foundations-01-names-values.json | `/activities/13/lines/0/line` | `ad7a631b25947d0e2e6084303cf90d48a53e57af3e490810163e9a82d2de2796` |
| cg-foundations-01-names-values.json | `/activities/13/lines/1/line` | `fc1fc66b49629ba7ccc7f9d59b4207b54d304e7b5bd2012491bb2f2c9fb06fab` |
| cg-foundations-01-names-values.json | `/activities/13/lines/2/line` | `8072775a0b12fca3ca52506e1a11616cd0ee3c05af49966f665becf2391dea93` |
| cg-foundations-01-names-values.json | `/activities/13/lines/3/line` | `fc1fc66b49629ba7ccc7f9d59b4207b54d304e7b5bd2012491bb2f2c9fb06fab` |
| cg-foundations-01-names-values.json | `/activities/14/lines/0/line` | `ed5e625f02087f3da022aee284eeb1785e6d9e682081a04003e0ebf84adcdf81` |
| cg-foundations-01-names-values.json | `/activities/14/lines/1/line` | `24e8188a1d6d35b41a746ad5c53019f999c0f1be58d7bae6971a0b106637684b` |
| cg-foundations-01-names-values.json | `/activities/14/lines/2/line` | `80f672069d5aedad8a71493e8405c162985357ab74e2e914757ba1112bbd7e92` |
| cg-foundations-01-names-values.json | `/activities/14/lines/3/line` | `24e8188a1d6d35b41a746ad5c53019f999c0f1be58d7bae6971a0b106637684b` |
| cg-foundations-01-names-values.json | `/bridge/rows/0/lua` | `08beef600c377147d2cdc3baa935d6b5c8bf2bc77167b887780f669f7a8ce4cc` |
| cg-foundations-01-names-values.json | `/bridge/rows/0/python` | `fca15913da6c71ae6f298a822e637764d054a534ad2ee964739cda712ccd490a` |
| cg-foundations-01-names-values.json | `/bridge/rows/1/lua` | `400c630026f45acf4b60efe02f07a7efbb6704c129c96fd367c716ba761c2875` |
| cg-foundations-01-names-values.json | `/bridge/rows/1/python` | `b2ccee0ac465034edb343f72bd52edefaacbf7b405c5ece7815a0be9460dae1a` |
| cg-foundations-01-names-values.json | `/bridge/rows/2/lua` | `7a820c8904240e17a637309166af6b2023bdf54365f5d3a1c36bbbd0ef4eb5c7` |
| cg-foundations-01-names-values.json | `/bridge/rows/2/python` | `3456841bd5b81c6b22c05acb6faba194ec59096c64fceeb7a6d055e94513cdf0` |
| cg-foundations-01-names-values.json | `/bridge/rows/3/lua` | `25fee446d8b59581b27f4b31a6701bcfa7755fb4143cb4231c05a5c61d3c42fc` |
| cg-foundations-01-names-values.json | `/bridge/rows/3/python` | `e5fe6fecde546a822900197fb2d1168d84f830d5f3243e0656a734306da490ea` |
| cg-foundations-01-names-values.json | `/bridge/rows/4/lua` | `4bcf3a8a441295bd3b7aa0da052bc9a93869311cbe48b7dffabccb110b51d867` |
| cg-foundations-01-names-values.json | `/bridge/rows/4/python` | `007fa65d11085fe922b7f7cb74a8eafb833a0125294b3959bf08ed935db04212` |
| cg-foundations-01-names-values.json | `/bridge/rows/5/lua` | `872f9eb332931990ddc08ba166985bde0e4d913f5b94f0460404f9885d4a20a6` |
| cg-foundations-01-names-values.json | `/bridge/rows/5/python` | `096938ce6ca6ab8881a1e9cd318a25e8b0eeab2beb42e077767e9d2939146d31` |
| cg-foundations-02-conditionals.json | `/activities/0/code` | `c920feacaf8a8bcb32a891a8e9c31b6155b9504edc44c5974fa5346cfd05368f` |
| cg-foundations-02-conditionals.json | `/activities/1/code` | `860f54b1f7c8ebfbd433df9b8df469db08882143ba2dd04ef1ad7c47aaacb80a` |
| cg-foundations-02-conditionals.json | `/activities/2/code` | `4754bd8072fd0cc80a795a7be60547821d45543e79e587e6bdb8097a3c3983c5` |
| cg-foundations-02-conditionals.json | `/activities/3/code` | `148cd7482a48b09dfe6f9c11989e5e59b5cf4518406c6b484d8e559a295e3fca` |
| cg-foundations-02-conditionals.json | `/activities/4/code` | `575c806fee38a8a8e9f3cebc4756643001d516eb6b21ec86097cbbb3c02e7fb6` |
| cg-foundations-02-conditionals.json | `/activities/4/fixes/0/fixLine` | `4e3a0668b985bb16c427dba4639c2dad22ccd2eec0ec63e36955eaa79f951a5d` |
| cg-foundations-02-conditionals.json | `/activities/4/fixes/1/fixLine` | `8bcaf68f7e1af6def315a08b14a1313d020862f8448a70c5bbf0a74789cc5b48` |
| cg-foundations-02-conditionals.json | `/activities/4/fixes/2/fixLine` | `245f81f7480f318e1b99c53c793605bf846968e25da11204f287064e2e78d02a` |
| cg-foundations-02-conditionals.json | `/activities/5/distractors/0/line` | `ea1777e498c1d14a9bfa3a471965cf4fa11af70ff37524b7620e3d3736f7c4d1` |
| cg-foundations-02-conditionals.json | `/activities/5/lines/0/line` | `bb68624843efe654e4e79efb83fedfecd9e392d3c87f1b60aee485b09c4e0757` |
| cg-foundations-02-conditionals.json | `/activities/5/lines/1/line` | `b915854cf7bf5ee47ce766e33a28124a47ad61616e8f4446b5f3de2098e7ef86` |
| cg-foundations-02-conditionals.json | `/activities/5/lines/2/line` | `8e98a837db696340c3f87a0146c27ee63e5599f6803fc414a4f448ab4a44ec23` |
| cg-foundations-02-conditionals.json | `/activities/5/lines/3/line` | `b842c21b96356e450b2c4b7c7f551ea1635bf0b0ca21387d4769210322fc1516` |
| cg-foundations-02-conditionals.json | `/activities/7/code` | `b2521df23e4b6f24dfa120dee7d34dcad9d740b327d1ef7eab3b37574ad82e60` |
| cg-foundations-02-conditionals.json | `/activities/8/code` | `91390165f9c845a64456f73a3529784990cf51cb42ca434c213ab534c43737bf` |
| cg-foundations-02-conditionals.json | `/activities/9/code` | `5feb236e25b7a6b5f7157058b514b4af574f223442525ae11a9fa61f6d9317ac` |
| cg-foundations-02-conditionals.json | `/activities/10/code` | `213772c2d461dcd0995a03c707d592affa4548b245fff43baca93a5d36e33447` |
| cg-foundations-02-conditionals.json | `/activities/11/code` | `7d2eb79072c70999c2d07f167d0a5447965c008226575da89505f59040616118` |
| cg-foundations-02-conditionals.json | `/activities/11/fixes/0/fixLine` | `213a479ac01bd0eb4f8549c6709da1f8cd5d3e8202f7b61b63f3e60bca149b18` |
| cg-foundations-02-conditionals.json | `/activities/11/fixes/1/fixLine` | `4194f3b5f9ca9f2804d243e368c46989af56762e755d624972e043f44197a15d` |
| cg-foundations-02-conditionals.json | `/activities/11/fixes/2/fixLine` | `0afb80d867c9112b59482fea90125993732a627163f95f3369f0d4a3e40a0061` |
| cg-foundations-02-conditionals.json | `/activities/12/code` | `c64e2206771f9132fd1d6a8a5eddebf4b8497e1d4a2bc161e8b489a1f443e9e8` |
| cg-foundations-02-conditionals.json | `/activities/12/fixes/0/fixLine` | `9723bbbb340e3a27afed23963a5a255354e5911c0f67e58976b087876fc622d7` |
| cg-foundations-02-conditionals.json | `/activities/12/fixes/1/fixLine` | `f8ba7d5b378909ad0182d95591ed477ae9cd17be0d3b042773583c201853eda9` |
| cg-foundations-02-conditionals.json | `/activities/12/fixes/2/fixLine` | `55442700915890d758912828ace65a8842f66e242b1e89f4881a620d037e7844` |
| cg-foundations-02-conditionals.json | `/activities/13/lines/0/line` | `f7b472f006aaaadd3a5ffc03ccecbdf5beaea685c2a5e96df2f557029730986a` |
| cg-foundations-02-conditionals.json | `/activities/13/lines/1/line` | `394f7d638a1592fa1b7b56eb83a48704636642b8928a9e32101985266eef6142` |
| cg-foundations-02-conditionals.json | `/activities/13/lines/2/line` | `9db229b5d839ba34127f6eabccc789c0853b294a2318ee0181812c8973d3a452` |
| cg-foundations-02-conditionals.json | `/activities/13/lines/3/line` | `fc510de369b8eaed357b1ad1688e6368b812874feafceaca7ac636ccf7e90137` |
| cg-foundations-02-conditionals.json | `/activities/13/lines/4/line` | `fc5c0cecdded0ebebdfac93bb3ccfa5f5ef47ebbc9d120a2c2ecb446ba2bb773` |
| cg-foundations-02-conditionals.json | `/activities/14/lines/0/line` | `d9e0a858f2ddf5f5405ffe0eba72f67d48351c6c58036762f4a4b1ad5dd0ff65` |
| cg-foundations-02-conditionals.json | `/activities/14/lines/1/line` | `cbefbfc89f2262e4a3f82a52cf67ec20a1f2e75353fe1117ee9de8abce615abc` |
| cg-foundations-02-conditionals.json | `/activities/14/lines/2/line` | `c831d76d89f64a1b5571e8983d152056b7d4218125b10295e86cd7f9557e89a9` |
| cg-foundations-02-conditionals.json | `/activities/14/lines/3/line` | `f562127f6e7805bc6a633e5a324d266e4f514419fdf2812f6ecef71a1970a9d6` |
| cg-foundations-02-conditionals.json | `/activities/14/lines/4/line` | `3f154f36424961abae657bbffe1e1acfc40f5533e43569c3f953defa9ac9db09` |
| cg-foundations-02-conditionals.json | `/bridge/rows/0/lua` | `12ab0c61a3cb01f07d9d8959efb7c1db054db94f21e74f687f0abe23cadc8342` |
| cg-foundations-02-conditionals.json | `/bridge/rows/0/python` | `a44c184f535c24509aa22c4c48794ecf27938a612df9b1051f7dbdfebf0040b7` |
| cg-foundations-02-conditionals.json | `/bridge/rows/1/lua` | `3a3eb7cfa9c6b4218f69559db476a0576de580cf46afcf0a21ab4ac56d8ae8b5` |
| cg-foundations-02-conditionals.json | `/bridge/rows/1/python` | `996f98659dd279eae2507105b7a3a986132e2cb3d286c5109369517a0a4af4d5` |
| cg-foundations-02-conditionals.json | `/bridge/rows/2/lua` | `f970375ca1db5b6983c0e18c5aac17b34a5aa3096397ad3b39b3ddc479bab16d` |
| cg-foundations-02-conditionals.json | `/bridge/rows/2/python` | `d4d1834186e0a94df520b5d4e6c69241e7e212fda76a1889388718fed56baad6` |
| cg-foundations-02-conditionals.json | `/bridge/rows/3/lua` | `4c0d4f0f688754f2b6e1add62182c7b2101abf5de31d811f8fa777e3443579f7` |
| cg-foundations-02-conditionals.json | `/bridge/rows/3/python` | `4c0d4f0f688754f2b6e1add62182c7b2101abf5de31d811f8fa777e3443579f7` |
| cg-foundations-02-conditionals.json | `/bridge/rows/4/lua` | `58d2b2d980471cfe4d66963594f10a0d13f118e75f25fd01c057f7a7684b1ccd` |
| cg-foundations-02-conditionals.json | `/bridge/rows/4/python` | `56f2cd720778b2686df9b1ad0980d6d1389cfad74e6a1139dae5c656c1a32a26` |
| cg-foundations-03-loops.json | `/activities/0/code` | `ca0f8f7012c342ce44ee4ab147bcf7557779e83eeed2714828570168bd7e018c` |
| cg-foundations-03-loops.json | `/activities/1/code` | `22ac3f4727e039663350a78dbcaf609ff09a00f161747d13c182c9019f7d4a00` |
| cg-foundations-03-loops.json | `/activities/2/code` | `ce16ed9d7eac691a7655014562b47ac7bb00b5179a146385b3f35c8c47267fcd` |
| cg-foundations-03-loops.json | `/activities/3/code` | `8566aa273647efe18b986b2c12942b5dd1ed749f6cae94c532d520100fbd871b` |
| cg-foundations-03-loops.json | `/activities/4/code` | `ee9a8f4c3e9d5610e610e1848b730f1655b11b423fbf1a178ec02286da360f35` |
| cg-foundations-03-loops.json | `/activities/4/fixes/0/fixLine` | `1b2646bbfc0e4b7d1aaa1a9d758ef550360ecc685c376bcadb3b12c3b75e1ad4` |
| cg-foundations-03-loops.json | `/activities/4/fixes/1/fixLine` | `139a414365429e4a95dd2a8c581b565c888f9ecdd9b319e722713406c8cf801b` |
| cg-foundations-03-loops.json | `/activities/4/fixes/2/fixLine` | `1c1571de5f66666074b2d1b800cbe65504c9705150f020c7e2e7bd48812dde2a` |
| cg-foundations-03-loops.json | `/activities/5/distractors/0/line` | `175e8c46fcf4cf4cd524f22882f3105a0a0389899788ffd587ed5510006e27e7` |
| cg-foundations-03-loops.json | `/activities/5/lines/0/line` | `12ad5f41550418a539a13b3599f4c64b025a543c81da885dcc5e2e9469c149e7` |
| cg-foundations-03-loops.json | `/activities/5/lines/1/line` | `512a4b4a267e06b49953b0745da8753063d452194765e19750b8308ceb05a8ed` |
| cg-foundations-03-loops.json | `/activities/5/lines/2/line` | `b6a90a69db2fdbb244e8310f5c0061f1a17893ff9cc4a8c02dd81ee44dec4299` |
| cg-foundations-03-loops.json | `/activities/5/lines/3/line` | `33375db46665a14ca291274b9776fda20e52199b365c0de0447110952292195d` |
| cg-foundations-03-loops.json | `/activities/7/code` | `7ea2210001a82c817a1143974236841e6a7fa7c644f00cf0e45f35736e57dc31` |
| cg-foundations-03-loops.json | `/activities/8/code` | `5973c29a6464433f06836aad6ca83b515444376cb8358f93971f2562830ee5c0` |
| cg-foundations-03-loops.json | `/activities/9/code` | `cd557d80153581a64561f5af9473ac5e25f5abe14d19e2f461486dd590d3f714` |
| cg-foundations-03-loops.json | `/activities/10/code` | `6321ba38780d7072ad0f5c685a0554a221e666e1b8799fda246b2881835b2890` |
| cg-foundations-03-loops.json | `/activities/11/code` | `8ed73998c4706362d256b4a20039c5d1534dbda503f188983c9254b59bf730ea` |
| cg-foundations-03-loops.json | `/activities/11/fixes/0/fixLine` | `b6a90a69db2fdbb244e8310f5c0061f1a17893ff9cc4a8c02dd81ee44dec4299` |
| cg-foundations-03-loops.json | `/activities/11/fixes/1/fixLine` | `4e9dff06c3e895e16cf1c9192225b2b88b17d6a83c592e654a56b9823d363349` |
| cg-foundations-03-loops.json | `/activities/11/fixes/2/fixLine` | `2f3f0509cb66361df5937333d5bcdf5f31b7de268af7a8c841b24c242c154967` |
| cg-foundations-03-loops.json | `/activities/12/code` | `13365e18bbb8da5c1ecc778a4bde5c3287b72b3b21d1e5dbb484fcadd54a86ee` |
| cg-foundations-03-loops.json | `/activities/12/fixes/0/fixLine` | `8a63fac452ca90130559791cfb02f225c3acba203e6319bffb43c5659748ae30` |
| cg-foundations-03-loops.json | `/activities/12/fixes/1/fixLine` | `19107a2805bf6138a234a2323705cb30ed597117fd4b76c79f6f7bb0561e1a12` |
| cg-foundations-03-loops.json | `/activities/12/fixes/2/fixLine` | `e846a452816e4cfce42102e35dd08cf63d75e9ce6ac365ad5e49cb51639c30b9` |
| cg-foundations-03-loops.json | `/activities/13/distractors/0/line` | `0038423df9a51a9a7710fe5b7b7cd91031c8e16a61f24fe12ffb1b213f5b8ef7` |
| cg-foundations-03-loops.json | `/activities/13/lines/0/line` | `083d2261a04c0ff3ea6720a943523693077ab5ed365e97f2de23195831d1fd4e` |
| cg-foundations-03-loops.json | `/activities/13/lines/1/line` | `de51c211c6a1816d8377f72a7065566a0c8261044f83c3df7d1d8d6c8e2ea849` |
| cg-foundations-03-loops.json | `/activities/13/lines/2/line` | `7c4e5469acb5777c44074ecd795f4ad0c175dbe28faafe9394cee5fbd76d3957` |
| cg-foundations-03-loops.json | `/activities/14/distractors/0/line` | `e855e75d76a6fb4a98135e204fda888ec1e5cb5675e84db319af1b6b58486c04` |
| cg-foundations-03-loops.json | `/activities/14/lines/0/line` | `60897e49625fab2bed333815295988065c3a88e477f91ccd1c86a704f28af5ee` |
| cg-foundations-03-loops.json | `/activities/14/lines/1/line` | `f7d35a450bcc821156f8655d7e90bfe38f6014fd5e57472511bdb02c56ac6020` |
| cg-foundations-03-loops.json | `/activities/14/lines/2/line` | `517cc82443e5de265fc92099f8bb513c2fcf03d43e4adbd746f5e9733effcbff` |
| cg-foundations-03-loops.json | `/bridge/rows/0/lua` | `22fd3096a9e4d91fa7360af8d532ffe2fc5ce0264abc73eb3de57204d6ee0582` |
| cg-foundations-03-loops.json | `/bridge/rows/0/python` | `045b4d24f0b54365bc653987655edc083c0c6f9ef8412127e75bb6c526580a8c` |
| cg-foundations-03-loops.json | `/bridge/rows/1/lua` | `3fbc8d8db998f4913586d3d816bfddb25ce8157be45760c9f21d955af592cd40` |
| cg-foundations-03-loops.json | `/bridge/rows/1/python` | `1b2646bbfc0e4b7d1aaa1a9d758ef550360ecc685c376bcadb3b12c3b75e1ad4` |
| cg-foundations-03-loops.json | `/bridge/rows/2/lua` | `4f47a11aabc7c7664554e7fd3926412df8762d97c282652ac6e03e906c9afcb7` |
| cg-foundations-03-loops.json | `/bridge/rows/2/python` | `cf41edb0d34ebcf65140d1468478821773f7dd59054594a8d4c0817dc09bc4bf` |
| cg-foundations-03-loops.json | `/bridge/rows/3/lua` | `e733d739c0fa4d5d1892e4b26d89e074e079c87d1af8e0783197a1d4b6cf22a1` |
| cg-foundations-03-loops.json | `/bridge/rows/3/python` | `66f5ba423d8d64e88019229d4b379e124b188bbe4a5bc3d1d4a50c13780b4d34` |
| cg-foundations-03-loops.json | `/bridge/rows/4/lua` | `39ae9a2052c79aeb8d3acdf5d2bef43ebeb424fb59946c4846e7f641882d6531` |
| cg-foundations-03-loops.json | `/bridge/rows/4/python` | `abf5e6bd518a8bcfe2647057e45bbf2358c8d0bc438a91835feb6e4115c50b20` |
| cg-foundations-03-loops.json | `/bridge/rows/5/lua` | `bb163546deeee0f0c42e159d8da7095218af394a865cee2ee95ba94b340c6d69` |
| cg-foundations-03-loops.json | `/bridge/rows/5/python` | `bb163546deeee0f0c42e159d8da7095218af394a865cee2ee95ba94b340c6d69` |
| cg-foundations-03-loops.json | `/bridge/rows/6/lua` | `40104d6bb3e82e0f16b86718f4e37a63387429fb27552e5ec9acd82ea8b4e347` |
| cg-foundations-03-loops.json | `/bridge/rows/6/python` | `9aeaf2b3f51b680d550d7af212375ec0548dcb8375c6d0f396dc61ff0be2c298` |
| cg-foundations-04-functions.json | `/activities/0/code` | `aa86d0df8e8f8571d397675f2c9c1a8b43acf167e7d04da22aec2a28b913e100` |
| cg-foundations-04-functions.json | `/activities/1/code` | `c1574234295846088db3742b1b971fc7bb3089fec896136e2b4ff20d573b613e` |
| cg-foundations-04-functions.json | `/activities/2/code` | `50adf68108e10a6d985bc3fe70921ec15656b858a0f0eca552bacfbd04d26c11` |
| cg-foundations-04-functions.json | `/activities/3/code` | `e7da6ef93cda2ab862448a24c0a67795115fcb80ad8e84810213a3d5053f4a3f` |
| cg-foundations-04-functions.json | `/activities/4/code` | `145deaffc0acfea0e35fcca5299c89a06ef1568e1bf72fcaffc193fae4918776` |
| cg-foundations-04-functions.json | `/activities/4/fixes/0/fixLine` | `55efae6d8e713730f2f8ae62d6c72e41972ab318bb68a3e984ea0cbab8f63fdb` |
| cg-foundations-04-functions.json | `/activities/4/fixes/1/fixLine` | `f7ce794c5a3e220a93f33ab2faddc6e9782aa2d6d487a5aa1b47b2d6422ca76e` |
| cg-foundations-04-functions.json | `/activities/4/fixes/2/fixLine` | `ea0c5b1963b71c7e17c770e8da61c87a392685661a5ae512b829262521f2e876` |
| cg-foundations-04-functions.json | `/activities/5/distractors/0/line` | `1c153af9932f95d8dd1300c08bf7aac2e0efa51edbcecb2f48b39cbd391d196d` |
| cg-foundations-04-functions.json | `/activities/5/lines/0/line` | `f40002e381da3d00d5973deed3e63c71a4111b9625fcd964b42f5d0b2089526e` |
| cg-foundations-04-functions.json | `/activities/5/lines/1/line` | `9155fd146914d935d681e1b125cbe579b06265ed026aefc3dc957a97717eea49` |
| cg-foundations-04-functions.json | `/activities/5/lines/2/line` | `c1eedea5c47c4a7f04f9a2a987bf87ea22b6b08189cc0689de0f24fb92aa7052` |
| cg-foundations-04-functions.json | `/activities/5/lines/3/line` | `0243a6400b957e59006d36e0c9f2c3b232ab905f62d4876fc2581a117a53457e` |
| cg-foundations-04-functions.json | `/activities/5/lines/4/line` | `cba65ef349a41ed0da1582ede8d362eed8cae232c5dd93eb5a26c15862001dde` |
| cg-foundations-04-functions.json | `/activities/7/code` | `743edef237047cd8c91f17198c29445036586f18054c3763e550d9f70c62c7d3` |
| cg-foundations-04-functions.json | `/activities/8/code` | `ed7b0818a49928a833ae4835e0351eded2f1e1b44b341ed8300461fbc8c4b192` |
| cg-foundations-04-functions.json | `/activities/9/code` | `d48a293fed1cb3f1cd0b7e8610ea044f5c9a85ccb114987814b0bcfef3f8dc31` |
| cg-foundations-04-functions.json | `/activities/10/code` | `43c069376674d1843b0914989c6ec8e3c74a9c4927703d3b39d68aa267f4676b` |
| cg-foundations-04-functions.json | `/activities/11/code` | `0ac64fc58a53890b3628ddcbca845466eaef9b8d4f5e1db49421e4fc15aede64` |
| cg-foundations-04-functions.json | `/activities/11/fixes/0/fixLine` | `ffa3b60aa8b8a02f755717159f75653481f99eb1184f6da85df66ebebda55ff7` |
| cg-foundations-04-functions.json | `/activities/11/fixes/1/fixLine` | `0519c04f20a6afe45bceb036406dc3910585cd190e7ad2b4cb5c46e86663bb1a` |
| cg-foundations-04-functions.json | `/activities/11/fixes/2/fixLine` | `c36dcb4394af91d0251125481268053b25ebd185192020b45b9093b5220dd9f7` |
| cg-foundations-04-functions.json | `/activities/12/code` | `6bdcc0b731d4fe74f38ec6b8189f7dcedf83f702f6eac9773600998a37ab6615` |
| cg-foundations-04-functions.json | `/activities/12/fixes/0/fixLine` | `a326b6ec8a3db7614d571e951afb0ee7e6f86c03a77b7bf67b9d3f172dcfda8b` |
| cg-foundations-04-functions.json | `/activities/12/fixes/1/fixLine` | `0d8f224091ad055ee4ac3373b2dd1b4baff5bb713abb0dc59298f8f746033000` |
| cg-foundations-04-functions.json | `/activities/12/fixes/2/fixLine` | `f044c501d39f9779dc285d5a92c02758b074732a0d88d36ec705b27bb2f924bc` |
| cg-foundations-04-functions.json | `/activities/13/distractors/0/line` | `0bc1ac884601f7611112785bacd318577ef71a57b0379371bb53622917d92454` |
| cg-foundations-04-functions.json | `/activities/13/lines/0/line` | `26a49215ae6872451b619f2702bc10940cececa905cb81ed12a25766bf18b27d` |
| cg-foundations-04-functions.json | `/activities/13/lines/1/line` | `61ac27e64183311f111ad2b51da404c93fe98397de717bd4bc144251b9363571` |
| cg-foundations-04-functions.json | `/activities/13/lines/2/line` | `8022aa4811fec4ffc0718ca92f5c35ebc12bdcb8ec74eb90f66663c45696ee52` |
| cg-foundations-04-functions.json | `/activities/13/lines/3/line` | `1de5557d3d1d27c0c11ead0115a91011208593a27a50411013ff0a59040b0295` |
| cg-foundations-04-functions.json | `/activities/13/lines/4/line` | `585a066c5168e9b025059a1099ece68932052ccceba1776d4f288871fc707581` |
| cg-foundations-04-functions.json | `/activities/13/lines/5/line` | `8387e572d1b9f638e361fb928c863f87bd474312b42448fb79a1266a0d152660` |
| cg-foundations-04-functions.json | `/activities/14/distractors/0/line` | `c285e20dfdd1201eb21fca123bab2c715c005028c758cbcc0b9fe251cae5e32e` |
| cg-foundations-04-functions.json | `/activities/14/lines/0/line` | `94386aab7e2fb28126078c394c414f8fc89fa4f9b05abb9ba2d5fedf0bc96ec1` |
| cg-foundations-04-functions.json | `/activities/14/lines/1/line` | `f9aeda747d21a09d3a141503038ae3a589bb8352a093613eaab8e2cb6ef36fe2` |
| cg-foundations-04-functions.json | `/activities/14/lines/2/line` | `48429d0869a73e12272c7b8310223fe0dc53130238b543a2bbe880ed3487e919` |
| cg-foundations-04-functions.json | `/activities/14/lines/3/line` | `48b03f3e5061751d1cb15a28715a67921e4e739e259958d97206ca3867a131a5` |
| cg-foundations-04-functions.json | `/activities/14/lines/4/line` | `9b83b48e367488c9afd46f404c687ec6ebfdcd99c31bb421a8801f7e31217446` |
| cg-foundations-04-functions.json | `/activities/14/lines/5/line` | `0f76968e5ccf33549c31d5355ec9ab3f09d673d3042d633f1d9ce13c334d441d` |
| cg-foundations-04-functions.json | `/bridge/rows/0/lua` | `6a33f25fac290b1f326e0ddc30a7555d083b105e659180b71cf4dd2b50d33fda` |
| cg-foundations-04-functions.json | `/bridge/rows/0/python` | `8b4a8902352435024f0dd4e6732652a99ecb40833d19b92f8885f3570400322f` |
| cg-foundations-04-functions.json | `/bridge/rows/1/lua` | `5b179d83897507415d3e0aee427c49d097eaddf88ed0705351dbda9aef878e6f` |
| cg-foundations-04-functions.json | `/bridge/rows/1/python` | `fb757faa27187624cfb50ee67b701095b16c5ef1dbb41f42f670f634fc3589f0` |
| cg-foundations-04-functions.json | `/bridge/rows/2/lua` | `736e7980601bc0619e1e88239dd7a19aad790d5e6293951c4e901e8a3f687b6a` |
| cg-foundations-04-functions.json | `/bridge/rows/2/python` | `a5da259d7cad2c9c3e70f588fafcb9dbd1eb260e7fd30859849c3e46f2aeecf0` |
| cg-foundations-04-functions.json | `/bridge/rows/3/lua` | `d64908326f8a0747bb245353b87cc02de883bba70ce1feae180f82a1c5ee3824` |
| cg-foundations-04-functions.json | `/bridge/rows/3/python` | `d64908326f8a0747bb245353b87cc02de883bba70ce1feae180f82a1c5ee3824` |
| cg-foundations-04-functions.json | `/bridge/rows/4/lua` | `d351ae60611c370990d2d81396f3f67af7eea2b53d22a6029248c83c238c24ef` |
| cg-foundations-04-functions.json | `/bridge/rows/4/python` | `a5dd37d360401b9d75acd5146c67cae083474a77313c3261979d1a4d229aff19` |
| cg-foundations-05-lists-dicts.json | `/activities/0/code` | `b4b53f062f36c2fca163111f4bd0a5d83ca732ad83b0f3a4542d2ec600fb33b4` |
| cg-foundations-05-lists-dicts.json | `/activities/1/code` | `13109d7e9f4c8437d246b3d2a870c7b0103f812da81c5f12306b145192ee4956` |
| cg-foundations-05-lists-dicts.json | `/activities/2/code` | `57fe24a73e1b79175fc09e87cadab0f3aec87116b7aa52cb0712035fda622680` |
| cg-foundations-05-lists-dicts.json | `/activities/3/code` | `8c024b57666e8938e02a34cfba1cf93d53c2045b2da8675b127184db20c595b0` |
| cg-foundations-05-lists-dicts.json | `/activities/4/code` | `5b39dc31b4325abe998b34b01dae710c4bbde0886791ba0eae48cca9c3b87c48` |
| cg-foundations-05-lists-dicts.json | `/activities/4/fixes/0/fixLine` | `4bc8c4b5f60560d568cc6b1010909aab101e9d904f014a6bb2e5cbd352510085` |
| cg-foundations-05-lists-dicts.json | `/activities/4/fixes/1/fixLine` | `b0d0d43ff67a0120f3b603c15bd60001c9a171206eb1fd8d23f56bd6a20b0bee` |
| cg-foundations-05-lists-dicts.json | `/activities/4/fixes/2/fixLine` | `c4539c55d8a98cc589f6ff265df5526789ea7138d090120e7286764d3212e2ee` |
| cg-foundations-05-lists-dicts.json | `/activities/5/distractors/0/line` | `a056fa63e967cd801294e5859e58d536b1f7793489a2c9b32da66df59c00f54d` |
| cg-foundations-05-lists-dicts.json | `/activities/5/lines/0/line` | `a1e479a51fd5ed6b346e4660854978cf2188e44a8d92abe626bab6a861004ab2` |
| cg-foundations-05-lists-dicts.json | `/activities/5/lines/1/line` | `dd2d741fc7639781e44971decb2b85d8b379c17b520a468e54665257a6107aa4` |
| cg-foundations-05-lists-dicts.json | `/activities/5/lines/2/line` | `87c0ef359cb4ffc31d4611823b5a3d4e55c19c01b2f1fa1673fbb35c9d6e5845` |
| cg-foundations-05-lists-dicts.json | `/activities/5/lines/3/line` | `0a9b7348c83741a57d4b697e269638bb8eda40a07af22d435eba2bc3e8f8129e` |
| cg-foundations-05-lists-dicts.json | `/activities/5/lines/4/line` | `75e881a2b2ba0609dec16b249a60f14a047c2cf7b3db0a80fec2c754230d2456` |
| cg-foundations-05-lists-dicts.json | `/activities/7/code` | `5777fbb40c9b890d7d31a2bcb6316d380d22704cd7ab668bb6fbd2e74c9f0045` |
| cg-foundations-05-lists-dicts.json | `/activities/8/code` | `20585ca776871a674d1794af1c84cc0b67ddb75fb2c071e5b5395a68d1d90b57` |
| cg-foundations-05-lists-dicts.json | `/activities/9/code` | `afa49b74ac2ef1c54e5bb0c789234586723cddb042a198999519e0f99bd2ba76` |
| cg-foundations-05-lists-dicts.json | `/activities/10/code` | `bd3c0c3a4abee29f9e899cd04525de4675926b05eb8142c6cda2269027bcfdaa` |
| cg-foundations-05-lists-dicts.json | `/activities/11/code` | `f28425d7db87f08dcd506759927f083ea673fda28c9c1d3bed9700fc435f718e` |
| cg-foundations-05-lists-dicts.json | `/activities/11/fixes/0/fixLine` | `579a3b89137bbcee9dfe91337079a6d453f1a1744de206242b7b23563fe8bb01` |
| cg-foundations-05-lists-dicts.json | `/activities/11/fixes/1/fixLine` | `3663fd498a702f85598798a5ee0d31f53373b0f3aff5c0b911dcb266955eafb5` |
| cg-foundations-05-lists-dicts.json | `/activities/11/fixes/2/fixLine` | `52c91ce07323ad3e039ed4016d9aeba130a3673ef45e1e3fe624536694271f8c` |
| cg-foundations-05-lists-dicts.json | `/activities/12/code` | `010c428fdc23b6385e0444525cf3c4a8cdc3ffffc38b22e1e30a2f81c5bd06fe` |
| cg-foundations-05-lists-dicts.json | `/activities/12/fixes/0/fixLine` | `a42c417ba08340dcf0ef7eef6870586bc0b3d9e7320e6581af98af5419336ac0` |
| cg-foundations-05-lists-dicts.json | `/activities/12/fixes/1/fixLine` | `3be044940140af297e3bdf481b07172fc6b992e693a69ed0de8a99232aafd4fe` |
| cg-foundations-05-lists-dicts.json | `/activities/12/fixes/2/fixLine` | `831ee896fcf78bc7307c655aa27de5bfa7291ba8a95052fbb82c3f0ea853bc0a` |
| cg-foundations-05-lists-dicts.json | `/activities/13/distractors/0/line` | `f4470abe821bb1b170649a9330b6faff42cce2aa45a5dfcd22dabc4dbbc56638` |
| cg-foundations-05-lists-dicts.json | `/activities/13/lines/0/line` | `52b2bdf9377ed8a2a0bfaa2774174042f40f8b56d8ba2dd363538006c2badbbc` |
| cg-foundations-05-lists-dicts.json | `/activities/13/lines/1/line` | `0edc0ede37147ba535e923a56f8435b3f012e15c26e11d5186d010b3781605b3` |
| cg-foundations-05-lists-dicts.json | `/activities/13/lines/2/line` | `02a422825dd9472ae58c1cfc763bfecb10382970e40108caf82aba226102e465` |
| cg-foundations-05-lists-dicts.json | `/activities/13/lines/3/line` | `07ea21086b14a269265b5a0fb6526719416db38f3ab1375bc16c1002c53e1f03` |
| cg-foundations-05-lists-dicts.json | `/activities/13/lines/4/line` | `0a01e99efd6b23c3341239bd3aaf87ba8f7ef712427b413c87a46d4ae7c8f1d5` |
| cg-foundations-05-lists-dicts.json | `/activities/14/distractors/0/line` | `c335d3534013f3ed855122f352eaec1fb872437b7f89335dd9ff014cf558ecc4` |
| cg-foundations-05-lists-dicts.json | `/activities/14/lines/0/line` | `c1f26ae8cf357161b29b596fd06b7b92a4924559cc110b57621ddcc4eaed2469` |
| cg-foundations-05-lists-dicts.json | `/activities/14/lines/1/line` | `710ba01cd994216dd07af71dadf2d8621b71f4879829b7805acf5119c0f8ff79` |
| cg-foundations-05-lists-dicts.json | `/activities/14/lines/2/line` | `efea74e18318dffc1037235f233248d8c699e362380c7d91daa7e0f6fc3ac529` |
| cg-foundations-05-lists-dicts.json | `/activities/14/lines/3/line` | `2ec12ff405b9d971c92ee75052c8ff0833168aedcfe2e1ac1b965a6fcc2d85bc` |
| cg-foundations-05-lists-dicts.json | `/activities/14/lines/4/line` | `ed61f50f050917bca9415a653f779b2c8e4451e0aa2a0c9f390a60fcbd7b5954` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/0/lua` | `08dbbdf5f09bf51988db2f83bbe7f289410312c8d59b93b67d45c1bf39ca034b` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/0/python` | `e0fb2e147ea8f34b550674f23dc29f5a09722d4d66a1b06069407ce11a5c0f1a` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/1/lua` | `7d1b764d3ee4d2de1fd94ab62dd31b8dc17d1d9b9a31f45145ccfdfca99fb01f` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/1/python` | `0d80c556f81e0c182b57cd1a105591cc9b9678e3943df658213ea3291b17549b` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/2/lua` | `49e79f9ef477c30d5fc5d8d29d934b4fdbdc9fd9e50c8842692833b2be97cbe3` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/2/python` | `c5c79c2f859f989fc03d6fcfc2b1701b100dd2d8855b2e526975f59190fbc3d4` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/3/lua` | `8e3fc5c7ae4cf81b88aa3125d2390014111b894694c9f57d885d4b6111e74c96` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/3/python` | `26a1b901c220f750521e12e36428000e485fea43890698071cb3b2303c88db33` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/4/lua` | `aa5708b9b6748e4a70a87715f72659fe6fe6e610818743712ad0dcd0e1f859ca` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/4/python` | `0c62665505600f2d22bc0e5f3dd39989485e7493c63db08f7759091df30a06a7` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/5/lua` | `1ba2f13309d42c1debb5a8b453067ec38015b8d8dd701f30327dc928ae0241e5` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/5/python` | `d87fe929fd3d202d1f51b418f6931d726e82d160440056bc0e695958921f07cd` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/6/lua` | `9c6f692531554bc213442ff8285cc19cbb9aae4b3b6bc00a9e41650f272b6561` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/6/python` | `ff5f8dd5d23f3998f0ad6c629c2b6cd827b8a9a8379e48c5c36c9d3dc2f4ca4f` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/7/lua` | `bb31746496b1e0382f91d1d6e07e01286dc2ae3e9f9656c01cdd2dc439547c71` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/7/python` | `9927ad4f2267e44a093d41e34d446d844d398439088a2f99e6883e3405d9e246` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/8/lua` | `5721a2bc46bda7ef8fa872670d1d8ff65b0a7705f607d9cae806da81ce871fe2` |
| cg-foundations-05-lists-dicts.json | `/bridge/rows/8/python` | `6b8422a4e177c253f150b8f3439b2bc653d5d105614e299d7d9e2c3fcfaa2602` |
| cg-foundations-06-recursion.json | `/activities/0/code` | `ed9f3a7c12193bc0c1a9683b62e5193ebb34d6253043457c68b5d50423a9db12` |
| cg-foundations-06-recursion.json | `/activities/1/code` | `539dc80dc0ce5aa1c6d20b6fbbb06e92423b9373870887cd5a63253af334549d` |
| cg-foundations-06-recursion.json | `/activities/2/code` | `422794d86b305dab3bd52f627eeca9d7391bdeef75c195ad178e749631079306` |
| cg-foundations-06-recursion.json | `/activities/3/code` | `da84ed53d3791df3515d5f0990a53ba50bf836b85cd80816f8af09bdd24f0a10` |
| cg-foundations-06-recursion.json | `/activities/4/code` | `40d4c82038c00322fc29dad23b8baed8c67b0a3a036c0aac99723957373ae9e5` |
| cg-foundations-06-recursion.json | `/activities/4/fixes/0/fixLine` | `9fdffca7226696fdb61229012e5268ef85848e4b2284594fecc257d0959799d5` |
| cg-foundations-06-recursion.json | `/activities/4/fixes/1/fixLine` | `e2684d39358a1ff7b748d21e09422f32882e29270ca47750f3a8b86b5aa3354c` |
| cg-foundations-06-recursion.json | `/activities/4/fixes/2/fixLine` | `dfb4f02e414597c89c3cdacf17c0a38871df05f92c5e6615eda5afea37eb3558` |
| cg-foundations-06-recursion.json | `/activities/5/distractors/0/line` | `acec239d4c0c81bebfef81a9b148cca871d2a434bad47b1987dff210abcccba2` |
| cg-foundations-06-recursion.json | `/activities/5/lines/0/line` | `c98d8b0d1cfcac6de25b970d64efb6ebda13b60d73de425e5e0e0eb248c78eb6` |
| cg-foundations-06-recursion.json | `/activities/5/lines/1/line` | `9b7e2189eb9092b66d08e02a6e6fc7b6ffea1cf2540e899303b6751166df25e5` |
| cg-foundations-06-recursion.json | `/activities/5/lines/2/line` | `21134e6e35015d1c158e84bbd6ec9f58e76aaeee3107450d454c1198b7286863` |
| cg-foundations-06-recursion.json | `/activities/5/lines/3/line` | `991d9c970775d5ca01b37485570e8142e2173e1eaf3312e2e7104c03cab6e18c` |
| cg-foundations-06-recursion.json | `/activities/5/lines/4/line` | `99533e36ca1500f94db7a7542d913543db1b2e602042bea0dc5c171b6be87510` |
| cg-foundations-06-recursion.json | `/activities/7/code` | `30579fc9ba5d7dcb7ada03e6f46aa2d4cca710775cf49533832480363eeacfa9` |
| cg-foundations-06-recursion.json | `/activities/8/code` | `f93edcbf4caaa26a1359d62330d3ba8559640ae957dba8fee1bd577f829a20d4` |
| cg-foundations-06-recursion.json | `/activities/9/code` | `3dfbc26bdb906203e68801bfffb1b0fc7a027331d44baed7d47e8c550b03f934` |
| cg-foundations-06-recursion.json | `/activities/10/code` | `a09eb973c39784bebe273f7acd6222f602286b2f15acfccd56e3d3d5afe6815f` |
| cg-foundations-06-recursion.json | `/activities/11/code` | `b31a0349f0b448daead4742110f79efab77c6b69416507da86150d8eec82d06d` |
| cg-foundations-06-recursion.json | `/activities/11/fixes/0/fixLine` | `ecc13d454caf65cd25b5bf6af22d01f709dc0e8e0281800468ac687ac643df37` |
| cg-foundations-06-recursion.json | `/activities/11/fixes/1/fixLine` | `405d68bf2468b7e8e24ee0542df2eca02ad4eb289d1eb0671740149b7fbc4a0b` |
| cg-foundations-06-recursion.json | `/activities/11/fixes/2/fixLine` | `61b916bfd87b04398b0b08364393443d5ccd3aee077dfde60dd78c04b19c47b3` |
| cg-foundations-06-recursion.json | `/activities/12/code` | `94ff1fbebafd93c83c225e870e00e300bef781273d06828a811305621170c36d` |
| cg-foundations-06-recursion.json | `/activities/12/fixes/0/fixLine` | `92dec1653d08d75016bfa326d1f3f7d0a02662a3dbda4dc93c59e22d6180ca25` |
| cg-foundations-06-recursion.json | `/activities/12/fixes/1/fixLine` | `bec6b51b1a6defc761d2d37767ca9ee0db00370ffa79546b0007fe184faf87de` |
| cg-foundations-06-recursion.json | `/activities/12/fixes/2/fixLine` | `63a8315e14cbda8eb197d91018d2b5b545602195e8b443885d2fa7a7025eff5c` |
| cg-foundations-06-recursion.json | `/activities/13/lines/0/line` | `439d47d8808a8e17dbe4cb9ed596aeebe38fe994a5527f80452d6ea1feec4598` |
| cg-foundations-06-recursion.json | `/activities/13/lines/1/line` | `fa00960fe35256600c3b8ca5048d18beff5703a08d03d6b55fb5f15355e941f6` |
| cg-foundations-06-recursion.json | `/activities/13/lines/2/line` | `e79a0befb602af460b105b8f02b73b4bbd2cf3e90675210a7264415dfc627b9e` |
| cg-foundations-06-recursion.json | `/activities/13/lines/3/line` | `b27415e4916e9eb1f0c8511cc2cd9dfedfdc644b2a2723e373c68b0736187b37` |
| cg-foundations-06-recursion.json | `/activities/13/lines/4/line` | `70c4303a30f32b40e63384565c0b2fdb3ac164884bb60806dce20d686175bf40` |
| cg-foundations-06-recursion.json | `/activities/13/lines/5/line` | `21b9710546e3a27bb69b4196ca9e170262b98841b20e6ff0b04a59df8fe75449` |
| cg-foundations-06-recursion.json | `/activities/14/distractors/0/line` | `21134e6e35015d1c158e84bbd6ec9f58e76aaeee3107450d454c1198b7286863` |
| cg-foundations-06-recursion.json | `/activities/14/lines/0/line` | `26abe79aefe04a69967f1ae2734f4688008fe75b0150ba1c99f375458e82bad3` |
| cg-foundations-06-recursion.json | `/activities/14/lines/1/line` | `fa00960fe35256600c3b8ca5048d18beff5703a08d03d6b55fb5f15355e941f6` |
| cg-foundations-06-recursion.json | `/activities/14/lines/2/line` | `ecc13d454caf65cd25b5bf6af22d01f709dc0e8e0281800468ac687ac643df37` |
| cg-foundations-06-recursion.json | `/activities/14/lines/3/line` | `bd99dc26238bcab69a6e460d6de588f59ad8d8733db9e570c8b9d21440dfeccf` |
| cg-foundations-06-recursion.json | `/activities/14/lines/4/line` | `a368304635d68632d201ce453aafc65cbbc0765f3478f400cde4ce93f7754092` |
| cg-foundations-06-recursion.json | `/bridge/rows/0/lua` | `263322577e16ca7a78a14db19ded62e5d43760af4a9a6eb401366d01229d214c` |
| cg-foundations-06-recursion.json | `/bridge/rows/0/python` | `7645c17db888e5e538d00d672c439b0f534cfbb7aaa0755fd370984518d3f0ed` |
| cg-foundations-06-recursion.json | `/bridge/rows/1/lua` | `fdbefdbf7d46bcf3ab57d85013091cd6cbe88043ab13c888b70a0b7f6aef40ae` |
| cg-foundations-06-recursion.json | `/bridge/rows/1/python` | `2ec415127d0e5444bd910905af29732bb118260232081a4e74d48f36224179a2` |
| cg-foundations-06-recursion.json | `/bridge/rows/2/lua` | `913e7d70e0cafc4c9633909549f69c9a99793a6e420e6602e66ad03cf4056f29` |
| cg-foundations-06-recursion.json | `/bridge/rows/2/python` | `654881f50f89b337961fe3fafa3759324d1757d13632f5fbde7d20beecf99007` |
| cg-foundations-06-recursion.json | `/bridge/rows/3/lua` | `b86635c9257d297fdfdfd70f896a5a9e38ff283dfb6bb8ea268cf775c8e8f554` |
| cg-foundations-06-recursion.json | `/bridge/rows/3/python` | `0110841abb03fc331d49c322c1b224d4bb1ed9f46e9ac7c6eb7fa40294906819` |

## Withheld source subtrees

These hashes identify excluded source values without publishing their contents. Origin: original by owner AI agents; disposition: excluded under learner export contract. Lesson filenames are relative to the source scope above.

| Source lesson | JSON pointer | Category | SHA-256 |
| --- | --- | --- | --- |
| 01-names-values.json | `/relatedNative` | relatedNative | `d34d9c5979ab88144ff8278d7c902452b04dbae476a73c1f37b0648204a01c67` |
| 01-names-values.json | `/provenance` | provenance | `749d5efb7a1e45b66e223cc108723d49200d6bd31053fedf7101f7f18b24f51a` |
| 02-conditionals.json | `/provenance` | provenance | `749d5efb7a1e45b66e223cc108723d49200d6bd31053fedf7101f7f18b24f51a` |
| 03-loops.json | `/provenance` | provenance | `749d5efb7a1e45b66e223cc108723d49200d6bd31053fedf7101f7f18b24f51a` |
| 04-functions.json | `/provenance` | provenance | `749d5efb7a1e45b66e223cc108723d49200d6bd31053fedf7101f7f18b24f51a` |
| 05-lists-dicts.json | `/provenance` | provenance | `749d5efb7a1e45b66e223cc108723d49200d6bd31053fedf7101f7f18b24f51a` |
| 06-recursion.json | `/provenance` | provenance | `749d5efb7a1e45b66e223cc108723d49200d6bd31053fedf7101f7f18b24f51a` |

Additional course-level excluded fields: `course.activityKinds`, `course.audience`, `course.execution`, `course.helpPolicy`, `course.nextCourse`, `course.provenance`, `course.provides`, `course.roadmap`, `course.shape`, `course.status`.


## Format-v1 revision (2026-11-14)

Status: proposed; human approval pending. `course.json` now contains exhaustive source mappings for the course, topics, materials, questions, lessons, steps, activities and media. All eight original projection resources across the two courses remain declared JSON media; legacy package-level ledgers and provisional manifests are removed. The original inventory above covers embedded teaching content; structured public activity copies also map to the owner-AI source and the public revision source. Input declarations and keyboard/remote instructions are public additions, not evidence of implemented player controls. No withheld source answer fields were restored.

Parsons exercises retain every distractor and accepted order in media. Their format-v1 activities are explicitly self-check explanations, since its single full permutation cannot encode these richer exercises. Typed prediction/checkpoint responses and written explanations require a keyboard; finite-choice activities and reading-based Parsons have focus/select alternatives for a remote.

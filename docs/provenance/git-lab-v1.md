# Git Lab v1 provenance audit

Status: verified export inventory; proposed public draft; human rights and teaching review pending.
Checked: 2026-11-14 UTC.
Source baseline: `cc40e0a6315a9f86d21496f268b34aa8547786d3` (owner-authorized private course repository).
Source scope: `content/git-lab/course-v1` and `native-study/scripts/export_courses.py` at that baseline. No private repository URL or source-only prose is republished.

## Origin and permission

Every included item below is classified **original by the owner's AI agents**. Creator and rights attestation: Collin Craig; owner direction dated 2026-11-14 authorizes these original course materials under CC-BY-SA-4.0. This records the owner's grant and source evidence, not independent legal verification or a claim that AI output is necessarily copyrightable. AI-written content needs human review; status stays `draft`. No third-party licensed works, images or attributed external quotations were identified. Quoted misconceptions and sample strings are original instructional text, covered by their containing item. Any newly discovered unknown origin or incompatible third-party material must be excluded before promotion.

Evidence: source introduction commit `e7c274ada48538e283c5b22a5bb21efb6a61870d` (2026-11-03); its source change record identifies the AI content lane and generated authorship. Existing synthetic virtual-shell exercises were extended for the owner. Source code and review conversations are not copied.

## Inclusion and exclusion counts

Included: **6 lessons; 29 tasks; 147 inventory units; 145 embedded code/command sample locations**. Units contain all their descendant prose, hints, rubrics, choices, examples and recorded data; sample locations overlap those units and are not additional activities. Images: 0. Third-party attributed quotes: 0. Third-party licensed items: 0.

Excluded whole learning items: **2** — `git-course-reset-v1.g1` (one task containing a password-like example with unresolved string origin; excluded conservatively, never published) and `git-course-capstone-harbor-v1` (one capstone withheld by the private export contract). No other task or lesson is omitted. The capstone and course metadata also contain references to that withheld extension; the export retains only its explicit unavailable notice.

Withheld source subtrees listed below: **146** (separate from whole-item counts). Source README, tools and tests are excluded in full; they are author/integration material, not learner content. Source course-map metadata not admitted by the exporter is excluded.

## Privacy and answer boundary

The only absolute paths in the learner projection are synthetic `/home/<fixture>.txt` virtual-lab paths, not host directories. Keep them unchanged: goal matching depends on them. No real account, filesystem or service is referenced. Reviewer task references/mutants, debug fixes/results/explanations, walkthrough expectations, prediction reveals, observed misconception states and parity metadata stay withheld. Exporter-admitted checks/answers, progressive hints and after-attempt worked help remain available; these are learner-facing by contract.

Scan scope: every source JSON in these two course directories and every resulting public course asset; review URLs, names, paths, credential patterns and embedded samples. No class/instructor sources, real-person data, private-service URLs or credentials were identified in included material. Automated pattern and gitleaks results are recorded in the PR; they do not prove rights or factual accuracy. Owner approval required before status in-review/reviewed and before any announcement.

## Included item ledger

All rows: origin `original by owner AI agents`; disposition `included`; licence `CC-BY-SA-4.0`; creator `Collin Craig`. Pointers address public attachment JSON. Hashes use the exporter’s sorted compact UTF-8 JSON encoding with trailing newline. Course/lesson metadata rows cover the indicated metadata subset, not the full subtree. Bridge titles and all non-inventoried structural fields inherit their containing lesson provenance.

| Attachment | JSON pointer | Item kind | Stable ID | SHA-256 |
| --- | --- | --- | --- | --- |
| learner.json | `/lessons/0` | lesson | git-course-snapshots-v1 | `e87b4c47c944c918ea09682e19721a8f792f4ffba006c8f96c4fe64dc93e2677` |
| learner.json | `/lessons/0/learn/concept/0` | concept | — | `9d2fa6e85676ce3115682924ee0a28280ffaaec3048dac912d819642b1a6822b` |
| learner.json | `/lessons/0/learn/concept/1` | concept | — | `b0bbcd69a8e2fdae4eeeb8d1299c0bb8beeaa4932eda2a5dc522b22f96727170` |
| learner.json | `/lessons/0/learn/concept/2` | concept | — | `57ffc766e842d66efd91bd38315ff80d293f6e06f9826071207780aacccf2d0b` |
| learner.json | `/lessons/0/learn/concept/3` | concept | — | `89428596e16526d8d1eb8ebed19144cb9338b8bad0422a0e421bbfa5944fee6e` |
| learner.json | `/lessons/0/learn/concept/4` | concept | — | `345092f20577787605dd1fbe88f985c8e392fdc7d4e6a9c17eee2788ea8314ad` |
| learner.json | `/lessons/0/learn/assumptions/0` | assumptions | — | `522c9dadff2d222c900bb8cb8f3fb2595d7ddade42c27a042e7e834921f58465` |
| learner.json | `/lessons/0/learn/assumptions/1` | assumptions | — | `97fe61fed07db27a1baff969bd355e03de653269f5f4975d9ffb47b6a7f84e20` |
| learner.json | `/lessons/0/learn/assumptions/2` | assumptions | — | `01e071d5e8ef4c827de70b0d652537f0c54e116a8441d3bd7a183105b87ae457` |
| learner.json | `/lessons/0/learn/walkthrough` | walkthrough | — | `05f47229d61f615ec53d11f19387b3d96473108b064683f319e589763abe137a` |
| learner.json | `/lessons/0/learn/questions/0` | questions | git-course-snapshots-v1.predict | `554075e49fb89d70b7c399a1a3df47a4f5f1e9d7d5d4567aa2282ef61c60b9de` |
| learner.json | `/lessons/0/learn/questions/1` | questions | git-course-snapshots-v1.check | `d0a6ba4efb6acd558b4a61761570861844665f582bb2f37cbad6ed551ba4b04f` |
| learner.json | `/lessons/0/learn/misconceptions/0` | misconceptions | git-course-snapshots-v1.m-commit-saves-all | `e7743a5eedc15d9b4f3d1fddfc1a35e109d2b89183ac7ff03d367a3d1faa35be` |
| learner.json | `/lessons/0/learn/misconceptions/1` | misconceptions | git-course-snapshots-v1.m-add-once | `a043e07587bc601131537da10afcb764e733f3c2530452d8f76da8434321596b` |
| learner.json | `/lessons/0/learn/realGit/0` | realGit | — | `326580dae4b595103c38caf714165929cd936dc50234027dd734ff43aebdc6c3` |
| learner.json | `/lessons/0/learn/realGit/1` | realGit | — | `45a3233b8009303c9844fd66de85fe80b5449740ce8d93aa458aee73c513bf08` |
| learner.json | `/lessons/0/learn/realGit/2` | realGit | — | `000255e1951ef94bed5c231a5f45b7a55058c985d20b3faddeb422109a15235f` |
| learner.json | `/lessons/0/learn/realGit/3` | realGit | — | `70a024de8e6f119edcd38285a559f20e08b40222b75bead76bf78031f9014a85` |
| learner.json | `/lessons/0/learn/realGit/4` | realGit | — | `e5280b644f1abb678f37d0eef4a6a8fbd2b0fa24072ee3c6036680920893f272` |
| learner.json | `/lessons/0/learn/realGit/5` | realGit | — | `87dfe9919030a941d14917350239001665a28edc8e87d22615669e50273f11c9` |
| learner.json | `/lessons/0/tasks/0` | activity | git-course-snapshots-v1.g1 | `7e57620af2159b829f2338b18c0348d6c73693505fdeb391a228d39a20f6bc77` |
| learner.json | `/lessons/0/tasks/1` | activity | git-course-snapshots-v1.g2 | `5ae7ea9ae1a5d466838b28fd4ffa32e06fa92d78c95bf12bdea6777ed02331d1` |
| learner.json | `/lessons/0/tasks/2` | activity | git-course-snapshots-v1.debug | `6fa713304bb87f30d0d0d5217db4aaabc316fb60de22c3fcce9687476ce83a94` |
| learner.json | `/lessons/0/tasks/3` | activity | git-course-snapshots-v1.o1 | `32f6cb5bed5f0fb0daa1e572364cac7b59040ca8e11a91f044b5678dfb88ce35` |
| learner.json | `/lessons/0/tasks/4` | activity | git-course-snapshots-v1.o1.comeback.v2 | `44f7f9c71cd1bbc5cea230cb32118b5c28c6001ac2ce8689e9fb418b7468f981` |
| learner.json | `/lessons/0/referenceCard` | reference card | — | `267f0c4f6e3a7e69dda56fa33af0bb72f84d79684084d4a79d121738fdf87ca4` |
| learner.json | `/lessons/1` | lesson | git-course-branches-v1 | `87d323b8873a2cfe12efdc7750ae54b2053db9eac5ee2768b82ae83bd900e7a7` |
| learner.json | `/lessons/1/learn/concept/0` | concept | — | `7f0e1601e850450e1018d3b36eb07c5946347a85c51afbc00fa8d2550c981304` |
| learner.json | `/lessons/1/learn/concept/1` | concept | — | `ca0ff3ce559c421d56a68699904bf9118ba3a5d33d5cd64429ddbdd6be40e903` |
| learner.json | `/lessons/1/learn/concept/2` | concept | — | `2ebf44e8a9e844e33b867626177e6424ecf256f3cc6742ae24433cba082af9b6` |
| learner.json | `/lessons/1/learn/concept/3` | concept | — | `5413e3f4e375599840c6dc6a9e4e40071b7d9d1ca12b662860095b3f821c58c2` |
| learner.json | `/lessons/1/learn/concept/4` | concept | — | `9240bdd9bc28cdace6141775659b00bb902c76d577287ba6e017bdf5705072dd` |
| learner.json | `/lessons/1/learn/assumptions/0` | assumptions | — | `b0eca48f5556efd524974541e9c568b35339ca7d5df682b93df9f66a2245cad7` |
| learner.json | `/lessons/1/learn/assumptions/1` | assumptions | — | `704e59602a945389fa488c9f3c2cf4e8a1ed57eb5765ece0f7375f0a7a4cb2f3` |
| learner.json | `/lessons/1/learn/walkthrough` | walkthrough | — | `589d9e20dd47801f94c00c561f0f00579a779aad7000d0af377198d6f16402c0` |
| learner.json | `/lessons/1/learn/questions/0` | questions | git-course-branches-v1.predict | `a4792b87de1a4f504a6cf95c861b2bb239de9373611cb93db343fc65ca5ab5b7` |
| learner.json | `/lessons/1/learn/questions/1` | questions | git-course-branches-v1.check | `a5db7852b5096e244f275fde5375e8867a22cf501f30229aba441c23f679f063` |
| learner.json | `/lessons/1/learn/misconceptions/0` | misconceptions | git-course-branches-v1.m-copy | `4c70f821f83a4b42d2ffe956a3d87cfa6f932ca7ad750d3e1aa1b7ca6b5cd271` |
| learner.json | `/lessons/1/learn/misconceptions/1` | misconceptions | git-course-branches-v1.m-vanish | `512a0045c4dab07e964fa3194217a6b2ca47971080e921b53a3e2a60bca7b009` |
| learner.json | `/lessons/1/learn/misconceptions/2` | misconceptions | git-course-branches-v1.m-untracked-branch | `4f5d05026fba125409658c647f4284f944eb20a5148a9bb8f1b497a1ccbb8e3d` |
| learner.json | `/lessons/1/learn/realGit/0` | realGit | — | `b507e83ed7529ea4d8ebc78763bd6b5bf48dc2b7f66649859e147feaa09e6574` |
| learner.json | `/lessons/1/learn/realGit/1` | realGit | — | `65e029cd18118901aece682a1b5657c1a69128df75919d5e8cca90ccc6c35a1a` |
| learner.json | `/lessons/1/learn/realGit/2` | realGit | — | `83669815b254edb92a5935bef1b64d21c4df85a8b5496dbce599d72103178326` |
| learner.json | `/lessons/1/learn/realGit/3` | realGit | — | `e5c615fef010f7e3350f55dd0c043c039533addca1bb35b5d55d949af598d32e` |
| learner.json | `/lessons/1/tasks/0` | activity | git-course-branches-v1.g1 | `180ac7d11cd72f5c17df4a95a2f4880e8fd93aec60838bdc63017e06ef2b85b0` |
| learner.json | `/lessons/1/tasks/1` | activity | git-course-branches-v1.g2 | `8f8cc03bb4736c4dae1355edfd7cc488f61ac4f8c123f2c676c77a1ca41cc7c6` |
| learner.json | `/lessons/1/tasks/2` | activity | git-course-branches-v1.debug | `156d6524b7255c396960246da3932256d4725fdb9ec271e4037a0d66a46e03f4` |
| learner.json | `/lessons/1/tasks/3` | activity | git-course-branches-v1.o1 | `032d8682944a4418f633912ec4083f0bb96b255559450af905f3f91a0553e865` |
| learner.json | `/lessons/1/tasks/4` | activity | git-course-branches-v1.o1.comeback.v2 | `cbfa16dd527907186dd355b0373debff087107d6fab0291bcf55af79a6f35412` |
| learner.json | `/lessons/1/referenceCard` | reference card | — | `0fa080d06e817f2643dbdbc3a4aa0d418e82a3702f0d5da49f6537b7e2916cb4` |
| learner.json | `/lessons/2` | lesson | git-course-merge-v1 | `28fff99252e66a23a025ec2d159290a10e96943d3fa63028c8eb4e6f886e22a7` |
| learner.json | `/lessons/2/learn/concept/0` | concept | — | `aaf42c017cbe8c0c4dc5eb7597cd2fd6633769de02a011f94fbefdae423f25de` |
| learner.json | `/lessons/2/learn/concept/1` | concept | — | `bae3cce2894b2e48bd77c423f9f3cee2d4209336da6a453515f27121237a5811` |
| learner.json | `/lessons/2/learn/concept/2` | concept | — | `da679953c36ae354b32606fee8996f2f57555cd7bb8571ff6219c744758c3371` |
| learner.json | `/lessons/2/learn/concept/3` | concept | — | `80bd93213a90c768f667084e48dfc8cfd1f113c362df1098cfbdb13ccc4da04a` |
| learner.json | `/lessons/2/learn/concept/4` | concept | — | `2f2dae440b3036e8d1ca06b77b356f11291e65be412077d7588fdbdc8ce3729e` |
| learner.json | `/lessons/2/learn/assumptions/0` | assumptions | — | `37eaddcb48ad1d9063ddf7e3bed88733db2a2275bb7e9779d83a077d281b5b24` |
| learner.json | `/lessons/2/learn/assumptions/1` | assumptions | — | `0d60acb9185f26791f90de1e1aec41842241bd7639457b0f84b90b431ccd1caf` |
| learner.json | `/lessons/2/learn/walkthrough` | walkthrough | — | `a9f8520a250895fdabbcf7c50e40cf8779fe66fdbd536a0365bd23b1d80b2e36` |
| learner.json | `/lessons/2/learn/questions/0` | questions | git-course-merge-v1.predict | `043a6e4b3dbc6c965ca4272193797254e33f5b0641be4a754b02a93a04f501fc` |
| learner.json | `/lessons/2/learn/questions/1` | questions | git-course-merge-v1.check | `dd8a4b530a128985f57ed6ecf4ec0577d4ca45adff7f6fbc48fa0ca6aa18ab85` |
| learner.json | `/lessons/2/learn/misconceptions/0` | misconceptions | git-course-merge-v1.m-always-commit | `ec03a26f8440e39babb330e5cf0450260b5b3d55efbf0e54efcd03258fd492d1` |
| learner.json | `/lessons/2/learn/misconceptions/1` | misconceptions | git-course-merge-v1.m-direction | `9216077f8162b5327fcb735096c8e9e25da84a673d14bb707192585d722c0edb` |
| learner.json | `/lessons/2/learn/misconceptions/2` | misconceptions | git-course-merge-v1.m-same-change | `f3fb48909d193301bc07e7ab9a1b1315c2564f425aa430fa0ed414d4f2e8ae62` |
| learner.json | `/lessons/2/learn/realGit/0` | realGit | — | `0a688421cb7818b690eb421d5ec3de6ad88579f01c7a173ea94d7622e4639a92` |
| learner.json | `/lessons/2/learn/realGit/1` | realGit | — | `002c5cdfcb006c320642dbc9c78f16172e3d41d23dd061ce7cccd33134ce8e8a` |
| learner.json | `/lessons/2/learn/realGit/2` | realGit | — | `ab6694094948f83c66a181287f56fce858c6cde9b54d2f4c543b3c9ac7ce1f38` |
| learner.json | `/lessons/2/learn/realGit/3` | realGit | — | `adb34c022234af357204e810cd220aeb5afc08f906af6dc4af14c53127115bce` |
| learner.json | `/lessons/2/tasks/0` | activity | git-course-merge-v1.g1 | `95d6c3772bbba1e9f9c41e955796d7bb9e7ce87e62e79f723198a5c1a2646b67` |
| learner.json | `/lessons/2/tasks/1` | activity | git-course-merge-v1.g2 | `00d546dd4fb469f5c90211be910626f3838ee7c86c09b1ed8ba2eb72f06bed6a` |
| learner.json | `/lessons/2/tasks/2` | activity | git-course-merge-v1.debug | `abc6be821f2fa08887f0afb34279b28b6593bc9072e9050512ed7c6109ad276f` |
| learner.json | `/lessons/2/tasks/3` | activity | git-course-merge-v1.o1 | `82dca2e637855f4d8cdd55e7b1e14ad9398d1872989e7c7c68588227d1881324` |
| learner.json | `/lessons/2/tasks/4` | activity | git-course-merge-v1.o1.comeback.v2 | `9206be85c820c278382652eb967d45456d6f1ef6e7b75f1b21786b2d4e813535` |
| learner.json | `/lessons/2/referenceCard` | reference card | — | `a23b3abc12e45bfac736e2b4dd992a6447d6368c3f1e63014f25316a9eac795c` |
| learner.json | `/lessons/3` | lesson | git-course-rebase-v1 | `1f4aad270c457cb3cb30dd50c8f6191a58210b780e98316aa569a98e9d529a8f` |
| learner.json | `/lessons/3/learn/concept/0` | concept | — | `a6d97b2c894999d0d7b793d1828fdf4592e534e89bfbe601d462adc89b534a29` |
| learner.json | `/lessons/3/learn/concept/1` | concept | — | `9a8ae0477f24557ec3da600102da8393d6233c3ed57cc00664b505ca6c4f0e3f` |
| learner.json | `/lessons/3/learn/concept/2` | concept | — | `fdc1159ada5af5f6d5da83313d01dc33df4a2fbf426b55814f5a5dd5625c8641` |
| learner.json | `/lessons/3/learn/concept/3` | concept | — | `b207e799e17fdaf9dd70c74183b481b7aa6c716abe71a6221a0ad2deefda12be` |
| learner.json | `/lessons/3/learn/concept/4` | concept | — | `986fcffccd602b0e07265a6f57321d2c26d466f78910535495e3d646ad9de25e` |
| learner.json | `/lessons/3/learn/assumptions/0` | assumptions | — | `e7f976d950b9f830f152715b617e8c10d6776646fe389ba51427a84f43634265` |
| learner.json | `/lessons/3/learn/assumptions/1` | assumptions | — | `591e82459e6ed054cff33efd8e663ecabb3e5bb52ff49612ef0c212e1393f28d` |
| learner.json | `/lessons/3/learn/walkthrough` | walkthrough | — | `61a0d784e429b73e129cca33c42340023e2d130c5d58191947dab69cdf9e6370` |
| learner.json | `/lessons/3/learn/questions/0` | questions | git-course-rebase-v1.predict | `87bdf67ff91cb257f5d3cd29d455f52931d9cd79ef0a495d2261f2fe10f7627f` |
| learner.json | `/lessons/3/learn/questions/1` | questions | git-course-rebase-v1.check | `6d548f682b1437b1307ddf6c1b8e93ec80a8c15324a3fd8dcdee31b8dbc71987` |
| learner.json | `/lessons/3/learn/misconceptions/0` | misconceptions | git-course-rebase-v1.m-moves | `4d7dc2dea1773bfddab71b254fe1a07433f01aec4040806e92007d594a53edb0` |
| learner.json | `/lessons/3/learn/misconceptions/1` | misconceptions | git-course-rebase-v1.m-shared | `f4a4eb5b2578817999257decb2145a0e9204e4c2247f2da0cdb724a227357b36` |
| learner.json | `/lessons/3/learn/misconceptions/2` | misconceptions | git-course-rebase-v1.m-no-conflicts | `d9066620e2e8694dd723e596f1d09e1ee63823930bf995d9a08a85100846f8ce` |
| learner.json | `/lessons/3/learn/realGit/0` | realGit | — | `9798d0d2fbfe58bbfd626108c95dc6b84f6c55de8d26b6afb104f9040be5ed8a` |
| learner.json | `/lessons/3/learn/realGit/1` | realGit | — | `bbb7c820bb0e06a909e15cc024741a7222bf95ceee71f55b57114f771b0974eb` |
| learner.json | `/lessons/3/learn/realGit/2` | realGit | — | `24fc9fadfb117e9f4183bd94a2ccd6fb92a8bf16e38e0d0799b950e382b92be5` |
| learner.json | `/lessons/3/learn/realGit/3` | realGit | — | `8af1fa488bea251d0ec1e46737de73385eb7983fbe3a03119867d9ee1d256882` |
| learner.json | `/lessons/3/tasks/0` | activity | git-course-rebase-v1.g1 | `6ff4a7e57fea225403ef7e0fc0aa3fbc8cff797eda8032e27bfd1e1f4a2f7f26` |
| learner.json | `/lessons/3/tasks/1` | activity | git-course-rebase-v1.g2 | `8333af4207d90fb2735ee3aaf3d2d5b736a424ff6aba0af0bc02e072b1587285` |
| learner.json | `/lessons/3/tasks/2` | activity | git-course-rebase-v1.debug | `7efd30814bfb01d0cc15db6218f032b517b064559ff74f79415807da233a3e7c` |
| learner.json | `/lessons/3/tasks/3` | activity | git-course-rebase-v1.o1 | `ce1feeebec7c64d7cb5aad7270e7bf0b55e9a6047fcb6b030ede9ccf4a4e82ba` |
| learner.json | `/lessons/3/tasks/4` | activity | git-course-rebase-v1.o1.comeback.v2 | `1b0bd8a852966647d07534b94f534645e8bea0585ee964b993d4b99700f556ee` |
| learner.json | `/lessons/3/referenceCard` | reference card | — | `2264e8c1782d8923027c529b723b24ffee93636f3c680d4a3b07ad60c9276088` |
| learner.json | `/lessons/4` | lesson | git-course-reset-v1 | `8ae1113d33c3cd81362045f1234ec97f7351a6d5e2bf47b694060eb2786c8a13` |
| learner.json | `/lessons/4/learn/concept/0` | concept | — | `41c2a1889b852325a16360643d46537f6985104161bf73eeaf0e4d50cbb3a213` |
| learner.json | `/lessons/4/learn/concept/1` | concept | — | `0be584ab00e58492310536f20bbf10ddbeac876c00a818455db1b391a227f7d7` |
| learner.json | `/lessons/4/learn/concept/2` | concept | — | `fc4eba1d319c40ab1b1e447ab5829d6b41ad2814b849b652e5d945f528f65580` |
| learner.json | `/lessons/4/learn/concept/3` | concept | — | `9982afe27b283e0f3163f64a19f86ba45b06e3a07179b669c4ad266cb0c05117` |
| learner.json | `/lessons/4/learn/concept/4` | concept | — | `8516619079aec4053a176aa72c62aca1281c26fa87b3174276187407eb8c446e` |
| learner.json | `/lessons/4/learn/concept/5` | concept | — | `62f7d417fc20173b5a806e6c9bf6f9cec7f56b295c6f563960cd60f3c8bf88de` |
| learner.json | `/lessons/4/learn/assumptions/0` | assumptions | — | `aa7d9e3bd0da656fdbb44d9bd2b58aa3cfe65462ce88bf55ec44c42ad634af1b` |
| learner.json | `/lessons/4/learn/assumptions/1` | assumptions | — | `d4e0379d3181e7424365c9269518a469a712b81ff13c2c1d96516fd1277b6542` |
| learner.json | `/lessons/4/learn/walkthrough` | walkthrough | — | `eb8a68eb7ca352f8d32cef5a1bd1b3cedbaf6fbe5b633a3c2467834d80b8f22d` |
| learner.json | `/lessons/4/learn/questions/0` | questions | git-course-reset-v1.predict | `42dfc2b54ac204d3be922177e8c652969564f86b7aee0bb1520a80065a13b689` |
| learner.json | `/lessons/4/learn/questions/1` | questions | git-course-reset-v1.check | `87f711a9f6c962448223dd134f5e841ad9ddd43a6bad8c6efd806685bbc0066c` |
| learner.json | `/lessons/4/learn/misconceptions/0` | misconceptions | git-course-reset-v1.m-soft-undoes | `a8c4775695bd20ca4c32a31d292190223553023046db519145fb273f72b408fb` |
| learner.json | `/lessons/4/learn/misconceptions/1` | misconceptions | git-course-reset-v1.m-deletes-commit | `4c79fa0309a78963f7b05d3acbbc4f87e298f585c58ca9c3e4ab2df32b1b2dd0` |
| learner.json | `/lessons/4/learn/misconceptions/2` | misconceptions | git-course-reset-v1.m-mixed-loses | `3546431cadbc277f2735a83572a1d3157ab997995059bf9d11812464667f69cb` |
| learner.json | `/lessons/4/learn/realGit/0` | realGit | — | `6e9566eab712f45dc0191e7cbc121633d9de1267a7a6312d99f5506e22209d14` |
| learner.json | `/lessons/4/learn/realGit/1` | realGit | — | `9f6d3627c807aff7e8fcd355530f9c3965ff6e33fd186a793d0a2e8d1a571be7` |
| learner.json | `/lessons/4/learn/realGit/2` | realGit | — | `d2854fafb6660984bab48eb4ad29202c4dff94b8f9aa78f5bf3814d8fdb2726e` |
| learner.json | `/lessons/4/learn/realGit/3` | realGit | — | `85f1ca65843a099e8e916dbfa0a55b8bce2aa8b31876b0240d105c82a2ccc86e` |
| learner.json | `/lessons/4/tasks/0` | activity | git-course-reset-v1.g2 | `b74af63e3c3e5716a72350df6fae42d4f41bcbe99a7c80201a5e752d5488574d` |
| learner.json | `/lessons/4/tasks/1` | activity | git-course-reset-v1.debug | `64584f0613762db7cde50694a9415f4e8fa1d9f112aa494c06ccd99e34f1a942` |
| learner.json | `/lessons/4/tasks/2` | activity | git-course-reset-v1.o1 | `c06b87144d522835be84ab516604f7e36e2a2847860525ba4783d15c7d76ba99` |
| learner.json | `/lessons/4/tasks/3` | activity | git-course-reset-v1.o1.comeback.v2 | `b965d0775586047a81443fb609f0374b855821626b50dafceb7b1ba17ac8a442` |
| learner.json | `/lessons/4/referenceCard` | reference card | — | `e8f077fdd14a45e953048641a0c1164b513d9e400d10ca788999ca18c11fbeda` |
| learner.json | `/lessons/5` | lesson | git-course-recovery-v1 | `5dec45eaacdfa63f5f02b6fd9f0a388f7761085b401773bc075338aebf8da46a` |
| learner.json | `/lessons/5/learn/concept/0` | concept | — | `4299178a45c8da00997c3c7946851a6efbfdd3b42fe0ec07229e9393ed412f77` |
| learner.json | `/lessons/5/learn/concept/1` | concept | — | `3a2a6ef9061dc8a25da0fae4bc3e763e607228fa878f785922a4307f12a4c15e` |
| learner.json | `/lessons/5/learn/concept/2` | concept | — | `641f9f7a36007e1c2ffaaaf85a2e572c9c2d04e6ab54882d06cd90a2e0547ad8` |
| learner.json | `/lessons/5/learn/concept/3` | concept | — | `eab0396a7ed2041cf6c06b8dbf4392e9d10cee5b70f455e16442ad04a098ecf3` |
| learner.json | `/lessons/5/learn/concept/4` | concept | — | `174986c360723e3fda47335bed6e197cec1ebcd2081d7a2c7140d9683a8401f8` |
| learner.json | `/lessons/5/learn/assumptions/0` | assumptions | — | `1b0c1cbb19958345d4337e88ee8cad636ae5fe1a23c555408be803309d521689` |
| learner.json | `/lessons/5/learn/assumptions/1` | assumptions | — | `536cb7fa043e41c967aadc613f994b256173e6e6823dfc0bc058265a2fd1af23` |
| learner.json | `/lessons/5/learn/walkthrough` | walkthrough | — | `cabec0eccd7ae9408b4c5f2329ea9bf81d8d12d9451710ea752bceaeb4dfd340` |
| learner.json | `/lessons/5/learn/questions/0` | questions | git-course-recovery-v1.predict | `b84b5c6fe57da6bdea040b3999b6eef4513f619f2ad883755391ebd18986a75f` |
| learner.json | `/lessons/5/learn/questions/1` | questions | git-course-recovery-v1.check | `d08011301db8cca171caa8dfb194c94e18c51af8934aa332877fe6d4083142ec` |
| learner.json | `/lessons/5/learn/misconceptions/0` | misconceptions | git-course-recovery-v1.m-log-means-gone | `63be24d6d324a7d49f9d563ca80c6b5e915b641fdaf36a09fc189db04761cc82` |
| learner.json | `/lessons/5/learn/misconceptions/1` | misconceptions | git-course-recovery-v1.m-everything | `4cb692088f794778f281ddad26da7f9d519b21e7588451d2f58e211c54904145` |
| learner.json | `/lessons/5/learn/misconceptions/2` | misconceptions | git-course-recovery-v1.m-staged-safe | `47e7874c60c179372affd0ddf15eb40b77903ee14b30a439ecbd379345f751ea` |
| learner.json | `/lessons/5/learn/realGit/0` | realGit | — | `ac159fdcb8292c7762af5471e924e37881a7685ad1999e338331214dcf0f5703` |
| learner.json | `/lessons/5/learn/realGit/1` | realGit | — | `274a64f9044ac0f5e36682f2ef7608307281a9e3073ee4e28489d69c42440a47` |
| learner.json | `/lessons/5/learn/realGit/2` | realGit | — | `a9cac0cd0db25359a707c88bffb15cb5a11abb3b96d67f756242ae9d5b16b9c9` |
| learner.json | `/lessons/5/learn/realGit/3` | realGit | — | `aa47237a5632f42ab9d8e5d6e2b8563e56e0052230a11e3863f71f5d45e491d5` |
| learner.json | `/lessons/5/tasks/0` | activity | git-course-recovery-v1.g1 | `c64e3c713c7bbf1047799f55ce55d5eb035062661000ca0db4d2f61c2a9791b4` |
| learner.json | `/lessons/5/tasks/1` | activity | git-course-recovery-v1.g2 | `fbe2082232aa5699420497fa8e17bac3e6c6421cf87bbb59922050f090afc559` |
| learner.json | `/lessons/5/tasks/2` | activity | git-course-recovery-v1.debug | `283c5d6f2bb5c27d0af277240050eec462741599b3b78c909d0b480085241c0f` |
| learner.json | `/lessons/5/tasks/3` | activity | git-course-recovery-v1.o1 | `063846de28059d08bd608a9c656bf3bb7f105d41136215ec92a104a62dc0e5c0` |
| learner.json | `/lessons/5/tasks/4` | activity | git-course-recovery-v1.o1.comeback.v2 | `88e3869ce2759714c7e7f8fb5b74db77299ff58d0e42a86514e5020fc9d4860a` |
| learner.json | `/lessons/5/referenceCard` | reference card | — | `f654af37effe59ad14277d93ae703ab7e783393cb0c2d06e82cdfce2c19b196c` |
| learner.json | `/` | course metadata | git-course-v1 | `8e6505866542935a80c6604c1d8d9025e7a7f8d328e23d748fab740216f72040` |

## Embedded samples

Each code/command location inherits the original origin, licence and included disposition above. Inline snippets and quoted strings embedded in prose are covered by their complete parent unit. No external images or quotations are linked.

| Attachment | JSON pointer | SHA-256 |
| --- | --- | --- |
| learner.json | `/lessons/0/learn/walkthrough/setup` | `3180645383303b9a857b21c2ce89f089b28ad42575fe7e523fdf5dcd663cd3dc` |
| learner.json | `/lessons/0/learn/walkthrough/steps/0/command` | `1af96cde098093f3ed7fd90380ae25b69b78cbe59b28c9d875f1de0300b621c4` |
| learner.json | `/lessons/0/learn/walkthrough/steps/1/command` | `4ffc45a18249bc0019c0546517b1a6e13d231da3c31d8751d81677a4b2268975` |
| learner.json | `/lessons/0/learn/walkthrough/steps/2/command` | `88fd08f392214efa7f37f2f7176686c928390866cac91d50d56ff811c736e591` |
| learner.json | `/lessons/0/learn/walkthrough/steps/3/command` | `4ffc45a18249bc0019c0546517b1a6e13d231da3c31d8751d81677a4b2268975` |
| learner.json | `/lessons/0/learn/walkthrough/steps/4/command` | `440c8dcf90da4b81c6be0eed4bd851e8ef308937674916a9a6841a4c86890b11` |
| learner.json | `/lessons/0/learn/walkthrough/steps/5/command` | `9bdc16c3bb7d973ed2139455ebd1adf7574a16e829c48293dd64d2a68aba85ea` |
| learner.json | `/lessons/0/learn/walkthrough/steps/6/command` | `e396045cdadd815e0c54f91ff39bf8cfff4cb2848c8183e6b70e29d35641dc10` |
| learner.json | `/lessons/0/learn/walkthrough/steps/7/command` | `dfb68f091018362c5dd33577747c4df91204c69a8da73b2afddc2ee4cc24288b` |
| learner.json | `/lessons/0/learn/walkthrough/steps/8/command` | `a4b5f4a801b41a295944b72801f60c6a189b2bf61b6482a167de71656a42c802` |
| learner.json | `/lessons/0/learn/walkthrough/steps/9/command` | `9e6ab3db7d68529811e66cf2a5ec914a265eecef43445aa793529188a94784e5` |
| learner.json | `/lessons/0/learn/walkthrough/steps/10/command` | `3ea71ec650ef4ee3d28ce66fca8b869f38ce0ce110bff52330089a5dd2608629` |
| learner.json | `/lessons/0/learn/questions/0/setup` | `08553ebecfb4f44ae0a935c5cd632750c75509f2566a01c13739b6296eab9e82` |
| learner.json | `/lessons/0/learn/questions/0/commands` | `aa90e231c1bbf600b24d72ebc143033e09d47dc27cbc52512403fdba3ae8b83c` |
| learner.json | `/lessons/0/learn/misconceptions/0/setup` | `a126aed7c38365e536299efca1ed735d6c2c8b35db25f6cd9f4f7d62c8c9894d` |
| learner.json | `/lessons/0/learn/misconceptions/0/commands` | `8596e9bc72bfbefdaae0e3ba9fe647a2a02f45750c352eb140580337ba15d224` |
| learner.json | `/lessons/0/learn/misconceptions/1/setup` | `b0dcca4d779458d22c23f70f2cc37ce38de0822a178049e6e3db305172bae7d7` |
| learner.json | `/lessons/0/learn/misconceptions/1/commands` | `cf8346c0ed0a7e5154b5265d661c4e9e734e35feff6df1b5af9096292d90349f` |
| learner.json | `/lessons/0/referenceCard/commands` | `2cd955d8dec8b64eb90e7b12c680c47f4557a6ac61d47416c775dd1a65fd07a4` |
| learner.json | `/lessons/0/tasks/0/setup` | `0e671efebea962b19cb0e7cc0b7a4ba4c1b9237d7044b09b93822dce28fe7e73` |
| learner.json | `/lessons/0/tasks/1/setup` | `607152ed6b1381aae9fe59b9354722cb9f1164a9b91df5835974d2345c0d6205` |
| learner.json | `/lessons/0/tasks/2/setup` | `544e12847aa64da8f690fb040f1f014a614a946c18ec60c886b5141834e7e16a` |
| learner.json | `/lessons/0/tasks/2/broken` | `97be9e9cb69722e4847bf05d7571f537c4b02a481768fafc41f4f65aa8b118dc` |
| learner.json | `/lessons/0/tasks/3/setup` | `8e1d679722015010f6631f3a713bce0a7105576353dae7ae860dc07d36b49311` |
| learner.json | `/lessons/0/tasks/4/setup` | `a689e5042c85a62c310b1a8cad4354516b498ae11c1254f97f3fd89ab2bff37e` |
| learner.json | `/lessons/1/learn/walkthrough/setup` | `41807df191235931ed10d6b7c4c67c690fef290682d7640e7cfac8400c2d4f63` |
| learner.json | `/lessons/1/learn/walkthrough/steps/0/command` | `e3636df562fb8f5642177b1cdf9b199d46429cf6ba3ca579655fa664bbfd4392` |
| learner.json | `/lessons/1/learn/walkthrough/steps/1/command` | `efa4c2ab608eedd54bb87ece90c2a9954f72abcf09ce567da9b603d3ee85c673` |
| learner.json | `/lessons/1/learn/walkthrough/steps/2/command` | `93550e17eaef6c78a2e45ddd55b4270eca79a2d4713982f21ee39299abfa4457` |
| learner.json | `/lessons/1/learn/walkthrough/steps/3/command` | `93face2ad41b70a252bad6e229279446e0c33fa92acfde54b8642486e2b495ca` |
| learner.json | `/lessons/1/learn/walkthrough/steps/4/command` | `19825f31ccc936d86af7fbf5cf117e5f86195f01f39b2f40a45b97cc3d9581fb` |
| learner.json | `/lessons/1/learn/walkthrough/steps/5/command` | `2588a0f9e70ac23974ba09dbdd8e2334f2a216009647c4224b2da082292e7d96` |
| learner.json | `/lessons/1/learn/walkthrough/steps/6/command` | `165e47fbc57e0abe977bc143de465070ede753b6cd267c7cebcf4c9b5cff1b1d` |
| learner.json | `/lessons/1/learn/walkthrough/steps/7/command` | `41a67bc01203f7b93a42f1abe85d688c179455be8dabf4d7010c80aedc783976` |
| learner.json | `/lessons/1/learn/walkthrough/steps/8/command` | `c4008b91e1e22f367981342ef058c3c0337f2355fbe9ca959c4bab82427971d4` |
| learner.json | `/lessons/1/learn/walkthrough/steps/9/command` | `585513fedae08640ad1668cb5e8411b52fef89892734fb5d7c38c41d743620fe` |
| learner.json | `/lessons/1/learn/walkthrough/steps/10/command` | `2f305482b38913378fd11eb0e34995c4b3873b9e09c8b60d526bc5800ccd7264` |
| learner.json | `/lessons/1/learn/walkthrough/steps/11/command` | `93550e17eaef6c78a2e45ddd55b4270eca79a2d4713982f21ee39299abfa4457` |
| learner.json | `/lessons/1/learn/questions/0/setup` | `22a65a249d57b875b975a38e5dc4e15727d576371e14f1b6559f051cd8ed51e9` |
| learner.json | `/lessons/1/learn/questions/0/commands` | `d73409753e9e0b2fe0947002b9c2a1e1fcdc78ba4799692e21894ba24a01d75f` |
| learner.json | `/lessons/1/learn/misconceptions/0/setup` | `14f7f99089aac3a8b367d46ad654ffdc6e3514c70800ed64e4f5625ba78d985c` |
| learner.json | `/lessons/1/learn/misconceptions/0/commands` | `3b8647d960d5c89124509995ae463fe7e29a1c0e3ac68530e5b26ec5b5a017dc` |
| learner.json | `/lessons/1/learn/misconceptions/1/setup` | `616124cc591b424ba7f95b17b820cfb81db37cd922595e0b2cd5fcbbffa84126` |
| learner.json | `/lessons/1/learn/misconceptions/1/commands` | `d73409753e9e0b2fe0947002b9c2a1e1fcdc78ba4799692e21894ba24a01d75f` |
| learner.json | `/lessons/1/learn/misconceptions/2/setup` | `9f1e353ca05f086abd08bc2c85dc7429c153bf112d5e5cb3aa53cb9cb0a708d1` |
| learner.json | `/lessons/1/learn/misconceptions/2/commands` | `d73409753e9e0b2fe0947002b9c2a1e1fcdc78ba4799692e21894ba24a01d75f` |
| learner.json | `/lessons/1/referenceCard/commands` | `af081cbd553a421b1d0250509f0a13f6c9c7f4e400271a0dc9be4a5a758ec060` |
| learner.json | `/lessons/1/tasks/0/setup` | `ce7c02109f6fd81239396c681b1c27e65616cdb16dcf9903dbc87238de3556bc` |
| learner.json | `/lessons/1/tasks/1/setup` | `fbd5f6c98652a336f8d837c70ac5956ae28b144201e9af683557aa902b34c01f` |
| learner.json | `/lessons/1/tasks/2/setup` | `4bb290154a79744a2214d42000c0b2fc46dc568393a6ae9255bb3e5192f9b97e` |
| learner.json | `/lessons/1/tasks/2/broken` | `f01c5eb23b75a4bb8925df40244061a1900e7a0227eae5964b6ac05a888b01b6` |
| learner.json | `/lessons/1/tasks/3/setup` | `0915149771289399cc1a9ce4efb63851732e65685e27a96823ad31d059dffd28` |
| learner.json | `/lessons/1/tasks/4/setup` | `fa95fdd5709f09063c39f23c28a4af3e8c3f94c021e5da1d8e8f6fcb8afd96ef` |
| learner.json | `/lessons/2/learn/walkthrough/setup` | `7ed39542f818560273b6c7fe110fc674d991804f7507e914d8762785663a989e` |
| learner.json | `/lessons/2/learn/walkthrough/steps/0/command` | `d110323220c6140d73cc89907d28cb244ac6504b87858c9395daa9120a739a0d` |
| learner.json | `/lessons/2/learn/walkthrough/steps/1/command` | `05104fa3ea225ae0649e3fb759e474464c3f15036b9a5e9b0fdaa03e2d4bdf46` |
| learner.json | `/lessons/2/learn/walkthrough/steps/2/command` | `18364c4f23d3fef159177e700b437e096e0e2c2ab2022307e9d53a87481871b7` |
| learner.json | `/lessons/2/learn/walkthrough/steps/3/command` | `7f7cabe28dd43e1a56d1bcbe12e447fdc3095fa78cdfc21614f4418e4385330c` |
| learner.json | `/lessons/2/learn/walkthrough/steps/4/command` | `df4fc852dcc4bf3f82caf2431be715556b38c1ca1c5db98251a3b21bffa117d5` |
| learner.json | `/lessons/2/learn/walkthrough/steps/5/command` | `3f3c2410e6930db01a364a9e34975abaaab81714c8659113d55bbf79ac1bb5b0` |
| learner.json | `/lessons/2/learn/walkthrough/steps/6/command` | `0115ee46efa3a8a088cf0d2d849f2d6978d834ec3c8ce734e1fa67570e2518cf` |
| learner.json | `/lessons/2/learn/walkthrough/steps/7/command` | `0e75ffba2f57bed69bc40e3e9e5b5306b2af48e5ffaa33e9ed3888b2449be610` |
| learner.json | `/lessons/2/learn/walkthrough/steps/8/command` | `940cf5609f3d54fe56d1c4ee596980aab84063fdea1f0bff505c86382951ca6e` |
| learner.json | `/lessons/2/learn/walkthrough/steps/9/command` | `165e47fbc57e0abe977bc143de465070ede753b6cd267c7cebcf4c9b5cff1b1d` |
| learner.json | `/lessons/2/learn/walkthrough/steps/10/command` | `7fa00fa728d9015469b94b7503fc7eab92082325d314e88f887836ddcb03af90` |
| learner.json | `/lessons/2/learn/walkthrough/steps/11/command` | `3ea71ec650ef4ee3d28ce66fca8b869f38ce0ce110bff52330089a5dd2608629` |
| learner.json | `/lessons/2/learn/questions/0/setup` | `3769dde1752404fb0e91581859198df510fdb1c916c769b330609d42582a6687` |
| learner.json | `/lessons/2/learn/questions/0/commands` | `a2a3422f113aae1a4d36175f1ef557cc9e2736027f6ca808f0b70a043eca635b` |
| learner.json | `/lessons/2/learn/misconceptions/0/setup` | `b5ff6aa7068b744d10b3da845af2c621b27551fd5ac275e91295930b23a47b58` |
| learner.json | `/lessons/2/learn/misconceptions/0/commands` | `e6687098c1e6d151967d1ffc6a36e8b722353fd7c167700205ae8fab0d0aeac3` |
| learner.json | `/lessons/2/learn/misconceptions/1/setup` | `625d5e74d1a9561f08cee457effa29869cf5527fdacc2a0f4feb1c61ba68dd4b` |
| learner.json | `/lessons/2/learn/misconceptions/1/commands` | `8b390fc3a373f01bc19800a853ee88e168e977c2c9d095464cddae1fbd2de531` |
| learner.json | `/lessons/2/learn/misconceptions/2/setup` | `4a458d487893b46af0c946617c6217007771ef6b82c45213a1d8c7962a40f386` |
| learner.json | `/lessons/2/learn/misconceptions/2/commands` | `8a580289c0a9a430f5c6d827996cfab4b34816e411271ca39d98582c6cb7755b` |
| learner.json | `/lessons/2/referenceCard/commands` | `6e393f903ea0ca1b9ad1ed142bee265b2fad4f8f69fdf57320d95d15cf10bb0a` |
| learner.json | `/lessons/2/tasks/0/setup` | `4894f9c06e10b17864879f232c1c833bf8c5f41f73e859d5d662ddf9cd5a2aa5` |
| learner.json | `/lessons/2/tasks/1/setup` | `97c30176469e3e537c7c4ffaf12e995170dd044d99e49fbed73225cfc5c7e25e` |
| learner.json | `/lessons/2/tasks/2/setup` | `c6ca661f35b6bbfdd7ed557e664839d0b93125d4d0b5a01f3bd12e359c21927f` |
| learner.json | `/lessons/2/tasks/2/broken` | `71a3dea614060a28f651b1f2a5c6712e6ac9c3520736a4a5e178a5b5bab0f329` |
| learner.json | `/lessons/2/tasks/3/setup` | `7eacd0efb6a237f2040e4b0ce4adf7fbabfd15568e04c7f58acf0ba51bf4d87a` |
| learner.json | `/lessons/2/tasks/4/setup` | `6a01cec8787a3f559fdef64082576a83d3c7a3e8e21415011547822036977c9a` |
| learner.json | `/lessons/3/learn/walkthrough/setup` | `47e15e803e0db3cbdb944e8b542a05ae88e667a98a01f8d2f33b2444bfd31bc3` |
| learner.json | `/lessons/3/learn/walkthrough/steps/0/command` | `15aeaf2dc6a4c5631f3d827dfc260897fda96dfd3ff85505d0568133d1b809ae` |
| learner.json | `/lessons/3/learn/walkthrough/steps/1/command` | `3ea71ec650ef4ee3d28ce66fca8b869f38ce0ce110bff52330089a5dd2608629` |
| learner.json | `/lessons/3/learn/walkthrough/steps/2/command` | `3aaffe8689f6339b5e1a9cfb59fdec24f76e02abc102ede28ed7ed4fe1260cfc` |
| learner.json | `/lessons/3/learn/walkthrough/steps/3/command` | `3ea71ec650ef4ee3d28ce66fca8b869f38ce0ce110bff52330089a5dd2608629` |
| learner.json | `/lessons/3/learn/walkthrough/steps/4/command` | `165e47fbc57e0abe977bc143de465070ede753b6cd267c7cebcf4c9b5cff1b1d` |
| learner.json | `/lessons/3/learn/walkthrough/steps/5/command` | `80c6acefdd569f1c87d26f28ab6d5921b5c18aeef80dc9f063d74eba2ef347cf` |
| learner.json | `/lessons/3/learn/questions/0/setup` | `ddc8664c1b166359d7a0c0adff43a50f380d7c708509da066f4f58ea3126c3b1` |
| learner.json | `/lessons/3/learn/questions/0/commands` | `e7c2dbbdd82e4dba4c8a00cfd0d969f088c2e6d19693270240df223aa2dd69c8` |
| learner.json | `/lessons/3/learn/misconceptions/0/setup` | `ddc8664c1b166359d7a0c0adff43a50f380d7c708509da066f4f58ea3126c3b1` |
| learner.json | `/lessons/3/learn/misconceptions/0/commands` | `e7c2dbbdd82e4dba4c8a00cfd0d969f088c2e6d19693270240df223aa2dd69c8` |
| learner.json | `/lessons/3/learn/misconceptions/1/setup` | `3509e55efc8a9e0b30deb1feb20779db25097d9234c536d3418c178b049082f5` |
| learner.json | `/lessons/3/learn/misconceptions/1/commands` | `8771449d56301c4406012f3a2e0deae20756b287752c525f54111793384cf86b` |
| learner.json | `/lessons/3/learn/misconceptions/2/setup` | `0366030242e8531809cfcc76ec9b0322041175937f593ff05ef6a71e5abd7a9d` |
| learner.json | `/lessons/3/learn/misconceptions/2/commands` | `e7c2dbbdd82e4dba4c8a00cfd0d969f088c2e6d19693270240df223aa2dd69c8` |
| learner.json | `/lessons/3/referenceCard/commands` | `d0bdd839b8271327cfba8244e7aa6bdc4729e57e05efe5b06bc29e7b34ad8b77` |
| learner.json | `/lessons/3/tasks/0/setup` | `4f9fc602adedbff830ad1263b247f9312970d14017d73c57ec8b894218dd37d6` |
| learner.json | `/lessons/3/tasks/1/setup` | `55663d536199d2bcd67c35ba719ca7c85cb6257fa89299973418293e8e7c4569` |
| learner.json | `/lessons/3/tasks/2/setup` | `8f2e3a2de3abe74e93f794fc08d5145ce6e0f274ecef855292665a2301c25c38` |
| learner.json | `/lessons/3/tasks/2/broken` | `e7c2dbbdd82e4dba4c8a00cfd0d969f088c2e6d19693270240df223aa2dd69c8` |
| learner.json | `/lessons/3/tasks/3/setup` | `6d9527434b137a4881a87cab9510472e4d71405717a890c18d3480d6d1cf9d1d` |
| learner.json | `/lessons/3/tasks/4/setup` | `f675ce10bfe402e0dcd047310cfb0879873e996100ec8704e6db38b85d5f4818` |
| learner.json | `/lessons/4/learn/walkthrough/setup` | `84cc04232da01e603945457d9fa80c8341370b93b4f3e0cc1eac5341cd91e331` |
| learner.json | `/lessons/4/learn/walkthrough/steps/0/command` | `a523e0cba61adacd9cb30d322fed72d9f0a2e55921a8bbd169807216c29da88e` |
| learner.json | `/lessons/4/learn/walkthrough/steps/1/command` | `8e9e1827b5b7b863156e64f0927185f5bbd7bdec45161bc4c15f17212d14bdd6` |
| learner.json | `/lessons/4/learn/walkthrough/steps/2/command` | `7e7ae6b1418ce6bfec597f00dc8c61dd71b1695c25952550d2d8d8ef69c1db4b` |
| learner.json | `/lessons/4/learn/walkthrough/steps/3/command` | `3ea71ec650ef4ee3d28ce66fca8b869f38ce0ce110bff52330089a5dd2608629` |
| learner.json | `/lessons/4/learn/walkthrough/steps/4/command` | `568b9ab0fb39ef08a005afc59fc18647a86b55f165b521fa60319f32859e967a` |
| learner.json | `/lessons/4/learn/questions/0/setup` | `c5d9fecf2d9eda5cb0621094ca1564b2063cd51f0950e0cd1f269e09864bf4f6` |
| learner.json | `/lessons/4/learn/questions/0/commands` | `c177ee45e14ce93eb51a9f2fc0af516cb25cbbdad38f729b00aa4009c76bf8e1` |
| learner.json | `/lessons/4/learn/misconceptions/0/setup` | `ce0280a5845fc0954ee919f23c3946d1d1614dbd0f46636f466f54f4dff44387` |
| learner.json | `/lessons/4/learn/misconceptions/0/commands` | `1b9f51eda10e14dfb41ff22c94c94e6eb05960e28f6489e2f5009fe760b7159e` |
| learner.json | `/lessons/4/learn/misconceptions/1/setup` | `ce0280a5845fc0954ee919f23c3946d1d1614dbd0f46636f466f54f4dff44387` |
| learner.json | `/lessons/4/learn/misconceptions/1/commands` | `c177ee45e14ce93eb51a9f2fc0af516cb25cbbdad38f729b00aa4009c76bf8e1` |
| learner.json | `/lessons/4/learn/misconceptions/2/setup` | `b2a5e0b79d87f5012925bae8dc1abb66736092567979effaeb3a04dfc4d6059e` |
| learner.json | `/lessons/4/learn/misconceptions/2/commands` | `de6d768ca7f59e1f3c7ae9a5312ac0c55b9a9f864748986350d12b0d4c1ef47c` |
| learner.json | `/lessons/4/referenceCard/commands` | `9b09327848f4623f306293f591f7afca3f404f546fa1e4b6443bfdf6daa2949f` |
| learner.json | `/lessons/4/tasks/0/setup` | `dcc35af12b9aa7dc715e12c939f0cff956ef8dd41df36027c3035f59fc1895e9` |
| learner.json | `/lessons/4/tasks/1/setup` | `ce0280a5845fc0954ee919f23c3946d1d1614dbd0f46636f466f54f4dff44387` |
| learner.json | `/lessons/4/tasks/1/broken` | `1b9f51eda10e14dfb41ff22c94c94e6eb05960e28f6489e2f5009fe760b7159e` |
| learner.json | `/lessons/4/tasks/2/setup` | `1b83ab281fa252d2fbd764c91f93d2c4b1bfe0d6d6f803eef171b6120b6a48f0` |
| learner.json | `/lessons/4/tasks/3/setup` | `36d7035f7845b411787a722d0bf4609bcb1f213995ff88544fbc26ec949da2da` |
| learner.json | `/lessons/5/learn/walkthrough/setup` | `61cca3f3913bcbecfa73a0769c7cd74ff01a765e8a57c5332c8cffc8a866b190` |
| learner.json | `/lessons/5/learn/walkthrough/steps/0/command` | `0a34fc335bde2abbab2a26be64b7423a13600c4266bcf5d8b6e44e5ef1e09be0` |
| learner.json | `/lessons/5/learn/walkthrough/steps/1/command` | `3ea71ec650ef4ee3d28ce66fca8b869f38ce0ce110bff52330089a5dd2608629` |
| learner.json | `/lessons/5/learn/walkthrough/steps/2/command` | `f925f190818f850bd4a80185df028575d8ebf3606613dbe145b1adbe80a23c85` |
| learner.json | `/lessons/5/learn/walkthrough/steps/3/command` | `9a8877095ae466fa537b6bafd94f99685ee9dc2409cdc4e733db465bd52184c6` |
| learner.json | `/lessons/5/learn/walkthrough/steps/4/command` | `5fac3467210fb5339fc930fa45de59d695f4e0e2a8cd614099e66cab1c1e8bc4` |
| learner.json | `/lessons/5/learn/walkthrough/steps/5/command` | `13753f47be58eb47d38fbdb8653e24215deeddfa7f11216827c94d363020b6c3` |
| learner.json | `/lessons/5/learn/questions/0/setup` | `b2fb5179fb5c4e607eaf5848550be833043ab4b282ed8e9eea64eb6a111452a8` |
| learner.json | `/lessons/5/learn/questions/0/commands` | `5b1a8f8e77cead9f12cd6bd30fb41a62958e382b959fbbd03fe9ef98ec963fac` |
| learner.json | `/lessons/5/learn/misconceptions/0/setup` | `d1cfdfedef12b57396bf76dcd26ed64b27bffd607ee5f3acaf0da2b0ff0faf76` |
| learner.json | `/lessons/5/learn/misconceptions/0/commands` | `5b1a8f8e77cead9f12cd6bd30fb41a62958e382b959fbbd03fe9ef98ec963fac` |
| learner.json | `/lessons/5/learn/misconceptions/1/setup` | `45db95615b15c1847684391d0210e278ae846b0e7e38322cf0509312aeb0cd36` |
| learner.json | `/lessons/5/learn/misconceptions/1/commands` | `4121ee61177329aeba759ee6c8f0a3813a3ac4564aa033524f70b2dc2a7f95ee` |
| learner.json | `/lessons/5/learn/misconceptions/2/setup` | `9647fe66f9206bb84d790581df0a44674cfae6911cad1f7bc105d8686bffa188` |
| learner.json | `/lessons/5/learn/misconceptions/2/commands` | `4121ee61177329aeba759ee6c8f0a3813a3ac4564aa033524f70b2dc2a7f95ee` |
| learner.json | `/lessons/5/referenceCard/commands` | `7ee1e96f9b4ea975b9b902a54cc89c3225f5b6904716bf87c15c826cb363a846` |
| learner.json | `/lessons/5/tasks/0/setup` | `73b35126e50fdb0085eac31f874dc58f93029ec4b3fe8466ab9e657361692fec` |
| learner.json | `/lessons/5/tasks/1/setup` | `df21e3c5d6dedcb2864c459440cd7d65b06d95b402c6b5f43a8a1f2677b68b11` |
| learner.json | `/lessons/5/tasks/2/setup` | `73b35126e50fdb0085eac31f874dc58f93029ec4b3fe8466ab9e657361692fec` |
| learner.json | `/lessons/5/tasks/2/broken` | `c771ae5d266e4a1c8882d7da706dabcd80d938ff6d5545afefd12ba123f34f23` |
| learner.json | `/lessons/5/tasks/3/setup` | `8db3c158278d4b6ad21aab4c355392c1b88753dc2270b417346986af3325116a` |
| learner.json | `/lessons/5/tasks/4/setup` | `dac21b82f2e6d66dd776e8d900aaf3d7e8f89194c8919dac6f5dab035df51d4f` |

## Withheld source subtrees

These hashes identify excluded source values without publishing their contents. Origin: original by owner AI agents; disposition: excluded under learner export contract. Lesson filenames are relative to the source scope above.

| Source lesson | JSON pointer | Category | SHA-256 |
| --- | --- | --- | --- |
| 01-snapshots.json | `/learn/walkthrough/steps/0/expect` | expect | `e2c6d80dc04b5b4cb1a1dfe921af25fcbaf626ad047eb119998f2857518e43ff` |
| 01-snapshots.json | `/learn/walkthrough/steps/1/expect` | expect | `a2a99b9bdb76f6c79421863a188f0ec20cd2eabf51b4ace27101b5a674609248` |
| 01-snapshots.json | `/learn/walkthrough/steps/2/expect` | expect | `693faeaf83e763b59b5b742780aa085f28f6e85ed2adf26f0b0bb3bae3438989` |
| 01-snapshots.json | `/learn/walkthrough/steps/3/expect` | expect | `6aab795726ca1d36460d8f51aa0bf4a99b69a09104760e6285dc21b5dceba1c9` |
| 01-snapshots.json | `/learn/walkthrough/steps/4/expect` | expect | `c0549115bcc9764060bb2a5a73d49994ae30163f2e9018f507b0d44d8f78d622` |
| 01-snapshots.json | `/learn/walkthrough/steps/5/expect` | expect | `1a570a37f1fba2f73f2af0aebcb650d3c872f2ea337084fe0608f4f4c7d50d81` |
| 01-snapshots.json | `/learn/walkthrough/steps/6/expect` | expect | `5e6dd83bc25800b74e2701cac77d793cbbde08ea0e047dab0229c8f4551bfd03` |
| 01-snapshots.json | `/learn/walkthrough/steps/7/expect` | expect | `39c8ca69e33d6e8084767135d6eb5d6578b2a5bdb4d8e5bda61dc8c195a0f567` |
| 01-snapshots.json | `/learn/walkthrough/steps/8/expect` | expect | `5e6dd83bc25800b74e2701cac77d793cbbde08ea0e047dab0229c8f4551bfd03` |
| 01-snapshots.json | `/learn/walkthrough/steps/9/expect` | expect | `093e50e42cfef791ff55a8b6291569463cb501b2aa6d102ea8695e6e0702977f` |
| 01-snapshots.json | `/learn/walkthrough/steps/10/expect` | expect | `948dfe36bf1b8737d39ff2d4f8577f3c4c322238ca15fed93d2f6b735dd8bd16` |
| 01-snapshots.json | `/learn/prediction/reveal` | reveal | `a65d58c4abfd30a23f8404c7c9599301f6797ebe03e5a09d8073385650b3bea6` |
| 01-snapshots.json | `/learn/misconceptions/0/observed` | observed | `d754ebfdfa632c75c0cc67c20bfff6c306fcf0ff10a0f20330d9adfc0b629f14` |
| 01-snapshots.json | `/learn/misconceptions/1/observed` | observed | `15317843f8f6b25caa8682fa98e241ffe83fe396906ae3bd6c13d9f938d9abfe` |
| 01-snapshots.json | `/guided/0/reference` | reference | `3269f57e8fc4441b3b162deff22ee86a0422b56562455abcd34425af1bd425fb` |
| 01-snapshots.json | `/guided/0/mutants` | mutants | `f111c880e530bac869478dc3aeb62e86d681d9a410c0e14b1ca6936860405531` |
| 01-snapshots.json | `/guided/1/reference` | reference | `7b5e44a974615febbd6365d056561101db0bfdefcd6f655d390268a8499f4760` |
| 01-snapshots.json | `/guided/1/mutants` | mutants | `c2fb2fc455142d5ab08b34557191eccfcb9eb6d6bcdbc79d409434df77f58e74` |
| 01-snapshots.json | `/debug/0/brokenResult` | brokenResult | `15317843f8f6b25caa8682fa98e241ffe83fe396906ae3bd6c13d9f938d9abfe` |
| 01-snapshots.json | `/debug/0/fixed` | fixed | `fd1d5c432ef1c684cfc6ff2459f571cb0c5537dba3c6fe3ffb097e64d747ea63` |
| 01-snapshots.json | `/debug/0/explanation` | explanation | `2d590d642830cae50a3a78524525f1bc23abea060a42391dab4b8149a2bb338d` |
| 01-snapshots.json | `/onYourOwn/0/reference` | reference | `0909db901ccf0c236a9b05dd5e4ff29f453f86e4eccfc92e4efb4e878a72ee00` |
| 01-snapshots.json | `/onYourOwn/0/mutants` | mutants | `cede2699b0c148789facaa4178e04e2cdc540f8649904dbfb975ef1fa82d073e` |
| 01-snapshots.json | `/onYourOwn/0/comeback/reference` | reference | `0fb924e2e64198b89673fc8eb19273fca8e28a16b640cdaca397038dc27bfede` |
| 01-snapshots.json | `/onYourOwn/0/comeback/mutants` | mutants | `27131d3a9ea934260ec619cb089b3ba04005bb47f15bd0604bd9525ff610b749` |
| 02-branches.json | `/learn/walkthrough/steps/0/expect` | expect | `62424ff303bc34afa082c93a92c8aa2e504df8db5ef1c6ad46a622ed360a3d15` |
| 02-branches.json | `/learn/walkthrough/steps/1/expect` | expect | `58ba047571bef60447c8086802c3d7dabc4ed7dcd1fd660ef12eac476b473b9a` |
| 02-branches.json | `/learn/walkthrough/steps/2/expect` | expect | `49e502921975391cb29d8f06cf1a11cea2894a6ae157a8c061f0c804de3f4205` |
| 02-branches.json | `/learn/walkthrough/steps/3/expect` | expect | `69ed98965a9a2aa2a07197cb9aa7102d2d674b1d7d509b515de031def0fa30fe` |
| 02-branches.json | `/learn/walkthrough/steps/4/expect` | expect | `1b04bed2a36e2c5c6e9e4fd78bab96088ed6529eba0c6712f88859f66f28f266` |
| 02-branches.json | `/learn/walkthrough/steps/5/expect` | expect | `024f74d51e514af6b2f6ffd640fe8b9ca9090a2eef5fbd5d8edc7d1c12e54dd0` |
| 02-branches.json | `/learn/walkthrough/steps/6/expect` | expect | `fcef17a48f31a7b5f8840c92a4dc23c84e1b85791c3fe0b63153abbb06628be1` |
| 02-branches.json | `/learn/walkthrough/steps/7/expect` | expect | `0c2d838d06b680b3ebdede2341292034366f47286337e6f4be6719e4c76f37fb` |
| 02-branches.json | `/learn/walkthrough/steps/8/expect` | expect | `3677b24fac4eea68e6173e4c9c00a88764621427472c9f107808a04e2e9132e2` |
| 02-branches.json | `/learn/walkthrough/steps/9/expect` | expect | `01202d4d67c7e3524d391b0dfe045644efb8582f2cf061f60585db329d018a03` |
| 02-branches.json | `/learn/walkthrough/steps/10/expect` | expect | `248bdd7554a21f79baa2b83900f9d5992f823b246c61bb089bb5644545ec194f` |
| 02-branches.json | `/learn/walkthrough/steps/11/expect` | expect | `295b12f98060c3e42bfbd022101081c1b4085811e02c51acdaf314c0fcf1685d` |
| 02-branches.json | `/learn/prediction/parity` | parity | `3d04cf9c77839a5cce5945fee582500679f1c69e172614721f7ad0d714441b3e` |
| 02-branches.json | `/learn/prediction/reveal` | reveal | `764fc53fe2802b3dc7c43da877d2465ac3622ef64cc5116a5e3e7f0525950ff1` |
| 02-branches.json | `/learn/misconceptions/0/observed` | observed | `d53a271906aa639a5012d7186578caf38810f49de43797c133b95a7a4320caab` |
| 02-branches.json | `/learn/misconceptions/1/observed` | observed | `f214e4af91f7c8119a5c548849c5cb45b0d57be2e03c711c4dfd3fcc40566ed4` |
| 02-branches.json | `/learn/misconceptions/2/observed` | observed | `bb221cb888d9b349783b69487313eea6b15299bfb9ffc1d3b26e73323a9e7d78` |
| 02-branches.json | `/guided/0/reference` | reference | `0c57f1b90b44150774f6c8d291ebf69edf199ec0956356f2a23747ade04742ca` |
| 02-branches.json | `/guided/0/mutants` | mutants | `eb76c6ade86de378857a51c89403591f2418169fed32c7ec2910c7af223840f6` |
| 02-branches.json | `/guided/1/reference` | reference | `c83389a8e2a81db361c17bd2ffd5d642efc2b9f97a9da8da26540d8c420b8c02` |
| 02-branches.json | `/guided/1/mutants` | mutants | `c2a7078e97314255b63f4bfb4f2fc098c3fe830684a32f2297c0fe574366faac` |
| 02-branches.json | `/debug/0/brokenResult` | brokenResult | `ea42a73ed3a763a1b0f348ff0d2fa35feea2f20b4a7cf9a4e092bec2d1933f9f` |
| 02-branches.json | `/debug/0/fixed` | fixed | `cbc0e160f719d0202f75bdd2b076720d467e9f87b68c14304b7e7d6f7533be27` |
| 02-branches.json | `/debug/0/explanation` | explanation | `bbf60a67f320a5603fde290cfd6eedbce819e9ef13638ac796577ff44f6d277a` |
| 02-branches.json | `/onYourOwn/0/reference` | reference | `fb0096e26b7e33288ce443bfb63c311a942e492a263cecf8d7264f85447d6d34` |
| 02-branches.json | `/onYourOwn/0/mutants` | mutants | `105a8fe6850aa0b0643dee38c48f098b27296edd9d8462e33156faedd8572310` |
| 02-branches.json | `/onYourOwn/0/comeback/reference` | reference | `0a7a362778aba2e3f58f5660621e2087fd8cf92e65d1ceaf168911b54a2e82b6` |
| 02-branches.json | `/onYourOwn/0/comeback/mutants` | mutants | `e6083d2805aac3194d852ad7f7ac0bbdc91f1383c3d2ea592719e012dc3f223e` |
| 03-merge.json | `/learn/walkthrough/steps/0/expect` | expect | `576ee3010f9ffa0506b12516f3649b69dd48820dad762fc330350966f5eaac77` |
| 03-merge.json | `/learn/walkthrough/steps/1/expect` | expect | `305e6b88202dc6badd2043028d15373000b1d9124a4a16875ce638117a43954f` |
| 03-merge.json | `/learn/walkthrough/steps/2/expect` | expect | `1871e0f9fe316ba022aa468b05418c6adabbbffacd9d7b2900dc8eaa73474bb2` |
| 03-merge.json | `/learn/walkthrough/steps/3/expect` | expect | `1580bd5102fa0e06fb141aeafa3147f26bee3d837a42fc4b2348b43d632c7f57` |
| 03-merge.json | `/learn/walkthrough/steps/4/expect` | expect | `9a7d462f14d7c56c69c1dd5d7bd9e3b8202afade033adeaa37d4f094cf069dd7` |
| 03-merge.json | `/learn/walkthrough/steps/5/expect` | expect | `045ccce12533033d2b27a4227ff77836ec0f1eeaa51e11598df7e37668cc1850` |
| 03-merge.json | `/learn/walkthrough/steps/6/expect` | expect | `8b02cc2c15428eeb085b1417b9ab85f3a9c4b0751fcf67437c724720ba7879eb` |
| 03-merge.json | `/learn/walkthrough/steps/7/expect` | expect | `b952f29227781447d5277d0864b0c0f8439237db478fa6278c2fbae855df3f29` |
| 03-merge.json | `/learn/walkthrough/steps/8/expect` | expect | `7c00f53180aba107ca9948ade29368a4c69235d31c3a61a5e8537e33864428e7` |
| 03-merge.json | `/learn/walkthrough/steps/9/expect` | expect | `a22415bb3abf2b6b13e3f8cd3316ac19d80113590768d7e25ef4a786f02ced18` |
| 03-merge.json | `/learn/walkthrough/steps/10/expect` | expect | `9e05d098cf9b1ec518c585312cdfceb91b48942f0243e8b6592f64b8f227ad8c` |
| 03-merge.json | `/learn/walkthrough/steps/11/expect` | expect | `2e7dd2b2bbc7f5b6898973e46d94c7a1312fda03989a449e550a225ffa8cd0f0` |
| 03-merge.json | `/learn/prediction/parity` | parity | `2ed27c1421e6928dbe13dbfdb5c59e1045b30341fe7ebe05700006bc5ac572c0` |
| 03-merge.json | `/learn/prediction/parityNote` | parityNote | `46fe026404365bca5a242392f4d012b36910208e70a1f46a420f78ca70be0567` |
| 03-merge.json | `/learn/prediction/reveal` | reveal | `e1aeb962fce67078ffccae51f7717b2fba68343bb6bc7d1e06a8cef3f3c011e3` |
| 03-merge.json | `/learn/misconceptions/0/observed` | observed | `1dc577af37153e6909bf7dc0388656b5f49bcd5ddd1089ebc927bef557b3f847` |
| 03-merge.json | `/learn/misconceptions/1/observed` | observed | `b59705c4657698cafededbf63790206dd752d9dde6908e632a0208b4517288c2` |
| 03-merge.json | `/learn/misconceptions/2/observed` | observed | `95ca414708a1fa29a48faaf6c64a3cd8f8d365f2483209bbc97095cf33ce9844` |
| 03-merge.json | `/guided/0/reference` | reference | `c8a69e9d4e445d7541e2d6dddf1169836b5c28c2c005086cac48120d34406afd` |
| 03-merge.json | `/guided/0/mutants` | mutants | `db9498baac9a3a365de2741623b8317307ae9378cc1160c8c6ea4b1adda7e234` |
| 03-merge.json | `/guided/1/reference` | reference | `33684706c2a4a32a408e31d4cfa31c4bea13ad79e202d53f5c952904932795ab` |
| 03-merge.json | `/guided/1/mutants` | mutants | `8347084370a7a999a8207888bc9f45307df447b77bdef8e2840bf1e9c8f42721` |
| 03-merge.json | `/debug/0/brokenResult` | brokenResult | `5f8e0e59d73ffb36c5a0d6a63b0ce240d61a945559c791b4ae00720bb863f9d5` |
| 03-merge.json | `/debug/0/fixed` | fixed | `412b5a081046dc60f36560a472f0f33800046f7e8b972c7cb78d0ff7504127e5` |
| 03-merge.json | `/debug/0/explanation` | explanation | `ae9051c47773eb5fe9b0245e713d3a9dc23ba8ab3c572b86290b8ca2d30fdc7a` |
| 03-merge.json | `/onYourOwn/0/reference` | reference | `43054bafca1350693490d85c1f639a1de6c0931e2e13e97cc9e442c79d38c641` |
| 03-merge.json | `/onYourOwn/0/mutants` | mutants | `7042ffe81eed11266e194c88739d9d9d8205d0882b642adb87389edd29d3ea62` |
| 03-merge.json | `/onYourOwn/0/comeback/reference` | reference | `974d6676011d244cbd470572dcb57c1e25c93995e05637682da82b8344d55252` |
| 03-merge.json | `/onYourOwn/0/comeback/mutants` | mutants | `f2bb3aa8473a89772c6b41870c0329e7b103e0658f1ad8ef1b2a3aa97cfd1324` |
| 04-rebase.json | `/learn/walkthrough/steps/0/expect` | expect | `cfe45f702b59cf19babac0d539f47f0d5a9dd0c60a21486a4b1bcc05a631e42d` |
| 04-rebase.json | `/learn/walkthrough/steps/1/expect` | expect | `d82d5fb6ea99d3d970725808f10301aa0526d1fbbc57da128a4715e05268184d` |
| 04-rebase.json | `/learn/walkthrough/steps/2/expect` | expect | `14c9ef219f1db8cc82fcda277362cc275e9c5e241b23dcd9dbd5a9fbd206e9ee` |
| 04-rebase.json | `/learn/walkthrough/steps/3/expect` | expect | `1d97058abe68202ff1c517fc91dd6936da6135abdfaa68195784240f01d334ad` |
| 04-rebase.json | `/learn/walkthrough/steps/4/expect` | expect | `a22415bb3abf2b6b13e3f8cd3316ac19d80113590768d7e25ef4a786f02ced18` |
| 04-rebase.json | `/learn/walkthrough/steps/5/expect` | expect | `c2e01a45162853bbec78ba12dd8edd7fb3475cd3e4e6bf9db68531882ff108cf` |
| 04-rebase.json | `/learn/prediction/reveal` | reveal | `5e095af9e1a7604320122353620d9070abd055ff335e61ee6f76849ec96479ba` |
| 04-rebase.json | `/learn/misconceptions/0/observed` | observed | `ac9b001f067ffb93d2d11bce1b91b5232b7b87e41cbdd225e1d0c5e69aa231de` |
| 04-rebase.json | `/learn/misconceptions/1/observed` | observed | `39e75bbe79a3c9918d3bfba0049acc5353a13bb5a829ec523654db820bd7435d` |
| 04-rebase.json | `/learn/misconceptions/2/parity` | parity | `2ed27c1421e6928dbe13dbfdb5c59e1045b30341fe7ebe05700006bc5ac572c0` |
| 04-rebase.json | `/learn/misconceptions/2/parityNote` | parityNote | `1fb0ef7327c0f54649fad369af077370cdb3a4917b72a19371638fc0fb2724d5` |
| 04-rebase.json | `/learn/misconceptions/2/observed` | observed | `de4bb95763fce63524a11b8a3d41921a92eb1edd7b5afdfa6bb6b88a86a7424f` |
| 04-rebase.json | `/guided/0/reference` | reference | `297826597827ce40fb9c5cdf304ed5aac60456ef736fc60dcc633f2958e79907` |
| 04-rebase.json | `/guided/0/mutants` | mutants | `432441bc56a165a617a9c7f11a7efc011dd1e07f703f705322e492e78f9edb98` |
| 04-rebase.json | `/guided/1/reference` | reference | `e7c2dbbdd82e4dba4c8a00cfd0d969f088c2e6d19693270240df223aa2dd69c8` |
| 04-rebase.json | `/guided/1/mutants` | mutants | `485ed522b82393843ba78713e4d6f88d79ed7a9541763ce8979144834e03bb39` |
| 04-rebase.json | `/debug/0/brokenResult` | brokenResult | `10c0a263ae6b14f7545b74e67c7d8a5316c7a9f1752ba1bf8c4dec3581d9aca4` |
| 04-rebase.json | `/debug/0/fixed` | fixed | `158b10f2ae6e5c28fe7af5342ab3435173f55fc1315c58bce775b9306120a6b6` |
| 04-rebase.json | `/debug/0/explanation` | explanation | `cca8c97c18569a8ee93cefd146ab543bd19a016c1fcb1ec332091739e52b34b5` |
| 04-rebase.json | `/onYourOwn/0/reference` | reference | `dc6cf2888943c45208a5f8d747a9dd4ef57c8d40af0752a43ee19aec5bc4ecac` |
| 04-rebase.json | `/onYourOwn/0/mutants` | mutants | `b33eac4191d75acf0c8c90e3bc87c06806cf4d2851c3adb1fe82056b8ddb0c3a` |
| 04-rebase.json | `/onYourOwn/0/comeback/reference` | reference | `8bc25011399f44782a2844d458a946177983beeea6c04f5bd4e70bc7e2211088` |
| 04-rebase.json | `/onYourOwn/0/comeback/mutants` | mutants | `cef3e741a8a149aae8baea886ffc503720587ac057bc0d247a5e714b7f34bec8` |
| 05-reset.json | `/learn/walkthrough/steps/0/expect` | expect | `c20c19d405b2cf8d1df35474d671aa0e3a640e0fab4c7e03bdc772ad3cb990de` |
| 05-reset.json | `/learn/walkthrough/steps/1/expect` | expect | `7f8cd5da2f98b99b17015f6cad26136e830aa145040652618f2778983eb407d2` |
| 05-reset.json | `/learn/walkthrough/steps/2/expect` | expect | `be15766b164caade4c6410e93048b38d47252c4ecc74a1d28df04f865f2386be` |
| 05-reset.json | `/learn/walkthrough/steps/3/expect` | expect | `606d71c355110df500e4bf9d10c0371fc8a258ac5b78271c4c20d6f3520f1de8` |
| 05-reset.json | `/learn/walkthrough/steps/4/expect` | expect | `46aceb2e56f86e1c6c382cbe64e557b63409f36d96fd9c21209b40896525c54e` |
| 05-reset.json | `/learn/prediction/reveal` | reveal | `d55c6c8a5aca26a483d42489c956e0165f7118c5ac5c5792dd505b131b381689` |
| 05-reset.json | `/learn/misconceptions/0/observed` | observed | `6263cf71c9636c3206bb973c4454001652a4eca0eee7b9db5edee9b739fe9a6a` |
| 05-reset.json | `/learn/misconceptions/1/observed` | observed | `a9eb3858f8168ce76a820e6033867ffc1e278f53d63465d7caa2b2435610f655` |
| 05-reset.json | `/learn/misconceptions/2/observed` | observed | `0f04fdd17dffc55f437d3687e482ebbb30dd6f47013e35a4830e2e22aec712a9` |
| 05-reset.json | `/guided/0/reference` | reference | `cff6bb72cb6a7e5e022fc6289b224238785ed7724b61dea78dc419bf2373d026` |
| 05-reset.json | `/guided/0/mutants` | mutants | `031e59b96a226776e6c16d67f35957cfd402b3a8485511eb0d11139ae1f1884f` |
| 05-reset.json | `/guided/1/reference` | reference | `a8f500750b16ac919b908bf33e1b18c51cd9720ee9064a829d7094b956bb73b6` |
| 05-reset.json | `/guided/1/mutants` | mutants | `42ba1cc1fd3277f73ee537bcea245093a5d59343eddc2d39153e73cc2b551374` |
| 05-reset.json | `/debug/0/brokenResult` | brokenResult | `4e4b01804045d23caf13e03c40e52e007067f96f7c25d4f8ab3d2ed392188030` |
| 05-reset.json | `/debug/0/fixed` | fixed | `c177ee45e14ce93eb51a9f2fc0af516cb25cbbdad38f729b00aa4009c76bf8e1` |
| 05-reset.json | `/debug/0/explanation` | explanation | `4dbbc9e1897b0fd0544718c44cd542dd05229394de8ff891c15844ca4492f511` |
| 05-reset.json | `/onYourOwn/0/reference` | reference | `f34132445c847bf912b3ce443406fc1ebeb430599d8acc0027b0f65044cf77ef` |
| 05-reset.json | `/onYourOwn/0/mutants` | mutants | `f017d61c7197ed5579de543770324eb4a3c9b43c34fddc3aa50fdbda3ad6993c` |
| 05-reset.json | `/onYourOwn/0/comeback/reference` | reference | `486147677c1dc0ead7e0285338f0030cc8366ff79c0f40704cefe7c5ae3c34f7` |
| 05-reset.json | `/onYourOwn/0/comeback/mutants` | mutants | `773fdd6dcf9c05495ef9e08927948fc8a85e7472c00688f79d3a2613e81bfeeb` |
| 06-recovery.json | `/learn/walkthrough/steps/0/expect` | expect | `4f60717b78211ee981879616dddf0d7bbaa49215760020ff85fa244577b25e8c` |
| 06-recovery.json | `/learn/walkthrough/steps/1/expect` | expect | `89889e6f736988d6127ff50d9294d1508c7c76931e5f9008fef8ae0ea3a0e172` |
| 06-recovery.json | `/learn/walkthrough/steps/2/expect` | expect | `52a5c419649b9a33dc93f2a01007283e260610dd56db11cb5fad53b3bcc01cce` |
| 06-recovery.json | `/learn/walkthrough/steps/3/expect` | expect | `069d9ebf52b67919ac43330b37227b6ae742020ab9e1491fd579d640e0e152b4` |
| 06-recovery.json | `/learn/walkthrough/steps/4/expect` | expect | `fa5a19fa8b22dacfac6e966172d72174be1ec9229106f22ec34e6c9557111949` |
| 06-recovery.json | `/learn/walkthrough/steps/5/expect` | expect | `f5453f8dd8a18b6577f729e7054d629d234465e7097d52c7e3ce6b53a85dd360` |
| 06-recovery.json | `/learn/prediction/reveal` | reveal | `950aa96dc5dbd7bf1dff23de5a65e95f03786e74776ce641eea5847d22175a83` |
| 06-recovery.json | `/learn/misconceptions/0/observed` | observed | `ac81203ae73e95c8ecbf9c7bb234152bb4fa92eeedd256be912c1c5b5394d918` |
| 06-recovery.json | `/learn/misconceptions/1/observed` | observed | `fcf2e391294fb831ff90371bb5176fd56fa1456044cdbe005613daebf512bed7` |
| 06-recovery.json | `/learn/misconceptions/2/observed` | observed | `a2c4ea051ccf924ce265bec299257eeaa94d13652f8ed18cfc0199a2913a4ac3` |
| 06-recovery.json | `/guided/0/reference` | reference | `c771ae5d266e4a1c8882d7da706dabcd80d938ff6d5545afefd12ba123f34f23` |
| 06-recovery.json | `/guided/0/mutants` | mutants | `e0333761771cea33b079facb280170643c01d01bb60d1368c96f5820ec482e6a` |
| 06-recovery.json | `/guided/1/reference` | reference | `5b1a8f8e77cead9f12cd6bd30fb41a62958e382b959fbbd03fe9ef98ec963fac` |
| 06-recovery.json | `/guided/1/mutants` | mutants | `387cb47c6f955ed0089b473c68fc15acb9c758a58c93f4c55fa079c76511a8ce` |
| 06-recovery.json | `/debug/0/brokenResult` | brokenResult | `5b44269cf2af765e2aca90e1b9bdb0fea1cae51945b25fe3cc6bb9fd19242593` |
| 06-recovery.json | `/debug/0/fixed` | fixed | `78a9ac7e87fa7e7c0884e71ccc69267e678cb4977c56872927b267c87a9a5479` |
| 06-recovery.json | `/debug/0/explanation` | explanation | `7a0d34de68affb4c438ceee1a4f5f7fd8ef845014c5c232ffec750ff2436bf2f` |
| 06-recovery.json | `/onYourOwn/0/reference` | reference | `5a4a15bb195a87680e87189910248ca944dd449bd446f99a8a4b7860de26adef` |
| 06-recovery.json | `/onYourOwn/0/mutants` | mutants | `c9056b75aecc7a8b47f3a09c9ed8fd241fbf69bace1964e6c012992af2a219be` |
| 06-recovery.json | `/onYourOwn/0/comeback/reference` | reference | `aa6d3af42c9fa9abb9fcea2c4231300d09b1ac5500bb59297b3884a2a6907a56` |
| 06-recovery.json | `/onYourOwn/0/comeback/mutants` | mutants | `aba3f262883f235a441dda41790a4cfd3a1886dafbb1f081183591307c6fd5c7` |

## Verification receipt (2026-11-14)

Verified: public asset and registry hashes; CourseBundle validation for both drafts and the existing demo (Swift 6.0.3, Python 3.12.3); five public tests passed. Source/export equality was checked by decoded JSON value: all seven Code Gym resources match; Git differs only by removal of the named exercise. Gitleaks directory scans of both source course folders and both public course folders reported no leaks. Public attachment URL, email, private-host-path and credential-key scans found only the documented synthetic Git fixture paths.

Pending / NOT RUN: independent human provenance and factual review, private author-host semantic replay/parity tests, Python trace regeneration, native player/device acceptance and the future format-v1 review pipeline. These results do not establish teaching accuracy or public-app importability.

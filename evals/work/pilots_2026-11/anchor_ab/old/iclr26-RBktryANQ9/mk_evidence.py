import json,re,os
D=os.path.dirname(os.path.abspath(__file__))
paper=open(os.path.join(D,'reviewer_copy.txt')).read()
rev=open(os.path.join(D,'review.md')).read()
def norm(s):
    s=re.sub(r'-\s*\n\s*','',s)  # dehyphenate across lines (approx)
    s=re.sub(r'\s+',' ',s); return s.lower()
# build column-agnostic search: just check each word sequence appears in order nearby -> approximate by checking all words present
Q=["a novel approach that leverages dataset distillation for noise removal",
"avoids the feedback loop common in existing techniques and enhances training efficiency",
"providing strong privacy protection through offline processing",
"ensures privacy protection through offline dataset distillation",
"We propose a new approach to model learning from noisy data that avoids vicious cycles",
"clean but challenging samples, such as those from tail classes in imbalanced datasets, may undergo lossy compression",
"We further hypothesize that challenging clean samples, such as tail data in imbalanced datasets, are at risk",
"Final test accuracies are reported throughout the distillation process",
"The validation performance over symmetric noise",
"at noise rates of 0.6 and 0.8, a single distilled sample per class surpasses the baseline",
"At a noise rate of 0.2, fewer than 50 samples per class significantly outperform the baseline",
"surpassing the CIFAR100N baseline using fewer than 10 distilled images per class",
"the validation accuracy matches that of the original dataset",
"the distillation process primarily captures common patterns while ignoring outliers such as noise",
"Only the DATM method achieves comparable performance to the benchmark at noise rate",
"a three-layer ConvNet for CIFAR and a four-layer ConvNet for Tiny-ImageNet",
"Realted Works","major contributions bellow","Both of which are widely employed",
"high-volume datasets like Clothing1M [48] and WebVision [27] serve as classic benchmarks",
"This corollary succinctly states the upper bound",
"Unless otherwise specified, Benchmark-I referenced later denotes this accelerated version",
"consistently demonstrate significant performance gains",
"Why not directly distill a clean subset that enables effective training?",
"This work first benchmarks existing representative distillation approaches",
"How much data should be distilled from a noisy dataset to create a meaningful distilled set?",
"This is why data distillation often yields suboptimal results in low-noise settings",
"a single distilled image retains discriminative features despite high noise ratios",
"especially in high-privacy environments where noise is prevalent",
"significant scalability challenges",
"training on the full dataset at the corresponding noise rate",
"following the evaluation protocols of DATM, DANCE, and RCIG, with data augmentation applied for RCIG as recommended",
"remain largely effective even in the presence of an unknown fixed noise rate",
]
# Two-column text: verify via a sliding check that words appear in order within a window
words=re.findall(r"[a-z0-9]+",norm(paper))
def found(q):
    qw=re.findall(r"[a-z0-9]+",norm(q))
    for i,wd in enumerate(words):
        if wd!=qw[0]: continue
        j=i; ok=True
        for x in qw[1:]:
            try: k=words.index(x,j+1,j+60)
            except ValueError:
                # handle hyphen split: try joined pieces
                ok=False;break
            j=k
        if ok: return True
    return False
bad=[q for q in Q if not found(q)]
print("not found:",bad)
inrev=[q for q in Q if q.lower()[:30] not in rev.lower()]
print("not in review:",inrev)

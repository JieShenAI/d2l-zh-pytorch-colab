from cProfile import label
import os

start_file = lambda s: [f for f in os.listdir(".") if str(f).startswith(s)]
# print(*fs,sep="\n")

txts = """chapter_introduction/index
chapter_preliminaries/index
chapter_linear-networks/index
chapter_multilayer-perceptrons/index
chapter_deep-learning-computation/index
chapter_convolutional-neural-networks/index
chapter_convolutional-modern/index
chapter_recurrent-neural-networks/index
chapter_recurrent-modern/index
chapter_attention-mechanisms/index
chapter_optimization/index
chapter_computational-performance/index
chapter_computer-vision/index
chapter_natural-language-processing-pretraining/index
chapter_natural-language-processing-applications/index
chapter_appendix-tools-for-deep-learning/index"""
# order_txt = ['chapter_introductio', 'chapter_preliminaries', 'chapter_linear-networks', 'chapter_multilayer-perceptrons', 'chapter_deep-learning-computatio', 'chapter_convolutional-neural-networks', 'chapter_convolutional-moder', 'chapter_recurrent-neural-networks', 'chapter_recurrent-moder', 'chapter_attention-mechanisms', 'chapter_optimization', 'chapter_computational-performanc', 'chapter_computer-visio', 'chapter_natural-language-processing-pretraining', 'chapter_natural-language-processing-applications', 'chapter_appendix-tools-for-deep-learning']
order_txt = [_.replace("/index","") for _ in txts.split("\n")]
# print(order_txt)
chapters = start_file("chapter")
# for _ in start_file("0") + start_file("1"):
#     os.rename(_,_[2::])
cnt = 1
for _ in order_txt:
    if _ in chapters:
        os.rename(_,str(cnt).zfill(2)+ "_" + _)
        cnt += 1
'''
100 out of 10,000 women at age forty who participate in routine screening have breast cancer. 80 of every 100 women with breast cancer will get a positive mammogram. 950 out of 9,900 women without breast cancer will also get a positive mammogram.

Solve: If 10,000 women in this age group undergo a routine screening, about what fraction of women with positive mammograms will actually have breast cancer?

Answer: 7.8%
'''

total_woman = 10000
woman_w_cancer = int(total_woman * .01)
pos_mammogram_w_cancer = int(woman_w_cancer * .8)
pos_mammogram_without_cancer = int((total_woman - woman_w_cancer) * .096)

print "Women with cancer: %s" % woman_w_cancer
print "Women with cancer and positive mammogram: %s" % pos_mammogram_w_cancer
print "Women without cancer and positive mammogram: %s" % pos_mammogram_without_cancer
